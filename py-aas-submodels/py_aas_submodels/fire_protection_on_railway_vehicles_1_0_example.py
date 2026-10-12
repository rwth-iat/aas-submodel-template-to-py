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


class RailwayFireProtection(aas.Submodel):

    class ManufacturerInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ManufacturerName",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Manufacturer name"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"name of the organization legally responsible for manufacturing the product or component."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ManufacturerName/1"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerProductDesignation(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ManufacturerProductDesignation",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Manufacturer product designation"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"designation assigned by the manufacturer to identify the product or component within its product portfolio."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ManufacturerProductDesignation/1"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OrderCodeOfManufacturer(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OrderCodeOfManufacturer",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Order code of manufacturer"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"ordering identifier defined by the manufacturer to uniquely reference the product or component for purchasing purposes."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/OrderCodeOfManufacturer/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductArticleNumberOfManufacturer(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductArticleNumberOfManufacturer",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Product article number of manufacturer"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"article number used by the manufacturer to uniquely identify the product or component in catalogs and information systems"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProductArticleNumberOfManufacturer/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ManufacturerInformation",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Manufacturer information"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"identifies the material or component and its manufacturer, including product designation and reference identifiers, ensuring unambiguous attribution of the fire protection data."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ManufacturerInformation/1"),
            }

        def __init__(
            self,
            manufacturerName: Union[aas.MultiLanguageTextType, ManufacturerName],
            manufacturerProductDesignation: Union[aas.MultiLanguageTextType, ManufacturerProductDesignation],
            orderCodeOfManufacturer: Union[str, OrderCodeOfManufacturer],
            productArticleNumberOfManufacturer: Union[str, ProductArticleNumberOfManufacturer],
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

            if orderCodeOfManufacturer is not None and not isinstance(orderCodeOfManufacturer, aas.SubmodelElement):
                orderCodeOfManufacturer = self.OrderCodeOfManufacturer(orderCodeOfManufacturer)

            # Build a submodel element if a raw value was passed in the argument

            if productArticleNumberOfManufacturer is not None and not isinstance(
                productArticleNumberOfManufacturer, aas.SubmodelElement
            ):
                productArticleNumberOfManufacturer = self.ProductArticleNumberOfManufacturer(
                    productArticleNumberOfManufacturer
                )

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                manufacturerName,
                manufacturerProductDesignation,
                orderCodeOfManufacturer,
                productArticleNumberOfManufacturer,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FireProtectionCertificates(aas.SubmodelElementCollection):

        class RequirementsSets(GeneratedSubmodelElementList):

            class Requirementssets_item(aas.SubmodelElementCollection):

                class HazardLevel(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"HazardLevel",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Hazard level"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": 'hazard level indicating the achieved fire hazard classification of the product, component, or material according to the applicable fire protection standard.\n\n\nFollowing values can be assigned:\n\n"Compliant: Hazard Level 1"\n\n"Compliant: Hazard Level 2"\n\n"Compliant: Hazard Level 3"\n\n"Approved Functional Necessity Report"\n\n"Missing Test Results"\n\n"Not Compliant"'
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/RailwayFireProtection/Submodel/1/HazardLevel"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReportReferences(GeneratedSubmodelElementList):

                    class Reportreferences_item(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Report reference"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"reference linking a requirement to the corresponding verification report or certificate"
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReportReference/1"),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"ReportReferences",
                            "type_value_list_element": aas.ReferenceElement,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Report references"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"list of references to reports providing evidence for compliance with requirements"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReportReferences/1"),
                        }

                    def __init__(
                        self,
                        reportreferences_items: Iterable[Union[aas.Reference, Reportreferences_item]],
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(reportreferences_items, str):
                            raise TypeError("reportreferences_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if reportreferences_items:
                            reportreferences_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Reportreferences_item(i)
                                for i in reportreferences_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reportreferences_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Requirement(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Requirement",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Requirement"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"individual fire protection requirement to be fulfilled according to the applicable standard"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Requirement/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Requirement set"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"collection of fire protection requirements applicable to a specific product, component, or material."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RequirementsSet/1"),
                    }

                def __init__(
                    self,
                    hazardLevel: Union[str, HazardLevel],
                    reportReferences: Union[
                        Iterable[Union[aas.Reference, ReportReferences.Reportreferences_item]], ReportReferences
                    ],
                    requirement: Union[str, Requirement],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if hazardLevel is not None and not isinstance(hazardLevel, aas.SubmodelElement):
                        hazardLevel = self.HazardLevel(hazardLevel)

                    # A str would be split into its characters
                    if isinstance(reportReferences, str):
                        raise TypeError("reportReferences takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if reportReferences is not None and not isinstance(reportReferences, aas.SubmodelElement):
                        reportReferences = self.ReportReferences(reportReferences)

                    # Build a submodel element if a raw value was passed in the argument

                    if requirement is not None and not isinstance(requirement, aas.SubmodelElement):
                        requirement = self.Requirement(requirement)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(hazardLevel, reportReferences, requirement)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"RequirementsSets",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reqirements sets"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"list of requirement sets defining applicable fire protection requirements"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RequirementsSets/1"),
                }

            def __init__(
                self,
                requirementssets_items: Iterable[Requirementssets_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(requirementssets_items, str):
                    raise TypeError("requirementssets_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(requirementssets_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Reports(GeneratedSubmodelElementList):

            class Reports_item(aas.SubmodelElementCollection):

                class ReportFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"ReportFile",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Report file"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"digital file containing the report document, such as a test report or certificate"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReportFile/1"),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/pdf",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class Tests(GeneratedSubmodelElementList):

                    class Tests_item(aas.SubmodelElementCollection):

                        class TestProcedure(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TestProcedure",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Test procedure"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"description of the test method or procedure applied to verify fire protection requirements"
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestProcedure/1"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class TestResult(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TestResult",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Test result"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"outcome of the performed fire protection test, indicating conformity or non‑conformity"
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestResult/1"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class TestDate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TestDate",
                                    "value_type": xsd.Date,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Test date"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={r"en": r"date on which the fire protection test was performed"}
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestDate/1"),
                                }

                            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class TestReportNumber(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"TestReportNumber",
                                    "value_type": str,
                                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Test report number"}),
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"unique identifier assigned to the fire protection test report by the issuing body"
                                        }
                                    ),
                                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestReportNumber/1"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": None,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Test"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"collection of test-related information"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Test/1"),
                            }

                        def __init__(
                            self,
                            testProcedure: Union[str, TestProcedure],
                            testResult: Union[str, TestResult],
                            testDate: Union[xsd.Date, TestDate],
                            testReportNumber: Union[str, TestReportNumber],
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if testProcedure is not None and not isinstance(testProcedure, aas.SubmodelElement):
                                testProcedure = self.TestProcedure(testProcedure)

                            # Build a submodel element if a raw value was passed in the argument

                            if testResult is not None and not isinstance(testResult, aas.SubmodelElement):
                                testResult = self.TestResult(testResult)

                            # Build a submodel element if a raw value was passed in the argument

                            if testDate is not None and not isinstance(testDate, aas.SubmodelElement):
                                testDate = self.TestDate(testDate)

                            # Build a submodel element if a raw value was passed in the argument

                            if testReportNumber is not None and not isinstance(testReportNumber, aas.SubmodelElement):
                                testReportNumber = self.TestReportNumber(testReportNumber)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                testProcedure, testResult, testDate, testReportNumber
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Tests",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Tests"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"list of tests performed to verify conformity with specified fire protection requirements."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Tests/1"),
                        }

                    def __init__(
                        self, tests_items: Iterable[Tests_item], **kwargs: Unpack[SubmodelElementListMetadata]
                    ):

                        # A str would be split into its characters
                        if isinstance(tests_items, str):
                            raise TypeError("tests_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(tests_items, number_repeated=False)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class LabInformation(aas.SubmodelElementCollection):

                    class LabName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LabName",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Lab name"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"name of the laboratory that carried out the fire protection test"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LabName/1"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class LabAddress(aas.SubmodelElementCollection):

                        class AddressOfAdditionalLink(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"AddressOfAdditionalLink",
                                    "value_type": str,
                                    "semantic_id": global_ref(r"0173-1#02-AAQ326#002"),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class NationalCode(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"NationalCode",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r" Note: country codes defined accord. to ISO 3166-1. Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAO134#002"),
                                }

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class CityTown(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {"id_short": r"CityTown", "semantic_id": global_ref(r"0173-1#02-AAO132#002")}

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Company(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {"id_short": r"Company", "semantic_id": global_ref(r"0173-1#02-AAW001#001")}

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Phone(aas.SubmodelElementCollection):

                            class TelephoneNumber(aas.MultiLanguageProperty):

                                @staticmethod
                                def template_defaults() -> MultiLanguagePropertyMetadata:
                                    return {
                                        "id_short": r"TelephoneNumber",
                                        "description": aas.MultiLanguageTextType(
                                            dict_={
                                                r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                            }
                                        ),
                                        "semantic_id": global_ref(r"0173-1#02-AAO136#002"),
                                    }

                                def __init__(
                                    self,
                                    value: aas.MultiLanguageTextType,
                                    **kwargs: Unpack[MultiLanguagePropertyMetadata],
                                ):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {
                                    "id_short": r"Phone",
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone"
                                    ),
                                }

                            def __init__(
                                self,
                                telephoneNumber: Union[aas.MultiLanguageTextType, TelephoneNumber],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if telephoneNumber is not None and not isinstance(telephoneNumber, aas.SubmodelElement):
                                    telephoneNumber = self.TelephoneNumber(telephoneNumber)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(telephoneNumber)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Email(aas.SubmodelElementCollection):

                            class EmailAddress(aas.Property):

                                @staticmethod
                                def template_defaults() -> PropertyMetadata:
                                    return {
                                        "id_short": r"EmailAddress",
                                        "value_type": str,
                                        "semantic_id": global_ref(r"0173-1#02-AAO198#002"),
                                    }

                                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                    super().__init__(value=value, **(self.template_defaults() | kwargs))

                            @staticmethod
                            def template_defaults() -> SubmodelElementCollectionMetadata:
                                return {"id_short": r"Email", "semantic_id": global_ref(r"0173-1#02-AAQ836#005")}

                            def __init__(
                                self,
                                emailAddress: Union[str, EmailAddress],
                                **kwargs: Unpack[SubmodelElementCollectionMetadata],
                            ):

                                # Build a submodel element if a raw value was passed in the argument

                                if emailAddress is not None and not isinstance(emailAddress, aas.SubmodelElement):
                                    emailAddress = self.EmailAddress(emailAddress)

                                # Add all passed/initialized submodel elements to a single list

                                embedded_submodel_elements = collect_submodel_elements(emailAddress)

                                super().__init__(
                                    value=embedded_submodel_elements, **(self.template_defaults() | kwargs)
                                )

                        class Street(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {"id_short": r"Street", "semantic_id": global_ref(r"0173-1#02-AAO128#002")}

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Zipcode(aas.MultiLanguageProperty):

                            @staticmethod
                            def template_defaults() -> MultiLanguagePropertyMetadata:
                                return {
                                    "id_short": r"Zipcode",
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                                        }
                                    ),
                                    "semantic_id": global_ref(r"0173-1#02-AAO129#002"),
                                }

                            def __init__(
                                self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                            ):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        @staticmethod
                        def template_defaults() -> SubmodelElementCollectionMetadata:
                            return {
                                "id_short": r"LabAddress",
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Lab address"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": "reference to the address or contact information of the testing laboratory\n\n\ndrop‑in definition of the Contact Information 1.0 Submodel; all or a subset of the defined elements of the Contact Information 1.0 Submodel may be used within this SMC."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
                                ),
                                "supplemental_semantic_id": (
                                    global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                                ),
                            }

                        def __init__(
                            self,
                            addressOfAdditionalLink: Optional[Union[str, AddressOfAdditionalLink]] = None,
                            nationalCode: Optional[Union[aas.MultiLanguageTextType, NationalCode]] = None,
                            cityTown: Optional[Union[aas.MultiLanguageTextType, CityTown]] = None,
                            company: Optional[Union[aas.MultiLanguageTextType, Company]] = None,
                            phone: Optional[Phone] = None,
                            email: Optional[Email] = None,
                            street: Optional[Union[aas.MultiLanguageTextType, Street]] = None,
                            zipcode: Optional[Union[aas.MultiLanguageTextType, Zipcode]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if addressOfAdditionalLink is not None and not isinstance(
                                addressOfAdditionalLink, aas.SubmodelElement
                            ):
                                addressOfAdditionalLink = self.AddressOfAdditionalLink(addressOfAdditionalLink)

                            # Build a submodel element if a raw value was passed in the argument

                            if nationalCode is not None and not isinstance(nationalCode, aas.SubmodelElement):
                                nationalCode = self.NationalCode(nationalCode)

                            # Build a submodel element if a raw value was passed in the argument

                            if cityTown is not None and not isinstance(cityTown, aas.SubmodelElement):
                                cityTown = self.CityTown(cityTown)

                            # Build a submodel element if a raw value was passed in the argument

                            if company is not None and not isinstance(company, aas.SubmodelElement):
                                company = self.Company(company)

                            # Build a submodel element if a raw value was passed in the argument

                            if street is not None and not isinstance(street, aas.SubmodelElement):
                                street = self.Street(street)

                            # Build a submodel element if a raw value was passed in the argument

                            if zipcode is not None and not isinstance(zipcode, aas.SubmodelElement):
                                zipcode = self.Zipcode(zipcode)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(
                                addressOfAdditionalLink, nationalCode, cityTown, company, phone, email, street, zipcode
                            )

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    class LabAccreditation(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"LabAccreditation",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Lab accreditation"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"information about the laboratory’s accreditation according to relevant standards or schemes"
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LabAccreditation/1"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ReportAuthor(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ReportAuthor",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Report author"}),
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"name of the person or organization responsible for creating or issuing the report"
                                    }
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReportAuthor/1"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"LabInformation",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Lab information"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"collection of information describing the laboratory responsible for performing the tests"
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReportComment/1"),
                        }

                    def __init__(
                        self,
                        labName: Union[str, LabName],
                        labAddress: LabAddress,
                        labAccreditation: Union[str, LabAccreditation],
                        reportAuthor: Union[str, ReportAuthor],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if labName is not None and not isinstance(labName, aas.SubmodelElement):
                            labName = self.LabName(labName)

                        # Build a submodel element if a raw value was passed in the argument

                        if labAccreditation is not None and not isinstance(labAccreditation, aas.SubmodelElement):
                            labAccreditation = self.LabAccreditation(labAccreditation)

                        # Build a submodel element if a raw value was passed in the argument

                        if reportAuthor is not None and not isinstance(reportAuthor, aas.SubmodelElement):
                            reportAuthor = self.ReportAuthor(reportAuthor)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            labName, labAddress, labAccreditation, reportAuthor
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Report"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"collection of a report providing verification evidence for fire protection compliance."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Report/1"),
                    }

                def __init__(
                    self,
                    reportFile: ReportFile,
                    tests: Union[Iterable[Tests.Tests_item], Tests],
                    labInformation: LabInformation,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(tests, str):
                        raise TypeError("tests takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if tests is not None and not isinstance(tests, aas.SubmodelElement):
                        tests = self.Tests(tests)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(reportFile, tests, labInformation)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"Reports",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Reports"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"list of reports providing verification evidence for fire protection compliance."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Reports/1"),
                }

            def __init__(self, reports_items: Iterable[Reports_item], **kwargs: Unpack[SubmodelElementListMetadata]):

                # A str would be split into its characters
                if isinstance(reports_items, str):
                    raise TypeError("reports_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(reports_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"FireProtectionCertificates",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Fire certificate inventory list"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"structures fire protection compliance by linking applicable requirements with their verification evidence, such as test reports and certificates in accordance with EN 45545‑2."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FireProtectionCertificates/1"),
            }

        def __init__(
            self,
            requirementsSets: Union[Iterable[RequirementsSets.Requirementssets_item], RequirementsSets],
            reports: Union[Iterable[Reports.Reports_item], Reports],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(requirementsSets, str):
                raise TypeError("requirementsSets takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if requirementsSets is not None and not isinstance(requirementsSets, aas.SubmodelElement):
                requirementsSets = self.RequirementsSets(requirementsSets)

            # A str would be split into its characters
            if isinstance(reports, str):
                raise TypeError("reports takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if reports is not None and not isinstance(reports, aas.SubmodelElement):
                reports = self.Reports(reports)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(requirementsSets, reports)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Material(aas.SubmodelElementCollection):

        class MaterialName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaterialName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Material name"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"name of the material used "}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaterialName/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaterialCharacteristics(aas.Range):

            @staticmethod
            def template_defaults() -> RangeMetadata:
                return {
                    "id_short": r"MaterialCharacteristics",
                    "value_type": xsd.Int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Material characteristics"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"normalized index (0–100) derived from fire performance parameters according to EN 45545‑2"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaterialCharacteristics/1"),
                }

            def __init__(self, min: xsd.Int, max: xsd.Int, **kwargs: Unpack[RangeMetadata]):

                super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

        class Masses(aas.SubmodelElementCollection):

            class TotalMassPerUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TotalMassPerUnit",
                        "value_type": xsd.Float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"total mass of the material per defined unit, used for fire behavior assessment"
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TotalMassPerUnit/1"),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CombustibleMassPerUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CombustibleMassPerUnit",
                        "value_type": xsd.Float,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"portion of the material mass per unit that is combustible"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/CombustibleMassPerUnit/1"),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Unit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Unit",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Unit/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {"id_short": r"Masses", "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Masses/1")}

            def __init__(
                self,
                totalMassPerUnit: Union[xsd.Float, TotalMassPerUnit],
                combustibleMassPerUnit: Union[xsd.Float, CombustibleMassPerUnit],
                unit: Union[str, Unit],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if totalMassPerUnit is not None and not isinstance(totalMassPerUnit, aas.SubmodelElement):
                    totalMassPerUnit = self.TotalMassPerUnit(totalMassPerUnit)

                # Build a submodel element if a raw value was passed in the argument

                if combustibleMassPerUnit is not None and not isinstance(combustibleMassPerUnit, aas.SubmodelElement):
                    combustibleMassPerUnit = self.CombustibleMassPerUnit(combustibleMassPerUnit)

                # Build a submodel element if a raw value was passed in the argument

                if unit is not None and not isinstance(unit, aas.SubmodelElement):
                    unit = self.Unit(unit)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(totalMassPerUnit, combustibleMassPerUnit, unit)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TestedMaterialCombinationDescription(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TestedMaterialCombinationDescription",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Tested material combination description"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"description of the material combination as tested in fire protection assessments"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/cds/TestedMaterialCombinationDescription/1"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Material",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Material information"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"describes the fire‑relevant characteristics of the materials used, providing the technical basis for fire behavior assessment and interpretation of test results."
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Material/1"),
            }

        def __init__(
            self,
            materialName: Union[str, MaterialName],
            materialCharacteristics: Union[Tuple[xsd.Int, xsd.Int], MaterialCharacteristics],
            masses: Masses,
            testedMaterialCombinationDescription: Union[str, TestedMaterialCombinationDescription],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if materialName is not None and not isinstance(materialName, aas.SubmodelElement):
                materialName = self.MaterialName(materialName)

            # Build a submodel element if a raw value was passed in the argument

            if materialCharacteristics is not None and not isinstance(materialCharacteristics, aas.SubmodelElement):
                materialCharacteristics = self.MaterialCharacteristics(
                    min=materialCharacteristics[0], max=materialCharacteristics[1]
                )

            # Build a submodel element if a raw value was passed in the argument

            if testedMaterialCombinationDescription is not None and not isinstance(
                testedMaterialCombinationDescription, aas.SubmodelElement
            ):
                testedMaterialCombinationDescription = self.TestedMaterialCombinationDescription(
                    testedMaterialCombinationDescription
                )

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                materialName, materialCharacteristics, masses, testedMaterialCombinationDescription
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"RailwayFireProtection",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Railway Fire Protection Submodel"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Contains the fire protection information associated with the product or component."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RailwayFireProtection/1"),
        }

    def __init__(
        self,
        id_: str,
        manufacturerInformation: ManufacturerInformation,
        fireProtectionCertificates: FireProtectionCertificates,
        material: Material,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            manufacturerInformation, fireProtectionCertificates, material
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
