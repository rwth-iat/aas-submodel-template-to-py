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


class TechnicalData(aas.Submodel):

    class GeneralInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerName",
                    "value_type": str,
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market.\n\nDIN DKE Spec 99100 chapter reference: 6.1.2.4 c) "
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO677#004"),
                    "supplemental_semantic_id": (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-AAO677-004"),
                        global_ref(r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#manufacturerName"),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CompanyLogo(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"CompanyLogo",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Imagefile for logo of manufacturer provided in common format (.png, .jpg)."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABI776#002"),
                    "supplemental_semantic_id": (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABI776-002"),
                        global_ref(r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#companyLogo"),
                    ),
                }

            def __init__(self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class ManufacturerIdentifier(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerIdentifier",
                    "value_type": str,
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#manufacturerIdentifier"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BatteryCategory(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"BatteryCategory",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": 'A battery passport must include the battery category.\n\nThe battery category must be provided on the battery label.\n\nThe battery must be categorised by its intended use in (string values):\n- "lmt"\n- "ev" \n- "industrial", or\n- "stationary"\n\nDIN DKE Spec 99100 chapter reference: 6.1.3.5\n\n'
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryCategory"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-AAR724#007"),),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BatteryMass(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"BatteryMass",
                    "value_type": xsd.Float,
                    "category": r"PARAMETER",
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryMass",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-AAF040#010"),),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductImages(GeneratedSubmodelElementList):

            class Productimages_item(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Image file for associated product provided in common format (.png, .jpg)."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.shared:3.1.0#ResourceWithContentType"),
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"ProductImages",
                    "type_value_list_element": aas.File,
                    "semantic_id_list_element": global_ref(r"0173-1#02-ABM220#001/0173-1#01-AHY911#001"),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List for image file(s) for associated product provided in common format (.png, .jpg)."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-ABM220#001"),
                    "supplemental_semantic_id": (
                        global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABM220-001"),
                        global_ref(r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#productImages"),
                    ),
                }

            def __init__(
                self, productimages_items: Iterable[Productimages_item], **kwargs: Unpack[SubmodelElementListMetadata]
            ):

                # A str would be split into its characters
                if isinstance(productimages_items, str):
                    raise TypeError("productimages_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(productimages_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class WarrantyInformation(aas.SubmodelElementCollection):

            class WarrantyPeriod(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WarrantyPeriod",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"warranty period"}),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyPeriod"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-AAX540#004"),),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"WarrantyInformation",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"warranty information"}),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyInformation"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO677#004"),),
                }

            def __init__(
                self, warrantyPeriod: Union[str, WarrantyPeriod], **kwargs: Unpack[SubmodelElementCollectionMetadata]
            ):

                # Build a submodel element if a raw value was passed in the argument

                if warrantyPeriod is not None and not isinstance(warrantyPeriod, aas.SubmodelElement):
                    warrantyPeriod = self.WarrantyPeriod(warrantyPeriod)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(warrantyPeriod)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"GeneralInformation",
                "semantic_id": global_ref(r"0173-1#02-ABK161#002/0173-1#01-AHX838#002"),
                "supplemental_semantic_id": (
                    global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#generalInformation"),
                ),
            }

        def __init__(
            self,
            manufacturerName: Union[str, ManufacturerName],
            manufacturerIdentifier: Union[str, ManufacturerIdentifier],
            batteryCategory: Union[str, BatteryCategory],
            batteryMass: Union[xsd.Float, BatteryMass],
            warrantyInformation: WarrantyInformation,
            companyLogo: Optional[CompanyLogo] = None,
            productImages: Optional[Union[Iterable[ProductImages.Productimages_item], ProductImages]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerIdentifier is not None and not isinstance(manufacturerIdentifier, aas.SubmodelElement):
                manufacturerIdentifier = self.ManufacturerIdentifier(manufacturerIdentifier)

            # Build a submodel element if a raw value was passed in the argument

            if batteryCategory is not None and not isinstance(batteryCategory, aas.SubmodelElement):
                batteryCategory = self.BatteryCategory(batteryCategory)

            # Build a submodel element if a raw value was passed in the argument

            if batteryMass is not None and not isinstance(batteryMass, aas.SubmodelElement):
                batteryMass = self.BatteryMass(batteryMass)

            # A str would be split into its characters
            if isinstance(productImages, str):
                raise TypeError("productImages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if productImages is not None and not isinstance(productImages, aas.SubmodelElement):
                productImages = self.ProductImages(productImages)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                manufacturerName,
                companyLogo,
                manufacturerIdentifier,
                batteryCategory,
                batteryMass,
                productImages,
                warrantyInformation,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TechnicalPropertyAreas(aas.SubmodelElementCollection):

        class CapacityEnergyVoltage(aas.SubmodelElementCollection):

            class NominalVoltage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NominalVoltage",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "voltage - NOM\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.11"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL588#001"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#nominalVoltage"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MinVoltage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinVoltage",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "voltage - MIN\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.9"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL587#001"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#minimumVoltage"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaxVoltage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaxVoltage",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "voltage - MAX\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.10"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL589#001"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumVoltage"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RatedCapacity(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RatedCapacity",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "rated capacity\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.2"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL869#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedCapacity"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CapacityFade(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CapacityFade",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "capacity fade\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.4"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL828#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityFade"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CertifiedUsableBatteryEnergy(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CertifiedUsableBatteryEnergy",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Certified usable battery energy (UBE certified)\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.5"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL829#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedEnergy"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CapacityEnergyVoltage",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Information on battery capacity, energy and voltage.\n\nDIN DKE Spec 99100 chapter reference: 6.7.2"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityEnergyVoltage"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                nominalVoltage: Union[xsd.Float, NominalVoltage],
                minVoltage: Union[xsd.Float, MinVoltage],
                maxVoltage: Union[xsd.Float, MaxVoltage],
                ratedCapacity: Union[xsd.Float, RatedCapacity],
                capacityFade: Optional[Union[xsd.Float, CapacityFade]] = None,
                certifiedUsableBatteryEnergy: Optional[Union[xsd.Float, CertifiedUsableBatteryEnergy]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if nominalVoltage is not None and not isinstance(nominalVoltage, aas.SubmodelElement):
                    nominalVoltage = self.NominalVoltage(nominalVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if minVoltage is not None and not isinstance(minVoltage, aas.SubmodelElement):
                    minVoltage = self.MinVoltage(minVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if maxVoltage is not None and not isinstance(maxVoltage, aas.SubmodelElement):
                    maxVoltage = self.MaxVoltage(maxVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if ratedCapacity is not None and not isinstance(ratedCapacity, aas.SubmodelElement):
                    ratedCapacity = self.RatedCapacity(ratedCapacity)

                # Build a submodel element if a raw value was passed in the argument

                if capacityFade is not None and not isinstance(capacityFade, aas.SubmodelElement):
                    capacityFade = self.CapacityFade(capacityFade)

                # Build a submodel element if a raw value was passed in the argument

                if certifiedUsableBatteryEnergy is not None and not isinstance(
                    certifiedUsableBatteryEnergy, aas.SubmodelElement
                ):
                    certifiedUsableBatteryEnergy = self.CertifiedUsableBatteryEnergy(certifiedUsableBatteryEnergy)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    nominalVoltage, minVoltage, maxVoltage, ratedCapacity, capacityFade, certifiedUsableBatteryEnergy
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RoundTripEnergyEfficiency(aas.SubmodelElementCollection):

            class InitialRoundTripEnergyEfficiency(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InitialRoundTripEnergyEfficiency",
                        "value_type": int,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "initial round trip energy efficiency\n\nDIN DKE Spec 99100 chapter reference: 6.7.4.2"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL833#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialRoundTripEnergyEfficiency"
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RoundTripEnergyEfficiencyAt50PercentOfCycleLife(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RoundTripEnergyEfficiencyAt50PercentOfCycleLife",
                        "value_type": int,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "round trip energy efficiency at 50% of cycle life\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.3"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL866#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEfficiencyAt50PercentCycleLife"
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EnergyRoundTripEfficiencyFade(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EnergyRoundTripEfficiencyFade",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "round trip energy efficiency fade\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.5"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL827#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#energyRoundTripEfficiencyFade"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InitialSelfDischargingRate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InitialSelfDischargingRate",
                        "value_type": int,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "initial self-discharging rate\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.6"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL834#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialSelfDischargingRate"
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"RoundTripEnergyEfficiency",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Information regarding round trip energy efficiency.\n\nDIN DKE Spec 99100 chapter reference: 6.7.4"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEnergyEfficiency"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                initialRoundTripEnergyEfficiency: Union[int, InitialRoundTripEnergyEfficiency],
                roundTripEnergyEfficiencyAt50PercentOfCycleLife: Union[
                    int, RoundTripEnergyEfficiencyAt50PercentOfCycleLife
                ],
                energyRoundTripEfficiencyFade: Optional[Union[xsd.Float, EnergyRoundTripEfficiencyFade]] = None,
                initialSelfDischargingRate: Optional[Union[int, InitialSelfDischargingRate]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if initialRoundTripEnergyEfficiency is not None and not isinstance(
                    initialRoundTripEnergyEfficiency, aas.SubmodelElement
                ):
                    initialRoundTripEnergyEfficiency = self.InitialRoundTripEnergyEfficiency(
                        initialRoundTripEnergyEfficiency
                    )

                # Build a submodel element if a raw value was passed in the argument

                if roundTripEnergyEfficiencyAt50PercentOfCycleLife is not None and not isinstance(
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife, aas.SubmodelElement
                ):
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife = (
                        self.RoundTripEnergyEfficiencyAt50PercentOfCycleLife(
                            roundTripEnergyEfficiencyAt50PercentOfCycleLife
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if energyRoundTripEfficiencyFade is not None and not isinstance(
                    energyRoundTripEfficiencyFade, aas.SubmodelElement
                ):
                    energyRoundTripEfficiencyFade = self.EnergyRoundTripEfficiencyFade(energyRoundTripEfficiencyFade)

                # Build a submodel element if a raw value was passed in the argument

                if initialSelfDischargingRate is not None and not isinstance(
                    initialSelfDischargingRate, aas.SubmodelElement
                ):
                    initialSelfDischargingRate = self.InitialSelfDischargingRate(initialSelfDischargingRate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    initialRoundTripEnergyEfficiency,
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife,
                    energyRoundTripEfficiencyFade,
                    initialSelfDischargingRate,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Resistance(aas.SubmodelElementCollection):

            class InitialInternalResistanceOnBatteryCellLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InitialInternalResistanceOnBatteryCellLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Internal battery cell and pack resistance - Internal resistance (in Ohm)\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL844#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryCell"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InitialInternalResistanceOnBatteryPackLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InitialInternalResistanceOnBatteryPackLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Initial (Pre-Use) internal resistance on battery pack level. \n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL846#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryPack"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InitialInternalResistanceOnBatteryModuleLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InitialInternalResistanceOnBatteryModuleLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Initial internal resistance on battery module level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL832#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InternalResistanceIncreaseOfBatteryCellLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InternalResistanceIncreaseOfBatteryCellLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "initial internal resistance on battery cell level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.3"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryCell",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL831#002"),),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InternalResistanceIncreaseOfBatteryPackLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InternalResistanceIncreaseOfBatteryPackLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "initial internal resistance on battery pack level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.3"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryPack"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL831#001"),),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InternalResistanceIncreaseOfBatteryModuleLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InternalResistanceIncreaseOfBatteryModuleLevel",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL836#001"),),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Resistance",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Data elements regarding internal resistance and electrochemical impedance.\n\nDIN DKE Spec 99100 chapter reference: 6.7.5\n\n"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#resistance"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                initialInternalResistanceOnBatteryCellLevel: Union[
                    xsd.Float, InitialInternalResistanceOnBatteryCellLevel
                ],
                initialInternalResistanceOnBatteryPackLevel: Union[
                    xsd.Float, InitialInternalResistanceOnBatteryPackLevel
                ],
                internalResistanceIncreaseOfBatteryPackLevel: Union[
                    xsd.Float, InternalResistanceIncreaseOfBatteryPackLevel
                ],
                initialInternalResistanceOnBatteryModuleLevel: Optional[
                    Union[xsd.Float, InitialInternalResistanceOnBatteryModuleLevel]
                ] = None,
                internalResistanceIncreaseOfBatteryCellLevel: Optional[
                    Union[xsd.Float, InternalResistanceIncreaseOfBatteryCellLevel]
                ] = None,
                internalResistanceIncreaseOfBatteryModuleLevel: Optional[
                    Union[xsd.Float, InternalResistanceIncreaseOfBatteryModuleLevel]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if initialInternalResistanceOnBatteryCellLevel is not None and not isinstance(
                    initialInternalResistanceOnBatteryCellLevel, aas.SubmodelElement
                ):
                    initialInternalResistanceOnBatteryCellLevel = self.InitialInternalResistanceOnBatteryCellLevel(
                        initialInternalResistanceOnBatteryCellLevel
                    )

                # Build a submodel element if a raw value was passed in the argument

                if initialInternalResistanceOnBatteryPackLevel is not None and not isinstance(
                    initialInternalResistanceOnBatteryPackLevel, aas.SubmodelElement
                ):
                    initialInternalResistanceOnBatteryPackLevel = self.InitialInternalResistanceOnBatteryPackLevel(
                        initialInternalResistanceOnBatteryPackLevel
                    )

                # Build a submodel element if a raw value was passed in the argument

                if initialInternalResistanceOnBatteryModuleLevel is not None and not isinstance(
                    initialInternalResistanceOnBatteryModuleLevel, aas.SubmodelElement
                ):
                    initialInternalResistanceOnBatteryModuleLevel = self.InitialInternalResistanceOnBatteryModuleLevel(
                        initialInternalResistanceOnBatteryModuleLevel
                    )

                # Build a submodel element if a raw value was passed in the argument

                if internalResistanceIncreaseOfBatteryCellLevel is not None and not isinstance(
                    internalResistanceIncreaseOfBatteryCellLevel, aas.SubmodelElement
                ):
                    internalResistanceIncreaseOfBatteryCellLevel = self.InternalResistanceIncreaseOfBatteryCellLevel(
                        internalResistanceIncreaseOfBatteryCellLevel
                    )

                # Build a submodel element if a raw value was passed in the argument

                if internalResistanceIncreaseOfBatteryPackLevel is not None and not isinstance(
                    internalResistanceIncreaseOfBatteryPackLevel, aas.SubmodelElement
                ):
                    internalResistanceIncreaseOfBatteryPackLevel = self.InternalResistanceIncreaseOfBatteryPackLevel(
                        internalResistanceIncreaseOfBatteryPackLevel
                    )

                # Build a submodel element if a raw value was passed in the argument

                if internalResistanceIncreaseOfBatteryModuleLevel is not None and not isinstance(
                    internalResistanceIncreaseOfBatteryModuleLevel, aas.SubmodelElement
                ):
                    internalResistanceIncreaseOfBatteryModuleLevel = (
                        self.InternalResistanceIncreaseOfBatteryModuleLevel(
                            internalResistanceIncreaseOfBatteryModuleLevel
                        )
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    initialInternalResistanceOnBatteryCellLevel,
                    initialInternalResistanceOnBatteryPackLevel,
                    initialInternalResistanceOnBatteryModuleLevel,
                    internalResistanceIncreaseOfBatteryCellLevel,
                    internalResistanceIncreaseOfBatteryPackLevel,
                    internalResistanceIncreaseOfBatteryModuleLevel,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class PowerCapability(aas.SubmodelElementCollection):

            class MaximumPermittedBatteryPower(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumPermittedBatteryPower",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "maximum permitted battery power\n\nDIN DKE Spec 99100 chapter reference:  6.7.3.5"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL843#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumPermittedBatteryPower"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PowerFade(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PowerFade",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "Power fade\n\nDIN DKE Spec 99100 chapter reference: 6.7.3.4"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL852#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerFade"),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RatioNominalBatteryPowerAndBatteryEnergy(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RatioNominalBatteryPowerAndBatteryEnergy",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityRatio"
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OriginalPowerCapability(GeneratedSubmodelElementList):

                class Originalpowercapability_item(aas.SubmodelElementCollection):

                    class AtSoc(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"atSoc",
                                "value_type": xsd.UnsignedInt,
                                "semantic_id": global_ref(
                                    r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#atSoC"
                                ),
                                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL821#001"),),
                            }

                        def __init__(self, value: xsd.UnsignedInt, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class PowerCapabilityAt(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"powerCapabilityAt",
                                "value_type": xsd.Float,
                                "semantic_id": global_ref(
                                    r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityAt"
                                ),
                                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL853#001"),),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": "Power capability measured at a reference condition, for example at 80% or 20% state of charge (SoC).\n\nDIN DKE Spec 99100 chapter reference: 6.7.3.2"
                                }
                            ),
                            "semantic_id": global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt"
                            ),
                        }

                    def __init__(
                        self,
                        atSoc: Union[xsd.UnsignedInt, AtSoc],
                        powerCapabilityAt: Union[xsd.Float, PowerCapabilityAt],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if atSoc is not None and not isinstance(atSoc, aas.SubmodelElement):
                            atSoc = self.AtSoc(atSoc)

                        # Build a submodel element if a raw value was passed in the argument

                        if powerCapabilityAt is not None and not isinstance(powerCapabilityAt, aas.SubmodelElement):
                            powerCapabilityAt = self.PowerCapabilityAt(powerCapabilityAt)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(atSoc, powerCapabilityAt)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"OriginalPowerCapability",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt"
                        ),
                        "semantic_id": global_ref(r"0173-1#02-ABL853#002"),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#originalPowerCapability"
                            ),
                        ),
                    }

                def __init__(
                    self,
                    originalpowercapability_items: Iterable[Originalpowercapability_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(originalpowercapability_items, str):
                        raise TypeError("originalpowercapability_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        originalpowercapability_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"PowerCapability",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Information regarding power capability.\n\nDIN DKE Spec 99100 chapter reference: 6.7.3"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapability"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                maximumPermittedBatteryPower: Union[xsd.Float, MaximumPermittedBatteryPower],
                powerFade: Union[xsd.Float, PowerFade],
                originalPowerCapability: Union[
                    Iterable[OriginalPowerCapability.Originalpowercapability_item], OriginalPowerCapability
                ],
                ratioNominalBatteryPowerAndBatteryEnergy: Optional[
                    Union[xsd.Float, RatioNominalBatteryPowerAndBatteryEnergy]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if maximumPermittedBatteryPower is not None and not isinstance(
                    maximumPermittedBatteryPower, aas.SubmodelElement
                ):
                    maximumPermittedBatteryPower = self.MaximumPermittedBatteryPower(maximumPermittedBatteryPower)

                # Build a submodel element if a raw value was passed in the argument

                if powerFade is not None and not isinstance(powerFade, aas.SubmodelElement):
                    powerFade = self.PowerFade(powerFade)

                # Build a submodel element if a raw value was passed in the argument

                if ratioNominalBatteryPowerAndBatteryEnergy is not None and not isinstance(
                    ratioNominalBatteryPowerAndBatteryEnergy, aas.SubmodelElement
                ):
                    ratioNominalBatteryPowerAndBatteryEnergy = self.RatioNominalBatteryPowerAndBatteryEnergy(
                        ratioNominalBatteryPowerAndBatteryEnergy
                    )

                # A str would be split into its characters
                if isinstance(originalPowerCapability, str):
                    raise TypeError("originalPowerCapability takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if originalPowerCapability is not None and not isinstance(originalPowerCapability, aas.SubmodelElement):
                    originalPowerCapability = self.OriginalPowerCapability(originalPowerCapability)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    maximumPermittedBatteryPower,
                    powerFade,
                    ratioNominalBatteryPowerAndBatteryEnergy,
                    originalPowerCapability,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Temperature(aas.SubmodelElementCollection):

            class TemperatureRangeIdleState_LowerBoundary(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TemperatureRangeIdleState_LowerBoundary",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "temperature range idle state (lower boundary)\n\nDIN DKE Spec 99100 chapter reference:  6.7.7.3"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL842#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateLowerBoundary"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TemperatureRangeIdleState_UpperBoundary(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TemperatureRangeIdleState_UpperBoundary",
                        "value_type": xsd.Float,
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "temperature range idle state (upper boundary)\n\nDIN DKE Spec 99100 chapter reference: 6.7.7.4"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL871#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateUpperBoundary"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Temperature",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Information regarding temperature conditions.\n\nDIN DKE Spec 99100 chapter reference: 6.7.7"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperature"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                temperatureRangeIdleState_LowerBoundary: Union[xsd.Float, TemperatureRangeIdleState_LowerBoundary],
                temperatureRangeIdleState_UpperBoundary: Union[xsd.Float, TemperatureRangeIdleState_UpperBoundary],
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if temperatureRangeIdleState_LowerBoundary is not None and not isinstance(
                    temperatureRangeIdleState_LowerBoundary, aas.SubmodelElement
                ):
                    temperatureRangeIdleState_LowerBoundary = self.TemperatureRangeIdleState_LowerBoundary(
                        temperatureRangeIdleState_LowerBoundary
                    )

                # Build a submodel element if a raw value was passed in the argument

                if temperatureRangeIdleState_UpperBoundary is not None and not isinstance(
                    temperatureRangeIdleState_UpperBoundary, aas.SubmodelElement
                ):
                    temperatureRangeIdleState_UpperBoundary = self.TemperatureRangeIdleState_UpperBoundary(
                        temperatureRangeIdleState_UpperBoundary
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    temperatureRangeIdleState_LowerBoundary, temperatureRangeIdleState_UpperBoundary
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Lifetime(aas.SubmodelElementCollection):

            class ExpectedLifetimeInCalendarYears(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpectedLifetimeInCalendarYears",
                        "value_type": xsd.UnsignedInt,
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedLifetime"
                        ),
                    }

                def __init__(self, value: xsd.UnsignedInt, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExpectedNumberOfCycles(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpectedNumberOfCycles",
                        "value_type": xsd.UnsignedInt,
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedNumberOfCycles"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL830#001"),),
                    }

                def __init__(self, value: xsd.UnsignedInt, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CapacityThresholdExhaustion(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CapacityThresholdExhaustion",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"capacity threshold for exhaustion"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "interpreted as minimum percentage of rated capacity, above which the battery is still considered operational as EV battery in its current life. The value has to be provided by the economic operator. This metric may serve as indicator for a necessary end of current life as EV and may be understood in the context of warranty.\n\nDIN DKE Spec 99100 chapter reference:  6.7.6.9"
                            }
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(aas.Key(type_=aas.KeyTypes.CONCEPT_DESCRIPTION, value=r"0173-1#02-ABL838#002"),),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                        "supplemental_semantic_id": (
                            global_ref(
                                r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityThresholdForExhaustion"
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CRateOfRelevantCycleLifeTest(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CRateOfRelevantCycleLifeTest",
                        "value_type": xsd.Decimal,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "This data attribute is a measurement parameter for “Expected lifetime: Number of charge-discharge cycles”: Applied charge and discharge rate in terms of rated capacity (C-rate) of relevant cycle-life reference test.\n\nDIN DKE Spec 99100 chapter reference:  6.7.6.6"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#cRateLifeCycleTest"
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Lifetime",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Information regarding battery lifetime.\n\nDIN DKE Spec 99100 chapter reference: 6.7.6"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#lifetime"
                    ),
                    "supplemental_semantic_id": (global_ref(r"0173-1#02-ABL358#002/0173-1#01-AHX773#002"),),
                }

            def __init__(
                self,
                expectedLifetimeInCalendarYears: Union[xsd.UnsignedInt, ExpectedLifetimeInCalendarYears],
                expectedNumberOfCycles: Union[xsd.UnsignedInt, ExpectedNumberOfCycles],
                cRateOfRelevantCycleLifeTest: Union[xsd.Decimal, CRateOfRelevantCycleLifeTest],
                capacityThresholdExhaustion: Optional[Union[xsd.Float, CapacityThresholdExhaustion]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if expectedLifetimeInCalendarYears is not None and not isinstance(
                    expectedLifetimeInCalendarYears, aas.SubmodelElement
                ):
                    expectedLifetimeInCalendarYears = self.ExpectedLifetimeInCalendarYears(
                        expectedLifetimeInCalendarYears
                    )

                # Build a submodel element if a raw value was passed in the argument

                if expectedNumberOfCycles is not None and not isinstance(expectedNumberOfCycles, aas.SubmodelElement):
                    expectedNumberOfCycles = self.ExpectedNumberOfCycles(expectedNumberOfCycles)

                # Build a submodel element if a raw value was passed in the argument

                if capacityThresholdExhaustion is not None and not isinstance(
                    capacityThresholdExhaustion, aas.SubmodelElement
                ):
                    capacityThresholdExhaustion = self.CapacityThresholdExhaustion(capacityThresholdExhaustion)

                # Build a submodel element if a raw value was passed in the argument

                if cRateOfRelevantCycleLifeTest is not None and not isinstance(
                    cRateOfRelevantCycleLifeTest, aas.SubmodelElement
                ):
                    cRateOfRelevantCycleLifeTest = self.CRateOfRelevantCycleLifeTest(cRateOfRelevantCycleLifeTest)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    expectedLifetimeInCalendarYears,
                    expectedNumberOfCycles,
                    capacityThresholdExhaustion,
                    cRateOfRelevantCycleLifeTest,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"TechnicalPropertyAreas",
                "semantic_id": global_ref(r"0173-1#02-ABK163#002"),
                "supplemental_semantic_id": (
                    global_ref(r"https://api.eclass-cdp.com/0173-1-02-ABK163-002"),
                    global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#technicalPropertyAreas"),
                ),
            }

        def __init__(
            self,
            capacityEnergyVoltage: CapacityEnergyVoltage,
            roundTripEnergyEfficiency: RoundTripEnergyEfficiency,
            resistance: Resistance,
            powerCapability: PowerCapability,
            temperature: Temperature,
            lifetime: Lifetime,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                capacityEnergyVoltage, roundTripEnergyEfficiency, resistance, powerCapability, temperature, lifetime
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"TechnicalData",
            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"technical data"}),
            "description": aas.MultiLanguageTextType(dict_={r"en": r"Technical data of the battery."}),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"IDTA-02003-2-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/digitalbatterypassport/TechnicalData/1/0"),
            "supplemental_semantic_id": (
                global_ref(r"0173-1#01-AHX837#002"),
                global_ref(r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#TechnicalData"),
            ),
        }

    def __init__(
        self,
        id_: str,
        generalInformation: GeneralInformation,
        technicalPropertyAreas: TechnicalPropertyAreas,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(generalInformation, technicalPropertyAreas)

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
