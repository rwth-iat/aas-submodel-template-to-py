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


class RelationshipElementMetadata(TypedDict, total=False):
    """Metadata of aas.RelationshipElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    first: Optional[aas.Reference]
    second: Optional[aas.Reference]
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


class DEXPI(aas.Submodel):

    class PlantMetadata(aas.SubmodelElementCollection):

        class EnterpriseReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"EnterpriseReference",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/EnterpriseReference"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SiteReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"SiteReference",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SiteReference"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IndustrialComplexReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"IndustrialComplexReference",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/IndustrialComplexReference"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProcessPlantReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ProcessPlantReference",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ProcessPlantReference"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PlantSectionReference(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"PlantSectionReference",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/PlantSectionReference"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EnterpriseIdentificationCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EnterpriseIdentificationCode",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"http://sandbox.dexpi.org/rdl/EnterpriseIdentificationCodeAssignmentClass"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EnterpriseName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EnterpriseName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/EnterpriseNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IndustrialComplexIdentificationCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IndustrialComplexIdentificationCode",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"http://sandbox.dexpi.org/rdl/IndustrialComplexIdentificationCodeAssignmentClass"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IndustrialComplexName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IndustrialComplexName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/IndustrialComplexNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PlantSectionIdentificationCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PlantSectionIdentificationCode",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"http://sandbox.dexpi.org/rdl/PlantSectionIdentificationCodeAssignmentClass"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PlantSectionName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PlantSectionName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/PlantSectionNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProcessPlantIdentificationCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProcessPlantIdentificationCode",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"http://sandbox.dexpi.org/rdl/ProcessPlantIdentificationCodeAssignmentClass"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProcessPlantName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProcessPlantName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/ProcessPlantNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProjectName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProjectName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/ProjectNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProjectNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProjectNumber",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/ProjectNumberAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SiteIdentificationCode(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SiteIdentificationCode",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/SiteIdentificationCodeAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SiteName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SiteName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/SiteNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SubProjectName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SubProjectName",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/SubProjectNameAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SubProjectNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SubProjectNumber",
                    "value_type": str,
                    "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/SubProjectNumberAssignmentClass"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {"id_short": r"ManufacturerName", "value_type": str}

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DateOfManufacture(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {"id_short": r"DateOfManufacture", "value_type": xsd.Date}

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndProductCASName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {"id_short": r"EndProductCASName", "value_type": str}

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndProductName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {"id_short": r"EndProductName", "value_type": str}

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"PlantMetadata",
                "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/PlantMetadata"),
            }

        def __init__(
            self,
            enterpriseReference: Optional[Union[aas.Reference, EnterpriseReference]] = None,
            siteReference: Optional[Union[aas.Reference, SiteReference]] = None,
            industrialComplexReference: Optional[Union[aas.Reference, IndustrialComplexReference]] = None,
            processPlantReference: Optional[Union[aas.Reference, ProcessPlantReference]] = None,
            plantSectionReference: Optional[Union[aas.Reference, PlantSectionReference]] = None,
            enterpriseIdentificationCode: Optional[Union[str, EnterpriseIdentificationCode]] = None,
            enterpriseName: Optional[Union[str, EnterpriseName]] = None,
            industrialComplexIdentificationCode: Optional[Union[str, IndustrialComplexIdentificationCode]] = None,
            industrialComplexName: Optional[Union[str, IndustrialComplexName]] = None,
            plantSectionIdentificationCode: Optional[Union[str, PlantSectionIdentificationCode]] = None,
            plantSectionName: Optional[Union[str, PlantSectionName]] = None,
            processPlantIdentificationCode: Optional[Union[str, ProcessPlantIdentificationCode]] = None,
            processPlantName: Optional[Union[str, ProcessPlantName]] = None,
            projectName: Optional[Union[str, ProjectName]] = None,
            projectNumber: Optional[Union[str, ProjectNumber]] = None,
            siteIdentificationCode: Optional[Union[str, SiteIdentificationCode]] = None,
            siteName: Optional[Union[str, SiteName]] = None,
            subProjectName: Optional[Union[str, SubProjectName]] = None,
            subProjectNumber: Optional[Union[str, SubProjectNumber]] = None,
            manufacturerName: Optional[Union[str, ManufacturerName]] = None,
            dateOfManufacture: Optional[Union[xsd.Date, DateOfManufacture]] = None,
            endProductCASName: Optional[Iterable[Union[str, EndProductCASName]]] = None,
            endProductName: Optional[Iterable[Union[str, EndProductName]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if enterpriseReference is not None and not isinstance(enterpriseReference, aas.SubmodelElement):
                enterpriseReference = self.EnterpriseReference(enterpriseReference)

            # Build a submodel element if a raw value was passed in the argument

            if siteReference is not None and not isinstance(siteReference, aas.SubmodelElement):
                siteReference = self.SiteReference(siteReference)

            # Build a submodel element if a raw value was passed in the argument

            if industrialComplexReference is not None and not isinstance(
                industrialComplexReference, aas.SubmodelElement
            ):
                industrialComplexReference = self.IndustrialComplexReference(industrialComplexReference)

            # Build a submodel element if a raw value was passed in the argument

            if processPlantReference is not None and not isinstance(processPlantReference, aas.SubmodelElement):
                processPlantReference = self.ProcessPlantReference(processPlantReference)

            # Build a submodel element if a raw value was passed in the argument

            if plantSectionReference is not None and not isinstance(plantSectionReference, aas.SubmodelElement):
                plantSectionReference = self.PlantSectionReference(plantSectionReference)

            # Build a submodel element if a raw value was passed in the argument

            if enterpriseIdentificationCode is not None and not isinstance(
                enterpriseIdentificationCode, aas.SubmodelElement
            ):
                enterpriseIdentificationCode = self.EnterpriseIdentificationCode(enterpriseIdentificationCode)

            # Build a submodel element if a raw value was passed in the argument

            if enterpriseName is not None and not isinstance(enterpriseName, aas.SubmodelElement):
                enterpriseName = self.EnterpriseName(enterpriseName)

            # Build a submodel element if a raw value was passed in the argument

            if industrialComplexIdentificationCode is not None and not isinstance(
                industrialComplexIdentificationCode, aas.SubmodelElement
            ):
                industrialComplexIdentificationCode = self.IndustrialComplexIdentificationCode(
                    industrialComplexIdentificationCode
                )

            # Build a submodel element if a raw value was passed in the argument

            if industrialComplexName is not None and not isinstance(industrialComplexName, aas.SubmodelElement):
                industrialComplexName = self.IndustrialComplexName(industrialComplexName)

            # Build a submodel element if a raw value was passed in the argument

            if plantSectionIdentificationCode is not None and not isinstance(
                plantSectionIdentificationCode, aas.SubmodelElement
            ):
                plantSectionIdentificationCode = self.PlantSectionIdentificationCode(plantSectionIdentificationCode)

            # Build a submodel element if a raw value was passed in the argument

            if plantSectionName is not None and not isinstance(plantSectionName, aas.SubmodelElement):
                plantSectionName = self.PlantSectionName(plantSectionName)

            # Build a submodel element if a raw value was passed in the argument

            if processPlantIdentificationCode is not None and not isinstance(
                processPlantIdentificationCode, aas.SubmodelElement
            ):
                processPlantIdentificationCode = self.ProcessPlantIdentificationCode(processPlantIdentificationCode)

            # Build a submodel element if a raw value was passed in the argument

            if processPlantName is not None and not isinstance(processPlantName, aas.SubmodelElement):
                processPlantName = self.ProcessPlantName(processPlantName)

            # Build a submodel element if a raw value was passed in the argument

            if projectName is not None and not isinstance(projectName, aas.SubmodelElement):
                projectName = self.ProjectName(projectName)

            # Build a submodel element if a raw value was passed in the argument

            if projectNumber is not None and not isinstance(projectNumber, aas.SubmodelElement):
                projectNumber = self.ProjectNumber(projectNumber)

            # Build a submodel element if a raw value was passed in the argument

            if siteIdentificationCode is not None and not isinstance(siteIdentificationCode, aas.SubmodelElement):
                siteIdentificationCode = self.SiteIdentificationCode(siteIdentificationCode)

            # Build a submodel element if a raw value was passed in the argument

            if siteName is not None and not isinstance(siteName, aas.SubmodelElement):
                siteName = self.SiteName(siteName)

            # Build a submodel element if a raw value was passed in the argument

            if subProjectName is not None and not isinstance(subProjectName, aas.SubmodelElement):
                subProjectName = self.SubProjectName(subProjectName)

            # Build a submodel element if a raw value was passed in the argument

            if subProjectNumber is not None and not isinstance(subProjectNumber, aas.SubmodelElement):
                subProjectNumber = self.SubProjectNumber(subProjectNumber)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if dateOfManufacture is not None and not isinstance(dateOfManufacture, aas.SubmodelElement):
                dateOfManufacture = self.DateOfManufacture(dateOfManufacture)

            # A str would be split into its characters
            if isinstance(endProductCASName, str):
                raise TypeError("endProductCASName takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if endProductCASName:
                endProductCASName = [
                    i if isinstance(i, aas.SubmodelElement) else self.EndProductCASName(i) for i in endProductCASName
                ]

            # A str would be split into its characters
            if isinstance(endProductName, str):
                raise TypeError("endProductName takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if endProductName:
                endProductName = [
                    i if isinstance(i, aas.SubmodelElement) else self.EndProductName(i) for i in endProductName
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                enterpriseReference,
                siteReference,
                industrialComplexReference,
                processPlantReference,
                plantSectionReference,
                enterpriseIdentificationCode,
                enterpriseName,
                industrialComplexIdentificationCode,
                industrialComplexName,
                plantSectionIdentificationCode,
                plantSectionName,
                processPlantIdentificationCode,
                processPlantName,
                projectName,
                projectNumber,
                siteIdentificationCode,
                siteName,
                subProjectName,
                subProjectNumber,
                manufacturerName,
                dateOfManufacture,
                endProductCASName,
                endProductName,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Model(aas.SubmodelElementCollection):

        class ModelMetadata(aas.SubmodelElementCollection):

            class ApprovalDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ApprovalDate",
                        "value_type": xsd.Date,
                        "semantic_id": global_ref(
                            r"http://sandbox.dexpi.org/rdl/ApprovalDateRepresentationAssignmentClass"
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ApprovalDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"ApprovalDescription",
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/ApprovalDescriptionAssignmentClass"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ArchiveNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ArchiveNumber",
                        "value_type": str,
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/ArchiveNumberAssignmentClass"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CheckerName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CheckerName",
                        "value_type": str,
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/CheckerNameAssignmentClass"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CreationDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CreationDate",
                        "value_type": xsd.Date,
                        "semantic_id": global_ref(
                            r"http://sandbox.dexpi.org/rdl/CreationDateRepresentationAssignmentClass"
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CreatorName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CreatorName",
                        "value_type": str,
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/CreatorNameAssignmentClass"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DesignerName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignerName",
                        "value_type": str,
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/DesignerNameAssignmentClass"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DrawingNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DrawingNumber",
                        "value_type": str,
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/DrawingNumberAssignmentClass"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DrawingSubTitle(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"DrawingSubTitle",
                        "semantic_id": global_ref(r"http://sandbox.dexpi.org/rdl/DrawingSubTitleAssignmentClass"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LastModificationDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LastModificationDate",
                        "value_type": xsd.Date,
                        "semantic_id": global_ref(
                            r"http://sandbox.dexpi.org/rdl/LastModificationDateRepresentationAssignmentClass"
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ModelMetadata",
                    "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ModelMetadata"),
                }

            def __init__(
                self,
                approvalDate: Optional[Union[xsd.Date, ApprovalDate]] = None,
                approvalDescription: Optional[Union[aas.LangStringSet, ApprovalDescription]] = None,
                archiveNumber: Optional[Union[str, ArchiveNumber]] = None,
                checkerName: Optional[Union[str, CheckerName]] = None,
                creationDate: Optional[Union[xsd.Date, CreationDate]] = None,
                creatorName: Optional[Union[str, CreatorName]] = None,
                designerName: Optional[Union[str, DesignerName]] = None,
                drawingNumber: Optional[Union[str, DrawingNumber]] = None,
                drawingSubTitle: Optional[Union[aas.LangStringSet, DrawingSubTitle]] = None,
                lastModificationDate: Optional[Union[xsd.Date, LastModificationDate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if approvalDate is not None and not isinstance(approvalDate, aas.SubmodelElement):
                    approvalDate = self.ApprovalDate(approvalDate)

                # Build a submodel element if a raw value was passed in the argument

                if approvalDescription is not None and not isinstance(approvalDescription, aas.SubmodelElement):
                    approvalDescription = self.ApprovalDescription(approvalDescription)

                # Build a submodel element if a raw value was passed in the argument

                if archiveNumber is not None and not isinstance(archiveNumber, aas.SubmodelElement):
                    archiveNumber = self.ArchiveNumber(archiveNumber)

                # Build a submodel element if a raw value was passed in the argument

                if checkerName is not None and not isinstance(checkerName, aas.SubmodelElement):
                    checkerName = self.CheckerName(checkerName)

                # Build a submodel element if a raw value was passed in the argument

                if creationDate is not None and not isinstance(creationDate, aas.SubmodelElement):
                    creationDate = self.CreationDate(creationDate)

                # Build a submodel element if a raw value was passed in the argument

                if creatorName is not None and not isinstance(creatorName, aas.SubmodelElement):
                    creatorName = self.CreatorName(creatorName)

                # Build a submodel element if a raw value was passed in the argument

                if designerName is not None and not isinstance(designerName, aas.SubmodelElement):
                    designerName = self.DesignerName(designerName)

                # Build a submodel element if a raw value was passed in the argument

                if drawingNumber is not None and not isinstance(drawingNumber, aas.SubmodelElement):
                    drawingNumber = self.DrawingNumber(drawingNumber)

                # Build a submodel element if a raw value was passed in the argument

                if drawingSubTitle is not None and not isinstance(drawingSubTitle, aas.SubmodelElement):
                    drawingSubTitle = self.DrawingSubTitle(drawingSubTitle)

                # Build a submodel element if a raw value was passed in the argument

                if lastModificationDate is not None and not isinstance(lastModificationDate, aas.SubmodelElement):
                    lastModificationDate = self.LastModificationDate(lastModificationDate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    approvalDate,
                    approvalDescription,
                    archiveNumber,
                    checkerName,
                    creationDate,
                    creatorName,
                    designerName,
                    drawingNumber,
                    drawingSubTitle,
                    lastModificationDate,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ModelFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ModelFile",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/DEXPI/1/0/ModelFile"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/xml", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class ModelRepresentation(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ModelRepresentation",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/DEXPI/1/0/ModelRepresentation"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class MappingDirectory(aas.SubmodelElementCollection):

            class ProcessInstrumentationFunction_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProcessInstrumentationFunction_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ProcessInstrumentationFunction_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ProcessInstrumentationFunction-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ProcessInstrumentationFunction-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessInstrumentationFunction_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    processInstrumentationFunction_1_rel: ProcessInstrumentationFunction_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, processInstrumentationFunction_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessInstrumentationFunction_2(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProcessInstrumentationFunction_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ProcessInstrumentationFunction_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ProcessInstrumentationFunction-2",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ProcessInstrumentationFunction-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessInstrumentationFunction_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    processInstrumentationFunction_2_rel: ProcessInstrumentationFunction_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, processInstrumentationFunction_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessInstrumentationFunction_3(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProcessInstrumentationFunction_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ProcessInstrumentationFunction_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ProcessInstrumentationFunction-3",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ProcessInstrumentationFunction-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessInstrumentationFunction_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    processInstrumentationFunction_3_rel: ProcessInstrumentationFunction_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, processInstrumentationFunction_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ProcessInstrumentationFunction_4(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProcessInstrumentationFunction_4_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ProcessInstrumentationFunction_4_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ProcessInstrumentationFunction-4",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ProcessInstrumentationFunction-4"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessInstrumentationFunction_4",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    processInstrumentationFunction_4_rel: ProcessInstrumentationFunction_4_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, processInstrumentationFunction_4_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ActuatingFunction_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ActuatingFunction_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ActuatingFunction_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ActuatingFunction-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ActuatingFunction-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ActuatingFunction_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    actuatingFunction_1_rel: ActuatingFunction_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, actuatingFunction_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ActuatingFunction_2(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ActuatingFunction_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ActuatingFunction_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ActuatingFunction-2",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ActuatingFunction-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ActuatingFunction_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    actuatingFunction_2_rel: ActuatingFunction_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, actuatingFunction_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ActuatingFunction_3(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ActuatingFunction_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ActuatingFunction_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ActuatingFunction-3",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ActuatingFunction-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ActuatingFunction_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    actuatingFunction_3_rel: ActuatingFunction_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, actuatingFunction_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class PlateHeatExchanger_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PlateHeatExchanger_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"PlateHeatExchanger_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=PlateHeatExchanger-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/PlateHeatExchanger-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"PlateHeatExchanger_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    plateHeatExchanger_1_rel: PlateHeatExchanger_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, plateHeatExchanger_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TubularHeatExchanger_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TubularHeatExchanger_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"TubularHeatExchanger_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=TubularHeatExchanger-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/TubularHeatExchanger-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"TubularHeatExchanger_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    tubularHeatExchanger_1_rel: TubularHeatExchanger_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, tubularHeatExchanger_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CentrifugalPump_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CentrifugalPump_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"CentrifugalPump_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=CentrifugalPump-1"
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/CentrifugalPump-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"CentrifugalPump_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    centrifugalPump_1_rel: CentrifugalPump_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, centrifugalPump_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ReciprocatingPump_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReciprocatingPump_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ReciprocatingPump_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ReciprocatingPump-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ReciprocatingPump-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ReciprocatingPump_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    reciprocatingPump_1_rel: ReciprocatingPump_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tagName, class_, localId, reciprocatingPump_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Tank_1(aas.SubmodelElementCollection):

                class TagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Tank_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Tank_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Tank-1"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Tank-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Tank_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/TagMapping"),
                    }

                def __init__(
                    self,
                    tagName: Union[str, TagName],
                    localId: Union[str, LocalId],
                    tank_1_rel: Tank_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                        tagName = self.TagName(tagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(tagName, class_, localId, tank_1_rel)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ControlledActuator_1(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ControlledActuator_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ControlledActuator_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ControlledActuator-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ControlledActuator-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ControlledActuator_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    controlledActuator_1_rel: ControlledActuator_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, controlledActuator_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class OperatedValveReference_1(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OperatedValveReference_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"OperatedValveReference_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=OperatedValveReference-1",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/OperatedValveReference-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"OperatedValveReference_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    operatedValveReference_1_rel: OperatedValveReference_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, operatedValveReference_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ControlledActuator_2(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ControlledActuator_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ControlledActuator_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ControlledActuator-2",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ControlledActuator-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ControlledActuator_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    controlledActuator_2_rel: ControlledActuator_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, controlledActuator_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class OperatedValveReference_2(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OperatedValveReference_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"OperatedValveReference_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=OperatedValveReference-2",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/OperatedValveReference-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"OperatedValveReference_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    operatedValveReference_2_rel: OperatedValveReference_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, operatedValveReference_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ControlledActuator_3(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ControlledActuator_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"ControlledActuator_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=ControlledActuator-3",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/ControlledActuator-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ControlledActuator_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    controlledActuator_3_rel: ControlledActuator_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, controlledActuator_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class OperatedValveReference_3(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OperatedValveReference_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"OperatedValveReference_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(
                                        type_=aas.KeyTypes.FRAGMENT_REFERENCE,
                                        value=r"ProteusXML@ID=OperatedValveReference-3",
                                    ),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/OperatedValveReference-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"OperatedValveReference_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    operatedValveReference_3_rel: OperatedValveReference_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, operatedValveReference_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_3(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-3"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_3_rel: Nozzle_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_4(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_4_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_4_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-4"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-4"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_4",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_4_rel: Nozzle_4_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_4_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_13(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_13_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_13_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-13"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-13"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_13",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_13_rel: Nozzle_13_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_13_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_14(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_14_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_14_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-14"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-14"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_14",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_14_rel: Nozzle_14_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_14_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_1(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-1"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_1_rel: Chamber_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_2(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-2"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_2_rel: Chamber_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_10(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_10_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_10_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-10"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-10"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_10",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_10_rel: Nozzle_10_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_10_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_11(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_11_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_11_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-11"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-11"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_11",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_11_rel: Nozzle_11_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_11_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_16(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_16_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_16_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-16"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-16"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_16",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_16_rel: Nozzle_16_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_16_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_15(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_15_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_15_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-15"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-15"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_15",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_15_rel: Nozzle_15_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_15_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_3(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_3_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_3_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-3"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-3"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_3",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_3_rel: Chamber_3_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_3_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_4(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_4_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_4_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-4"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-4"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_4",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_4_rel: Chamber_4_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_4_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_1(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_1_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_1_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-1"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-1"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_1",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_1_rel: Nozzle_1_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_1_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_2(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_2_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_2_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-2"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-2"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_2",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_2_rel: Nozzle_2_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_2_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_7(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_7_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_7_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-7"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-7"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_7",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_7_rel: Nozzle_7_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_7_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_9(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_9_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_9_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-9"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-9"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_9",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_9_rel: Nozzle_9_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_9_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_5(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_5_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_5_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-5"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-5"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_5",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_5_rel: Nozzle_5_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_5_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_6(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_6_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_6_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-6"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-6"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_6",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_6_rel: Nozzle_6_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_6_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_18(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_18_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_18_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-18"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-18"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_18",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_18_rel: Nozzle_18_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_18_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_8(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_8_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_8_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-8"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-8"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_8",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_8_rel: Nozzle_8_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_8_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_12(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_12_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_12_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-12"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-12"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_12",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_12_rel: Nozzle_12_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_12_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_17(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_17_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_17_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-17"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-17"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_17",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_17_rel: Nozzle_17_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_17_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Nozzle_19(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Nozzle_19_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Nozzle_19_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Nozzle-19"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Nozzle-19"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Nozzle_19",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    nozzle_19_rel: Nozzle_19_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, nozzle_19_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_7(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_7_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_7_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-7"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-7"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_7",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_7_rel: Chamber_7_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_7_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Chamber_8(aas.SubmodelElementCollection):

                class SubTagName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubTagName",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagName"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ParentLocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ParentLocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/ParentTagLocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Class(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Class",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Class"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LocalId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LocalId",
                            "value_type": str,
                            "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/LocalId"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Chamber_8_rel(aas.RelationshipElement):

                    @staticmethod
                    def template_defaults() -> RelationshipElementMetadata:
                        return {
                            "id_short": r"Chamber_8_rel",
                            "first": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.SUBMODEL,
                                        value=r"https://epc.org/sm_id/9f236679-e52d-4a52-aa85-dea871a89f9b",
                                    ),
                                    aas.Key(type_=aas.KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r"Model01"),
                                    aas.Key(type_=aas.KeyTypes.FILE, value=r"ModelFile"),
                                    aas.Key(type_=aas.KeyTypes.FRAGMENT_REFERENCE, value=r"ProteusXML@ID=Chamber-8"),
                                ),
                                type_=type(None),
                                referred_semantic_id=None,
                            ),
                            "second": global_ref(r"https://epc.org/role/Chamber-8"),
                        }

                    def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                        super().__init__(**(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Chamber_8",
                        "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/SubTagMapping"),
                    }

                def __init__(
                    self,
                    subTagName: Union[str, SubTagName],
                    parentLocalId: Union[str, ParentLocalId],
                    localId: Union[str, LocalId],
                    chamber_8_rel: Chamber_8_rel,
                    class_: Optional[Union[str, Class]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if subTagName is not None and not isinstance(subTagName, aas.SubmodelElement):
                        subTagName = self.SubTagName(subTagName)

                    # Build a submodel element if a raw value was passed in the argument

                    if parentLocalId is not None and not isinstance(parentLocalId, aas.SubmodelElement):
                        parentLocalId = self.ParentLocalId(parentLocalId)

                    # Build a submodel element if a raw value was passed in the argument

                    if class_ is not None and not isinstance(class_, aas.SubmodelElement):
                        class_ = self.Class(class_)

                    # Build a submodel element if a raw value was passed in the argument

                    if localId is not None and not isinstance(localId, aas.SubmodelElement):
                        localId = self.LocalId(localId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        subTagName, parentLocalId, class_, localId, chamber_8_rel
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"MappingDirectory",
                    "semantic_id": global_ref(r"http://admin-shell.io/idta/DEXPI/1/0/MappingDirectory"),
                }

            def __init__(
                self,
                processInstrumentationFunction_1: Optional[ProcessInstrumentationFunction_1] = None,
                processInstrumentationFunction_2: Optional[ProcessInstrumentationFunction_2] = None,
                processInstrumentationFunction_3: Optional[ProcessInstrumentationFunction_3] = None,
                processInstrumentationFunction_4: Optional[ProcessInstrumentationFunction_4] = None,
                actuatingFunction_1: Optional[ActuatingFunction_1] = None,
                actuatingFunction_2: Optional[ActuatingFunction_2] = None,
                actuatingFunction_3: Optional[ActuatingFunction_3] = None,
                plateHeatExchanger_1: Optional[PlateHeatExchanger_1] = None,
                tubularHeatExchanger_1: Optional[TubularHeatExchanger_1] = None,
                centrifugalPump_1: Optional[CentrifugalPump_1] = None,
                reciprocatingPump_1: Optional[ReciprocatingPump_1] = None,
                tank_1: Optional[Tank_1] = None,
                controlledActuator_1: Optional[ControlledActuator_1] = None,
                operatedValveReference_1: Optional[OperatedValveReference_1] = None,
                controlledActuator_2: Optional[ControlledActuator_2] = None,
                operatedValveReference_2: Optional[OperatedValveReference_2] = None,
                controlledActuator_3: Optional[ControlledActuator_3] = None,
                operatedValveReference_3: Optional[OperatedValveReference_3] = None,
                nozzle_3: Optional[Nozzle_3] = None,
                nozzle_4: Optional[Nozzle_4] = None,
                nozzle_13: Optional[Nozzle_13] = None,
                nozzle_14: Optional[Nozzle_14] = None,
                chamber_1: Optional[Chamber_1] = None,
                chamber_2: Optional[Chamber_2] = None,
                nozzle_10: Optional[Nozzle_10] = None,
                nozzle_11: Optional[Nozzle_11] = None,
                nozzle_16: Optional[Nozzle_16] = None,
                nozzle_15: Optional[Nozzle_15] = None,
                chamber_3: Optional[Chamber_3] = None,
                chamber_4: Optional[Chamber_4] = None,
                nozzle_1: Optional[Nozzle_1] = None,
                nozzle_2: Optional[Nozzle_2] = None,
                nozzle_7: Optional[Nozzle_7] = None,
                nozzle_9: Optional[Nozzle_9] = None,
                nozzle_5: Optional[Nozzle_5] = None,
                nozzle_6: Optional[Nozzle_6] = None,
                nozzle_18: Optional[Nozzle_18] = None,
                nozzle_8: Optional[Nozzle_8] = None,
                nozzle_12: Optional[Nozzle_12] = None,
                nozzle_17: Optional[Nozzle_17] = None,
                nozzle_19: Optional[Nozzle_19] = None,
                chamber_7: Optional[Chamber_7] = None,
                chamber_8: Optional[Chamber_8] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    processInstrumentationFunction_1,
                    processInstrumentationFunction_2,
                    processInstrumentationFunction_3,
                    processInstrumentationFunction_4,
                    actuatingFunction_1,
                    actuatingFunction_2,
                    actuatingFunction_3,
                    plateHeatExchanger_1,
                    tubularHeatExchanger_1,
                    centrifugalPump_1,
                    reciprocatingPump_1,
                    tank_1,
                    controlledActuator_1,
                    operatedValveReference_1,
                    controlledActuator_2,
                    operatedValveReference_2,
                    controlledActuator_3,
                    operatedValveReference_3,
                    nozzle_3,
                    nozzle_4,
                    nozzle_13,
                    nozzle_14,
                    chamber_1,
                    chamber_2,
                    nozzle_10,
                    nozzle_11,
                    nozzle_16,
                    nozzle_15,
                    chamber_3,
                    chamber_4,
                    nozzle_1,
                    nozzle_2,
                    nozzle_7,
                    nozzle_9,
                    nozzle_5,
                    nozzle_6,
                    nozzle_18,
                    nozzle_8,
                    nozzle_12,
                    nozzle_17,
                    nozzle_19,
                    chamber_7,
                    chamber_8,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {"id_short": r"Model", "semantic_id": global_ref(r"http://admin-shell.io/dexpi/1/0/Model")}

        def __init__(
            self,
            modelMetadata: ModelMetadata,
            modelFile: ModelFile,
            modelRepresentation: Optional[ModelRepresentation] = None,
            mappingDirectory: Optional[MappingDirectory] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                modelMetadata, modelFile, modelRepresentation, mappingDirectory
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"DEXPI",
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/DEXPI/1/0"),
        }

    def __init__(
        self, id_: str, plantMetadata: PlantMetadata, model: Iterable[Model], **kwargs: Unpack[SubmodelMetadata]
    ):

        # A str would be split into its characters
        if isinstance(model, str):
            raise TypeError("model takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(plantMetadata, model)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
