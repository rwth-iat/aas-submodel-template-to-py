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


class Nameplate(aas.Submodel):

    class URIOfTheProduct(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"URIOfTheProduct",
                "value_type": xsd.AnyURI,
                "semantic_id": global_ref(r"0112/2///61987#ABN590#002"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABH173#003"),),
            }

        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerName(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"ManufacturerName",
                "semantic_id": global_ref(r"0112/2///61987#ABA565#009"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO677#004"),),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerProductDesignation(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"ManufacturerProductDesignation",
                "semantic_id": global_ref(r"0112/2///61987#ABA567#009"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAW338#003"),),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class AddressInformation(aas.SubmodelElementCollection):

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AddressInformation",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r'Note: this set of information is defined by SMT drop-in "Address Information"'}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
                ),
                "supplemental_semantic_id": (
                    global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                    global_ref(r"0112/2///61360_7#AAS002#001"),
                    global_ref(r"0173-1#02-AAQ837#008/0173-1#01-ADR448#008"),
                ),
            }

        def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements()

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ManufacturerProductRoot(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"ManufacturerProductRoot",
                "value_id": global_ref(r"0112/2///61987#ABP464#002"),
                "semantic_id": global_ref(r"0112/2///61360_7#AAS011#001"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAU732#003"),),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerProductFamily(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"ManufacturerProductFamily",
                "semantic_id": global_ref(r"0112/2///61987#ABP464#002"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAU731#003"),),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerProductType(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ManufacturerProductType",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA300#008"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO057#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class OrderCodeOfManufacturer(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"OrderCodeOfManufacturer",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA950#008"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO227#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ProductArticleNumberOfManufacturer(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ProductArticleNumberOfManufacturer",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA581#007"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO676#005"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class SerialNumber(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"SerialNumber",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA951#009"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAM556#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class YearOfConstruction(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"YearOfConstruction",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABP000#002"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAP906#003"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DateOfManufacture(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"DateOfManufacture",
                "value_type": xsd.Date,
                "semantic_id": global_ref(r"0112/2///61987#ABB757#007"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAR972#004"),),
            }

        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class HardwareVersion(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"HardwareVersion",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA926#008"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAN270#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class FirmwareVersion(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"FirmwareVersion",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA302#006"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAM985#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class SoftwareVersion(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"SoftwareVersion",
                "value_type": str,
                "semantic_id": global_ref(r"0112/2///61987#ABA601#008"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAM737#004"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class CountryOfOrigin(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"CountryOfOrigin",
                "value_type": str,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes"}
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABP462#001"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO259#007"),),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class UniqueFacilityIdentifier(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"UniqueFacilityIdentifier",
                "value_type": str,
                "semantic_id": global_ref(r"https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier"),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class CompanyLogo(aas.File):

        @staticmethod
        def template_defaults() -> FileMetadata:
            return {
                "id_short": r"CompanyLogo",
                "semantic_id": global_ref(r"0112/2///61987#ABP463#001"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI776#002"),),
            }

        def __init__(self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]):

            super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

    class Markings(GeneratedSubmodelElementList):

        class Markings_item(aas.SubmodelElementCollection):

            class MarkingName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MarkingName",
                        "value_type": str,
                        "semantic_id": global_ref(r"0112/2///61987#ABA231#009"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI190#003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DesignationOfCertificateOrApproval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignationOfCertificateOrApproval",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Approval identifier, reference to the certificate number, to be entered without spaces "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABH783#003"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI975#002"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IssueDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IssueDate",
                        "value_type": xsd.Date,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABO097#001"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL774#001"),),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExpiryDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpiryDate",
                        "value_type": xsd.Date,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABH830#002"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL775#001"),),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MarkingFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"MarkingFile",
                        "semantic_id": global_ref(r"0112/2///61987#ABO100#002"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI191#003"),),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class MarkingAdditionalText(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MarkingAdditionalText",
                        "value_type": str,
                        "semantic_id": global_ref(r"0112/2///61987#ABB146#007"),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI192#003"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission"
                        }
                    ),
                    "semantic_id": global_ref(r"0112/2///61360_7#AAS009#001"),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI564#003/0173-1#01-AHF850#003"),),
                }

            def __init__(
                self,
                markingName: Union[str, MarkingName],
                markingFile: MarkingFile,
                designationOfCertificateOrApproval: Optional[Union[str, DesignationOfCertificateOrApproval]] = None,
                issueDate: Optional[Union[xsd.Date, IssueDate]] = None,
                expiryDate: Optional[Union[xsd.Date, ExpiryDate]] = None,
                markingAdditionalText: Optional[Iterable[Union[str, MarkingAdditionalText]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if markingName is not None and not isinstance(markingName, aas.SubmodelElement):
                    markingName = self.MarkingName(markingName)

                # Build a submodel element if a raw value was passed in the argument

                if designationOfCertificateOrApproval is not None and not isinstance(
                    designationOfCertificateOrApproval, aas.SubmodelElement
                ):
                    designationOfCertificateOrApproval = self.DesignationOfCertificateOrApproval(
                        designationOfCertificateOrApproval
                    )

                # Build a submodel element if a raw value was passed in the argument

                if issueDate is not None and not isinstance(issueDate, aas.SubmodelElement):
                    issueDate = self.IssueDate(issueDate)

                # Build a submodel element if a raw value was passed in the argument

                if expiryDate is not None and not isinstance(expiryDate, aas.SubmodelElement):
                    expiryDate = self.ExpiryDate(expiryDate)

                # A str would be split into its characters
                if isinstance(markingAdditionalText, str):
                    raise TypeError("markingAdditionalText takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if markingAdditionalText:
                    markingAdditionalText = [
                        i if isinstance(i, aas.SubmodelElement) else self.MarkingAdditionalText(i)
                        for i in markingAdditionalText
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    markingName,
                    designationOfCertificateOrApproval,
                    issueDate,
                    expiryDate,
                    markingFile,
                    markingAdditionalText,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"Markings",
                "type_value_list_element": aas.SubmodelElementCollection,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Note: CE marking is declared as mandatory according to EU Blue Guide"}
                ),
                "semantic_id": global_ref(r"0112/2///61360_7#AAS006#001"),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABI563#003/0173-1#01-AHF849#003"),),
            }

        def __init__(self, markings_items: Iterable[Markings_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(markings_items, str):
                raise TypeError("markings_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(markings_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class AssetSpecificProperties(aas.SubmodelElementCollection):

        class ArbitraryProperty(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ArbitraryProperty",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Note: Every property can be used. Note: The idShort is arbitrary Note: The use of a displayName is recommended."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryProp"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ArbitraryMLP(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"ArbitraryMLP",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary Note: The use of a displayName is recommended."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryMLP"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ArbitraryFile(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"ArbitraryFile",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Note: Every file can be used. The idShort is arbitrary Note: The use of a displayName is recommended."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryFile"),
                }

            def __init__(
                self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class GuidelineSpecificProperties(GeneratedSubmodelElementList):

            class Guidelinespecificproperties_item(aas.SubmodelElementCollection):

                class GuidelineForConformityDeclaration(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GuidelineForConformityDeclaration",
                            "value_type": str,
                            "semantic_id": global_ref(r"0173-1#02-AAO856#002"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryProperty(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArbitraryProperty",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every property can be used. Note: The idShort is arbitrary Note: The use of a displayName is recommended."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryProp"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArbitraryFile(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"ArbitraryFile",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every file can be used. The idShort is arbitrary Note: The use of a displayName is recommended."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryFile"),
                        }

                    def __init__(
                        self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                class ArbitraryMLP(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ArbitraryMLP",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Note: Every multilanguage property can be used. Note: The idShort is arbitrary Note: The use of a displayName is recommended."
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/SMT/General/ArbitraryMLP"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {"id_short": None, "semantic_id": global_ref(r"0173-1#01-AHD205#004")}

                def __init__(
                    self,
                    guidelineForConformityDeclaration: Union[str, GuidelineForConformityDeclaration],
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                    arbitraryFile: Optional[Iterable[ArbitraryFile]] = None,
                    arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if guidelineForConformityDeclaration is not None and not isinstance(
                        guidelineForConformityDeclaration, aas.SubmodelElement
                    ):
                        guidelineForConformityDeclaration = self.GuidelineForConformityDeclaration(
                            guidelineForConformityDeclaration
                        )

                    # A str would be split into its characters
                    if isinstance(arbitraryProperty, str):
                        raise TypeError("arbitraryProperty takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryProperty:
                        arbitraryProperty = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i)
                            for i in arbitraryProperty
                        ]

                    # A str would be split into its characters
                    if isinstance(arbitraryFile, str):
                        raise TypeError("arbitraryFile takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(arbitraryMLP, str):
                        raise TypeError("arbitraryMLP takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if arbitraryMLP:
                        arbitraryMLP = [
                            i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        guidelineForConformityDeclaration, arbitraryProperty, arbitraryFile, arbitraryMLP
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"GuidelineSpecificProperties",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id": global_ref(r"0173-1#02-ABI219#003/0173-1#01-AHD205#004"),
                }

            def __init__(
                self,
                guidelinespecificproperties_items: Iterable[Guidelinespecificproperties_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(guidelinespecificproperties_items, str):
                    raise TypeError("guidelinespecificproperties_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    guidelinespecificproperties_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AssetSpecificProperties",
                "semantic_id": global_ref(r"0173-1#02-ABI218#003/0173-1#01-AGZ672#004"),
            }

        def __init__(
            self,
            arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
            arbitraryMLP: Optional[Iterable[Union[aas.MultiLanguageTextType, ArbitraryMLP]]] = None,
            arbitraryFile: Optional[Iterable[ArbitraryFile]] = None,
            guidelineSpecificProperties: Optional[
                Union[
                    Iterable[GuidelineSpecificProperties.Guidelinespecificproperties_item], GuidelineSpecificProperties
                ]
            ] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(arbitraryProperty, str):
                raise TypeError("arbitraryProperty takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if arbitraryProperty:
                arbitraryProperty = [
                    i if isinstance(i, aas.SubmodelElement) else self.ArbitraryProperty(i) for i in arbitraryProperty
                ]

            # A str would be split into its characters
            if isinstance(arbitraryMLP, str):
                raise TypeError("arbitraryMLP takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if arbitraryMLP:
                arbitraryMLP = [i if isinstance(i, aas.SubmodelElement) else self.ArbitraryMLP(i) for i in arbitraryMLP]

            # A str would be split into its characters
            if isinstance(arbitraryFile, str):
                raise TypeError("arbitraryFile takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(guidelineSpecificProperties, str):
                raise TypeError("guidelineSpecificProperties takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if guidelineSpecificProperties is not None and not isinstance(
                guidelineSpecificProperties, aas.SubmodelElement
            ):
                guidelineSpecificProperties = self.GuidelineSpecificProperties(guidelineSpecificProperties)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                arbitraryProperty, arbitraryMLP, arbitraryFile, guidelineSpecificProperties
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"Nameplate",
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Contains the nameplate information attached to the product"}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"3",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02006-3-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/nameplate/3/0/Nameplate"),
        }

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[xsd.AnyURI, URIOfTheProduct],
        manufacturerName: Union[aas.MultiLanguageTextType, ManufacturerName],
        manufacturerProductDesignation: Union[aas.MultiLanguageTextType, ManufacturerProductDesignation],
        addressInformation: AddressInformation,
        orderCodeOfManufacturer: Union[str, OrderCodeOfManufacturer],
        manufacturerProductRoot: Optional[Union[aas.MultiLanguageTextType, ManufacturerProductRoot]] = None,
        manufacturerProductFamily: Optional[Union[aas.MultiLanguageTextType, ManufacturerProductFamily]] = None,
        manufacturerProductType: Optional[Union[str, ManufacturerProductType]] = None,
        productArticleNumberOfManufacturer: Optional[Union[str, ProductArticleNumberOfManufacturer]] = None,
        serialNumber: Optional[Union[str, SerialNumber]] = None,
        yearOfConstruction: Optional[Union[str, YearOfConstruction]] = None,
        dateOfManufacture: Optional[Union[xsd.Date, DateOfManufacture]] = None,
        hardwareVersion: Optional[Union[str, HardwareVersion]] = None,
        firmwareVersion: Optional[Union[str, FirmwareVersion]] = None,
        softwareVersion: Optional[Union[str, SoftwareVersion]] = None,
        countryOfOrigin: Optional[Union[str, CountryOfOrigin]] = None,
        uniqueFacilityIdentifier: Optional[Union[str, UniqueFacilityIdentifier]] = None,
        companyLogo: Optional[CompanyLogo] = None,
        markings: Optional[Union[Iterable[Markings.Markings_item], Markings]] = None,
        assetSpecificProperties: Optional[AssetSpecificProperties] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if uRIOfTheProduct is not None and not isinstance(uRIOfTheProduct, aas.SubmodelElement):
            uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
            manufacturerName = self.ManufacturerName(manufacturerName)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerProductDesignation is not None and not isinstance(
            manufacturerProductDesignation, aas.SubmodelElement
        ):
            manufacturerProductDesignation = self.ManufacturerProductDesignation(manufacturerProductDesignation)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerProductRoot is not None and not isinstance(manufacturerProductRoot, aas.SubmodelElement):
            manufacturerProductRoot = self.ManufacturerProductRoot(manufacturerProductRoot)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerProductFamily is not None and not isinstance(manufacturerProductFamily, aas.SubmodelElement):
            manufacturerProductFamily = self.ManufacturerProductFamily(manufacturerProductFamily)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerProductType is not None and not isinstance(manufacturerProductType, aas.SubmodelElement):
            manufacturerProductType = self.ManufacturerProductType(manufacturerProductType)

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

        # Build a submodel element if a raw value was passed in the argument

        if serialNumber is not None and not isinstance(serialNumber, aas.SubmodelElement):
            serialNumber = self.SerialNumber(serialNumber)

        # Build a submodel element if a raw value was passed in the argument

        if yearOfConstruction is not None and not isinstance(yearOfConstruction, aas.SubmodelElement):
            yearOfConstruction = self.YearOfConstruction(yearOfConstruction)

        # Build a submodel element if a raw value was passed in the argument

        if dateOfManufacture is not None and not isinstance(dateOfManufacture, aas.SubmodelElement):
            dateOfManufacture = self.DateOfManufacture(dateOfManufacture)

        # Build a submodel element if a raw value was passed in the argument

        if hardwareVersion is not None and not isinstance(hardwareVersion, aas.SubmodelElement):
            hardwareVersion = self.HardwareVersion(hardwareVersion)

        # Build a submodel element if a raw value was passed in the argument

        if firmwareVersion is not None and not isinstance(firmwareVersion, aas.SubmodelElement):
            firmwareVersion = self.FirmwareVersion(firmwareVersion)

        # Build a submodel element if a raw value was passed in the argument

        if softwareVersion is not None and not isinstance(softwareVersion, aas.SubmodelElement):
            softwareVersion = self.SoftwareVersion(softwareVersion)

        # Build a submodel element if a raw value was passed in the argument

        if countryOfOrigin is not None and not isinstance(countryOfOrigin, aas.SubmodelElement):
            countryOfOrigin = self.CountryOfOrigin(countryOfOrigin)

        # Build a submodel element if a raw value was passed in the argument

        if uniqueFacilityIdentifier is not None and not isinstance(uniqueFacilityIdentifier, aas.SubmodelElement):
            uniqueFacilityIdentifier = self.UniqueFacilityIdentifier(uniqueFacilityIdentifier)

        # A str would be split into its characters
        if isinstance(markings, str):
            raise TypeError("markings takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if markings is not None and not isinstance(markings, aas.SubmodelElement):
            markings = self.Markings(markings)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            manufacturerName,
            manufacturerProductDesignation,
            addressInformation,
            manufacturerProductRoot,
            manufacturerProductFamily,
            manufacturerProductType,
            orderCodeOfManufacturer,
            productArticleNumberOfManufacturer,
            serialNumber,
            yearOfConstruction,
            dateOfManufacture,
            hardwareVersion,
            firmwareVersion,
            softwareVersion,
            countryOfOrigin,
            uniqueFacilityIdentifier,
            companyLogo,
            markings,
            assetSpecificProperties,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
