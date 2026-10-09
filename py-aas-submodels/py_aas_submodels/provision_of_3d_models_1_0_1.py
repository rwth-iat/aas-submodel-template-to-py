from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class Models3D(aas.Submodel):

    class Model3D(aas.SubmodelElementList):

        class Model3d_item(aas.SubmodelElementCollection):

            class File(aas.SubmodelElementCollection):

                class FileId(aas.SubmodelElementList):

                    class Fileid_item(aas.SubmodelElementCollection):

                        class FileDomainId(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileDomainId",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/FileDomaniId/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class ValueId(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ValueId",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/ValueId/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class IsPrimary(aas.Property):

                            def __init__(
                                self,
                                value: bool,
                                id_short: Optional[str] = r"IsPrimary",
                                value_type: aas.DataTypeDefXsd = bool,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/IsPrimary/1/0",
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
                                            value=r"ZeroToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            fileDomainId: Union[str, FileDomainId],
                            valueId: Union[str, ValueId],
                            isPrimary: Optional[
                                Iterable[Union[bool, IsPrimary]]
                            ] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if fileDomainId is not None and not isinstance(
                                fileDomainId, aas.SubmodelElement
                            ):
                                fileDomainId = self.FileDomainId(fileDomainId)

                            # Build a submodel element if a raw value was passed in the argument

                            if valueId is not None and not isinstance(
                                valueId, aas.SubmodelElement
                            ):
                                valueId = self.ValueId(valueId)

                            # A str would be split into its characters
                            if isinstance(isPrimary, str):
                                raise TypeError(
                                    "isPrimary takes several elements, got a str"
                                )

                            # Build submodel elements from raw values passed in the argument
                            if isPrimary:
                                isPrimary = [
                                    (
                                        i
                                        if isinstance(i, aas.SubmodelElement)
                                        else self.IsPrimary(i)
                                    )
                                    for i in isPrimary
                                ]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [fileDomainId, valueId, isPrimary]:
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
                        fileid_items: Optional[Iterable[Fileid_item]] = None,
                        id_short: Optional[str] = r"FileId",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(fileid_items, str):
                            raise TypeError(
                                "fileid_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileid_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class FileVersion(aas.SubmodelElementList):

                    class Fileversion_item(aas.SubmodelElementCollection):

                        class Title(aas.MultiLanguageProperty):

                            def __init__(
                                self,
                                value: aas.LangStringSet,
                                id_short: Optional[str] = r"Title",
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/Title/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class FileName(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileName",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileName/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class FileVersionId(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileVersionId",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileVersionID/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/StatusValue/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class SetDate(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Date,
                                id_short: Optional[str] = r"SetDate",
                                value_type: aas.DataTypeDefXsd = xsd.Date,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SetDate/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class BasedOn(aas.SubmodelElementList):

                            class Basedon_item(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
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
                                basedon_items: Optional[
                                    Iterable[Union[aas.Reference, Basedon_item]]
                                ] = None,
                                id_short: Optional[str] = r"BasedOn",
                                type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                                semantic_id_list_element: Optional[
                                    aas.Reference
                                ] = None,
                                value_type_list_element: Optional[
                                    aas.DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(basedon_items, str):
                                    raise TypeError(
                                        "basedon_items takes several elements, got a str"
                                    )

                                # Build submodel elements from raw values passed in the argument
                                if basedon_items:
                                    basedon_items = [
                                        (
                                            i
                                            if isinstance(i, aas.SubmodelElement)
                                            else self.Basedon_item(i)
                                        )
                                        for i in basedon_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [basedon_items]:
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
                                    isinstance(
                                        self.type_value_list_element, aas.Property
                                    )
                                    or isinstance(
                                        self.type_value_list_element, aas.Range
                                    )
                                    and not isinstance(
                                        new.value_type, self.value_type_list_element
                                    )
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

                        class RefersTo(aas.SubmodelElementList):

                            class Refersto_item(aas.ReferenceElement):

                                def __init__(
                                    self,
                                    value: aas.Reference,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
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
                                refersto_items: Optional[
                                    Iterable[Union[aas.Reference, Refersto_item]]
                                ] = None,
                                id_short: Optional[str] = r"RefersTo",
                                type_value_list_element: aas.SubmodelElement = aas.ReferenceElement,
                                semantic_id_list_element: Optional[
                                    aas.Reference
                                ] = None,
                                value_type_list_element: Optional[
                                    aas.DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(refersto_items, str):
                                    raise TypeError(
                                        "refersto_items takes several elements, got a str"
                                    )

                                # Build submodel elements from raw values passed in the argument
                                if refersto_items:
                                    refersto_items = [
                                        (
                                            i
                                            if isinstance(i, aas.SubmodelElement)
                                            else self.Refersto_item(i)
                                        )
                                        for i in refersto_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [refersto_items]:
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
                                    isinstance(
                                        self.type_value_list_element, aas.Property
                                    )
                                    or isinstance(
                                        self.type_value_list_element, aas.Range
                                    )
                                    and not isinstance(
                                        new.value_type, self.value_type_list_element
                                    )
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
                                content_type: Optional[str] = r"image/png",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/PreviewFile/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class DigitalFile(aas.File):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigitalFile",
                                content_type: Optional[str] = r"image/png",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/DigitalFile/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class ExternalFile(aas.SubmodelElementList):

                            class Externalfile_item(aas.SubmodelElementCollection):

                                class ExternalUrl(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"ExternalUrl",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/ExternalUrl/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class FileIdentifier(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"FileIdentifier",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/FileIdentifier/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class HostOrganization(aas.SubmodelElementCollection):

                                    class OrganizationName(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"OrganizationName",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationName/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            id_short: Optional[
                                                str
                                            ] = r"OrganizationOfficialName",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationOfficialName/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                        organizationName: Union[str, OrganizationName],
                                        organizationOfficialName: Union[
                                            str, OrganizationOfficialName
                                        ],
                                        id_short: Optional[str] = r"HostOrganization",
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            organizationName is not None
                                            and not isinstance(
                                                organizationName, aas.SubmodelElement
                                            )
                                        ):
                                            organizationName = self.OrganizationName(
                                                organizationName
                                            )

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            organizationOfficialName is not None
                                            and not isinstance(
                                                organizationOfficialName,
                                                aas.SubmodelElement,
                                            )
                                        ):
                                            organizationOfficialName = (
                                                self.OrganizationOfficialName(
                                                    organizationOfficialName
                                                )
                                            )

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [
                                            organizationName,
                                            organizationOfficialName,
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

                                class Api(aas.SubmodelElementList):

                                    class Api_item(aas.SubmodelElementCollection):

                                        class ApiVersion(aas.Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[str] = r"ApiVersion",
                                                value_type: aas.DataTypeDefXsd = str,
                                                value_id: Optional[
                                                    aas.Reference
                                                ] = None,
                                                display_name: Optional[
                                                    aas.MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    aas.MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    aas.Reference
                                                ] = aas.ExternalReference(
                                                    key=(
                                                        aas.Key(
                                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiVersion/1/0",
                                                        ),
                                                    ),
                                                    referred_semantic_id=None,
                                                ),
                                                qualifier: Iterable[
                                                    aas.Qualifier
                                                ] = None,
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
                                                            value=r"One",
                                                            value_id=None,
                                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                        class ApiDocumentationUrl(aas.Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[
                                                    str
                                                ] = r"ApiDocumentationUrl",
                                                value_type: aas.DataTypeDefXsd = str,
                                                value_id: Optional[
                                                    aas.Reference
                                                ] = None,
                                                display_name: Optional[
                                                    aas.MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    aas.MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    aas.Reference
                                                ] = aas.ExternalReference(
                                                    key=(
                                                        aas.Key(
                                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiDocumentationUrl/1/0",
                                                        ),
                                                    ),
                                                    referred_semantic_id=None,
                                                ),
                                                qualifier: Iterable[
                                                    aas.Qualifier
                                                ] = None,
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
                                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                        class ApiSpecificationUrl(aas.Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[
                                                    str
                                                ] = r"ApiSpecificationUrl",
                                                value_type: aas.DataTypeDefXsd = str,
                                                value_id: Optional[
                                                    aas.Reference
                                                ] = None,
                                                display_name: Optional[
                                                    aas.MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    aas.MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    aas.Reference
                                                ] = aas.ExternalReference(
                                                    key=(
                                                        aas.Key(
                                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiSpecificationUrl/1/0",
                                                        ),
                                                    ),
                                                    referred_semantic_id=None,
                                                ),
                                                qualifier: Iterable[
                                                    aas.Qualifier
                                                ] = None,
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
                                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                            apiVersion: Union[str, ApiVersion],
                                            apiDocumentationUrl: Optional[
                                                Union[str, ApiDocumentationUrl]
                                            ] = None,
                                            apiSpecificationUrl: Optional[
                                                Union[str, ApiSpecificationUrl]
                                            ] = None,
                                            id_short: Optional[str] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0",
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
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                        semantic_id=None,
                                                        supplemental_semantic_id=(),
                                                    ),
                                                )

                                            if embedded_data_specifications is None:
                                                embedded_data_specifications = []

                                            # Build a submodel element if a raw value was passed in the argument

                                            if (
                                                apiVersion is not None
                                                and not isinstance(
                                                    apiVersion, aas.SubmodelElement
                                                )
                                            ):
                                                apiVersion = self.ApiVersion(apiVersion)

                                            # Build a submodel element if a raw value was passed in the argument

                                            if (
                                                apiDocumentationUrl is not None
                                                and not isinstance(
                                                    apiDocumentationUrl,
                                                    aas.SubmodelElement,
                                                )
                                            ):
                                                apiDocumentationUrl = (
                                                    self.ApiDocumentationUrl(
                                                        apiDocumentationUrl
                                                    )
                                                )

                                            # Build a submodel element if a raw value was passed in the argument

                                            if (
                                                apiSpecificationUrl is not None
                                                and not isinstance(
                                                    apiSpecificationUrl,
                                                    aas.SubmodelElement,
                                                )
                                            ):
                                                apiSpecificationUrl = (
                                                    self.ApiSpecificationUrl(
                                                        apiSpecificationUrl
                                                    )
                                                )

                                            # Add all passed/initialized submodel elements to a single list
                                            embedded_submodel_elements = []
                                            for se_arg in [
                                                apiVersion,
                                                apiDocumentationUrl,
                                                apiSpecificationUrl,
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
                                        api_items: Optional[Iterable[Api_item]] = None,
                                        id_short: Optional[str] = r"Api",
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
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0",
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
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # A str would be split into its characters
                                        if isinstance(api_items, str):
                                            raise TypeError(
                                                "api_items takes several elements, got a str"
                                            )

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [api_items]:
                                            if se_arg is None:
                                                continue
                                            elif isinstance(
                                                se_arg, aas.SubmodelElement
                                            ):
                                                embedded_submodel_elements.append(
                                                    se_arg
                                                )
                                            elif isinstance(se_arg, Iterable):
                                                embedded_submodel_elements.extend(
                                                    se_arg
                                                )
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
                                            isinstance(
                                                self.type_value_list_element,
                                                aas.Property,
                                            )
                                            or isinstance(
                                                self.type_value_list_element, aas.Range
                                            )
                                            and not isinstance(
                                                new.value_type,
                                                self.value_type_list_element,
                                            )
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
                                                    and new.semantic_id
                                                    != item.semantic_id
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
                                    externalUrl: Union[str, ExternalUrl],
                                    fileIdentifier: Union[str, FileIdentifier],
                                    hostOrganization: HostOrganization,
                                    api: Optional[
                                        Union[Iterable[Api.Api_item], Api]
                                    ] = None,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument

                                    if externalUrl is not None and not isinstance(
                                        externalUrl, aas.SubmodelElement
                                    ):
                                        externalUrl = self.ExternalUrl(externalUrl)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if fileIdentifier is not None and not isinstance(
                                        fileIdentifier, aas.SubmodelElement
                                    ):
                                        fileIdentifier = self.FileIdentifier(
                                            fileIdentifier
                                        )

                                    # A str would be split into its characters
                                    if isinstance(api, str):
                                        raise TypeError(
                                            "api takes several elements, got a str"
                                        )

                                    # Build a submodel element if a raw value was passed in the argument

                                    if api is not None and not isinstance(
                                        api, aas.SubmodelElement
                                    ):
                                        api = self.Api(api)

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [
                                        externalUrl,
                                        fileIdentifier,
                                        hostOrganization,
                                        api,
                                    ]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
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
                                externalfile_items: Optional[
                                    Iterable[Externalfile_item]
                                ] = None,
                                id_short: Optional[str] = r"ExternalFile",
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(externalfile_items, str):
                                    raise TypeError(
                                        "externalfile_items takes several elements, got a str"
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [externalfile_items]:
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
                                    isinstance(
                                        self.type_value_list_element, aas.Property
                                    )
                                    or isinstance(
                                        self.type_value_list_element, aas.Range
                                    )
                                    and not isinstance(
                                        new.value_type, self.value_type_list_element
                                    )
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

                        class FileFormat(aas.SubmodelElementCollection):

                            class FormatName(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class FormatVersion(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatVersion",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatVersion/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class FormatQualifier(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatQualifier",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatQualifier/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                formatName: Union[str, FormatName],
                                formatVersion: Union[str, FormatVersion],
                                formatQualifier: Union[str, FormatQualifier],
                                id_short: Optional[str] = r"FileFormat",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if formatName is not None and not isinstance(
                                    formatName, aas.SubmodelElement
                                ):
                                    formatName = self.FormatName(formatName)

                                # Build a submodel element if a raw value was passed in the argument

                                if formatVersion is not None and not isinstance(
                                    formatVersion, aas.SubmodelElement
                                ):
                                    formatVersion = self.FormatVersion(formatVersion)

                                # Build a submodel element if a raw value was passed in the argument

                                if formatQualifier is not None and not isinstance(
                                    formatQualifier, aas.SubmodelElement
                                ):
                                    formatQualifier = self.FormatQualifier(
                                        formatQualifier
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    formatName,
                                    formatVersion,
                                    formatQualifier,
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

                        class SourceApplication(aas.SubmodelElementCollection):

                            class ApplicationName(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class ApplicationVersion(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationVersion",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationVersion/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class ApplicationQualifier(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationQualifier",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationQualifier/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class Api(aas.SubmodelElementList):

                                class Api_item(aas.SubmodelElementCollection):

                                    class ApiVersion(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"ApiVersion",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiVersion/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                    class ApiDocumentationUrl(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"ApiDocumentationUrl",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiDocumentationUrl/1/0",
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
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                    class ApiSpecificationUrl(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"ApiSpecificationUrl",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiSpecificationUrl/1/0",
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
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                        apiVersion: Union[str, ApiVersion],
                                        apiDocumentationUrl: Optional[
                                            Union[str, ApiDocumentationUrl]
                                        ] = None,
                                        apiSpecificationUrl: Optional[
                                            Union[str, ApiSpecificationUrl]
                                        ] = None,
                                        id_short: Optional[str] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0",
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
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument

                                        if apiVersion is not None and not isinstance(
                                            apiVersion, aas.SubmodelElement
                                        ):
                                            apiVersion = self.ApiVersion(apiVersion)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            apiDocumentationUrl is not None
                                            and not isinstance(
                                                apiDocumentationUrl, aas.SubmodelElement
                                            )
                                        ):
                                            apiDocumentationUrl = (
                                                self.ApiDocumentationUrl(
                                                    apiDocumentationUrl
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument

                                        if (
                                            apiSpecificationUrl is not None
                                            and not isinstance(
                                                apiSpecificationUrl, aas.SubmodelElement
                                            )
                                        ):
                                            apiSpecificationUrl = (
                                                self.ApiSpecificationUrl(
                                                    apiSpecificationUrl
                                                )
                                            )

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [
                                            apiVersion,
                                            apiDocumentationUrl,
                                            apiSpecificationUrl,
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
                                    api_items: Optional[Iterable[Api_item]] = None,
                                    id_short: Optional[str] = r"Api",
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
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # A str would be split into its characters
                                    if isinstance(api_items, str):
                                        raise TypeError(
                                            "api_items takes several elements, got a str"
                                        )

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [api_items]:
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
                                        isinstance(
                                            self.type_value_list_element, aas.Property
                                        )
                                        or isinstance(
                                            self.type_value_list_element, aas.Range
                                        )
                                        and not isinstance(
                                            new.value_type, self.value_type_list_element
                                        )
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

                            class VendorOrganization(aas.SubmodelElementCollection):

                                class OrganizationName(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"OrganizationName",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationName/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                        id_short: Optional[
                                            str
                                        ] = r"OrganizationOfficialName",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationOfficialName/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    organizationName: Union[str, OrganizationName],
                                    organizationOfficialName: Union[
                                        str, OrganizationOfficialName
                                    ],
                                    id_short: Optional[str] = r"VendorOrganization",
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument

                                    if organizationName is not None and not isinstance(
                                        organizationName, aas.SubmodelElement
                                    ):
                                        organizationName = self.OrganizationName(
                                            organizationName
                                        )

                                    # Build a submodel element if a raw value was passed in the argument

                                    if (
                                        organizationOfficialName is not None
                                        and not isinstance(
                                            organizationOfficialName,
                                            aas.SubmodelElement,
                                        )
                                    ):
                                        organizationOfficialName = (
                                            self.OrganizationOfficialName(
                                                organizationOfficialName
                                            )
                                        )

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [
                                        organizationName,
                                        organizationOfficialName,
                                    ]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
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
                                applicationName: Union[str, ApplicationName],
                                applicationVersion: Union[str, ApplicationVersion],
                                applicationQualifier: Union[str, ApplicationQualifier],
                                vendorOrganization: VendorOrganization,
                                api: Optional[
                                    Union[Iterable[Api.Api_item], Api]
                                ] = None,
                                id_short: Optional[str] = r"SourceApplication",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationName is not None and not isinstance(
                                    applicationName, aas.SubmodelElement
                                ):
                                    applicationName = self.ApplicationName(
                                        applicationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationVersion is not None and not isinstance(
                                    applicationVersion, aas.SubmodelElement
                                ):
                                    applicationVersion = self.ApplicationVersion(
                                        applicationVersion
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationQualifier is not None and not isinstance(
                                    applicationQualifier, aas.SubmodelElement
                                ):
                                    applicationQualifier = self.ApplicationQualifier(
                                        applicationQualifier
                                    )

                                # A str would be split into its characters
                                if isinstance(api, str):
                                    raise TypeError(
                                        "api takes several elements, got a str"
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if api is not None and not isinstance(
                                    api, aas.SubmodelElement
                                ):
                                    api = self.Api(api)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    applicationName,
                                    applicationVersion,
                                    applicationQualifier,
                                    api,
                                    vendorOrganization,
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

                        class ProvidingOrganization(aas.SubmodelElementCollection):

                            class OrganizationName(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"OrganizationName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/OrganizationName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[
                                        str
                                    ] = r"OrganizationOfficialName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization//OrganizationOfficialName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                organizationName: Union[str, OrganizationName],
                                organizationOfficialName: Union[
                                    str, OrganizationOfficialName
                                ],
                                id_short: Optional[str] = r"ProvidingOrganization",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationName is not None and not isinstance(
                                    organizationName, aas.SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(
                                        organizationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if (
                                    organizationOfficialName is not None
                                    and not isinstance(
                                        organizationOfficialName, aas.SubmodelElement
                                    )
                                ):
                                    organizationOfficialName = (
                                        self.OrganizationOfficialName(
                                            organizationOfficialName
                                        )
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    organizationName,
                                    organizationOfficialName,
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
                            title: Union[aas.LangStringSet, Title],
                            fileName: Union[str, FileName],
                            fileVersionId: Union[str, FileVersionId],
                            statusValue: Union[str, StatusValue],
                            setDate: Union[xsd.Date, SetDate],
                            previewFile: PreviewFile,
                            fileFormat: FileFormat,
                            providingOrganization: ProvidingOrganization,
                            basedOn: Optional[
                                Union[
                                    Iterable[
                                        Union[aas.Reference, BasedOn.Basedon_item]
                                    ],
                                    BasedOn,
                                ]
                            ] = None,
                            refersTo: Optional[
                                Union[
                                    Iterable[
                                        Union[aas.Reference, RefersTo.Refersto_item]
                                    ],
                                    RefersTo,
                                ]
                            ] = None,
                            digitalFile: Optional[DigitalFile] = None,
                            externalFile: Optional[
                                Union[
                                    Iterable[ExternalFile.Externalfile_item],
                                    ExternalFile,
                                ]
                            ] = None,
                            sourceApplication: Optional[SourceApplication] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if title is not None and not isinstance(
                                title, aas.SubmodelElement
                            ):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument

                            if fileName is not None and not isinstance(
                                fileName, aas.SubmodelElement
                            ):
                                fileName = self.FileName(fileName)

                            # Build a submodel element if a raw value was passed in the argument

                            if fileVersionId is not None and not isinstance(
                                fileVersionId, aas.SubmodelElement
                            ):
                                fileVersionId = self.FileVersionId(fileVersionId)

                            # Build a submodel element if a raw value was passed in the argument

                            if statusValue is not None and not isinstance(
                                statusValue, aas.SubmodelElement
                            ):
                                statusValue = self.StatusValue(statusValue)

                            # Build a submodel element if a raw value was passed in the argument

                            if setDate is not None and not isinstance(
                                setDate, aas.SubmodelElement
                            ):
                                setDate = self.SetDate(setDate)

                            # A str would be split into its characters
                            if isinstance(basedOn, str):
                                raise TypeError(
                                    "basedOn takes several elements, got a str"
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if basedOn is not None and not isinstance(
                                basedOn, aas.SubmodelElement
                            ):
                                basedOn = self.BasedOn(basedOn)

                            # A str would be split into its characters
                            if isinstance(refersTo, str):
                                raise TypeError(
                                    "refersTo takes several elements, got a str"
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if refersTo is not None and not isinstance(
                                refersTo, aas.SubmodelElement
                            ):
                                refersTo = self.RefersTo(refersTo)

                            # A str would be split into its characters
                            if isinstance(externalFile, str):
                                raise TypeError(
                                    "externalFile takes several elements, got a str"
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if externalFile is not None and not isinstance(
                                externalFile, aas.SubmodelElement
                            ):
                                externalFile = self.ExternalFile(externalFile)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                title,
                                fileName,
                                fileVersionId,
                                statusValue,
                                setDate,
                                basedOn,
                                refersTo,
                                previewFile,
                                digitalFile,
                                externalFile,
                                fileFormat,
                                sourceApplication,
                                providingOrganization,
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
                        fileversion_items: Optional[Iterable[Fileversion_item]] = None,
                        id_short: Optional[str] = r"FileVersion",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(fileversion_items, str):
                            raise TypeError(
                                "fileversion_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileversion_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class ConsumingApplication(aas.SubmodelElementList):

                    class Consumingapplication_item(aas.SubmodelElementCollection):

                        class ApplicationName(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationName",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationName/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class ApplicationVersion(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationVersion",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationVersion/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class ApplicationQualifier(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationQualifier",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationQualifier1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class VendorOrganization(aas.SubmodelElementCollection):

                            class OrganizationName(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"OrganizationName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[
                                        str
                                    ] = r"OrganizationOfficialName",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationOfficialName/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                organizationName: Union[str, OrganizationName],
                                organizationOfficialName: Union[
                                    str, OrganizationOfficialName
                                ],
                                id_short: Optional[str] = r"VendorOrganization",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationName is not None and not isinstance(
                                    organizationName, aas.SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(
                                        organizationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if (
                                    organizationOfficialName is not None
                                    and not isinstance(
                                        organizationOfficialName, aas.SubmodelElement
                                    )
                                ):
                                    organizationOfficialName = (
                                        self.OrganizationOfficialName(
                                            organizationOfficialName
                                        )
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    organizationName,
                                    organizationOfficialName,
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

                        class Api(aas.SubmodelElementList):

                            class Api_item(aas.SubmodelElementCollection):

                                class ApiVersion(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"ApiVersion",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiVersion/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class ApiDocumentationUrl(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[
                                            str
                                        ] = r"ApiDocumentationUrl",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiDocumentationUrl/1/0",
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
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class ApiSpecificationUrl(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[
                                            str
                                        ] = r"ApiSpecificationUrl",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiSpecificationUrl/1/0",
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
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    apiVersion: Union[str, ApiVersion],
                                    apiDocumentationUrl: Optional[
                                        Union[str, ApiDocumentationUrl]
                                    ] = None,
                                    apiSpecificationUrl: Optional[
                                        Union[str, ApiSpecificationUrl]
                                    ] = None,
                                    id_short: Optional[str] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument

                                    if apiVersion is not None and not isinstance(
                                        apiVersion, aas.SubmodelElement
                                    ):
                                        apiVersion = self.ApiVersion(apiVersion)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if (
                                        apiDocumentationUrl is not None
                                        and not isinstance(
                                            apiDocumentationUrl, aas.SubmodelElement
                                        )
                                    ):
                                        apiDocumentationUrl = self.ApiDocumentationUrl(
                                            apiDocumentationUrl
                                        )

                                    # Build a submodel element if a raw value was passed in the argument

                                    if (
                                        apiSpecificationUrl is not None
                                        and not isinstance(
                                            apiSpecificationUrl, aas.SubmodelElement
                                        )
                                    ):
                                        apiSpecificationUrl = self.ApiSpecificationUrl(
                                            apiSpecificationUrl
                                        )

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [
                                        apiVersion,
                                        apiDocumentationUrl,
                                        apiSpecificationUrl,
                                    ]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
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
                                api_items: Optional[Iterable[Api_item]] = None,
                                id_short: Optional[str] = r"Api",
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(api_items, str):
                                    raise TypeError(
                                        "api_items takes several elements, got a str"
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [api_items]:
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
                                    isinstance(
                                        self.type_value_list_element, aas.Property
                                    )
                                    or isinstance(
                                        self.type_value_list_element, aas.Range
                                    )
                                    and not isinstance(
                                        new.value_type, self.value_type_list_element
                                    )
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
                            applicationName: Union[str, ApplicationName],
                            applicationVersion: Union[str, ApplicationVersion],
                            applicationQualifier: Union[str, ApplicationQualifier],
                            vendorOrganization: VendorOrganization,
                            api: Optional[Union[Iterable[Api.Api_item], Api]] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationName is not None and not isinstance(
                                applicationName, aas.SubmodelElement
                            ):
                                applicationName = self.ApplicationName(applicationName)

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationVersion is not None and not isinstance(
                                applicationVersion, aas.SubmodelElement
                            ):
                                applicationVersion = self.ApplicationVersion(
                                    applicationVersion
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationQualifier is not None and not isinstance(
                                applicationQualifier, aas.SubmodelElement
                            ):
                                applicationQualifier = self.ApplicationQualifier(
                                    applicationQualifier
                                )

                            # A str would be split into its characters
                            if isinstance(api, str):
                                raise TypeError("api takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if api is not None and not isinstance(
                                api, aas.SubmodelElement
                            ):
                                api = self.Api(api)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                applicationName,
                                applicationVersion,
                                applicationQualifier,
                                vendorOrganization,
                                api,
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
                        consumingapplication_items: Optional[
                            Iterable[Consumingapplication_item]
                        ] = None,
                        id_short: Optional[str] = r"ConsumingApplication",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(consumingapplication_items, str):
                            raise TypeError(
                                "consumingapplication_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [consumingapplication_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class FileClassification(aas.SubmodelElementList):

                    class Fileclassification_item(aas.SubmodelElementCollection):

                        class ClassId(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ClassId",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassId/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassName/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ClassificationSystem/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0",
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
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
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
                        fileclassification_items: Iterable[Fileclassification_item],
                        id_short: Optional[str] = r"FileClassification",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(fileclassification_items, str):
                            raise TypeError(
                                "fileclassification_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileclassification_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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
                    fileId: Union[Iterable[FileId.Fileid_item], FileId],
                    fileClassification: Union[
                        Iterable[FileClassification.Fileclassification_item],
                        FileClassification,
                    ],
                    fileVersion: Optional[
                        Union[Iterable[FileVersion.Fileversion_item], FileVersion]
                    ] = None,
                    consumingApplication: Optional[
                        Union[
                            Iterable[ConsumingApplication.Consumingapplication_item],
                            ConsumingApplication,
                        ]
                    ] = None,
                    id_short: Optional[str] = r"File",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/1/0",
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
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(fileId, str):
                        raise TypeError("fileId takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if fileId is not None and not isinstance(
                        fileId, aas.SubmodelElement
                    ):
                        fileId = self.FileId(fileId)

                    # A str would be split into its characters
                    if isinstance(fileVersion, str):
                        raise TypeError("fileVersion takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if fileVersion is not None and not isinstance(
                        fileVersion, aas.SubmodelElement
                    ):
                        fileVersion = self.FileVersion(fileVersion)

                    # A str would be split into its characters
                    if isinstance(consumingApplication, str):
                        raise TypeError(
                            "consumingApplication takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if consumingApplication is not None and not isinstance(
                        consumingApplication, aas.SubmodelElement
                    ):
                        consumingApplication = self.ConsumingApplication(
                            consumingApplication
                        )

                    # A str would be split into its characters
                    if isinstance(fileClassification, str):
                        raise TypeError(
                            "fileClassification takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if fileClassification is not None and not isinstance(
                        fileClassification, aas.SubmodelElement
                    ):
                        fileClassification = self.FileClassification(fileClassification)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        fileId,
                        fileVersion,
                        consumingApplication,
                        fileClassification,
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

            class Capability(aas.SubmodelElementCollection):

                class PosModelPurpose(aas.SubmodelElementList):

                    class Posmodelpurpose_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        posmodelpurpose_items: Optional[
                            Iterable[Union[str, Posmodelpurpose_item]]
                        ] = None,
                        id_short: Optional[str] = r"PosModelPurpose",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(posmodelpurpose_items, str):
                            raise TypeError(
                                "posmodelpurpose_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if posmodelpurpose_items:
                            posmodelpurpose_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Posmodelpurpose_item(i)
                                )
                                for i in posmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [posmodelpurpose_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class NegModelPurpose(aas.SubmodelElementList):

                    class Negmodelpurpose_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        negmodelpurpose_items: Optional[
                            Iterable[Union[str, Negmodelpurpose_item]]
                        ] = None,
                        id_short: Optional[str] = r"NegModelPurpose",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(negmodelpurpose_items, str):
                            raise TypeError(
                                "negmodelpurpose_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if negmodelpurpose_items:
                            negmodelpurpose_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Negmodelpurpose_item(i)
                                )
                                for i in negmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [negmodelpurpose_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class EmbeddedInfo(aas.SubmodelElementList):

                    class Embeddedinfo_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        embeddedinfo_items: Optional[
                            Iterable[Union[str, Embeddedinfo_item]]
                        ] = None,
                        id_short: Optional[str] = r"EmbeddedInfo",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(embeddedinfo_items, str):
                            raise TypeError(
                                "embeddedinfo_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if embeddedinfo_items:
                            embeddedinfo_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.Embeddedinfo_item(i)
                                )
                                for i in embeddedinfo_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [embeddedinfo_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class State(aas.SubmodelElementList):

                    class State_item(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = None,
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                        state_items: Optional[Iterable[Union[str, State_item]]] = None,
                        id_short: Optional[str] = r"State",
                        type_value_list_element: aas.SubmodelElement = aas.Property,
                        semantic_id_list_element: Optional[aas.Reference] = None,
                        value_type_list_element: Optional[aas.DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(state_items, str):
                            raise TypeError(
                                "state_items takes several elements, got a str"
                            )

                        # Build submodel elements from raw values passed in the argument
                        if state_items:
                            state_items = [
                                (
                                    i
                                    if isinstance(i, aas.SubmodelElement)
                                    else self.State_item(i)
                                )
                                for i in state_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [state_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class ObjectType(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ObjectType",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/ObjectType/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                class Origin(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Origin",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Origin/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                class Simplification(aas.SubmodelElementCollection):

                    class Description(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Description",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/LevelDescription/1/0",
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
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                    class ReducedElements(aas.SubmodelElementList):

                        class Reducedelements_item(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = None,
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0",
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
                                            value=r"ZeroToMany",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                            reducedelements_items: Optional[
                                Iterable[Union[str, Reducedelements_item]]
                            ] = None,
                            id_short: Optional[str] = r"ReducedElements",
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
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0",
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
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(reducedelements_items, str):
                                raise TypeError(
                                    "reducedelements_items takes several elements, got a str"
                                )

                            # Build submodel elements from raw values passed in the argument
                            if reducedelements_items:
                                reducedelements_items = [
                                    (
                                        i
                                        if isinstance(i, aas.SubmodelElement)
                                        else self.Reducedelements_item(i)
                                    )
                                    for i in reducedelements_items
                                ]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [reducedelements_items]:
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
                                isinstance(self.type_value_list_element, aas.Property)
                                or isinstance(self.type_value_list_element, aas.Range)
                                and not isinstance(
                                    new.value_type, self.value_type_list_element
                                )
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

                    class DerivedFrom(aas.ReferenceElement):

                        def __init__(
                            self,
                            value: aas.Reference,
                            id_short: Optional[str] = r"DerivedFrom",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/DerivedFrom/1/0",
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
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
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
                        description_: Optional[Union[str, Description]] = None,
                        reducedElements: Optional[
                            Union[
                                Iterable[
                                    Union[str, ReducedElements.Reducedelements_item]
                                ],
                                ReducedElements,
                            ]
                        ] = None,
                        derivedFrom: Optional[Union[aas.Reference, DerivedFrom]] = None,
                        id_short: Optional[str] = r"Simplification",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if description_ is not None and not isinstance(
                            description_, aas.SubmodelElement
                        ):
                            description_ = self.Description(description_)

                        # A str would be split into its characters
                        if isinstance(reducedElements, str):
                            raise TypeError(
                                "reducedElements takes several elements, got a str"
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if reducedElements is not None and not isinstance(
                            reducedElements, aas.SubmodelElement
                        ):
                            reducedElements = self.ReducedElements(reducedElements)

                        # Build a submodel element if a raw value was passed in the argument

                        if derivedFrom is not None and not isinstance(
                            derivedFrom, aas.SubmodelElement
                        ):
                            derivedFrom = self.DerivedFrom(derivedFrom)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [description_, reducedElements, derivedFrom]:
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
                    posModelPurpose: Union[
                        Iterable[Union[str, PosModelPurpose.Posmodelpurpose_item]],
                        PosModelPurpose,
                    ],
                    origin: Union[str, Origin],
                    negModelPurpose: Optional[
                        Union[
                            Iterable[Union[str, NegModelPurpose.Negmodelpurpose_item]],
                            NegModelPurpose,
                        ]
                    ] = None,
                    embeddedInfo: Optional[
                        Union[
                            Iterable[Union[str, EmbeddedInfo.Embeddedinfo_item]],
                            EmbeddedInfo,
                        ]
                    ] = None,
                    state: Optional[
                        Union[Iterable[Union[str, State.State_item]], State]
                    ] = None,
                    objectType: Optional[Union[str, ObjectType]] = None,
                    simplification: Optional[Simplification] = None,
                    id_short: Optional[str] = r"Capability",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/1/0",
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
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(posModelPurpose, str):
                        raise TypeError(
                            "posModelPurpose takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if posModelPurpose is not None and not isinstance(
                        posModelPurpose, aas.SubmodelElement
                    ):
                        posModelPurpose = self.PosModelPurpose(posModelPurpose)

                    # A str would be split into its characters
                    if isinstance(negModelPurpose, str):
                        raise TypeError(
                            "negModelPurpose takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if negModelPurpose is not None and not isinstance(
                        negModelPurpose, aas.SubmodelElement
                    ):
                        negModelPurpose = self.NegModelPurpose(negModelPurpose)

                    # A str would be split into its characters
                    if isinstance(embeddedInfo, str):
                        raise TypeError(
                            "embeddedInfo takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if embeddedInfo is not None and not isinstance(
                        embeddedInfo, aas.SubmodelElement
                    ):
                        embeddedInfo = self.EmbeddedInfo(embeddedInfo)

                    # A str would be split into its characters
                    if isinstance(state, str):
                        raise TypeError("state takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if state is not None and not isinstance(state, aas.SubmodelElement):
                        state = self.State(state)

                    # Build a submodel element if a raw value was passed in the argument

                    if objectType is not None and not isinstance(
                        objectType, aas.SubmodelElement
                    ):
                        objectType = self.ObjectType(objectType)

                    # Build a submodel element if a raw value was passed in the argument

                    if origin is not None and not isinstance(
                        origin, aas.SubmodelElement
                    ):
                        origin = self.Origin(origin)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        posModelPurpose,
                        negModelPurpose,
                        embeddedInfo,
                        state,
                        objectType,
                        origin,
                        simplification,
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

            class Geometry(aas.SubmodelElementCollection):

                class Representation(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Representation",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/Representation/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                class LengthUnit(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LengthUnit",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/LengthUnit/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                class CartBoundingBox(aas.SubmodelElementList):

                    class Cartboundingbox_item(aas.SubmodelElementCollection):

                        class BoundingBoxKind(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"BoundingBoxKind",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/BoundingBoxKind/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                        class CartRefSystem(aas.SubmodelElementCollection):

                            class CartOffsetVector(aas.SubmodelElementCollection):

                                class X(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"X",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/X/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class Y(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Y",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Y/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class Z(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Z",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Z/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    x: Union[str, X],
                                    y: Union[str, Y],
                                    z: Union[str, Z],
                                    id_short: Optional[str] = r"CartOffsetVector",
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument

                                    if x is not None and not isinstance(
                                        x, aas.SubmodelElement
                                    ):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if y is not None and not isinstance(
                                        y, aas.SubmodelElement
                                    ):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if z is not None and not isinstance(
                                        z, aas.SubmodelElement
                                    ):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [x, y, z]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
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

                            class NormOrientationVector(aas.SubmodelElementList):

                                class Normorientationvector_item(
                                    aas.SubmodelElementCollection
                                ):

                                    class X(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"X",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/X/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                    class Y(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"Y",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Y/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                    class Z(aas.Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"Z",
                                            value_type: aas.DataTypeDefXsd = str,
                                            value_id: Optional[aas.Reference] = None,
                                            display_name: Optional[
                                                aas.MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                aas.MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                aas.Reference
                                            ] = aas.ExternalReference(
                                                key=(
                                                    aas.Key(
                                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Z/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                        x: Union[str, X],
                                        y: Union[str, Y],
                                        z: Union[str, Z],
                                        id_short: Optional[str] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0",
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
                                                    value=r"Three",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument

                                        if x is not None and not isinstance(
                                            x, aas.SubmodelElement
                                        ):
                                            x = self.X(x)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if y is not None and not isinstance(
                                            y, aas.SubmodelElement
                                        ):
                                            y = self.Y(y)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if z is not None and not isinstance(
                                            z, aas.SubmodelElement
                                        ):
                                            z = self.Z(z)

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [x, y, z]:
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
                                    normorientationvector_items: Iterable[
                                        Normorientationvector_item
                                    ],
                                    id_short: Optional[str] = r"NormOrientationVector",
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
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0",
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
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # A str would be split into its characters
                                    if isinstance(normorientationvector_items, str):
                                        raise TypeError(
                                            "normorientationvector_items takes several elements, got a str"
                                        )

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [normorientationvector_items]:
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
                                        isinstance(
                                            self.type_value_list_element, aas.Property
                                        )
                                        or isinstance(
                                            self.type_value_list_element, aas.Range
                                        )
                                        and not isinstance(
                                            new.value_type, self.value_type_list_element
                                        )
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
                                cartOffsetVector: Optional[CartOffsetVector] = None,
                                normOrientationVector: Optional[
                                    Union[
                                        Iterable[
                                            NormOrientationVector.Normorientationvector_item
                                        ],
                                        NormOrientationVector,
                                    ]
                                ] = None,
                                id_short: Optional[str] = r"CartRefSystem",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(normOrientationVector, str):
                                    raise TypeError(
                                        "normOrientationVector takes several elements, got a str"
                                    )

                                # Build a submodel element if a raw value was passed in the argument

                                if (
                                    normOrientationVector is not None
                                    and not isinstance(
                                        normOrientationVector, aas.SubmodelElement
                                    )
                                ):
                                    normOrientationVector = self.NormOrientationVector(
                                        normOrientationVector
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [cartOffsetVector, normOrientationVector]:
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

                        class CartBoundingVector(aas.SubmodelElementCollection):

                            class X(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"X",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/X/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class Y(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Y",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Y/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class Z(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Z",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Z/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                x: Union[str, X],
                                y: Union[str, Y],
                                z: Union[str, Z],
                                id_short: Optional[str] = r"CartBoundingVector",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if x is not None and not isinstance(
                                    x, aas.SubmodelElement
                                ):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument

                                if y is not None and not isinstance(
                                    y, aas.SubmodelElement
                                ):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument

                                if z is not None and not isinstance(
                                    z, aas.SubmodelElement
                                ):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [x, y, z]:
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
                            boundingBoxKind: Union[str, BoundingBoxKind],
                            cartBoundingVector: CartBoundingVector,
                            cartRefSystem: Optional[CartRefSystem] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if boundingBoxKind is not None and not isinstance(
                                boundingBoxKind, aas.SubmodelElement
                            ):
                                boundingBoxKind = self.BoundingBoxKind(boundingBoxKind)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                boundingBoxKind,
                                cartRefSystem,
                                cartBoundingVector,
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
                        cartboundingbox_items: Optional[
                            Iterable[Cartboundingbox_item]
                        ] = None,
                        id_short: Optional[str] = r"CartBoundingBox",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(cartboundingbox_items, str):
                            raise TypeError(
                                "cartboundingbox_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [cartboundingbox_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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

                class CartRefSystem(aas.SubmodelElementList):

                    class Cartrefsystem_item(aas.SubmodelElementCollection):

                        class CartOffsetVector(aas.SubmodelElementCollection):

                            class X(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"X",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/X/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class Y(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Y",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Y/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                            class Z(aas.Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Z",
                                    value_type: aas.DataTypeDefXsd = str,
                                    value_id: Optional[aas.Reference] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Z/1/0",
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
                                                value=r"One",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                x: Union[str, X],
                                y: Union[str, Y],
                                z: Union[str, Z],
                                id_short: Optional[str] = r"CartOffsetVector",
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
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument

                                if x is not None and not isinstance(
                                    x, aas.SubmodelElement
                                ):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument

                                if y is not None and not isinstance(
                                    y, aas.SubmodelElement
                                ):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument

                                if z is not None and not isinstance(
                                    z, aas.SubmodelElement
                                ):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [x, y, z]:
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

                        class NormOrientationVector(aas.SubmodelElementList):

                            class Normorientationvector_item(
                                aas.SubmodelElementCollection
                            ):

                                class X(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"X",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/X/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class Y(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Y",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Y/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

                                class Z(aas.Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Z",
                                        value_type: aas.DataTypeDefXsd = str,
                                        value_id: Optional[aas.Reference] = None,
                                        display_name: Optional[
                                            aas.MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            aas.MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            aas.Reference
                                        ] = aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Z/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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
                                    x: Union[str, X],
                                    y: Union[str, Y],
                                    z: Union[str, Z],
                                    id_short: Optional[str] = None,
                                    display_name: Optional[
                                        aas.MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[
                                        aas.MultiLanguageTextType
                                    ] = None,
                                    semantic_id: Optional[
                                        aas.Reference
                                    ] = aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0",
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
                                                value=r"Three",
                                                value_id=None,
                                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument

                                    if x is not None and not isinstance(
                                        x, aas.SubmodelElement
                                    ):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if y is not None and not isinstance(
                                        y, aas.SubmodelElement
                                    ):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if z is not None and not isinstance(
                                        z, aas.SubmodelElement
                                    ):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [x, y, z]:
                                        if se_arg is None:
                                            continue
                                        elif isinstance(se_arg, aas.SubmodelElement):
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
                                normorientationvector_items: Iterable[
                                    Normorientationvector_item
                                ],
                                id_short: Optional[str] = r"NormOrientationVector",
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
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0",
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
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # A str would be split into its characters
                                if isinstance(normorientationvector_items, str):
                                    raise TypeError(
                                        "normorientationvector_items takes several elements, got a str"
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [normorientationvector_items]:
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
                                    isinstance(
                                        self.type_value_list_element, aas.Property
                                    )
                                    or isinstance(
                                        self.type_value_list_element, aas.Range
                                    )
                                    and not isinstance(
                                        new.value_type, self.value_type_list_element
                                    )
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
                            cartOffsetVector: Optional[CartOffsetVector] = None,
                            normOrientationVector: Optional[
                                Union[
                                    Iterable[
                                        NormOrientationVector.Normorientationvector_item
                                    ],
                                    NormOrientationVector,
                                ]
                            ] = None,
                            id_short: Optional[str] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0",
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
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(normOrientationVector, str):
                                raise TypeError(
                                    "normOrientationVector takes several elements, got a str"
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if normOrientationVector is not None and not isinstance(
                                normOrientationVector, aas.SubmodelElement
                            ):
                                normOrientationVector = self.NormOrientationVector(
                                    normOrientationVector
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [cartOffsetVector, normOrientationVector]:
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
                        cartrefsystem_items: Optional[
                            Iterable[Cartrefsystem_item]
                        ] = None,
                        id_short: Optional[str] = r"CartRefSystem",
                        type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0",
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
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # A str would be split into its characters
                        if isinstance(cartrefsystem_items, str):
                            raise TypeError(
                                "cartrefsystem_items takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [cartrefsystem_items]:
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
                            isinstance(self.type_value_list_element, aas.Property)
                            or isinstance(self.type_value_list_element, aas.Range)
                            and not isinstance(
                                new.value_type, self.value_type_list_element
                            )
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
                    representation: Union[str, Representation],
                    lengthUnit: Union[str, LengthUnit],
                    cartBoundingBox: Optional[
                        Union[
                            Iterable[CartBoundingBox.Cartboundingbox_item],
                            CartBoundingBox,
                        ]
                    ] = None,
                    cartRefSystem: Optional[
                        Union[Iterable[CartRefSystem.Cartrefsystem_item], CartRefSystem]
                    ] = None,
                    id_short: Optional[str] = r"Geometry",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/1/0",
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
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if representation is not None and not isinstance(
                        representation, aas.SubmodelElement
                    ):
                        representation = self.Representation(representation)

                    # Build a submodel element if a raw value was passed in the argument

                    if lengthUnit is not None and not isinstance(
                        lengthUnit, aas.SubmodelElement
                    ):
                        lengthUnit = self.LengthUnit(lengthUnit)

                    # A str would be split into its characters
                    if isinstance(cartBoundingBox, str):
                        raise TypeError(
                            "cartBoundingBox takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if cartBoundingBox is not None and not isinstance(
                        cartBoundingBox, aas.SubmodelElement
                    ):
                        cartBoundingBox = self.CartBoundingBox(cartBoundingBox)

                    # A str would be split into its characters
                    if isinstance(cartRefSystem, str):
                        raise TypeError(
                            "cartRefSystem takes several elements, got a str"
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if cartRefSystem is not None and not isinstance(
                        cartRefSystem, aas.SubmodelElement
                    ):
                        cartRefSystem = self.CartRefSystem(cartRefSystem)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        representation,
                        lengthUnit,
                        cartBoundingBox,
                        cartRefSystem,
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
                file: File,
                capability: Optional[Capability] = None,
                geometry: Optional[Geometry] = None,
                id_short: Optional[str] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/Models3D/Model3D/1/0",
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
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [file, capability, geometry]:
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
            model3d_items: Optional[Iterable[Model3d_item]] = None,
            id_short: Optional[str] = r"Model3D",
            type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
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
                        value=r"https://admin-shell.io/idta/Models3D/Model3D/1/0",
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
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(model3d_items, str):
                raise TypeError("model3d_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [model3d_items]:
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
                isinstance(self.type_value_list_element, aas.Property)
                or isinstance(self.type_value_list_element, aas.Range)
                and not isinstance(new.value_type, self.value_type_list_element)
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
        model3D: Union[Iterable[Model3D.Model3d_item], Model3D],
        id_short: Optional[str] = r"Models3D",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[
            aas.AdministrativeInformation
        ] = aas.AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=None,
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/Models3D/1/0",
                ),
            ),
            type_=aas.Submodel,
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
        if isinstance(model3D, str):
            raise TypeError("model3D takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if model3D is not None and not isinstance(model3D, aas.SubmodelElement):
            model3D = self.Model3D(model3D)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [model3D]:
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
