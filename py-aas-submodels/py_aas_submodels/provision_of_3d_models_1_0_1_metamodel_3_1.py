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


class Models3D(aas.Submodel):

    class Model3D(GeneratedSubmodelElementList):

        class Model3d_item(aas.SubmodelElementCollection):

            class File(aas.SubmodelElementCollection):

                class FileId(GeneratedSubmodelElementList):

                    class Fileid_item(aas.SubmodelElementCollection):

                        class FileDomainId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"FileDomainId",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/FileDomaniId/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ValueId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ValueId",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/ValueId/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class IsPrimary(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"IsPrimary",
                                    "value_type": bool,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/IsPrimary/1/0"
                                    ),
                                }

                            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            fileDomainId: Union[str, FileDomainId],
                            valueId: Union[str, ValueId],
                            isPrimary: Optional[Iterable[Union[bool, IsPrimary]]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if fileDomainId is not None and not isinstance(fileDomainId, aas.SubmodelElement):
                                fileDomainId = self.FileDomainId(fileDomainId)

                            # Build a submodel element if a raw value was passed in the argument

                            if valueId is not None and not isinstance(valueId, aas.SubmodelElement):
                                valueId = self.ValueId(valueId)

                            # A str would be split into its characters
                            if isinstance(isPrimary, str):
                                raise TypeError("isPrimary takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if isPrimary:
                                isPrimary = [
                                    i if isinstance(i, aas.SubmodelElement) else self.IsPrimary(i) for i in isPrimary
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(fileDomainId, valueId, isPrimary)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"FileId",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/File/FileId/1/0"),
                        }

                    def __init__(
                        self,
                        fileid_items: Optional[Iterable[Fileid_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(fileid_items, str):
                            raise TypeError("fileid_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(fileid_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class FileVersion(GeneratedSubmodelElementList):

                    class Fileversion_item(aas.SubmodelElementCollection):

                        class Title(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"Title",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/Title/1/0"
                                    ),
                                }

                            def __init__(
                                self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FileName(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"FileName",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileName/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class FileVersionId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"FileVersionId",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileVersionID/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class StatusValue(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"StatusValue",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/StatusValue/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class SetDate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"SetDate",
                                    "value_type": xsd.Date,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SetDate/1/0"
                                    ),
                                }

                            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class BasedOn(GeneratedSubmodelElementList):

                            class Basedon_item(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0"
                                        ),
                                    }

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"BasedOn",
                                    "type_value_list_element": aas.ReferenceElement,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/BasedOn/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                basedon_items: Optional[Iterable[Union[aas.Reference, Basedon_item]]] = None,
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(basedon_items, str):
                                    raise TypeError("basedon_items takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if basedon_items:
                                    basedon_items = [
                                        i if isinstance(i, aas.SubmodelElement) else self.Basedon_item(i)
                                        for i in basedon_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    basedon_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class RefersTo(GeneratedSubmodelElementList):

                            class Refersto_item(aas.ReferenceElement):

                                @staticmethod
                                def template_defaults() -> ReferenceElementMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0"
                                        ),
                                    }

                                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"RefersTo",
                                    "type_value_list_element": aas.ReferenceElement,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/RefersTo/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                refersto_items: Optional[Iterable[Union[aas.Reference, Refersto_item]]] = None,
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(refersto_items, str):
                                    raise TypeError("refersto_items takes several elements, got a str")

                                # Build submodel elements from raw values passed in the argument
                                if refersto_items:
                                    refersto_items = [
                                        i if isinstance(i, aas.SubmodelElement) else self.Refersto_item(i)
                                        for i in refersto_items
                                    ]

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    refersto_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class PreviewFile(aas.File):

                            @staticmethod
                            def template_defaults() -> FileMetadata:
                                return {
                                    "id_short": r"PreviewFile",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/PreviewFile/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                value: str,
                                content_type: Optional[str] = r"image/png",
                                **kwargs: Unpack[FileMetadata],
                            ):

                                super().__init__(
                                    value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                                )

                        class DigitalFile(aas.File):

                            @staticmethod
                            def template_defaults() -> FileMetadata:
                                return {
                                    "id_short": r"DigitalFile",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/DigitalFile/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                value: str,
                                content_type: Optional[str] = r"image/png",
                                **kwargs: Unpack[FileMetadata],
                            ):

                                super().__init__(
                                    value=value, content_type=content_type, **(self.template_defaults() | kwargs)
                                )

                        class ExternalFile(GeneratedSubmodelElementList):

                            class Externalfile_item(aas.SubmodelElementCollection):

                                class ExternalUrl(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"ExternalUrl",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/ExternalUrl/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class FileIdentifier(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"FileIdentifier",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/FileIdentifier/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class HostOrganization(aas.SubmodelElementCollection):

                                    class OrganizationName(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"OrganizationName",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationName/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class OrganizationOfficialName(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"OrganizationOfficialName",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/OrganizationOfficialName/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    @staticmethod
                                    def template_defaults() -> SubmodelElementCollectionMetadata:
                                        return {
                                            "id_short": r"HostOrganization",
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/HostOrganization/1/0"
                                            ),
                                        }

                                    def __init__(
                                        self,
                                        organizationName: Union[str, OrganizationName],
                                        organizationOfficialName: Union[str, OrganizationOfficialName],
                                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                    ):

                                        # Build a submodel element if a raw value was passed in the argument

                                        if organizationName is not None and not isinstance(
                                            organizationName, aas.SubmodelElement
                                        ):
                                            organizationName = self.OrganizationName(organizationName)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if organizationOfficialName is not None and not isinstance(
                                            organizationOfficialName, aas.SubmodelElement
                                        ):
                                            organizationOfficialName = self.OrganizationOfficialName(
                                                organizationOfficialName
                                            )

                                        # Add all passed/initialized submodel elements to a single list

                                        embedded_submodel_elements = collect_submodel_elements(
                                            organizationName, organizationOfficialName
                                        )

                                        super().__init__(
                                            value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                        )

                                class Api(GeneratedSubmodelElementList):

                                    class Api_item(aas.SubmodelElementCollection):

                                        class ApiVersion(aas.Property):

                                            @staticmethod
                                            def template_defaults() -> PropertyMetadata:
                                                return {
                                                    "id_short": r"ApiVersion",
                                                    "value_type": str,
                                                    "semantic_id": global_ref(
                                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiVersion/1/0"
                                                    ),
                                                }

                                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                                        class ApiDocumentationUrl(aas.Property):

                                            @staticmethod
                                            def template_defaults() -> PropertyMetadata:
                                                return {
                                                    "id_short": r"ApiDocumentationUrl",
                                                    "value_type": str,
                                                    "semantic_id": global_ref(
                                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiDocumentationUrl/1/0"
                                                    ),
                                                }

                                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                                        class ApiSpecificationUrl(aas.Property):

                                            @staticmethod
                                            def template_defaults() -> PropertyMetadata:
                                                return {
                                                    "id_short": r"ApiSpecificationUrl",
                                                    "value_type": str,
                                                    "semantic_id": global_ref(
                                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/ApiSpecificationUrl/1/0"
                                                    ),
                                                }

                                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                                        @staticmethod
                                        def template_defaults() -> SubmodelElementCollectionMetadata:
                                            return {
                                                "id_short": None,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0"
                                                ),
                                            }

                                        def __init__(
                                            self,
                                            apiVersion: Union[str, ApiVersion],
                                            apiDocumentationUrl: Optional[Union[str, ApiDocumentationUrl]] = None,
                                            apiSpecificationUrl: Optional[Union[str, ApiSpecificationUrl]] = None,
                                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                        ):

                                            # Build a submodel element if a raw value was passed in the argument

                                            if apiVersion is not None and not isinstance(
                                                apiVersion, aas.SubmodelElement
                                            ):
                                                apiVersion = self.ApiVersion(apiVersion)

                                            # Build a submodel element if a raw value was passed in the argument

                                            if apiDocumentationUrl is not None and not isinstance(
                                                apiDocumentationUrl, aas.SubmodelElement
                                            ):
                                                apiDocumentationUrl = self.ApiDocumentationUrl(apiDocumentationUrl)

                                            # Build a submodel element if a raw value was passed in the argument

                                            if apiSpecificationUrl is not None and not isinstance(
                                                apiSpecificationUrl, aas.SubmodelElement
                                            ):
                                                apiSpecificationUrl = self.ApiSpecificationUrl(apiSpecificationUrl)

                                            # Add all passed/initialized submodel elements to a single list

                                            embedded_submodel_elements = collect_submodel_elements(
                                                apiVersion, apiDocumentationUrl, apiSpecificationUrl
                                            )

                                            super().__init__(
                                                value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                            )

                                    @staticmethod
                                    def template_defaults() -> SubmodelElementListMetadata:
                                        return {
                                            "id_short": r"Api",
                                            "type_value_list_element": aas.SubmodelElementCollection,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/Api/1/0"
                                            ),
                                        }

                                    def __init__(
                                        self,
                                        api_items: Optional[Iterable[Api_item]] = None,
                                        **kwargs: Unpack[SubmodelElementListMetadata],
                                    ):

                                        # A str would be split into its characters
                                        if isinstance(api_items, str):
                                            raise TypeError("api_items takes several elements, got a str")

                                        # Add all passed/initialized submodel elements to a single list

                                        embedded_submodel_elements = collect_submodel_elements(
                                            api_items, number_repeated=False
                                        )

                                        super().__init__(
                                            value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                        )

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    externalUrl: Union[str, ExternalUrl],
                                    fileIdentifier: Union[str, FileIdentifier],
                                    hostOrganization: HostOrganization,
                                    api: Optional[Union[Iterable[Api.Api_item], Api]] = None,
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if externalUrl is not None and not isinstance(externalUrl, aas.SubmodelElement):
                                        externalUrl = self.ExternalUrl(externalUrl)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if fileIdentifier is not None and not isinstance(
                                        fileIdentifier, aas.SubmodelElement
                                    ):
                                        fileIdentifier = self.FileIdentifier(fileIdentifier)

                                    # A str would be split into its characters
                                    if isinstance(api, str):
                                        raise TypeError("api takes several elements, got a str")

                                    # Build a submodel element if a raw value was passed in the argument

                                    if api is not None and not isinstance(api, aas.SubmodelElement):
                                        api = self.Api(api)

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        externalUrl, fileIdentifier, hostOrganization, api
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"ExternalFile",
                                    "type_value_list_element": aas.SubmodelElementCollection,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ExternalFile/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                externalfile_items: Optional[Iterable[Externalfile_item]] = None,
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(externalfile_items, str):
                                    raise TypeError("externalfile_items takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    externalfile_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class FileFormat(aas.SubmodelElementCollection):

                            class FormatName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"FormatName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class FormatVersion(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"FormatVersion",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatVersion/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class FormatQualifier(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"FormatQualifier",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/FormatQualifier/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"FileFormat",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/FileFormat/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                formatName: Union[str, FormatName],
                                formatVersion: Union[str, FormatVersion],
                                formatQualifier: Union[str, FormatQualifier],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if formatName is not None and not isinstance(formatName, aas.SubmodelElement):
                                    formatName = self.FormatName(formatName)

                                # Build a submodel element if a raw value was passed in the argument

                                if formatVersion is not None and not isinstance(formatVersion, aas.SubmodelElement):
                                    formatVersion = self.FormatVersion(formatVersion)

                                # Build a submodel element if a raw value was passed in the argument

                                if formatQualifier is not None and not isinstance(formatQualifier, aas.SubmodelElement):
                                    formatQualifier = self.FormatQualifier(formatQualifier)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    formatName, formatVersion, formatQualifier
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class SourceApplication(aas.SubmodelElementCollection):

                            class ApplicationName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ApplicationName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class ApplicationVersion(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ApplicationVersion",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationVersion/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class ApplicationQualifier(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"ApplicationQualifier",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/ApplicationQualifier/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Api(GeneratedSubmodelElementList):

                                class Api_item(aas.SubmodelElementCollection):

                                    class ApiVersion(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"ApiVersion",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiVersion/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class ApiDocumentationUrl(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"ApiDocumentationUrl",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiDocumentationUrl/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class ApiSpecificationUrl(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"ApiSpecificationUrl",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/ApiSpecificationUrl/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    @staticmethod
                                    def template_defaults() -> SubmodelElementCollectionMetadata:
                                        return {
                                            "id_short": None,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0"
                                            ),
                                        }

                                    def __init__(
                                        self,
                                        apiVersion: Union[str, ApiVersion],
                                        apiDocumentationUrl: Optional[Union[str, ApiDocumentationUrl]] = None,
                                        apiSpecificationUrl: Optional[Union[str, ApiSpecificationUrl]] = None,
                                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                    ):

                                        # Build a submodel element if a raw value was passed in the argument

                                        if apiVersion is not None and not isinstance(apiVersion, aas.SubmodelElement):
                                            apiVersion = self.ApiVersion(apiVersion)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if apiDocumentationUrl is not None and not isinstance(
                                            apiDocumentationUrl, aas.SubmodelElement
                                        ):
                                            apiDocumentationUrl = self.ApiDocumentationUrl(apiDocumentationUrl)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if apiSpecificationUrl is not None and not isinstance(
                                            apiSpecificationUrl, aas.SubmodelElement
                                        ):
                                            apiSpecificationUrl = self.ApiSpecificationUrl(apiSpecificationUrl)

                                        # Add all passed/initialized submodel elements to a single list

                                        embedded_submodel_elements = collect_submodel_elements(
                                            apiVersion, apiDocumentationUrl, apiSpecificationUrl
                                        )

                                        super().__init__(
                                            value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                        )

                                @staticmethod
                                def template_defaults() -> SubmodelElementListMetadata:
                                    return {
                                        "id_short": r"Api",
                                        "type_value_list_element": aas.SubmodelElementCollection,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/Api/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    api_items: Optional[Iterable[Api_item]] = None,
                                    **kwargs: Unpack[SubmodelElementListMetadata],
                                ):

                                    # A str would be split into its characters
                                    if isinstance(api_items, str):
                                        raise TypeError("api_items takes several elements, got a str")

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        api_items, number_repeated=False
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class VendorOrganization(aas.SubmodelElementCollection):

                                class OrganizationName(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"OrganizationName",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationName/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class OrganizationOfficialName(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"OrganizationOfficialName",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/OrganizationOfficialName/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"VendorOrganization",
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/VendorOrganization/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    organizationName: Union[str, OrganizationName],
                                    organizationOfficialName: Union[str, OrganizationOfficialName],
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if organizationName is not None and not isinstance(
                                        organizationName, aas.SubmodelElement
                                    ):
                                        organizationName = self.OrganizationName(organizationName)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if organizationOfficialName is not None and not isinstance(
                                        organizationOfficialName, aas.SubmodelElement
                                    ):
                                        organizationOfficialName = self.OrganizationOfficialName(
                                            organizationOfficialName
                                        )

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        organizationName, organizationOfficialName
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"SourceApplication",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/SourceApplication/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                applicationName: Union[str, ApplicationName],
                                applicationVersion: Union[str, ApplicationVersion],
                                applicationQualifier: Union[str, ApplicationQualifier],
                                vendorOrganization: VendorOrganization,
                                api: Optional[Union[Iterable[Api.Api_item], Api]] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationName is not None and not isinstance(applicationName, aas.SubmodelElement):
                                    applicationName = self.ApplicationName(applicationName)

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationVersion is not None and not isinstance(
                                    applicationVersion, aas.SubmodelElement
                                ):
                                    applicationVersion = self.ApplicationVersion(applicationVersion)

                                # Build a submodel element if a raw value was passed in the argument

                                if applicationQualifier is not None and not isinstance(
                                    applicationQualifier, aas.SubmodelElement
                                ):
                                    applicationQualifier = self.ApplicationQualifier(applicationQualifier)

                                # A str would be split into its characters
                                if isinstance(api, str):
                                    raise TypeError("api takes several elements, got a str")

                                # Build a submodel element if a raw value was passed in the argument

                                if api is not None and not isinstance(api, aas.SubmodelElement):
                                    api = self.Api(api)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    applicationName, applicationVersion, applicationQualifier, api, vendorOrganization
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class ProvidingOrganization(aas.SubmodelElementCollection):

                            class OrganizationName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"OrganizationName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/OrganizationName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class OrganizationOfficialName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"OrganizationOfficialName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization//OrganizationOfficialName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"ProvidingOrganization",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/ProvidingOrganization/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                organizationName: Union[str, OrganizationName],
                                organizationOfficialName: Union[str, OrganizationOfficialName],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationName is not None and not isinstance(
                                    organizationName, aas.SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(organizationName)

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationOfficialName is not None and not isinstance(
                                    organizationOfficialName, aas.SubmodelElement
                                ):
                                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    organizationName, organizationOfficialName
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0"
                                ),
                            }

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
                                Union[Iterable[Union[aas.Reference, BasedOn.Basedon_item]], BasedOn]
                            ] = None,
                            refersTo: Optional[
                                Union[Iterable[Union[aas.Reference, RefersTo.Refersto_item]], RefersTo]
                            ] = None,
                            digitalFile: Optional[DigitalFile] = None,
                            externalFile: Optional[
                                Union[Iterable[ExternalFile.Externalfile_item], ExternalFile]
                            ] = None,
                            sourceApplication: Optional[SourceApplication] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if title is not None and not isinstance(title, aas.SubmodelElement):
                                title = self.Title(title)

                            # Build a submodel element if a raw value was passed in the argument

                            if fileName is not None and not isinstance(fileName, aas.SubmodelElement):
                                fileName = self.FileName(fileName)

                            # Build a submodel element if a raw value was passed in the argument

                            if fileVersionId is not None and not isinstance(fileVersionId, aas.SubmodelElement):
                                fileVersionId = self.FileVersionId(fileVersionId)

                            # Build a submodel element if a raw value was passed in the argument

                            if statusValue is not None and not isinstance(statusValue, aas.SubmodelElement):
                                statusValue = self.StatusValue(statusValue)

                            # Build a submodel element if a raw value was passed in the argument

                            if setDate is not None and not isinstance(setDate, aas.SubmodelElement):
                                setDate = self.SetDate(setDate)

                            # A str would be split into its characters
                            if isinstance(basedOn, str):
                                raise TypeError("basedOn takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if basedOn is not None and not isinstance(basedOn, aas.SubmodelElement):
                                basedOn = self.BasedOn(basedOn)

                            # A str would be split into its characters
                            if isinstance(refersTo, str):
                                raise TypeError("refersTo takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if refersTo is not None and not isinstance(refersTo, aas.SubmodelElement):
                                refersTo = self.RefersTo(refersTo)

                            # A str would be split into its characters
                            if isinstance(externalFile, str):
                                raise TypeError("externalFile takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if externalFile is not None and not isinstance(externalFile, aas.SubmodelElement):
                                externalFile = self.ExternalFile(externalFile)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
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
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"FileVersion",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileVersion/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        fileversion_items: Optional[Iterable[Fileversion_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(fileversion_items, str):
                            raise TypeError("fileversion_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(fileversion_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ConsumingApplication(GeneratedSubmodelElementList):

                    class Consumingapplication_item(aas.SubmodelElementCollection):

                        class ApplicationName(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ApplicationName",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationName/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ApplicationVersion(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ApplicationVersion",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationVersion/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ApplicationQualifier(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ApplicationQualifier",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/ApplicationQualifier1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class VendorOrganization(aas.SubmodelElementCollection):

                            class OrganizationName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"OrganizationName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class OrganizationOfficialName(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"OrganizationOfficialName",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/OrganizationOfficialName/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"VendorOrganization",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/VendorOrganization/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                organizationName: Union[str, OrganizationName],
                                organizationOfficialName: Union[str, OrganizationOfficialName],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationName is not None and not isinstance(
                                    organizationName, aas.SubmodelElement
                                ):
                                    organizationName = self.OrganizationName(organizationName)

                                # Build a submodel element if a raw value was passed in the argument

                                if organizationOfficialName is not None and not isinstance(
                                    organizationOfficialName, aas.SubmodelElement
                                ):
                                    organizationOfficialName = self.OrganizationOfficialName(organizationOfficialName)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    organizationName, organizationOfficialName
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Api(GeneratedSubmodelElementList):

                            class Api_item(aas.SubmodelElementCollection):

                                class ApiVersion(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"ApiVersion",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiVersion/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class ApiDocumentationUrl(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"ApiDocumentationUrl",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiDocumentationUrl/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class ApiSpecificationUrl(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"ApiSpecificationUrl",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/ApiSpecificationUrl/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    apiVersion: Union[str, ApiVersion],
                                    apiDocumentationUrl: Optional[Union[str, ApiDocumentationUrl]] = None,
                                    apiSpecificationUrl: Optional[Union[str, ApiSpecificationUrl]] = None,
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if apiVersion is not None and not isinstance(apiVersion, aas.SubmodelElement):
                                        apiVersion = self.ApiVersion(apiVersion)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if apiDocumentationUrl is not None and not isinstance(
                                        apiDocumentationUrl, aas.SubmodelElement
                                    ):
                                        apiDocumentationUrl = self.ApiDocumentationUrl(apiDocumentationUrl)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if apiSpecificationUrl is not None and not isinstance(
                                        apiSpecificationUrl, aas.SubmodelElement
                                    ):
                                        apiSpecificationUrl = self.ApiSpecificationUrl(apiSpecificationUrl)

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        apiVersion, apiDocumentationUrl, apiSpecificationUrl
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"Api",
                                    "type_value_list_element": aas.SubmodelElementCollection,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/Api/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                api_items: Optional[Iterable[Api_item]] = None,
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(api_items, str):
                                    raise TypeError("api_items takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(api_items, number_repeated=False)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            applicationName: Union[str, ApplicationName],
                            applicationVersion: Union[str, ApplicationVersion],
                            applicationQualifier: Union[str, ApplicationQualifier],
                            vendorOrganization: VendorOrganization,
                            api: Optional[Union[Iterable[Api.Api_item], Api]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationName is not None and not isinstance(applicationName, aas.SubmodelElement):
                                applicationName = self.ApplicationName(applicationName)

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationVersion is not None and not isinstance(
                                applicationVersion, aas.SubmodelElement
                            ):
                                applicationVersion = self.ApplicationVersion(applicationVersion)

                            # Build a submodel element if a raw value was passed in the argument

                            if applicationQualifier is not None and not isinstance(
                                applicationQualifier, aas.SubmodelElement
                            ):
                                applicationQualifier = self.ApplicationQualifier(applicationQualifier)

                            # A str would be split into its characters
                            if isinstance(api, str):
                                raise TypeError("api takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if api is not None and not isinstance(api, aas.SubmodelElement):
                                api = self.Api(api)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                applicationName, applicationVersion, applicationQualifier, vendorOrganization, api
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ConsumingApplication",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/File/ConsumingApplication/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        consumingapplication_items: Optional[Iterable[Consumingapplication_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(consumingapplication_items, str):
                            raise TypeError("consumingapplication_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            consumingapplication_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class FileClassification(GeneratedSubmodelElementList):

                    class Fileclassification_item(aas.SubmodelElementCollection):

                        class ClassId(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ClassId",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassId/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ClassName(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"ClassName",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/ClassName/1/0"
                                    ),
                                }

                            def __init__(
                                self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class ClassificationSystem(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"ClassificationSystem",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/File/ClassificationSystem/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            classId: Union[str, ClassId],
                            className: Union[aas.LangStringSet, ClassName],
                            classificationSystem: Union[str, ClassificationSystem],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if classId is not None and not isinstance(classId, aas.SubmodelElement):
                                classId = self.ClassId(classId)

                            # Build a submodel element if a raw value was passed in the argument

                            if className is not None and not isinstance(className, aas.SubmodelElement):
                                className = self.ClassName(className)

                            # Build a submodel element if a raw value was passed in the argument

                            if classificationSystem is not None and not isinstance(
                                classificationSystem, aas.SubmodelElement
                            ):
                                classificationSystem = self.ClassificationSystem(classificationSystem)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                classId, className, classificationSystem
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"FileClassification",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/File/FileClassification/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        fileclassification_items: Iterable[Fileclassification_item],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(fileclassification_items, str):
                            raise TypeError("fileclassification_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            fileclassification_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"File",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/File/1/0"),
                    }

                def __init__(
                    self,
                    fileId: Union[Iterable[FileId.Fileid_item], FileId],
                    fileClassification: Union[Iterable[FileClassification.Fileclassification_item], FileClassification],
                    fileVersion: Optional[Union[Iterable[FileVersion.Fileversion_item], FileVersion]] = None,
                    consumingApplication: Optional[
                        Union[Iterable[ConsumingApplication.Consumingapplication_item], ConsumingApplication]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(fileId, str):
                        raise TypeError("fileId takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if fileId is not None and not isinstance(fileId, aas.SubmodelElement):
                        fileId = self.FileId(fileId)

                    # A str would be split into its characters
                    if isinstance(fileVersion, str):
                        raise TypeError("fileVersion takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if fileVersion is not None and not isinstance(fileVersion, aas.SubmodelElement):
                        fileVersion = self.FileVersion(fileVersion)

                    # A str would be split into its characters
                    if isinstance(consumingApplication, str):
                        raise TypeError("consumingApplication takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if consumingApplication is not None and not isinstance(consumingApplication, aas.SubmodelElement):
                        consumingApplication = self.ConsumingApplication(consumingApplication)

                    # A str would be split into its characters
                    if isinstance(fileClassification, str):
                        raise TypeError("fileClassification takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if fileClassification is not None and not isinstance(fileClassification, aas.SubmodelElement):
                        fileClassification = self.FileClassification(fileClassification)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        fileId, fileVersion, consumingApplication, fileClassification
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Capability(aas.SubmodelElementCollection):

                class PosModelPurpose(GeneratedSubmodelElementList):

                    class Posmodelpurpose_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"PosModelPurpose",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/PosModelPurpose/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        posmodelpurpose_items: Optional[Iterable[Union[str, Posmodelpurpose_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(posmodelpurpose_items, str):
                            raise TypeError("posmodelpurpose_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if posmodelpurpose_items:
                            posmodelpurpose_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Posmodelpurpose_item(i)
                                for i in posmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            posmodelpurpose_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class NegModelPurpose(GeneratedSubmodelElementList):

                    class Negmodelpurpose_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"NegModelPurpose",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/NegModelPurpos/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        negmodelpurpose_items: Optional[Iterable[Union[str, Negmodelpurpose_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(negmodelpurpose_items, str):
                            raise TypeError("negmodelpurpose_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if negmodelpurpose_items:
                            negmodelpurpose_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Negmodelpurpose_item(i)
                                for i in negmodelpurpose_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            negmodelpurpose_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class EmbeddedInfo(GeneratedSubmodelElementList):

                    class Embeddedinfo_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"EmbeddedInfo",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/EmbeddedInfo/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        embeddedinfo_items: Optional[Iterable[Union[str, Embeddedinfo_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(embeddedinfo_items, str):
                            raise TypeError("embeddedinfo_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if embeddedinfo_items:
                            embeddedinfo_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Embeddedinfo_item(i)
                                for i in embeddedinfo_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            embeddedinfo_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class State(GeneratedSubmodelElementList):

                    class State_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"State",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/State/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        state_items: Optional[Iterable[Union[str, State_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(state_items, str):
                            raise TypeError("state_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if state_items:
                            state_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.State_item(i) for i in state_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(state_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class ObjectType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ObjectType",
                            "value_type": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/ObjectType/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Origin(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Origin",
                            "value_type": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Origin/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Simplification(aas.SubmodelElementCollection):

                    class Description(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Description",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/LevelDescription/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReducedElements(GeneratedSubmodelElementList):

                        class Reducedelements_item(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": None,
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementListMetadata:
                            return {
                                "id_short": r"ReducedElements",
                                "type_value_list_element": aas.Property,
                                "value_type_list_element": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/ReducedElements/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            reducedelements_items: Optional[Iterable[Union[str, Reducedelements_item]]] = None,
                            **kwargs: Unpack[SubmodelElementListMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(reducedelements_items, str):
                                raise TypeError("reducedelements_items takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if reducedelements_items:
                                reducedelements_items = [
                                    i if isinstance(i, aas.SubmodelElement) else self.Reducedelements_item(i)
                                    for i in reducedelements_items
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                reducedelements_items, number_repeated=False
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class DerivedFrom(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"DerivedFrom",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/DerivedFrom/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Simplification",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Capability/Simplification/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        description_: Optional[Union[str, Description]] = None,
                        reducedElements: Optional[
                            Union[Iterable[Union[str, ReducedElements.Reducedelements_item]], ReducedElements]
                        ] = None,
                        derivedFrom: Optional[Union[aas.Reference, DerivedFrom]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                            description_ = self.Description(description_)

                        # A str would be split into its characters
                        if isinstance(reducedElements, str):
                            raise TypeError("reducedElements takes several elements, got a str")

                        # Build a submodel element if a raw value was passed in the argument

                        if reducedElements is not None and not isinstance(reducedElements, aas.SubmodelElement):
                            reducedElements = self.ReducedElements(reducedElements)

                        # Build a submodel element if a raw value was passed in the argument

                        if derivedFrom is not None and not isinstance(derivedFrom, aas.SubmodelElement):
                            derivedFrom = self.DerivedFrom(derivedFrom)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            description_, reducedElements, derivedFrom
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Capability",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/Capability/1/0"),
                    }

                def __init__(
                    self,
                    posModelPurpose: Union[Iterable[Union[str, PosModelPurpose.Posmodelpurpose_item]], PosModelPurpose],
                    origin: Union[str, Origin],
                    negModelPurpose: Optional[
                        Union[Iterable[Union[str, NegModelPurpose.Negmodelpurpose_item]], NegModelPurpose]
                    ] = None,
                    embeddedInfo: Optional[
                        Union[Iterable[Union[str, EmbeddedInfo.Embeddedinfo_item]], EmbeddedInfo]
                    ] = None,
                    state: Optional[Union[Iterable[Union[str, State.State_item]], State]] = None,
                    objectType: Optional[Union[str, ObjectType]] = None,
                    simplification: Optional[Simplification] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(posModelPurpose, str):
                        raise TypeError("posModelPurpose takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if posModelPurpose is not None and not isinstance(posModelPurpose, aas.SubmodelElement):
                        posModelPurpose = self.PosModelPurpose(posModelPurpose)

                    # A str would be split into its characters
                    if isinstance(negModelPurpose, str):
                        raise TypeError("negModelPurpose takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if negModelPurpose is not None and not isinstance(negModelPurpose, aas.SubmodelElement):
                        negModelPurpose = self.NegModelPurpose(negModelPurpose)

                    # A str would be split into its characters
                    if isinstance(embeddedInfo, str):
                        raise TypeError("embeddedInfo takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if embeddedInfo is not None and not isinstance(embeddedInfo, aas.SubmodelElement):
                        embeddedInfo = self.EmbeddedInfo(embeddedInfo)

                    # A str would be split into its characters
                    if isinstance(state, str):
                        raise TypeError("state takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if state is not None and not isinstance(state, aas.SubmodelElement):
                        state = self.State(state)

                    # Build a submodel element if a raw value was passed in the argument

                    if objectType is not None and not isinstance(objectType, aas.SubmodelElement):
                        objectType = self.ObjectType(objectType)

                    # Build a submodel element if a raw value was passed in the argument

                    if origin is not None and not isinstance(origin, aas.SubmodelElement):
                        origin = self.Origin(origin)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        posModelPurpose, negModelPurpose, embeddedInfo, state, objectType, origin, simplification
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Geometry(aas.SubmodelElementCollection):

                class Representation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Representation",
                            "value_type": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/Representation/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LengthUnit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LengthUnit",
                            "value_type": str,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/LengthUnit/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CartBoundingBox(GeneratedSubmodelElementList):

                    class Cartboundingbox_item(aas.SubmodelElementCollection):

                        class BoundingBoxKind(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"BoundingBoxKind",
                                    "value_type": str,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/BoundingBoxKind/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class CartRefSystem(aas.SubmodelElementCollection):

                            class CartOffsetVector(aas.SubmodelElementCollection):

                                class X(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"X",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/X/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Y(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"Y",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Y/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Z(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"Z",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/Z/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": r"CartOffsetVector",
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/CartOffsetVector/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    x: Union[str, X],
                                    y: Union[str, Y],
                                    z: Union[str, Z],
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if x is not None and not isinstance(x, aas.SubmodelElement):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if y is not None and not isinstance(y, aas.SubmodelElement):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if z is not None and not isinstance(z, aas.SubmodelElement):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(x, y, z)

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            class NormOrientationVector(GeneratedSubmodelElementList):

                                class Normorientationvector_item(aas.SubmodelElementCollection):

                                    class X(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"X",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/X/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class Y(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"Y",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Y/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    class Z(aas.Property):

                                        @staticmethod
                                        def template_defaults() -> PropertyMetadata:
                                            return {
                                                "id_short": r"Z",
                                                "value_type": str,
                                                "semantic_id": global_ref(
                                                    r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/Z/1/0"
                                                ),
                                            }

                                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                                    @staticmethod
                                    def template_defaults() -> SubmodelElementCollectionMetadata:
                                        return {
                                            "id_short": None,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0"
                                            ),
                                        }

                                    def __init__(
                                        self,
                                        x: Union[str, X],
                                        y: Union[str, Y],
                                        z: Union[str, Z],
                                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                    ):

                                        # Build a submodel element if a raw value was passed in the argument

                                        if x is not None and not isinstance(x, aas.SubmodelElement):
                                            x = self.X(x)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if y is not None and not isinstance(y, aas.SubmodelElement):
                                            y = self.Y(y)

                                        # Build a submodel element if a raw value was passed in the argument

                                        if z is not None and not isinstance(z, aas.SubmodelElement):
                                            z = self.Z(z)

                                        # Add all passed/initialized submodel elements to a single list

                                        embedded_submodel_elements = collect_submodel_elements(x, y, z)

                                        super().__init__(
                                            value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                        )

                                @staticmethod
                                def template_defaults() -> SubmodelElementListMetadata:
                                    return {
                                        "id_short": r"NormOrientationVector",
                                        "type_value_list_element": aas.SubmodelElementCollection,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/NormOrientationVector/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    normorientationvector_items: Iterable[Normorientationvector_item],
                                    **kwargs: Unpack[SubmodelElementListMetadata],
                                ):

                                    # A str would be split into its characters
                                    if isinstance(normorientationvector_items, str):
                                        raise TypeError("normorientationvector_items takes several elements, got a str")

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(
                                        normorientationvector_items, number_repeated=False
                                    )

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"CartRefSystem",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartRefSystem/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                cartOffsetVector: Optional[CartOffsetVector] = None,
                                normOrientationVector: Optional[
                                    Union[
                                        Iterable[NormOrientationVector.Normorientationvector_item],
                                        NormOrientationVector,
                                    ]
                                ] = None,
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(normOrientationVector, str):
                                    raise TypeError("normOrientationVector takes several elements, got a str")

                                # Build a submodel element if a raw value was passed in the argument

                                if normOrientationVector is not None and not isinstance(
                                    normOrientationVector, aas.SubmodelElement
                                ):
                                    normOrientationVector = self.NormOrientationVector(normOrientationVector)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    cartOffsetVector, normOrientationVector
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class CartBoundingVector(aas.SubmodelElementCollection):

                            class X(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"X",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/X/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Y(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"Y",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Y/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Z(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"Z",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/Z/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"CartBoundingVector",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/CartBoundingVector/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                x: Union[str, X],
                                y: Union[str, Y],
                                z: Union[str, Z],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if x is not None and not isinstance(x, aas.SubmodelElement):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument

                                if y is not None and not isinstance(y, aas.SubmodelElement):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument

                                if z is not None and not isinstance(z, aas.SubmodelElement):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(x, y, z)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            boundingBoxKind: Union[str, BoundingBoxKind],
                            cartBoundingVector: CartBoundingVector,
                            cartRefSystem: Optional[CartRefSystem] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if boundingBoxKind is not None and not isinstance(boundingBoxKind, aas.SubmodelElement):
                                boundingBoxKind = self.BoundingBoxKind(boundingBoxKind)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                boundingBoxKind, cartRefSystem, cartBoundingVector
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"CartBoundingBox",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartBoundingBox/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        cartboundingbox_items: Optional[Iterable[Cartboundingbox_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(cartboundingbox_items, str):
                            raise TypeError("cartboundingbox_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            cartboundingbox_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class CartRefSystem(GeneratedSubmodelElementList):

                    class Cartrefsystem_item(aas.SubmodelElementCollection):

                        class CartOffsetVector(aas.SubmodelElementCollection):

                            class X(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"X",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/X/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Y(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"Y",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Y/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            class Z(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"Z",
                                        "value_type": str,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/Z/1/0"
                                        ),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"CartOffsetVector",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/CartOffsetVector/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                x: Union[str, X],
                                y: Union[str, Y],
                                z: Union[str, Z],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if x is not None and not isinstance(x, aas.SubmodelElement):
                                    x = self.X(x)

                                # Build a submodel element if a raw value was passed in the argument

                                if y is not None and not isinstance(y, aas.SubmodelElement):
                                    y = self.Y(y)

                                # Build a submodel element if a raw value was passed in the argument

                                if z is not None and not isinstance(z, aas.SubmodelElement):
                                    z = self.Z(z)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(x, y, z)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class NormOrientationVector(GeneratedSubmodelElementList):

                            class Normorientationvector_item(aas.SubmodelElementCollection):

                                class X(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"X",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/X/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Y(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"Y",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Y/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                class Z(aas.Property):

                                    @staticmethod
                                    def template_defaults() -> PropertyMetadata:
                                        return {
                                            "id_short": r"Z",
                                            "value_type": str,
                                            "semantic_id": global_ref(
                                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/Z/1/0"
                                            ),
                                        }

                                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                                @staticmethod
                                def template_defaults() -> SubmodelElementCollectionMetadata:
                                    return {
                                        "id_short": None,
                                        "semantic_id": global_ref(
                                            r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0"
                                        ),
                                    }

                                def __init__(
                                    self,
                                    x: Union[str, X],
                                    y: Union[str, Y],
                                    z: Union[str, Z],
                                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                                ):

                                    # Build a submodel element if a raw value was passed in the argument

                                    if x is not None and not isinstance(x, aas.SubmodelElement):
                                        x = self.X(x)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if y is not None and not isinstance(y, aas.SubmodelElement):
                                        y = self.Y(y)

                                    # Build a submodel element if a raw value was passed in the argument

                                    if z is not None and not isinstance(z, aas.SubmodelElement):
                                        z = self.Z(z)

                                    # Add all passed/initialized submodel elements to a single list

                                    embedded_submodel_elements = collect_submodel_elements(x, y, z)

                                    super().__init__(
                                        value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                    )

                            @staticmethod
                            def template_defaults() -> SubmodelElementListMetadata:
                                return {
                                    "id_short": r"NormOrientationVector",
                                    "type_value_list_element": aas.SubmodelElementCollection,
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/NormOrientationVector/1/0"
                                    ),
                                }

                            def __init__(
                                self,
                                normorientationvector_items: Iterable[Normorientationvector_item],
                                **kwargs: Unpack[SubmodelElementListMetadata],
                            ):

                                # A str would be split into its characters
                                if isinstance(normorientationvector_items, str):
                                    raise TypeError("normorientationvector_items takes several elements, got a str")

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(
                                    normorientationvector_items, number_repeated=False
                                )

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            cartOffsetVector: Optional[CartOffsetVector] = None,
                            normOrientationVector: Optional[
                                Union[Iterable[NormOrientationVector.Normorientationvector_item], NormOrientationVector]
                            ] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(normOrientationVector, str):
                                raise TypeError("normOrientationVector takes several elements, got a str")

                            # Build a submodel element if a raw value was passed in the argument

                            if normOrientationVector is not None and not isinstance(
                                normOrientationVector, aas.SubmodelElement
                            ):
                                normOrientationVector = self.NormOrientationVector(normOrientationVector)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                cartOffsetVector, normOrientationVector
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"CartRefSystem",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/CartRefSystem/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        cartrefsystem_items: Optional[Iterable[Cartrefsystem_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(cartrefsystem_items, str):
                            raise TypeError("cartrefsystem_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            cartrefsystem_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Geometry",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/Geometry/1/0"),
                    }

                def __init__(
                    self,
                    representation: Union[str, Representation],
                    lengthUnit: Union[str, LengthUnit],
                    cartBoundingBox: Optional[
                        Union[Iterable[CartBoundingBox.Cartboundingbox_item], CartBoundingBox]
                    ] = None,
                    cartRefSystem: Optional[Union[Iterable[CartRefSystem.Cartrefsystem_item], CartRefSystem]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if representation is not None and not isinstance(representation, aas.SubmodelElement):
                        representation = self.Representation(representation)

                    # Build a submodel element if a raw value was passed in the argument

                    if lengthUnit is not None and not isinstance(lengthUnit, aas.SubmodelElement):
                        lengthUnit = self.LengthUnit(lengthUnit)

                    # A str would be split into its characters
                    if isinstance(cartBoundingBox, str):
                        raise TypeError("cartBoundingBox takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if cartBoundingBox is not None and not isinstance(cartBoundingBox, aas.SubmodelElement):
                        cartBoundingBox = self.CartBoundingBox(cartBoundingBox)

                    # A str would be split into its characters
                    if isinstance(cartRefSystem, str):
                        raise TypeError("cartRefSystem takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if cartRefSystem is not None and not isinstance(cartRefSystem, aas.SubmodelElement):
                        cartRefSystem = self.CartRefSystem(cartRefSystem)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        representation, lengthUnit, cartBoundingBox, cartRefSystem
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/1/0"),
                }

            def __init__(
                self,
                file: File,
                capability: Optional[Capability] = None,
                geometry: Optional[Geometry] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(file, capability, geometry)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Model3D",
                "type_value_list_element": aas.SubmodelElementCollection,
                "semantic_id": global_ref(r"https://admin-shell.io/idta/Models3D/Model3D/1/0"),
            }

        def __init__(
            self, model3d_items: Optional[Iterable[Model3d_item]] = None, **kwargs: Unpack[SubmodelElementListMetadata]
        ):

            # A str would be split into its characters
            if isinstance(model3d_items, str):
                raise TypeError("model3d_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(model3d_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"Models3D",
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/Models3D/1/0"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self, id_: str, model3D: Union[Iterable[Model3D.Model3d_item], Model3D], **kwargs: Unpack[SubmodelMetadata]
    ):

        # A str would be split into its characters
        if isinstance(model3D, str):
            raise TypeError("model3D takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if model3D is not None and not isinstance(model3D, aas.SubmodelElement):
            model3D = self.Model3D(model3D)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(model3D)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
