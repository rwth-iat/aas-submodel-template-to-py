from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class Models3D(Submodel):

    class Model3D(SubmodelElementList):

        class Model3d_item(SubmodelElementCollection):

            class File(SubmodelElementCollection):

                class FileId(SubmodelElementList):

                    class Fileid_item(SubmodelElementCollection):

                        class FileDomainId(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileDomainId",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/FileDomaniId/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class ValueId(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ValueId",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/ValueId/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class IsPrimary(Property):

                            def __init__(
                                self,
                                value: bool,
                                id_short: Optional[str] = r"IsPrimary",
                                value_type: DataTypeDefXsd = bool,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/IsPrimary/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                            id_short: Optional[str] = r"fileid_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if fileDomainId and not isinstance(
                                fileDomainId, SubmodelElement
                            ):
                                fileDomainId = self.FileDomainId(fileDomainId)

                            # Build a submodel element if a raw value was passed in the argument
                            if valueId and not isinstance(valueId, SubmodelElement):
                                valueId = self.ValueId(valueId)

                            # Build a list of submodel elements if a raw values were passed in the argument
                            if isPrimary and all(
                                [isinstance(i, bool) for i in isPrimary]
                            ):
                                isPrimary = [self.IsPrimary(i) for i in isPrimary]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [fileDomainId, valueId, isPrimary]:
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
                        fileid_items: Optional[Iterable[Fileid_item]] = None,
                        id_short: Optional[str] = r"FileId",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileid_items]:
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

                class FileVersion(SubmodelElementList):

                    class Fileversion_item(SubmodelElementCollection):

                        class Title(MultiLanguageProperty):

                            def __init__(
                                self,
                                value: LangStringSet,
                                id_short: Optional[str] = r"Title",
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/Title/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class FileName(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileName",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileName/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class FileVersionId(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"FileVersionId",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileVersionID/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/StatusValue/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class SetDate(Property):

                            def __init__(
                                self,
                                value: Date,
                                id_short: Optional[str] = r"SetDate",
                                value_type: DataTypeDefXsd = Date,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SetDate/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class BasedOn(SubmodelElementList):

                            class Basedon_item(ReferenceElement):

                                def __init__(
                                    self,
                                    value: Reference,
                                    id_short: Optional[str] = r"basedon_item",
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    Iterable[Union[Reference, Basedon_item]]
                                ] = None,
                                id_short: Optional[str] = r"BasedOn",
                                type_value_list_element: SubmodelElement = ReferenceElement,
                                semantic_id_list_element: Optional[Reference] = None,
                                value_type_list_element: Optional[
                                    DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a list of submodel elements if a raw values were passed in the argument
                                if basedon_items and all(
                                    [isinstance(i, Reference) for i in basedon_items]
                                ):
                                    basedon_items = [
                                        self.Basedon_item(i) for i in basedon_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [basedon_items]:
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

                        class RefersTo(SubmodelElementList):

                            class Refersto_item(ReferenceElement):

                                def __init__(
                                    self,
                                    value: Reference,
                                    id_short: Optional[str] = r"refersto_item",
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    Iterable[Union[Reference, Refersto_item]]
                                ] = None,
                                id_short: Optional[str] = r"RefersTo",
                                type_value_list_element: SubmodelElement = ReferenceElement,
                                semantic_id_list_element: Optional[Reference] = None,
                                value_type_list_element: Optional[
                                    DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a list of submodel elements if a raw values were passed in the argument
                                if refersto_items and all(
                                    [isinstance(i, Reference) for i in refersto_items]
                                ):
                                    refersto_items = [
                                        self.Refersto_item(i) for i in refersto_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [refersto_items]:
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

                        class PreviewFile(File):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"PreviewFile",
                                content_type: str = r"image/png",
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/PreviewFile/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class DigitalFile(File):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"DigitalFile",
                                content_type: str = r"image/png",
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/DigitalFile/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class ExternalFile(SubmodelElementList):

                            class Externalfile_item(SubmodelElementCollection):

                                class ExternalUrl(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"ExternalUrl",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/ExternalUrl/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class FileIdentifier(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"FileIdentifier",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/FileIdentifier/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class HostOrganization(SubmodelElementCollection):

                                    class OrganizationName(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"OrganizationName",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationName/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                            id_short: Optional[
                                                str
                                            ] = r"OrganizationOfficialName",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationOfficialName/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument
                                        if organizationName and not isinstance(
                                            organizationName, SubmodelElement
                                        ):
                                            organizationName = self.OrganizationName(
                                                organizationName
                                            )

                                        # Build a submodel element if a raw value was passed in the argument
                                        if organizationOfficialName and not isinstance(
                                            organizationOfficialName, SubmodelElement
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

                                class Api(SubmodelElementList):

                                    class Api_item(SubmodelElementCollection):

                                        class ApiVersion(Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[str] = r"ApiVersion",
                                                value_type: DataTypeDefXsd = str,
                                                value_id: Optional[Reference] = None,
                                                display_name: Optional[
                                                    MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    Reference
                                                ] = ExternalReference(
                                                    key=(
                                                        Key(
                                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiVersion/1/0",
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
                                                            value=r"One",
                                                            value_id=None,
                                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                        class ApiDocumentationUrl(Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[
                                                    str
                                                ] = r"ApiDocumentationUrl",
                                                value_type: DataTypeDefXsd = str,
                                                value_id: Optional[Reference] = None,
                                                display_name: Optional[
                                                    MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    Reference
                                                ] = ExternalReference(
                                                    key=(
                                                        Key(
                                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiDocumentationUrl/1/0",
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
                                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                        class ApiSpecificationUrl(Property):

                                            def __init__(
                                                self,
                                                value: str,
                                                id_short: Optional[
                                                    str
                                                ] = r"ApiSpecificationUrl",
                                                value_type: DataTypeDefXsd = str,
                                                value_id: Optional[Reference] = None,
                                                display_name: Optional[
                                                    MultiLanguageNameType
                                                ] = None,
                                                category: Optional[str] = None,
                                                description: Optional[
                                                    MultiLanguageTextType
                                                ] = None,
                                                semantic_id: Optional[
                                                    Reference
                                                ] = ExternalReference(
                                                    key=(
                                                        Key(
                                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiSpecificationUrl/1/0",
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
                                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                            id_short: Optional[str] = r"api_item",
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0",
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
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                                        semantic_id=None,
                                                        supplemental_semantic_id=(),
                                                    ),
                                                )

                                            if embedded_data_specifications is None:
                                                embedded_data_specifications = []

                                            # Build a submodel element if a raw value was passed in the argument
                                            if apiVersion and not isinstance(
                                                apiVersion, SubmodelElement
                                            ):
                                                apiVersion = self.ApiVersion(apiVersion)

                                            # Build a submodel element if a raw value was passed in the argument
                                            if apiDocumentationUrl and not isinstance(
                                                apiDocumentationUrl, SubmodelElement
                                            ):
                                                apiDocumentationUrl = (
                                                    self.ApiDocumentationUrl(
                                                        apiDocumentationUrl
                                                    )
                                                )

                                            # Build a submodel element if a raw value was passed in the argument
                                            if apiSpecificationUrl and not isinstance(
                                                apiSpecificationUrl, SubmodelElement
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
                                                    se_arg, SubmodelElement
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
                                        api_items: Optional[Iterable[Api_item]] = None,
                                        id_short: Optional[str] = r"Api",
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
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0",
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
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [api_items]:
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
                                                new.value_type,
                                                self.value_type_list_element,
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
                                                    and new.semantic_id
                                                    != item.semantic_id
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
                                    externalUrl: Union[str, ExternalUrl],
                                    fileIdentifier: Union[str, FileIdentifier],
                                    hostOrganization: HostOrganization,
                                    api: Optional[Api] = None,
                                    id_short: Optional[str] = r"externalfile_item",
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument
                                    if externalUrl and not isinstance(
                                        externalUrl, SubmodelElement
                                    ):
                                        externalUrl = self.ExternalUrl(externalUrl)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if fileIdentifier and not isinstance(
                                        fileIdentifier, SubmodelElement
                                    ):
                                        fileIdentifier = self.FileIdentifier(
                                            fileIdentifier
                                        )

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
                                type_value_list_element: SubmodelElement = SubmodelElementCollection,
                                semantic_id_list_element: Optional[Reference] = None,
                                value_type_list_element: Optional[
                                    DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [externalfile_items]:
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

                        class FileFormat(SubmodelElementCollection):

                            class FormatName(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class FormatVersion(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatVersion",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatVersion/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class FormatQualifier(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"FormatQualifier",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatQualifier/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if formatName and not isinstance(
                                    formatName, SubmodelElement
                                ):
                                    formatName = self.FormatName(formatName)

                                # Build a submodel element if a raw value was passed in the argument
                                if formatVersion and not isinstance(
                                    formatVersion, SubmodelElement
                                ):
                                    formatVersion = self.FormatVersion(formatVersion)

                                # Build a submodel element if a raw value was passed in the argument
                                if formatQualifier and not isinstance(
                                    formatQualifier, SubmodelElement
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

                        class SourceApplication(SubmodelElementCollection):

                            class ApplicationName(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class ApplicationVersion(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationVersion",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationVersion/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class ApplicationQualifier(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"ApplicationQualifier",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationQualifier/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class Api(SubmodelElementList):

                                class Api_item(SubmodelElementCollection):

                                    class ApiVersion(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"ApiVersion",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiVersion/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                    class ApiDocumentationUrl(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"ApiDocumentationUrl",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiDocumentationUrl/1/0",
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
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                    class ApiSpecificationUrl(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[
                                                str
                                            ] = r"ApiSpecificationUrl",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiSpecificationUrl/1/0",
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
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                        id_short: Optional[str] = r"api_item",
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0",
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
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument
                                        if apiVersion and not isinstance(
                                            apiVersion, SubmodelElement
                                        ):
                                            apiVersion = self.ApiVersion(apiVersion)

                                        # Build a submodel element if a raw value was passed in the argument
                                        if apiDocumentationUrl and not isinstance(
                                            apiDocumentationUrl, SubmodelElement
                                        ):
                                            apiDocumentationUrl = (
                                                self.ApiDocumentationUrl(
                                                    apiDocumentationUrl
                                                )
                                            )

                                        # Build a submodel element if a raw value was passed in the argument
                                        if apiSpecificationUrl and not isinstance(
                                            apiSpecificationUrl, SubmodelElement
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
                                    api_items: Optional[Iterable[Api_item]] = None,
                                    id_short: Optional[str] = r"Api",
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
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [api_items]:
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

                            class VendorOrganization(SubmodelElementCollection):

                                class OrganizationName(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"OrganizationName",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationName/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                        id_short: Optional[
                                            str
                                        ] = r"OrganizationOfficialName",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationOfficialName/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument
                                    if organizationName and not isinstance(
                                        organizationName, SubmodelElement
                                    ):
                                        organizationName = self.OrganizationName(
                                            organizationName
                                        )

                                    # Build a submodel element if a raw value was passed in the argument
                                    if organizationOfficialName and not isinstance(
                                        organizationOfficialName, SubmodelElement
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
                                api: Optional[Api] = None,
                                id_short: Optional[str] = r"SourceApplication",
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if applicationName and not isinstance(
                                    applicationName, SubmodelElement
                                ):
                                    applicationName = self.ApplicationName(
                                        applicationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if applicationVersion and not isinstance(
                                    applicationVersion, SubmodelElement
                                ):
                                    applicationVersion = self.ApplicationVersion(
                                        applicationVersion
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if applicationQualifier and not isinstance(
                                    applicationQualifier, SubmodelElement
                                ):
                                    applicationQualifier = self.ApplicationQualifier(
                                        applicationQualifier
                                    )

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

                        class ProvidingOrganization(SubmodelElementCollection):

                            class OrganizationName(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"OrganizationName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/OrganizationName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[
                                        str
                                    ] = r"OrganizationOfficialName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization//OrganizationOfficialName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if organizationName and not isinstance(
                                    organizationName, SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(
                                        organizationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if organizationOfficialName and not isinstance(
                                    organizationOfficialName, SubmodelElement
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
                            title: Union[LangStringSet, Title],
                            fileName: Union[str, FileName],
                            fileVersionId: Union[str, FileVersionId],
                            statusValue: Union[str, StatusValue],
                            setDate: Union[Date, SetDate],
                            previewFile: PreviewFile,
                            fileFormat: FileFormat,
                            providingOrganization: ProvidingOrganization,
                            basedOn: Optional[BasedOn] = None,
                            refersTo: Optional[RefersTo] = None,
                            digitalFile: Optional[DigitalFile] = None,
                            externalFile: Optional[ExternalFile] = None,
                            sourceApplication: Optional[SourceApplication] = None,
                            id_short: Optional[str] = r"fileversion_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if title and not isinstance(title, SubmodelElement):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument
                            if fileName and not isinstance(fileName, SubmodelElement):
                                fileName = self.FileName(fileName)

                            # Build a submodel element if a raw value was passed in the argument
                            if fileVersionId and not isinstance(
                                fileVersionId, SubmodelElement
                            ):
                                fileVersionId = self.FileVersionId(fileVersionId)

                            # Build a submodel element if a raw value was passed in the argument
                            if statusValue and not isinstance(
                                statusValue, SubmodelElement
                            ):
                                statusValue = self.StatusValue(statusValue)

                            # Build a submodel element if a raw value was passed in the argument
                            if setDate and not isinstance(setDate, SubmodelElement):
                                setDate = self.SetDate(setDate)

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
                        fileversion_items: Optional[Iterable[Fileversion_item]] = None,
                        id_short: Optional[str] = r"FileVersion",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileversion_items]:
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

                class ConsumingApplication(SubmodelElementList):

                    class Consumingapplication_item(SubmodelElementCollection):

                        class ApplicationName(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationName",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationName/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class ApplicationVersion(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationVersion",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationVersion/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class ApplicationQualifier(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ApplicationQualifier",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationQualifier1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class VendorOrganization(SubmodelElementCollection):

                            class OrganizationName(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"OrganizationName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[
                                        str
                                    ] = r"OrganizationOfficialName",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationOfficialName/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if organizationName and not isinstance(
                                    organizationName, SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(
                                        organizationName
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if organizationOfficialName and not isinstance(
                                    organizationOfficialName, SubmodelElement
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

                        class Api(SubmodelElementList):

                            class Api_item(SubmodelElementCollection):

                                class ApiVersion(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"ApiVersion",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiVersion/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class ApiDocumentationUrl(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[
                                            str
                                        ] = r"ApiDocumentationUrl",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiDocumentationUrl/1/0",
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
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class ApiSpecificationUrl(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[
                                            str
                                        ] = r"ApiSpecificationUrl",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiSpecificationUrl/1/0",
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
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[str] = r"api_item",
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument
                                    if apiVersion and not isinstance(
                                        apiVersion, SubmodelElement
                                    ):
                                        apiVersion = self.ApiVersion(apiVersion)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if apiDocumentationUrl and not isinstance(
                                        apiDocumentationUrl, SubmodelElement
                                    ):
                                        apiDocumentationUrl = self.ApiDocumentationUrl(
                                            apiDocumentationUrl
                                        )

                                    # Build a submodel element if a raw value was passed in the argument
                                    if apiSpecificationUrl and not isinstance(
                                        apiSpecificationUrl, SubmodelElement
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
                                type_value_list_element: SubmodelElement = SubmodelElementCollection,
                                semantic_id_list_element: Optional[Reference] = None,
                                value_type_list_element: Optional[
                                    DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [api_items]:
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
                            applicationName: Union[str, ApplicationName],
                            applicationVersion: Union[str, ApplicationVersion],
                            applicationQualifier: Union[str, ApplicationQualifier],
                            vendorOrganization: VendorOrganization,
                            api: Optional[Api] = None,
                            id_short: Optional[str] = r"consumingapplication_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if applicationName and not isinstance(
                                applicationName, SubmodelElement
                            ):
                                applicationName = self.ApplicationName(applicationName)

                            # Build a submodel element if a raw value was passed in the argument
                            if applicationVersion and not isinstance(
                                applicationVersion, SubmodelElement
                            ):
                                applicationVersion = self.ApplicationVersion(
                                    applicationVersion
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if applicationQualifier and not isinstance(
                                applicationQualifier, SubmodelElement
                            ):
                                applicationQualifier = self.ApplicationQualifier(
                                    applicationQualifier
                                )

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
                        consumingapplication_items: Optional[
                            Iterable[Consumingapplication_item]
                        ] = None,
                        id_short: Optional[str] = r"ConsumingApplication",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [consumingapplication_items]:
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

                class FileClassification(SubmodelElementList):

                    class Fileclassification_item(SubmodelElementCollection):

                        class ClassId(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ClassId",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassId/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassName/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/File/ClassificationSystem/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                            id_short: Optional[str] = r"fileclassification_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

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
                        fileclassification_items: Iterable[Fileclassification_item],
                        id_short: Optional[str] = r"FileClassification",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [fileclassification_items]:
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
                    fileId: FileId,
                    fileClassification: FileClassification,
                    fileVersion: Optional[FileVersion] = None,
                    consumingApplication: Optional[ConsumingApplication] = None,
                    id_short: Optional[str] = r"File",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/File/1/0",
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
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

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

            class Capability(SubmodelElementCollection):

                class PosModelPurpose(SubmodelElementList):

                    class Posmodelpurpose_item(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"posmodelpurpose_item",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        type_value_list_element: SubmodelElement = Property,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a list of submodel elements if a raw values were passed in the argument
                        if posmodelpurpose_items and all(
                            [isinstance(i, str) for i in posmodelpurpose_items]
                        ):
                            posmodelpurpose_items = [
                                self.Posmodelpurpose_item(i)
                                for i in posmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [posmodelpurpose_items]:
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

                class NegModelPurpose(SubmodelElementList):

                    class Negmodelpurpose_item(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"negmodelpurpose_item",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        type_value_list_element: SubmodelElement = Property,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a list of submodel elements if a raw values were passed in the argument
                        if negmodelpurpose_items and all(
                            [isinstance(i, str) for i in negmodelpurpose_items]
                        ):
                            negmodelpurpose_items = [
                                self.Negmodelpurpose_item(i)
                                for i in negmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [negmodelpurpose_items]:
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

                class EmbeddedInfo(SubmodelElementList):

                    class Embeddedinfo_item(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"embeddedinfo_item",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        type_value_list_element: SubmodelElement = Property,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a list of submodel elements if a raw values were passed in the argument
                        if embeddedinfo_items and all(
                            [isinstance(i, str) for i in embeddedinfo_items]
                        ):
                            embeddedinfo_items = [
                                self.Embeddedinfo_item(i) for i in embeddedinfo_items
                            ]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [embeddedinfo_items]:
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

                class State(SubmodelElementList):

                    class State_item(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"state_item",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                        type_value_list_element: SubmodelElement = Property,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = str,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a list of submodel elements if a raw values were passed in the argument
                        if state_items and all(
                            [isinstance(i, str) for i in state_items]
                        ):
                            state_items = [self.State_item(i) for i in state_items]

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [state_items]:
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

                class ObjectType(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ObjectType",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/ObjectType/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class Origin(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Origin",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Origin/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class Simplification(SubmodelElementCollection):

                    class Description(Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Description",
                            value_type: DataTypeDefXsd = str,
                            value_id: Optional[Reference] = None,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/LevelDescription/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                    class ReducedElements(SubmodelElementList):

                        class Reducedelements_item(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"reducedelements_item",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
                            type_value_list_element: SubmodelElement = Property,
                            semantic_id_list_element: Optional[Reference] = None,
                            value_type_list_element: Optional[DataTypeDefXsd] = str,
                            order_relevant: bool = True,
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a list of submodel elements if a raw values were passed in the argument
                            if reducedelements_items and all(
                                [isinstance(i, str) for i in reducedelements_items]
                            ):
                                reducedelements_items = [
                                    self.Reducedelements_item(i)
                                    for i in reducedelements_items
                                ]

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [reducedelements_items]:
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

                    class DerivedFrom(ReferenceElement):

                        def __init__(
                            self,
                            value: Reference,
                            id_short: Optional[str] = r"DerivedFrom",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/DerivedFrom/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                            Union[Iterable[str], ReducedElements]
                        ] = None,
                        derivedFrom: Optional[Union[Reference, DerivedFrom]] = None,
                        id_short: Optional[str] = r"Simplification",
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument
                        if description_ and not isinstance(
                            description_, SubmodelElement
                        ):
                            description_ = self.Description(description_)

                        # Build a submodel element if a raw value was passed in the argument
                        if reducedElements and not isinstance(
                            reducedElements, SubmodelElement
                        ):
                            reducedElements = self.ReducedElements(reducedElements)

                        # Build a submodel element if a raw value was passed in the argument
                        if derivedFrom and not isinstance(derivedFrom, SubmodelElement):
                            derivedFrom = self.DerivedFrom(derivedFrom)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [description_, reducedElements, derivedFrom]:
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
                    posModelPurpose: Union[Iterable[str], PosModelPurpose],
                    origin: Union[str, Origin],
                    negModelPurpose: Optional[
                        Union[Iterable[str], NegModelPurpose]
                    ] = None,
                    embeddedInfo: Optional[Union[Iterable[str], EmbeddedInfo]] = None,
                    state: Optional[Union[Iterable[str], State]] = None,
                    objectType: Optional[Union[str, ObjectType]] = None,
                    simplification: Optional[Simplification] = None,
                    id_short: Optional[str] = r"Capability",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Capability/1/0",
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
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if posModelPurpose and not isinstance(
                        posModelPurpose, SubmodelElement
                    ):
                        posModelPurpose = self.PosModelPurpose(posModelPurpose)

                    # Build a submodel element if a raw value was passed in the argument
                    if negModelPurpose and not isinstance(
                        negModelPurpose, SubmodelElement
                    ):
                        negModelPurpose = self.NegModelPurpose(negModelPurpose)

                    # Build a submodel element if a raw value was passed in the argument
                    if embeddedInfo and not isinstance(embeddedInfo, SubmodelElement):
                        embeddedInfo = self.EmbeddedInfo(embeddedInfo)

                    # Build a submodel element if a raw value was passed in the argument
                    if state and not isinstance(state, SubmodelElement):
                        state = self.State(state)

                    # Build a submodel element if a raw value was passed in the argument
                    if objectType and not isinstance(objectType, SubmodelElement):
                        objectType = self.ObjectType(objectType)

                    # Build a submodel element if a raw value was passed in the argument
                    if origin and not isinstance(origin, SubmodelElement):
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

            class Geometry(SubmodelElementCollection):

                class Representation(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Representation",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/Representation/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class LengthUnit(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"LengthUnit",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/LengthUnit/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class CartBoundingBox(SubmodelElementList):

                    class Cartboundingbox_item(SubmodelElementCollection):

                        class BoundingBoxKind(Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"BoundingBoxKind",
                                value_type: DataTypeDefXsd = str,
                                value_id: Optional[Reference] = None,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/BoundingBoxKind/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

                        class CartRefSystem(SubmodelElementCollection):

                            class CartOffsetVector(SubmodelElementCollection):

                                class X(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"X",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/X/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class Y(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Y",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Y/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class Z(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Z",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Z/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument
                                    if x and not isinstance(x, SubmodelElement):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if y and not isinstance(y, SubmodelElement):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if z and not isinstance(z, SubmodelElement):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [x, y, z]:
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
                                        display_name=display_name,
                                        category=category,
                                        description=description,
                                        semantic_id=semantic_id,
                                        qualifier=qualifier,
                                        extension=extension,
                                        supplemental_semantic_id=supplemental_semantic_id,
                                        embedded_data_specifications=embedded_data_specifications,
                                    )

                            class NormOrientationVector(SubmodelElementList):

                                class Normorientationvector_item(
                                    SubmodelElementCollection
                                ):

                                    class X(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"X",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/X/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                    class Y(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"Y",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Y/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                    class Z(Property):

                                        def __init__(
                                            self,
                                            value: str,
                                            id_short: Optional[str] = r"Z",
                                            value_type: DataTypeDefXsd = str,
                                            value_id: Optional[Reference] = None,
                                            display_name: Optional[
                                                MultiLanguageNameType
                                            ] = None,
                                            category: Optional[str] = None,
                                            description: Optional[
                                                MultiLanguageTextType
                                            ] = None,
                                            semantic_id: Optional[
                                                Reference
                                            ] = ExternalReference(
                                                key=(
                                                    Key(
                                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Z/1/0",
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
                                                        value=r"One",
                                                        value_id=None,
                                                        kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                        id_short: Optional[
                                            str
                                        ] = r"normorientationvector_item",
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0",
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
                                                    value=r"Three",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                                    semantic_id=None,
                                                    supplemental_semantic_id=(),
                                                ),
                                            )

                                        if embedded_data_specifications is None:
                                            embedded_data_specifications = []

                                        # Build a submodel element if a raw value was passed in the argument
                                        if x and not isinstance(x, SubmodelElement):
                                            x = self.X(x)

                                        # Build a submodel element if a raw value was passed in the argument
                                        if y and not isinstance(y, SubmodelElement):
                                            y = self.Y(y)

                                        # Build a submodel element if a raw value was passed in the argument
                                        if z and not isinstance(z, SubmodelElement):
                                            z = self.Z(z)

                                        # Add all passed/initialized submodel elements to a single list
                                        embedded_submodel_elements = []
                                        for se_arg in [x, y, z]:
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
                                    normorientationvector_items: Normorientationvector_item,
                                    id_short: Optional[str] = r"NormOrientationVector",
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
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [normorientationvector_items]:
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
                                cartOffsetVector: Optional[CartOffsetVector] = None,
                                normOrientationVector: Optional[
                                    NormOrientationVector
                                ] = None,
                                id_short: Optional[str] = r"CartRefSystem",
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [cartOffsetVector, normOrientationVector]:
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

                        class CartBoundingVector(SubmodelElementCollection):

                            class X(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"X",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/X/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class Y(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Y",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Y/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class Z(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Z",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Z/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if x and not isinstance(x, SubmodelElement):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument
                                if y and not isinstance(y, SubmodelElement):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument
                                if z and not isinstance(z, SubmodelElement):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [x, y, z]:
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
                            boundingBoxKind: Union[str, BoundingBoxKind],
                            cartBoundingVector: CartBoundingVector,
                            cartRefSystem: Optional[CartRefSystem] = None,
                            id_short: Optional[str] = r"cartboundingbox_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument
                            if boundingBoxKind and not isinstance(
                                boundingBoxKind, SubmodelElement
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
                        cartboundingbox_items: Optional[
                            Iterable[Cartboundingbox_item]
                        ] = None,
                        id_short: Optional[str] = r"CartBoundingBox",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [cartboundingbox_items]:
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

                class CartRefSystem(SubmodelElementList):

                    class Cartrefsystem_item(SubmodelElementCollection):

                        class CartOffsetVector(SubmodelElementCollection):

                            class X(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"X",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/X/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class Y(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Y",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Y/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

                            class Z(Property):

                                def __init__(
                                    self,
                                    value: str,
                                    id_short: Optional[str] = r"Z",
                                    value_type: DataTypeDefXsd = str,
                                    value_id: Optional[Reference] = None,
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Z/1/0",
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
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Build a submodel element if a raw value was passed in the argument
                                if x and not isinstance(x, SubmodelElement):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument
                                if y and not isinstance(y, SubmodelElement):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument
                                if z and not isinstance(z, SubmodelElement):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [x, y, z]:
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

                        class NormOrientationVector(SubmodelElementList):

                            class Normorientationvector_item(SubmodelElementCollection):

                                class X(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"X",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/X/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class Y(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Y",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Y/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                                class Z(Property):

                                    def __init__(
                                        self,
                                        value: str,
                                        id_short: Optional[str] = r"Z",
                                        value_type: DataTypeDefXsd = str,
                                        value_id: Optional[Reference] = None,
                                        display_name: Optional[
                                            MultiLanguageNameType
                                        ] = None,
                                        category: Optional[str] = None,
                                        description: Optional[
                                            MultiLanguageTextType
                                        ] = None,
                                        semantic_id: Optional[
                                            Reference
                                        ] = ExternalReference(
                                            key=(
                                                Key(
                                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Z/1/0",
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
                                                    value=r"One",
                                                    value_id=None,
                                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                                    id_short: Optional[
                                        str
                                    ] = r"normorientationvector_item",
                                    display_name: Optional[
                                        MultiLanguageNameType
                                    ] = None,
                                    category: Optional[str] = None,
                                    description: Optional[MultiLanguageTextType] = None,
                                    semantic_id: Optional[
                                        Reference
                                    ] = ExternalReference(
                                        key=(
                                            Key(
                                                type_=KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0",
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
                                                value=r"Three",
                                                value_id=None,
                                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                                semantic_id=None,
                                                supplemental_semantic_id=(),
                                            ),
                                        )

                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []

                                    # Build a submodel element if a raw value was passed in the argument
                                    if x and not isinstance(x, SubmodelElement):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if y and not isinstance(y, SubmodelElement):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument
                                    if z and not isinstance(z, SubmodelElement):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list
                                    embedded_submodel_elements = []
                                    for se_arg in [x, y, z]:
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
                                normorientationvector_items: Normorientationvector_item,
                                id_short: Optional[str] = r"NormOrientationVector",
                                type_value_list_element: SubmodelElement = SubmodelElementCollection,
                                semantic_id_list_element: Optional[Reference] = None,
                                value_type_list_element: Optional[
                                    DataTypeDefXsd
                                ] = None,
                                order_relevant: bool = True,
                                display_name: Optional[MultiLanguageNameType] = None,
                                category: Optional[str] = None,
                                description: Optional[MultiLanguageTextType] = None,
                                semantic_id: Optional[Reference] = ExternalReference(
                                    key=(
                                        Key(
                                            type_=KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0",
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
                                            kind=QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                    )

                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [normorientationvector_items]:
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
                            cartOffsetVector: Optional[CartOffsetVector] = None,
                            normOrientationVector: Optional[
                                NormOrientationVector
                            ] = None,
                            id_short: Optional[str] = r"cartrefsystem_item",
                            display_name: Optional[MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[MultiLanguageTextType] = None,
                            semantic_id: Optional[Reference] = ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0",
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
                                        kind=QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [cartOffsetVector, normOrientationVector]:
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
                        cartrefsystem_items: Optional[
                            Iterable[Cartrefsystem_item]
                        ] = None,
                        id_short: Optional[str] = r"CartRefSystem",
                        type_value_list_element: SubmodelElement = SubmodelElementCollection,
                        semantic_id_list_element: Optional[Reference] = None,
                        value_type_list_element: Optional[DataTypeDefXsd] = None,
                        order_relevant: bool = True,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0",
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
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [cartrefsystem_items]:
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
                    representation: Union[str, Representation],
                    lengthUnit: Union[str, LengthUnit],
                    cartBoundingBox: Optional[CartBoundingBox] = None,
                    cartRefSystem: Optional[CartRefSystem] = None,
                    id_short: Optional[str] = r"Geometry",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/1/0",
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
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if representation and not isinstance(
                        representation, SubmodelElement
                    ):
                        representation = self.Representation(representation)

                    # Build a submodel element if a raw value was passed in the argument
                    if lengthUnit and not isinstance(lengthUnit, SubmodelElement):
                        lengthUnit = self.LengthUnit(lengthUnit)

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
                file: File,
                capability: Optional[Capability] = None,
                geometry: Optional[Geometry] = None,
                id_short: Optional[str] = r"model3d_item",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/Models3D/Model3D/1/0",
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
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
            model3d_items: Optional[Iterable[Model3d_item]] = None,
            id_short: Optional[str] = r"Model3D",
            type_value_list_element: SubmodelElement = SubmodelElementCollection,
            semantic_id_list_element: Optional[Reference] = None,
            value_type_list_element: Optional[DataTypeDefXsd] = None,
            order_relevant: bool = True,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = None,
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/Models3D/Model3D/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [model3d_items]:
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
        model3D: Model3D,
        id_short: Optional[str] = r"Models3D",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = None,
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=None,
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/Models3D/1/0",
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
        for se_arg in [model3D]:
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
