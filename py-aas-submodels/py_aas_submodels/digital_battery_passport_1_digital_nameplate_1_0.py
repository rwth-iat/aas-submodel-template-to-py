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


class BatteryNameplate(aas.Submodel):

    class URIOfTheProduct(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"URIOfTheProduct",
                "value_type": xsd.AnyURI,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"URI of the product"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "The battery passport identifier is the unique identifier of a battery passport. \n\nDIN DKE Spec 99100 chapter reference: 6.1.2.1"
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABN590#002"),
                "supplemental_semantic_id": (
                    global_ref(r"0173-1#02-ABH173#003"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#uriOfTheProduct"),
                ),
            }

        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerName(aas.MultiLanguageProperty):

        @staticmethod
        def template_defaults() -> MultiLanguagePropertyMetadata:
            return {
                "id_short": r"ManufacturerName",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"manufacturer name"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information identifying the manufacturer with a name.\n\n\nDIN DKE Spec 99100 chapter reference: 6.1.2.4"
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABA565#009"),
                "supplemental_semantic_id": (
                    global_ref(r"0173-1#02-AAO677#004"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#manufacturerName"),
                ),
            }

        def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class AddressInformation(aas.SubmodelElementCollection):

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"AddressInformation",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"address information"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "The manufacturer information postal address, indicating a single contact point. Web address, if available; and web address, if available. \n\n\nDIN DKE Spec 99100 chapter reference: 6.1.2.3\n\n\nNote: This is drop-in of the ContactInformation Submodel"
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
                ),
                "supplemental_semantic_id": (
                    global_ref(r"https://admin-shell.io/smt-dropin/smt-dropin-use/1/0"),
                    global_ref(r"0112/2///61360_7#AAS002#001"),
                    global_ref(r"0173-1#02-AAQ837#008/0173-1#01-ADR448#008"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#addressInformation"),
                ),
            }

        def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements()

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SerialNumber(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"SerialNumber",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"serial number"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "The battery identifier should be serialised, i.e., identifying each battery via a serial number.\n\n\nDIN DKE Spec 99100 chapter reference: 6.1.2.2"
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABA951#009"),
                "supplemental_semantic_id": (
                    global_ref(r"0173-1#02-AAM556#004"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#serialNumber"),
                ),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DateOfManufacture(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"DateOfManufacture",
                "value_type": xsd.Date,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"date of manufacture"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "The manufacturing date should not only relate to the battery model, but to the battery item.\nThe date code should comply with DINISO8601-1:2020-12 and ISO8601-2:2019.\n\n\nDIN DKE Spec 99100 chapter reference: 6.1.3.2"
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61987#ABB757#007"),
                "supplemental_semantic_id": (
                    global_ref(r"0173-1#02-AAR972#004"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#dateOfManufacture"),
                ),
            }

        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class DateOfPuttingIntoService(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"DateOfPuttingIntoService",
                "value_type": xsd.Date,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"date of putting into service"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#dateOfPuttingIntoService"
                ),
            }

        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class UniqueFacilityIdentifier(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"UniqueFacilityIdentifier",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"unique facility identifier"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "The manufacturing place should be uniquely identifiable.\n\n\nDIN DKE Spec 99100 chapter reference: 6.1.3.1"
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier"),
                "supplemental_semantic_id": (
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#uniqueFacilityIdentifier"),
                    global_ref(r"0173-1#02-AAV646#003"),
                ),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class LifeCycleStage(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"LifeCycleStage",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"life cycle stage"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "A battery passport must include information on the life cycle status of the battery.\n\nThe status of the battery must be defined as 'original' (0173-1#07-ACC020#001), 'repurposed'(0173-1#07-ACC021#001), 're-used'(0173-1#07-ACC022#001), 'remanufactured' (0173-1#07-ACC023#001) or 'waste' (0173-1#07-ACC024#001).\n\nA new battery passport must be issued when a battery was subject to remanufacturing, repurpose or one of the treatment operations preparing for re-use and preparing for repurpose and is placed on the market again.\n\n\nDIN DKE Spec 99100 chapter reference: 6.1.3.7"
                    }
                ),
                "semantic_id": global_ref(r"0173-1#02-ABL841#001"),
                "supplemental_semantic_id": (
                    global_ref(r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#batteryStatus"),
                ),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class OperatorIdentifier(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"OperatorIdentifier",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"operator identifier"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#operatorIdentifier"
                ),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class ManufacturerIdentifier(aas.Property):

        @staticmethod
        def template_defaults() -> PropertyMetadata:
            return {
                "id_short": r"ManufacturerIdentifier",
                "value_type": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"manufacturer identifier"}),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#manufacturerIdentifier"
                ),
            }

        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

            super().__init__(value=value, **(self.template_defaults() | kwargs))

    class Markings(GeneratedSubmodelElementList):

        class Markings_item(aas.SubmodelElementCollection):

            class MarkingName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MarkingName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"marking name"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": 'Context name of the symbols, labels and documentation of conformity based on DIN DKE SPEC 99100:\n\n* "Separate collection symbol" (6.2.2)\n\n* "Symbols for cadmium and lead" (6.2.3)\n\n* "Carbon footprint label" (6.2.4)\n\n* "Extinguishing agent" (6.2.5)\n'
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABA231#009"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABI190#003"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#markingName"),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DesignationOfCertificateOrApproval(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignationOfCertificateOrApproval",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"designation of certificate or approval"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: Approval identifier, reference to the certificate number, to be entered without spaces "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABH783#003"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABI975#002"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#designationOfCertificateOrApproval"),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IssueDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IssueDate",
                        "value_type": xsd.Date,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"issue date"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABO097#001"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABL774#001"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#issueDate"),
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExpiryDate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpiryDate",
                        "value_type": xsd.Date,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"expiry date"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABH830#002"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABL775#001"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#expiryDate"),
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MarkingFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"MarkingFile",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"marking file"}),
                        "semantic_id": global_ref(r"0112/2///61987#ABO100#002"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABI191#003"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#markingFile"),
                        ),
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
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"marking additional text"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Text should be used to provide the meaning of labels and symbols.\n\nDIN DKE Spec 99100 chapter reference: 6.2.5, 6.2.6 "
                            }
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABB146#007"),
                        "supplemental_semantic_id": (
                            global_ref(r"0173-1#02-ABI192#003"),
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#markingAdditionalText"),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"markings 00"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Used to provide all relevant marking information of the battery passport based on DIN SPEC 99100."
                        }
                    ),
                    "semantic_id": global_ref(r"0112/2///61360_7#AAS009#001"),
                    "supplemental_semantic_id": (
                        global_ref(r"0173-1#02-ABI564#003/0173-1#01-AHF850#003"),
                        global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#Marking"),
                    ),
                }

            def __init__(
                self,
                markingName: Union[str, MarkingName],
                designationOfCertificateOrApproval: Optional[Union[str, DesignationOfCertificateOrApproval]] = None,
                issueDate: Optional[Union[xsd.Date, IssueDate]] = None,
                expiryDate: Optional[Union[xsd.Date, ExpiryDate]] = None,
                markingFile: Optional[MarkingFile] = None,
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
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"markings"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Should be used to provide all relevant marking information of the battery passport based on DIN DKE SPEC 99100 such as:\n\n* Separate collection symbol (6.2.2)\n\n* Symbols for cadmium and lead (6.2.3)\n\n* Carbon footprint label (6.2.4)\n\n* Extinguishing agent (6.2.5)\n\n* Meaning of labels and symbols (6.2.6)\n\nNote: CE marking is declared as mandatory according to EU Blue Guide\n\n\n\n"
                    }
                ),
                "semantic_id": global_ref(r"0112/2///61360_7#AAS006"),
                "supplemental_semantic_id": (
                    global_ref(r"0173-1#02-ABI563#003/0173-1#01-AHF849#003"),
                    global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#markings"),
                ),
            }

        def __init__(self, markings_items: Iterable[Markings_item], **kwargs: Unpack[SubmodelElementListMetadata]):

            # A str would be split into its characters
            if isinstance(markings_items, str):
                raise TypeError("markings_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(markings_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class EUDeclarationOfConformity(GeneratedSubmodelElementList):

        class Eudeclarationofconformity_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"document identifier"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Document identifier of the document (e.g., PDF) that can be found in the HandoverDocumentation Submodel.\n\nDIN DKE Spec 99100 chapter reference: 6.2.7"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"EUDeclarationOfConformity",
                "type_value_list_element": aas.Property,
                "value_type_list_element": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"EU declaration of conformity"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": "EU declaration of conformity\n\nDIN DKE Spec 99100 chapter reference: 6.2.7"}
                ),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#euDeclarationOfConformity"
                ),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABA889#003"),),
            }

        def __init__(
            self,
            eudeclarationofconformity_items: Iterable[Union[str, Eudeclarationofconformity_item]],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(eudeclarationofconformity_items, str):
                raise TypeError("eudeclarationofconformity_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if eudeclarationofconformity_items:
                eudeclarationofconformity_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Eudeclarationofconformity_item(i)
                    for i in eudeclarationofconformity_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                eudeclarationofconformity_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ResultsOfTestReportsProvingCompliance(GeneratedSubmodelElementList):

        class Resultsoftestreportsprovingcompliance_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"document identifier"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Document identifier of the document (e.g., PDF) that can be found in the HandoverDocumentation Submodel.\n\nDIN DKE Spec 99100 chapter reference: 6.2.8 "
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"ResultsOfTestReportsProvingCompliance",
                "type_value_list_element": aas.Property,
                "value_type_list_element": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"results of test reports proving compliance"}),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Results of test reports proving compliance\nDIN DKE Spec 99100 chapter reference: 6.2.8"
                    }
                ),
                "semantic_id": global_ref(
                    r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#resultsOfTestReportsProvingCompliance"
                ),
                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABA705#003"),),
            }

        def __init__(
            self,
            resultsoftestreportsprovingcompliance_items: Iterable[
                Union[str, Resultsoftestreportsprovingcompliance_item]
            ],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(resultsoftestreportsprovingcompliance_items, str):
                raise TypeError("resultsoftestreportsprovingcompliance_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if resultsoftestreportsprovingcompliance_items:
                resultsoftestreportsprovingcompliance_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Resultsoftestreportsprovingcompliance_item(i)
                    for i in resultsoftestreportsprovingcompliance_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                resultsoftestreportsprovingcompliance_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"BatteryNameplate",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"battery nameplate"}),
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Contains the static nameplate attributes attached to the battery."}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02035-1",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/digitalbatterypassport/nameplate/1/0/Nameplate"),
            "supplemental_semantic_id": (
                global_ref(r"urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0"),
                global_ref(r"urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0"),
                global_ref(r"https://admin-shell.io/idta/nameplate/3/0/Nameplate"),
            ),
        }

    def __init__(
        self,
        id_: str,
        uRIOfTheProduct: Union[xsd.AnyURI, URIOfTheProduct],
        manufacturerName: Union[aas.MultiLanguageTextType, ManufacturerName],
        addressInformation: AddressInformation,
        serialNumber: Union[str, SerialNumber],
        dateOfManufacture: Union[xsd.Date, DateOfManufacture],
        uniqueFacilityIdentifier: Union[str, UniqueFacilityIdentifier],
        lifeCycleStage: Union[str, LifeCycleStage],
        manufacturerIdentifier: Union[str, ManufacturerIdentifier],
        markings: Union[Iterable[Markings.Markings_item], Markings],
        eUDeclarationOfConformity: Union[
            Iterable[Union[str, EUDeclarationOfConformity.Eudeclarationofconformity_item]], EUDeclarationOfConformity
        ],
        resultsOfTestReportsProvingCompliance: Union[
            Iterable[Union[str, ResultsOfTestReportsProvingCompliance.Resultsoftestreportsprovingcompliance_item]],
            ResultsOfTestReportsProvingCompliance,
        ],
        dateOfPuttingIntoService: Optional[Union[xsd.Date, DateOfPuttingIntoService]] = None,
        operatorIdentifier: Optional[Union[str, OperatorIdentifier]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Build a submodel element if a raw value was passed in the argument

        if uRIOfTheProduct is not None and not isinstance(uRIOfTheProduct, aas.SubmodelElement):
            uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
            manufacturerName = self.ManufacturerName(manufacturerName)

        # Build a submodel element if a raw value was passed in the argument

        if serialNumber is not None and not isinstance(serialNumber, aas.SubmodelElement):
            serialNumber = self.SerialNumber(serialNumber)

        # Build a submodel element if a raw value was passed in the argument

        if dateOfManufacture is not None and not isinstance(dateOfManufacture, aas.SubmodelElement):
            dateOfManufacture = self.DateOfManufacture(dateOfManufacture)

        # Build a submodel element if a raw value was passed in the argument

        if dateOfPuttingIntoService is not None and not isinstance(dateOfPuttingIntoService, aas.SubmodelElement):
            dateOfPuttingIntoService = self.DateOfPuttingIntoService(dateOfPuttingIntoService)

        # Build a submodel element if a raw value was passed in the argument

        if uniqueFacilityIdentifier is not None and not isinstance(uniqueFacilityIdentifier, aas.SubmodelElement):
            uniqueFacilityIdentifier = self.UniqueFacilityIdentifier(uniqueFacilityIdentifier)

        # Build a submodel element if a raw value was passed in the argument

        if lifeCycleStage is not None and not isinstance(lifeCycleStage, aas.SubmodelElement):
            lifeCycleStage = self.LifeCycleStage(lifeCycleStage)

        # Build a submodel element if a raw value was passed in the argument

        if operatorIdentifier is not None and not isinstance(operatorIdentifier, aas.SubmodelElement):
            operatorIdentifier = self.OperatorIdentifier(operatorIdentifier)

        # Build a submodel element if a raw value was passed in the argument

        if manufacturerIdentifier is not None and not isinstance(manufacturerIdentifier, aas.SubmodelElement):
            manufacturerIdentifier = self.ManufacturerIdentifier(manufacturerIdentifier)

        # A str would be split into its characters
        if isinstance(markings, str):
            raise TypeError("markings takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if markings is not None and not isinstance(markings, aas.SubmodelElement):
            markings = self.Markings(markings)

        # A str would be split into its characters
        if isinstance(eUDeclarationOfConformity, str):
            raise TypeError("eUDeclarationOfConformity takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if eUDeclarationOfConformity is not None and not isinstance(eUDeclarationOfConformity, aas.SubmodelElement):
            eUDeclarationOfConformity = self.EUDeclarationOfConformity(eUDeclarationOfConformity)

        # A str would be split into its characters
        if isinstance(resultsOfTestReportsProvingCompliance, str):
            raise TypeError("resultsOfTestReportsProvingCompliance takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if resultsOfTestReportsProvingCompliance is not None and not isinstance(
            resultsOfTestReportsProvingCompliance, aas.SubmodelElement
        ):
            resultsOfTestReportsProvingCompliance = self.ResultsOfTestReportsProvingCompliance(
                resultsOfTestReportsProvingCompliance
            )

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            manufacturerName,
            addressInformation,
            serialNumber,
            dateOfManufacture,
            dateOfPuttingIntoService,
            uniqueFacilityIdentifier,
            lifeCycleStage,
            operatorIdentifier,
            manufacturerIdentifier,
            markings,
            eUDeclarationOfConformity,
            resultsOfTestReportsProvingCompliance,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
