import re

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


class PAMSpecificationSheet(aas.Submodel):

    class DocumentHeader(aas.SubmodelElementCollection):

        class PAMSpecificationSheetIdentification(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PAMSpecificationSheetIdentification",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"PAM Specification Sheet Identification",
                            r"de": r"PAM Spezifikationsbaltt Identification",
                        }
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Unique identifier for the PAM specification sheet."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV929#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AssetTypeClass(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AssetTypeClass",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Asset Type Class", r"de": r"Allgemeiner Asset-Typ"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Defines the general category of the asset described in the PAM specification sheet."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV939#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AssetTypeIdentification(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AssetTypeIdentification",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Asset Type Identification",
                            r"de": r"Identifizierung des allgemeinen Asset-Typs",
                        }
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": "Unique identifier for a general asset type's PAM specification sheet."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV940#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DocumentHeader",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Document Header", r"de": r"Dokumentenkopf"}),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Identifier for the asset type and associated PAM specification sheet."}
                ),
                "semantic_id": global_ref(r"0173-1#01-AGC974#002"),
            }

        def __init__(
            self,
            pAMSpecificationSheetIdentification: Union[str, PAMSpecificationSheetIdentification],
            assetTypeClass: Union[str, AssetTypeClass],
            assetTypeIdentification: Union[str, AssetTypeIdentification],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if pAMSpecificationSheetIdentification is not None and not isinstance(
                pAMSpecificationSheetIdentification, aas.SubmodelElement
            ):
                pAMSpecificationSheetIdentification = self.PAMSpecificationSheetIdentification(
                    pAMSpecificationSheetIdentification
                )

            # Build a submodel element if a raw value was passed in the argument

            if assetTypeClass is not None and not isinstance(assetTypeClass, aas.SubmodelElement):
                assetTypeClass = self.AssetTypeClass(assetTypeClass)

            # Build a submodel element if a raw value was passed in the argument

            if assetTypeIdentification is not None and not isinstance(assetTypeIdentification, aas.SubmodelElement):
                assetTypeIdentification = self.AssetTypeIdentification(assetTypeIdentification)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                pAMSpecificationSheetIdentification, assetTypeClass, assetTypeIdentification
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class GeneralInformation(aas.SubmodelElementCollection):

        class FunctionalLocation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FunctionalLocation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"FunctionalLocation", r"de": r"Technischer Platz"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Specifies the asset's logical position within a piping and instrumentation diagram."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV946#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TechnicalLocation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TechnicalLocation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Technical Location", r"de": r"Technischer Ort"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Specifies the actual location of the asset within the plant."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV947#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Description(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Description",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Description", r"de": r"Beschreibung"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": "Offers a concise explanation of the asset's primary function."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV948#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AssetSubtype(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AssetSubtype",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Asset Subtype", r"de": r"Asset-Typ"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Defines the specific subtype of the asset."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV949#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SpecificationSheetReference(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SpecificationSheetReference",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"Specification Sheet Reference",
                            r"de": r"Link zum technischen Spezifikationsblatt",
                        }
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Reference to the technical specification sheet accompanying the asset."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV952#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SafetyMeasure(aas.Property):

            ALLOWED_VALUES = (r"True", r"False")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SafetyMeasure",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Safety Measure", r"de": r"Schutzeinrichtung"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Denotes whether the asset is part of a safety equipment."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV950#001"),
                }

            def __init__(self, value: str = r"False", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RedundantAssets(aas.Property):

            ALLOWED_VALUES = (r"True", r"False")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RedundantAssets",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Redundant Assets", r"de": r"Redundanz vorhanden"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"References zero (if empty), one or more backup assets for redundancy purposes."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV951#001"),
                }

            def __init__(self, value: str = r"False", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SILCategory(aas.Property):

            ALLOWED_VALUES = (r"0", r"1", r"2", r"3", r"4")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SILCategory",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"SIL Category", r"de": r"SIL Kategorie"}),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Denotes the safety integrity level (SIL), categorized into four levels."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV930#002"),
                }

            def __init__(self, value: str = r"0", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FailureProbability(aas.Property):

            ALLOWED_VALUES = (r"low", r"medium", r"high", r"critical")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FailureProbability",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"FailureProbability", r"de": r"Fehlerwahrscheinlichkeit"}
                    ),
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the probability of a failure occurring, classified into three levels."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV942#001"),
                }

            def __init__(self, value: str = r"low", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FailureSeverity(aas.Property):

            ALLOWED_VALUES = (r"no impact", r"potential", r"measureable", r"significant")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FailureSeverity",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Failure Severity", r"de": r"Fehlerschwere"}
                    ),
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the potential impact or seriousness of a failure, classified into three levels."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV943#001"),
                }

            def __init__(self, value: str = r"significant", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CriticalityCategory(aas.Property):

            ALLOWED_VALUES = (r"low", r"medium", r"high", r"critical")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CriticalityCategory",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Criticality Category", r"de": r"Kritikalitätskategorie"}
                    ),
                    "category": r"VARIABLE",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"A computed value based on Failure Probability and Failure Severity, usually calculated automatically."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV941#001"),
                }

            def __init__(self, value: str = r"critical", **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FurtherInformation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FurtherInformation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"FurtherInformation", r"de": r"Weitere Angaben nach Bedarf"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Additional relevant details about the asset, such as maintenance schedules."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAW617#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FurtherInformationReference(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FurtherInformationReference",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Further Information Reference", r"de": r"Referenz auf weitere Informationen"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"A field for including references to supplementary information"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class GeneralTask(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"GeneralTask",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"General Task", r"de": r"Allgemeine Aufgabenstellung"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Detailed description of the task and installation or placement conditions of the specific asset."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV956#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"GeneralInformation",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"GeneralInformation", r"de": r"Allgemeine Angaben"}
                ),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Provides details about the specific asset."}),
                "semantic_id": global_ref(r"0173-1#01-AGC975#002"),
            }

        def __init__(
            self,
            sILCategory: Union[str, SILCategory],
            functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
            technicalLocation: Optional[Union[str, TechnicalLocation]] = None,
            description_: Optional[Union[str, Description]] = None,
            assetSubtype: Optional[Union[str, AssetSubtype]] = None,
            specificationSheetReference: Optional[Union[str, SpecificationSheetReference]] = None,
            safetyMeasure: Optional[Union[str, SafetyMeasure]] = None,
            redundantAssets: Optional[Union[str, RedundantAssets]] = None,
            failureProbability: Optional[Union[str, FailureProbability]] = None,
            failureSeverity: Optional[Union[str, FailureSeverity]] = None,
            criticalityCategory: Optional[Union[str, CriticalityCategory]] = None,
            furtherInformation: Optional[Iterable[Union[str, FurtherInformation]]] = None,
            furtherInformationReference: Optional[Iterable[Union[str, FurtherInformationReference]]] = None,
            generalTask: Optional[Union[str, GeneralTask]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if functionalLocation is not None and not isinstance(functionalLocation, aas.SubmodelElement):
                functionalLocation = self.FunctionalLocation(functionalLocation)

            # Build a submodel element if a raw value was passed in the argument

            if technicalLocation is not None and not isinstance(technicalLocation, aas.SubmodelElement):
                technicalLocation = self.TechnicalLocation(technicalLocation)

            # Build a submodel element if a raw value was passed in the argument

            if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                description_ = self.Description(description_)

            # Build a submodel element if a raw value was passed in the argument

            if assetSubtype is not None and not isinstance(assetSubtype, aas.SubmodelElement):
                assetSubtype = self.AssetSubtype(assetSubtype)

            # Build a submodel element if a raw value was passed in the argument

            if specificationSheetReference is not None and not isinstance(
                specificationSheetReference, aas.SubmodelElement
            ):
                specificationSheetReference = self.SpecificationSheetReference(specificationSheetReference)

            # Build a submodel element if a raw value was passed in the argument

            if safetyMeasure is not None and not isinstance(safetyMeasure, aas.SubmodelElement):
                safetyMeasure = self.SafetyMeasure(safetyMeasure)

            # Build a submodel element if a raw value was passed in the argument

            if redundantAssets is not None and not isinstance(redundantAssets, aas.SubmodelElement):
                redundantAssets = self.RedundantAssets(redundantAssets)

            # Build a submodel element if a raw value was passed in the argument

            if sILCategory is not None and not isinstance(sILCategory, aas.SubmodelElement):
                sILCategory = self.SILCategory(sILCategory)

            # Build a submodel element if a raw value was passed in the argument

            if failureProbability is not None and not isinstance(failureProbability, aas.SubmodelElement):
                failureProbability = self.FailureProbability(failureProbability)

            # Build a submodel element if a raw value was passed in the argument

            if failureSeverity is not None and not isinstance(failureSeverity, aas.SubmodelElement):
                failureSeverity = self.FailureSeverity(failureSeverity)

            # Build a submodel element if a raw value was passed in the argument

            if criticalityCategory is not None and not isinstance(criticalityCategory, aas.SubmodelElement):
                criticalityCategory = self.CriticalityCategory(criticalityCategory)

            # A str would be split into its characters
            if isinstance(furtherInformation, str):
                raise TypeError("furtherInformation takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if furtherInformation:
                furtherInformation = [
                    i if isinstance(i, aas.SubmodelElement) else self.FurtherInformation(i) for i in furtherInformation
                ]

            # A str would be split into its characters
            if isinstance(furtherInformationReference, str):
                raise TypeError("furtherInformationReference takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if furtherInformationReference:
                furtherInformationReference = [
                    i if isinstance(i, aas.SubmodelElement) else self.FurtherInformationReference(i)
                    for i in furtherInformationReference
                ]

            # Build a submodel element if a raw value was passed in the argument

            if generalTask is not None and not isinstance(generalTask, aas.SubmodelElement):
                generalTask = self.GeneralTask(generalTask)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                functionalLocation,
                technicalLocation,
                description_,
                assetSubtype,
                specificationSheetReference,
                safetyMeasure,
                redundantAssets,
                sILCategory,
                failureProbability,
                failureSeverity,
                criticalityCategory,
                furtherInformation,
                furtherInformationReference,
                generalTask,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CompleteSystem(aas.SubmodelElementCollection):

        class StatusCondition(aas.SubmodelElementCollection):

            class StatusConditionName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusConditionName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Status Condition Name", r"de": r"Zustands- und Fehlerbild"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Name of the asset's state, highlighting deviations from normal operations or reduced lifespan."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV958#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MonitoringRequired(aas.Property):

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MonitoringRequired",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Monitoring Required", r"de": r"Überwachung benötigt"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies whether the user is requiring monitoring."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV959#001"),
                    }

                def __init__(self, value: str = r"False", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Description", r"de": r"Beschreibung"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Offers further information about the asset's status/fault profile or status monitoring."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV960#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MethodAbbreviation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MethodAbbreviation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Method Abbreviation", r"de": r"Methode"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Captures the abbreviated name of the PAM method employed for monitoring purposes."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV961#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NE107Status(aas.Property):

                ALLOWED_VALUES = (r"failure", r"function check", r"out of specification", r"maintenance request")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NE107Status",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"NE107Status", r"de": r"Status nach NAMUR-Empfehlung NE 107"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Status according to NAMUR recommendation NE 107."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV962#001"),
                    }

                def __init__(self, value: str = r"failure", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NE129AlarmCategory(aas.Property):

                ALLOWED_VALUES = (r"Asset-Alarm", r"Asset-Notification", r"Asset-State Chance")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NE129AlarmCategory",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"NE129 Alarm Category",
                                r"de": r"Alarm-/Meldekategorie nach NAMUR Empfehlung NE129",
                            }
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Alarm/signaling category according to NAMUR recommendation NE 129."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV963#001"),
                    }

                def __init__(self, value: str = r"Asset-Alarm", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"StatusCondition",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Status Condition", r"de": r"Zustands- und Fehlerbild"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": "Characteristics of the asset's operational and failure states."}
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGC980#001"),
                }

            def __init__(
                self,
                statusConditionName: Union[str, StatusConditionName],
                monitoringRequired: Union[str, MonitoringRequired],
                description_: Union[str, Description],
                methodAbbreviation: Optional[Union[str, MethodAbbreviation]] = None,
                nE107Status: Optional[Union[str, NE107Status]] = None,
                nE129AlarmCategory: Optional[Union[str, NE129AlarmCategory]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if statusConditionName is not None and not isinstance(statusConditionName, aas.SubmodelElement):
                    statusConditionName = self.StatusConditionName(statusConditionName)

                # Build a submodel element if a raw value was passed in the argument

                if monitoringRequired is not None and not isinstance(monitoringRequired, aas.SubmodelElement):
                    monitoringRequired = self.MonitoringRequired(monitoringRequired)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if methodAbbreviation is not None and not isinstance(methodAbbreviation, aas.SubmodelElement):
                    methodAbbreviation = self.MethodAbbreviation(methodAbbreviation)

                # Build a submodel element if a raw value was passed in the argument

                if nE107Status is not None and not isinstance(nE107Status, aas.SubmodelElement):
                    nE107Status = self.NE107Status(nE107Status)

                # Build a submodel element if a raw value was passed in the argument

                if nE129AlarmCategory is not None and not isinstance(nE129AlarmCategory, aas.SubmodelElement):
                    nE129AlarmCategory = self.NE129AlarmCategory(nE129AlarmCategory)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    statusConditionName,
                    monitoringRequired,
                    description_,
                    methodAbbreviation,
                    nE107Status,
                    nE129AlarmCategory,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CompleteSystem",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Complete System", r"de": r"Komplettsystem"}),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Interconnected fields, incorporating status/fault profiles that apply to the entire asset rather than specific parts."
                    }
                ),
                "semantic_id": global_ref(r"0173-1#01-AGC979#001"),
            }

        def __init__(
            self,
            statusCondition: Optional[Iterable[StatusCondition]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(statusCondition, str):
                raise TypeError("statusCondition takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(statusCondition)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SubSystem(aas.SubmodelElementCollection):

        class SubSystemName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SubSystemName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Subsystem Name", r"de": r"Teilsystem Name"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Specifies the name of the subsystem."}),
                    "semantic_id": global_ref(r"0173-1#02-AAV965#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FunctionalLocation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FunctionalLocation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Functional Location", r"de": r"Technischer Platz"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Indicates the subsystem's logical position within a piping and instrumentation diagram."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV946#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TechnicalLocation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TechnicalLocation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Technical Location", r"de": r"Technischer Ort"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Specifies the actual location of the subsystem in the plant."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV947#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class StatusCondition(aas.SubmodelElementCollection):

            class StatusConditionName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StatusConditionName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Status Condition Name", r"de": r"Zustands- und Fehlerbild"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Name of the subsystem's state, highlighting deviations from normal operations or reduced lifespan."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV958#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MonitoringRequired(aas.Property):

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MonitoringRequired",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Monitoring Required", r"de": r"Überwachung benötigt"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies whether the user is requiring monitoring."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV959#001"),
                    }

                def __init__(self, value: str = r"True", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Description", r"de": r"Beschreibung"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Offers further information about the subsystem's status/fault profile or status monitoring."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV960#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MethodAbbreviation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MethodAbbreviation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Method Abbreviation", r"de": r"Methode"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Captures the abbreviated name of the PAM method employed for monitoring purposes."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV961#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NE107Status(aas.Property):

                ALLOWED_VALUES = (r"failure", r"function check", r"out of specification", r"maintenance request")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NE107Status",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"NE 107 Status", r"de": r"Status nach NAMUR-Empfehlung NE 107"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Status according to NAMUR recommendation NE 107."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV962#001"),
                    }

                def __init__(self, value: str = r"failure", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NE129AlarmCategory(aas.Property):

                ALLOWED_VALUES = (r"Asset-Alarm", r"Asset-Notification", r"Asset-State Chance")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NE129AlarmCategory",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"NE 129 Alarm Category",
                                r"de": r"Alarm-/Meldekategorie nach NAMUR Empfehlung",
                            }
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Alarm/signaling category according to NAMUR recommendation NE 129."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV963#001"),
                    }

                def __init__(self, value: str = r"Asset-Alarm", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"StatusCondition",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Status Condition", r"de": r"Zustands- und Fehlerbild"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": "Characteristics of the subsystems's operational and failure states."}
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGC980#001"),
                }

            def __init__(
                self,
                statusConditionName: Union[str, StatusConditionName],
                monitoringRequired: Union[str, MonitoringRequired],
                description_: Union[str, Description],
                methodAbbreviation: Optional[Union[str, MethodAbbreviation]] = None,
                nE107Status: Optional[Union[str, NE107Status]] = None,
                nE129AlarmCategory: Optional[Union[str, NE129AlarmCategory]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if statusConditionName is not None and not isinstance(statusConditionName, aas.SubmodelElement):
                    statusConditionName = self.StatusConditionName(statusConditionName)

                # Build a submodel element if a raw value was passed in the argument

                if monitoringRequired is not None and not isinstance(monitoringRequired, aas.SubmodelElement):
                    monitoringRequired = self.MonitoringRequired(monitoringRequired)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if methodAbbreviation is not None and not isinstance(methodAbbreviation, aas.SubmodelElement):
                    methodAbbreviation = self.MethodAbbreviation(methodAbbreviation)

                # Build a submodel element if a raw value was passed in the argument

                if nE107Status is not None and not isinstance(nE107Status, aas.SubmodelElement):
                    nE107Status = self.NE107Status(nE107Status)

                # Build a submodel element if a raw value was passed in the argument

                if nE129AlarmCategory is not None and not isinstance(nE129AlarmCategory, aas.SubmodelElement):
                    nE129AlarmCategory = self.NE129AlarmCategory(nE129AlarmCategory)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    statusConditionName,
                    monitoringRequired,
                    description_,
                    methodAbbreviation,
                    nE107Status,
                    nE129AlarmCategory,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SubSystemReference(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SubSystemReference",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Subsystem Reference", r"de": r"Subsystem Referenze"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Additional references associated to the subsystem."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAW622#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PAMSpecificationSheetIdentification(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PAMSpecificationSheetIdentification",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"PAM Specification Sheet Identification",
                            r"de": r"PAM Spezifikationsblatt Identifikation",
                        }
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"The distinct identifier for the PAM specification sheet for the subsystem."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV929#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PAMSpecificationSheetReference(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PAMSpecificationSheetReference",
                    "value_type": str,
                    "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"PAM Specification Sheet Reference", r"de": r"PAM Spezifikationsblatt Referenz"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Links to relevant PAM specification documentation for the subsystem."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAV967#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SubSystem",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Subsystem", r"de": r"Teilsystem"}),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Properties of the subsystem."}),
                "semantic_id": global_ref(r"0173-1#01-AGC981#001"),
            }

        def __init__(
            self,
            subSystemName: Union[str, SubSystemName],
            functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
            technicalLocation: Optional[Union[str, TechnicalLocation]] = None,
            statusCondition: Optional[Iterable[StatusCondition]] = None,
            subSystemReference: Optional[Union[str, SubSystemReference]] = None,
            pAMSpecificationSheetIdentification: Optional[Union[str, PAMSpecificationSheetIdentification]] = None,
            pAMSpecificationSheetReference: Optional[Union[str, PAMSpecificationSheetReference]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if subSystemName is not None and not isinstance(subSystemName, aas.SubmodelElement):
                subSystemName = self.SubSystemName(subSystemName)

            # Build a submodel element if a raw value was passed in the argument

            if functionalLocation is not None and not isinstance(functionalLocation, aas.SubmodelElement):
                functionalLocation = self.FunctionalLocation(functionalLocation)

            # Build a submodel element if a raw value was passed in the argument

            if technicalLocation is not None and not isinstance(technicalLocation, aas.SubmodelElement):
                technicalLocation = self.TechnicalLocation(technicalLocation)

            # A str would be split into its characters
            if isinstance(statusCondition, str):
                raise TypeError("statusCondition takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if subSystemReference is not None and not isinstance(subSystemReference, aas.SubmodelElement):
                subSystemReference = self.SubSystemReference(subSystemReference)

            # Build a submodel element if a raw value was passed in the argument

            if pAMSpecificationSheetIdentification is not None and not isinstance(
                pAMSpecificationSheetIdentification, aas.SubmodelElement
            ):
                pAMSpecificationSheetIdentification = self.PAMSpecificationSheetIdentification(
                    pAMSpecificationSheetIdentification
                )

            # Build a submodel element if a raw value was passed in the argument

            if pAMSpecificationSheetReference is not None and not isinstance(
                pAMSpecificationSheetReference, aas.SubmodelElement
            ):
                pAMSpecificationSheetReference = self.PAMSpecificationSheetReference(pAMSpecificationSheetReference)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                subSystemName,
                functionalLocation,
                technicalLocation,
                statusCondition,
                subSystemReference,
                pAMSpecificationSheetIdentification,
                pAMSpecificationSheetReference,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ApplicableMethod(aas.SubmodelElementCollection):

        class StaticParameters(aas.SubmodelElementCollection):

            class ParameterName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ParameterName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Parameter Name", r"de": r"Parametername"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of method parameter."}),
                        "semantic_id": global_ref(r"0173-1#02-AAV978#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Description", r"de": r"Beschreibung"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "Provides a concise explanation of the parameter's purpose."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV979#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StaticParameterValue(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StaticParameterValue",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Static Parameter Value", r"de": r"Statischer Parameter Wert"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A static parameter value of a method used for monitoring of this subsystem."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV980#001"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PhysicalUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PhysicalUnit",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PhysicalUnit", r"de": r"Einheit"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies the physical unit of the static parameter."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV981#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"StaticParameters",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Static Parameters", r"de": r"Statische Parameter"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"List of static parameters such as trigger limits."}
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGC984#001"),
                }

            def __init__(
                self,
                parameterName: Union[str, ParameterName],
                staticParameterValue: Union[float, StaticParameterValue],
                physicalUnit: Union[str, PhysicalUnit],
                description_: Optional[Union[str, Description]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if parameterName is not None and not isinstance(parameterName, aas.SubmodelElement):
                    parameterName = self.ParameterName(parameterName)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if staticParameterValue is not None and not isinstance(staticParameterValue, aas.SubmodelElement):
                    staticParameterValue = self.StaticParameterValue(staticParameterValue)

                # Build a submodel element if a raw value was passed in the argument

                if physicalUnit is not None and not isinstance(physicalUnit, aas.SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    parameterName, description_, staticParameterValue, physicalUnit
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class GeneratedSignals(aas.SubmodelElementCollection):

            class SignalName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SignalName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signal Name", r"de": r"Signalname"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the generated signal."}),
                        "semantic_id": global_ref(r"0173-1#02-AAV983#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Description", r"de": r"Beschreibung"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Provides a concise explanation of the generated signal."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV984#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ValueRange(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ValueRange",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Wertebereich"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies the possible range of values for the generated signal."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV985#001"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PhysicalUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PhysicalUnit",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PhysicalUnit", r"de": r"Einheit"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Physical unit of the generated signal."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV981#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RecordingRequired(aas.Property):

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RecordingRequired",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Recording Required", r"de": r"Aufzeichnung im PAM-System"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Determines whether the signal is transmitted to the PAM system for long-term archiving."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV986#001"),
                    }

                def __init__(self, value: str = r"True", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SignalType(aas.Property):

                ALLOWED_VALUES = (r"floating point", r"integer", r"binary")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SignalType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Signal Type", r"de": r"Signalart"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Indicates whether the generated signal from the method is a floating point, integer or binary value."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV987#001"),
                    }

                def __init__(self, value: str = r"floating point", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"GeneratedSignals",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Generated Signals", r"de": r"Generiertes Signal aus Methode"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"List of generated signals."}),
                    "semantic_id": global_ref(r"0173-1#01-AGC985#001"),
                }

            def __init__(
                self,
                signalName: Union[str, SignalName],
                recordingRequired: Union[str, RecordingRequired],
                signalType: Union[str, SignalType],
                description_: Optional[Union[str, Description]] = None,
                valueRange: Optional[Union[float, ValueRange]] = None,
                physicalUnit: Optional[Union[str, PhysicalUnit]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if signalName is not None and not isinstance(signalName, aas.SubmodelElement):
                    signalName = self.SignalName(signalName)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if valueRange is not None and not isinstance(valueRange, aas.SubmodelElement):
                    valueRange = self.ValueRange(valueRange)

                # Build a submodel element if a raw value was passed in the argument

                if physicalUnit is not None and not isinstance(physicalUnit, aas.SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Build a submodel element if a raw value was passed in the argument

                if recordingRequired is not None and not isinstance(recordingRequired, aas.SubmodelElement):
                    recordingRequired = self.RecordingRequired(recordingRequired)

                # Build a submodel element if a raw value was passed in the argument

                if signalType is not None and not isinstance(signalType, aas.SubmodelElement):
                    signalType = self.SignalType(signalType)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    signalName, description_, valueRange, physicalUnit, recordingRequired, signalType
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RequiredInputSignals(aas.SubmodelElementCollection):

            class Name(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Name",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Name", r"de": r"Eingangssignal-Name"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the required input signal."}),
                        "semantic_id": global_ref(r"0173-1#02-AAV989#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Description(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Description",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Description", r"de": r"Beschreibung"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Provides a concise explanation of the input signal."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV990#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ValueRange(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ValueRange",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Value Range", r"de": r"Wertebereich"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies the value range of the input signal."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV991#001"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PhysicalUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PhysicalUnit",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Physical Unit", r"de": r"Einheit"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Physical unit of the input signal."}),
                        "semantic_id": global_ref(r"0173-1#02-AAV981#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Required(aas.Property):

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Required",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Required", r"de": r"Benötigt"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Specifies whether the input signal is required for the method."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV992#001"),
                    }

                def __init__(self, value: str = r"True", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InputAvailable(aas.Property):

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InputAvailable",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Input Available", r"de": r"Vorhanden"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Clarification whether this input signal for the method is already available."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV993#001"),
                    }

                def __init__(self, value: str = r"True", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FunctionalLocation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FunctionalLocation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Functional Location", r"de": r"Technischer Platz"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Indicates the asset's logical position within a piping and instrumentation diagram"
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV946#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RecordingRequired(aas.Property):

                ALLOWED_PATTERN = r"True"

                ALLOWED_VALUES = (r"True", r"False")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RecordingRequired",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Recording Required", r"de": r"Aufzeichnung im PAM-System"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Determines whether the values of the input signal are transmitted to the PAM system for long-term archiving."
                            }
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV994#001"),
                    }

                def __init__(self, value: str = r"True", **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    if value is not None and not re.fullmatch(self.ALLOWED_PATTERN, xsd.xsd_repr(value)):
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_PATTERN}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"RequiredInputSignals",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Required Input Signals", r"de": r"Vorhandene, benötigte Sensoren, Geräte"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"List of necessary input signals of the method."}
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGC986#001"),
                }

            def __init__(
                self,
                name: Union[str, Name],
                required: Union[str, Required],
                inputAvailable: Union[str, InputAvailable],
                recordingRequired: Union[str, RecordingRequired],
                description_: Optional[Union[str, Description]] = None,
                valueRange: Optional[Union[float, ValueRange]] = None,
                physicalUnit: Optional[Union[str, PhysicalUnit]] = None,
                functionalLocation: Optional[Union[str, FunctionalLocation]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if name is not None and not isinstance(name, aas.SubmodelElement):
                    name = self.Name(name)

                # Build a submodel element if a raw value was passed in the argument

                if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                    description_ = self.Description(description_)

                # Build a submodel element if a raw value was passed in the argument

                if valueRange is not None and not isinstance(valueRange, aas.SubmodelElement):
                    valueRange = self.ValueRange(valueRange)

                # Build a submodel element if a raw value was passed in the argument

                if physicalUnit is not None and not isinstance(physicalUnit, aas.SubmodelElement):
                    physicalUnit = self.PhysicalUnit(physicalUnit)

                # Build a submodel element if a raw value was passed in the argument

                if required is not None and not isinstance(required, aas.SubmodelElement):
                    required = self.Required(required)

                # Build a submodel element if a raw value was passed in the argument

                if inputAvailable is not None and not isinstance(inputAvailable, aas.SubmodelElement):
                    inputAvailable = self.InputAvailable(inputAvailable)

                # Build a submodel element if a raw value was passed in the argument

                if functionalLocation is not None and not isinstance(functionalLocation, aas.SubmodelElement):
                    functionalLocation = self.FunctionalLocation(functionalLocation)

                # Build a submodel element if a raw value was passed in the argument

                if recordingRequired is not None and not isinstance(recordingRequired, aas.SubmodelElement):
                    recordingRequired = self.RecordingRequired(recordingRequired)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    name,
                    description_,
                    valueRange,
                    physicalUnit,
                    required,
                    inputAvailable,
                    functionalLocation,
                    recordingRequired,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ApplicableMethod",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Applicable Method", r"de": r"Anwendbare Methode"}
                ),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Characteristics of the method used for state or fault detection."}
                ),
                "semantic_id": global_ref(r"0173-1#01-AGC983#002"),
            }

        def __init__(
            self,
            generatedSignals: Iterable[GeneratedSignals],
            staticParameters: Optional[Iterable[StaticParameters]] = None,
            requiredInputSignals: Optional[Iterable[RequiredInputSignals]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(staticParameters, str):
                raise TypeError("staticParameters takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(generatedSignals, str):
                raise TypeError("generatedSignals takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(requiredInputSignals, str):
                raise TypeError("requiredInputSignals takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                staticParameters, generatedSignals, requiredInputSignals
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DocumentFooter(aas.SubmodelElementCollection):

        class DocumentConfirmation(aas.SubmodelElementCollection):

            class Date(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Date",
                        "value_type": str,
                        "value_id": global_ref(r"https://admin-shell.io/idta/prop/furtherinformationreference/1/0"),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Datum"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Date of revision of the PAM specification sheet."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAR969#002"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Author(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Author",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Author", r"de": r"Verfasser"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "The individual responsible for the document's revision."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV997#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Checked(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Checked",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Checked", r"de": r"Geprüft"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"The person who has checked the document."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV999#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Released(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Released",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Released", r"de": r"Genehmigt"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"The individual who has authorized the document for release."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAV998#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DocumentVersion(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DocumentVersion",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Document Version", r"de": r"Dokumentenidentifikation"}
                        ),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": "Identifier for the document's version."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAW000#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Company(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Company",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Company", r"de": r"Firma"}),
                        "category": r"PARAMETER",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"The name of the company associated with the confirmation of the document."}
                        ),
                        "semantic_id": global_ref(r"0173-1#02-AAW001#001"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DocumentConfirmation",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Document Confirmation", r"de": r"Dokument Bestätigung"}
                    ),
                    "category": r"PARAMETER",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information regarding the confirmation to the current status of the PAM specification sheet."
                        }
                    ),
                    "semantic_id": global_ref(r"0173-1#01-AGC988#001"),
                }

            def __init__(
                self,
                date: Union[str, Date],
                author: Union[str, Author],
                checked: Optional[Union[str, Checked]] = None,
                released: Optional[Union[str, Released]] = None,
                documentVersion: Optional[Union[str, DocumentVersion]] = None,
                company: Optional[Union[str, Company]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if date is not None and not isinstance(date, aas.SubmodelElement):
                    date = self.Date(date)

                # Build a submodel element if a raw value was passed in the argument

                if author is not None and not isinstance(author, aas.SubmodelElement):
                    author = self.Author(author)

                # Build a submodel element if a raw value was passed in the argument

                if checked is not None and not isinstance(checked, aas.SubmodelElement):
                    checked = self.Checked(checked)

                # Build a submodel element if a raw value was passed in the argument

                if released is not None and not isinstance(released, aas.SubmodelElement):
                    released = self.Released(released)

                # Build a submodel element if a raw value was passed in the argument

                if documentVersion is not None and not isinstance(documentVersion, aas.SubmodelElement):
                    documentVersion = self.DocumentVersion(documentVersion)

                # Build a submodel element if a raw value was passed in the argument

                if company is not None and not isinstance(company, aas.SubmodelElement):
                    company = self.Company(company)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    date, author, checked, released, documentVersion, company
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DocumentFooter",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Document Footer", r"de": r"Dokumentenfuß Anwender und Anbieter"}
                ),
                "category": r"PARAMETER",
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Release information related to the complete PAM specification sheet."}
                ),
                "semantic_id": global_ref(r"173-1#02-AAW627#001"),
            }

        def __init__(
            self,
            documentConfirmation: Iterable[DocumentConfirmation],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(documentConfirmation, str):
                raise TypeError("documentConfirmation takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(documentConfirmation)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"PAMSpecificationSheet",
            "display_name": aas.MultiLanguageNameType(
                dict_={r"en": r"PAM Specification Sheet", r"de": r"PAM Spezificationsblatt"}
            ),
            "category": r"VARIABLE",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"PAM Specification Sheet according to VDI/VDE GMA RL 2651-2 and specification of Plant Asset Management functions ",
                    r"de": r"Beschreibung und Spezifikation PAM Funktionen nach VDI GMA",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02019-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"0173-1#01-AGC973#003"),),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        documentHeader: DocumentHeader,
        generalInformation: GeneralInformation,
        applicableMethod: Iterable[ApplicableMethod],
        documentFooter: DocumentFooter,
        completeSystem: Optional[CompleteSystem] = None,
        subSystem: Optional[Iterable[SubSystem]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(subSystem, str):
            raise TypeError("subSystem takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(applicableMethod, str):
            raise TypeError("applicableMethod takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            documentHeader, generalInformation, completeSystem, subSystem, applicableMethod, documentFooter
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
