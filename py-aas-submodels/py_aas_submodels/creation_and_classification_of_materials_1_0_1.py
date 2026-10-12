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


class BackendSpecificMaterialInformation(aas.Submodel):

    class MaterialSystemProperties(aas.SubmodelElementCollection):

        class MaterialType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialType",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/MaterialType/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BaseUnitOfMeasure(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"BaseUnitOfMeasure",
                    "semantic_id": global_ref(
                        r"ttps://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/BaseUnitOfMeasure/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialStatus(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialStatus",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/MaterialStatus/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Industry(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Industry",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/Industry/1/0https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/Industry/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductName(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ProductName",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/ProductName/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialNumber",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/MaterialNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Description(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"Description",
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/Description/1/0"
                    ),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Plant(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Plant",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/Plant/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MaterialSystemProperties",
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/MaterialSystemProperties/1/0"
                ),
            }

        def __init__(
            self,
            materialType: Optional[Union[str, MaterialType]] = None,
            baseUnitOfMeasure: Optional[Union[aas.MultiLanguageTextType, BaseUnitOfMeasure]] = None,
            materialStatus: Optional[Union[str, MaterialStatus]] = None,
            industry: Optional[Union[str, Industry]] = None,
            productName: Optional[Union[aas.MultiLanguageTextType, ProductName]] = None,
            materialNumber: Optional[Union[str, MaterialNumber]] = None,
            description_: Optional[Union[aas.MultiLanguageTextType, Description]] = None,
            plant: Optional[Union[str, Plant]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if materialType is not None and not isinstance(materialType, aas.SubmodelElement):
                materialType = self.MaterialType(materialType)

            # Build a submodel element if a raw value was passed in the argument

            if baseUnitOfMeasure is not None and not isinstance(baseUnitOfMeasure, aas.SubmodelElement):
                baseUnitOfMeasure = self.BaseUnitOfMeasure(baseUnitOfMeasure)

            # Build a submodel element if a raw value was passed in the argument

            if materialStatus is not None and not isinstance(materialStatus, aas.SubmodelElement):
                materialStatus = self.MaterialStatus(materialStatus)

            # Build a submodel element if a raw value was passed in the argument

            if industry is not None and not isinstance(industry, aas.SubmodelElement):
                industry = self.Industry(industry)

            # Build a submodel element if a raw value was passed in the argument

            if productName is not None and not isinstance(productName, aas.SubmodelElement):
                productName = self.ProductName(productName)

            # Build a submodel element if a raw value was passed in the argument

            if materialNumber is not None and not isinstance(materialNumber, aas.SubmodelElement):
                materialNumber = self.MaterialNumber(materialNumber)

            # Build a submodel element if a raw value was passed in the argument

            if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                description_ = self.Description(description_)

            # Build a submodel element if a raw value was passed in the argument

            if plant is not None and not isinstance(plant, aas.SubmodelElement):
                plant = self.Plant(plant)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                materialType,
                baseUnitOfMeasure,
                materialStatus,
                industry,
                productName,
                materialNumber,
                description_,
                plant,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"BackendSpecificMaterialInformation",
            "semantic_id": global_ref(r"https://admin-shell.io/idta/BackendSpecificMaterialInformation/1/0"),
        }

    def __init__(
        self, id_: str, materialSystemProperties: MaterialSystemProperties, **kwargs: Unpack[SubmodelMetadata]
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(materialSystemProperties)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
