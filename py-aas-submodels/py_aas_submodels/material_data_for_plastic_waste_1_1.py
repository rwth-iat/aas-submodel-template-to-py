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


class MaterialDataForEN18065ClassificationOfPlastics(aas.Submodel):

    class DataQuality(aas.SubmodelElementCollection):

        class DataQualityLevel(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DataQualityLevel",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Data Quality Level (DQL)"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"DataQualityLevel (DQL) as per DIN EN 18065, Section 4 and elsewhere"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/DataQualityLevel/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DataQuality",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Data quality"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"Data Quality Level (DQL) as per EN 18065"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/DataQuality/1/0"),
            }

        def __init__(
            self,
            dataQualityLevel: Optional[Union[str, DataQualityLevel]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if dataQualityLevel is not None and not isinstance(dataQualityLevel, aas.SubmodelElement):
                dataQualityLevel = self.DataQualityLevel(dataQualityLevel)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(dataQualityLevel)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ApplicationSpecificStandards(GeneratedSubmodelElementList):

        class Applicationspecificstandards_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"ApplicationSpecificStandards",
                "type_value_list_element": aas.Property,
                "semantic_id_list_element": global_ref(
                    r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                ),
                "value_type_list_element": str,
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standards"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Relevant application-specific standards other than EN 18065"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/en18065materialdata/ApplicationSpecificStandards/1/0"
                ),
            }

        def __init__(
            self,
            applicationspecificstandards_items: Optional[
                Iterable[Union[str, Applicationspecificstandards_item]]
            ] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(applicationspecificstandards_items, str):
                raise TypeError("applicationspecificstandards_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if applicationspecificstandards_items:
                applicationspecificstandards_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Applicationspecificstandards_item(i)
                    for i in applicationspecificstandards_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                applicationspecificstandards_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class InformationCharacteristics(aas.SubmodelElementCollection):

        class MainMaterialType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MainMaterialType",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Main material type"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Main polymer type according to EN ISO 1043-1 (e.g., PE, PP, PET, ...)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/MainMaterialType/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TypeOfPackaging(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TypeOfPackaging",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type of packaging"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Packaging of the material (e.g., octabins, bagged goods, bale goods, silo, ...)"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/TypeOfPackaging/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ColorByVisualInspection(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ColorByVisualInspection",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Color by visual inspection"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Color of the material determined by visual inspection (e.g., black, natural, white, ...)"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/ColorByVisualInspection/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Form(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Form",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Form"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Physical form of the recyclate (e.g., agglomerate, flake, regrind, regenerate, regranulate, ...)"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/Form/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TradeName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TradeName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Trade name"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Commercial trade name of the recyclate"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/TradeName/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RecycledContent(aas.Property):

            ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.Decimal), xsd.from_xsd(r"100", xsd.Decimal))

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RecycledContent",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Recycled content"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Percentage by weight of recycled plastic in the material as calculated according to Section 5.1 of EN 18065"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/RecycledContent/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and (
                    value < self.ALLOWED_RANGE[0] or self.ALLOWED_RANGE[1] is not None and value > self.ALLOWED_RANGE[1]
                ):
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ChainOfCustody(aas.SubmodelElementCollection):

            class AttributionModel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AttributionModel",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Attribution model"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Attribution model"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/ChainOfCustody/AttributionModel/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RelevantEuropeanOrInternationalNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RelevantEuropeanOrInternationalNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Relevant European or international norm"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Relevant European or international norm"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/ChainOfCustody/RelevantEuropeanOrInternationalNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ChainOfCustody",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Chain of Custody"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Physical segregation, controlled blending, mass balance etc. (with indication, which attribution model has been used pursuant to European or international standard)"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/ChainOfCustody/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                attributionModel: Optional[Union[str, AttributionModel]] = None,
                relevantEuropeanOrInternationalNorm: Optional[Union[str, RelevantEuropeanOrInternationalNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if attributionModel is not None and not isinstance(attributionModel, aas.SubmodelElement):
                    attributionModel = self.AttributionModel(attributionModel)

                # Build a submodel element if a raw value was passed in the argument

                if relevantEuropeanOrInternationalNorm is not None and not isinstance(
                    relevantEuropeanOrInternationalNorm, aas.SubmodelElement
                ):
                    relevantEuropeanOrInternationalNorm = self.RelevantEuropeanOrInternationalNorm(
                        relevantEuropeanOrInternationalNorm
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    attributionModel, relevantEuropeanOrInternationalNorm
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RecyclingMethod(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RecyclingMethod",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Recycling Method"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about a mechanical recycling process, solvent-based process, etc."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/RecyclingMethod/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Source(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Source",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Source"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Source of the material (e.g., post-consumer, post-industrial/ pre-consumer, ...)"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/Source/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TypesOfFillers(GeneratedSubmodelElementList):

            class Typesoffillers_item(aas.SubmodelElementCollection):

                class Filler(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Filler",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Filler"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Filler type"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/TypesOfFillers/Filler/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class FillerMassPercentage(aas.Property):

                    ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.Decimal), xsd.from_xsd(r"100", xsd.Decimal))

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"FillerMassPercentage",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Filler Mass Percentage"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Mass percentage of the filler"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/TypesOfFillers/FillerMassPercentage/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and (
                            value < self.ALLOWED_RANGE[0]
                            or self.ALLOWED_RANGE[1] is not None
                            and value > self.ALLOWED_RANGE[1]
                        ):
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type of filler"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Types of fillers and mass percentages"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/TypeOfFiller/1/0"),
                    }

                def __init__(
                    self,
                    filler: Union[str, Filler],
                    fillerMassPercentage: Union[xsd.Decimal, FillerMassPercentage],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if filler is not None and not isinstance(filler, aas.SubmodelElement):
                        filler = self.Filler(filler)

                    # Build a submodel element if a raw value was passed in the argument

                    if fillerMassPercentage is not None and not isinstance(fillerMassPercentage, aas.SubmodelElement):
                        fillerMassPercentage = self.FillerMassPercentage(fillerMassPercentage)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(filler, fillerMassPercentage)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"TypesOfFillers",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id_list_element": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/TypeOfFiller/1/0"
                    ),
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Types of fillers"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Types of fillers"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/TypesOfFillers/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                typesoffillers_items: Optional[Iterable[Typesoffillers_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(typesoffillers_items, str):
                    raise TypeError("typesoffillers_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(typesoffillers_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LotNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LotNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Lot number"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"Batch or lot number for the material"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/LotNumber/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CertificateOfAnalysis(aas.SubmodelElementCollection):

            class TypeOfInspectionCertificate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TypeOfInspectionCertificate",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Type of Inspection Certificate"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Type of inspection certificate according to EN 10204 (2.1, 2.2, 3.1, or 3.2), or none"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/CertificateOfAnalysis/TypeOfInspectionCertificate/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Documentation(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"Documentation",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Documentation"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Documentation for the certificate of analysis"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/CertificateOfAnalysis/Documentation/1/0"
                        ),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"application/pdf", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CertificateOfAnalysis",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Certificate of analysis"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Reference to certificate of analysis according to EN 10204:2005, clause 3.1"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/CertificateOfAnalysis/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                typeOfInspectionCertificate: Union[str, TypeOfInspectionCertificate],
                documentation: Documentation,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if typeOfInspectionCertificate is not None and not isinstance(
                    typeOfInspectionCertificate, aas.SubmodelElement
                ):
                    typeOfInspectionCertificate = self.TypeOfInspectionCertificate(typeOfInspectionCertificate)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(typeOfInspectionCertificate, documentation)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ContentOfTheMainPlasticType(aas.Property):

            ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.Decimal), xsd.from_xsd(r"100", xsd.Decimal))

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ContentOfTheMainPlasticType",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Content of the main plastic type"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Content (mass percentage) of the main plastic type in the material"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/ContentOfTheMainPlasticType/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"3", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and (
                    value < self.ALLOWED_RANGE[0] or self.ALLOWED_RANGE[1] is not None and value > self.ALLOWED_RANGE[1]
                ):
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PercentConfidenceOfCertificateOfAnalysis(aas.Property):

            ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.Decimal), xsd.from_xsd(r"100", xsd.Decimal))

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PercentConfidenceOfCertificateOfAnalysis",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Percent Confidence of certificate of analysis"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Percentage confidence level of the certificate of analysis (CEN/TS 16010, CEN/TS 16011 - as explained in sec. 4.5.3 of EN 18065)"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/PercentConfidenceOfCertificateOfAnalysis/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"3", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and (
                    value < self.ALLOWED_RANGE[0] or self.ALLOWED_RANGE[1] is not None and value > self.ALLOWED_RANGE[1]
                ):
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CoefficientOfVariationWRTCertificateOfAnalysis(aas.Property):

            ALLOWED_RANGE = (xsd.from_xsd(r"0", xsd.Decimal), xsd.from_xsd(r"100", xsd.Decimal))

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CoefficientOfVariationWRTCertificateOfAnalysis",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Coefficient of variation with respect to the certificate of analysis"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Coefficient of variation with respect to the certificate of analysis (CEN/TS 16010, CEN/TS 16011 - as explained in sec. 4.5.3 of EN 18065)"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/CoefficientOfVariationWRTCertificateOfAnalysis/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"3", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and (
                    value < self.ALLOWED_RANGE[0] or self.ALLOWED_RANGE[1] is not None and value > self.ALLOWED_RANGE[1]
                ):
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_RANGE}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PresenceOfModifyingAdditives(GeneratedSubmodelElementList):

            class Presenceofmodifyingadditives_item(aas.SubmodelElementCollection):

                class ModifyingAdditiveName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ModifyingAdditiveName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modifying additive name"}),
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Name of the modifying additive"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/PresenceOfModifyingAdditives/ModifyingAdditive/ModifyingAdditiveName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ModifyingAdditiveCASNumber(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ModifyingAdditiveCASNumber",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modifying additive CAS number"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"CAS number of the modifying additive"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/PresenceOfModifyingAdditives/ModifyingAdditive/ModifyingAdditiveCASNumber/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Modifying additive"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Modifying additive"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/PresenceOfModifyingAdditives/ModifyingAdditive/1/0"
                        ),
                    }

                def __init__(
                    self,
                    modifyingAdditiveName: Union[str, ModifyingAdditiveName],
                    modifyingAdditiveCASNumber: Union[str, ModifyingAdditiveCASNumber],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if modifyingAdditiveName is not None and not isinstance(modifyingAdditiveName, aas.SubmodelElement):
                        modifyingAdditiveName = self.ModifyingAdditiveName(modifyingAdditiveName)

                    # Build a submodel element if a raw value was passed in the argument

                    if modifyingAdditiveCASNumber is not None and not isinstance(
                        modifyingAdditiveCASNumber, aas.SubmodelElement
                    ):
                        modifyingAdditiveCASNumber = self.ModifyingAdditiveCASNumber(modifyingAdditiveCASNumber)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        modifyingAdditiveName, modifyingAdditiveCASNumber
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"PresenceOfModifyingAdditives",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id_list_element": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/PresenceOfModifyingAdditives/ModifyingAdditive/1/0"
                    ),
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Presence of Modifying Additives"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Stabilizers, plasticizers, flame retardants, etc."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/PresenceOfModifyingAdditives/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                presenceofmodifyingadditives_items: Optional[Iterable[Presenceofmodifyingadditives_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(presenceofmodifyingadditives_items, str):
                    raise TypeError("presenceofmodifyingadditives_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    presenceofmodifyingadditives_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class OriginalUseOfMaterial(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OriginalUseOfMaterial",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Original use of the material"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Original use of the material: what is it derived from, how has it been processed, and what was it in contact with?"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/OriginalUseOfMaterial/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"4", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RecyclingFeedstockConversionTechnology(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RecyclingFeedstockConversionTechnology",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Recycling feedstock conversion technology"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Technology for the conversion of waste-derived feedstock for recycling"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/OriginalUseOfMaterial/RecyclingFeedstockConversionTechnology/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"4", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"InformationCharacteristics",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Information characteristics"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/en18065materialdata/InformationCharacteristics/1/0"
                ),
            }

        def __init__(
            self,
            mainMaterialType: Optional[Union[str, MainMaterialType]] = None,
            typeOfPackaging: Optional[Union[str, TypeOfPackaging]] = None,
            colorByVisualInspection: Optional[Union[str, ColorByVisualInspection]] = None,
            form: Optional[Union[str, Form]] = None,
            tradeName: Optional[Union[str, TradeName]] = None,
            recycledContent: Optional[Union[xsd.Decimal, RecycledContent]] = None,
            chainOfCustody: Optional[ChainOfCustody] = None,
            recyclingMethod: Optional[Union[str, RecyclingMethod]] = None,
            source: Optional[Union[str, Source]] = None,
            typesOfFillers: Optional[Union[Iterable[TypesOfFillers.Typesoffillers_item], TypesOfFillers]] = None,
            lotNumber: Optional[Union[str, LotNumber]] = None,
            certificateOfAnalysis: Optional[CertificateOfAnalysis] = None,
            contentOfTheMainPlasticType: Optional[Union[xsd.Decimal, ContentOfTheMainPlasticType]] = None,
            percentConfidenceOfCertificateOfAnalysis: Optional[
                Union[xsd.Decimal, PercentConfidenceOfCertificateOfAnalysis]
            ] = None,
            coefficientOfVariationWRTCertificateOfAnalysis: Optional[
                Union[xsd.Decimal, CoefficientOfVariationWRTCertificateOfAnalysis]
            ] = None,
            presenceOfModifyingAdditives: Optional[
                Union[
                    Iterable[PresenceOfModifyingAdditives.Presenceofmodifyingadditives_item],
                    PresenceOfModifyingAdditives,
                ]
            ] = None,
            originalUseOfMaterial: Optional[Union[str, OriginalUseOfMaterial]] = None,
            recyclingFeedstockConversionTechnology: Optional[Union[str, RecyclingFeedstockConversionTechnology]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if mainMaterialType is not None and not isinstance(mainMaterialType, aas.SubmodelElement):
                mainMaterialType = self.MainMaterialType(mainMaterialType)

            # Build a submodel element if a raw value was passed in the argument

            if typeOfPackaging is not None and not isinstance(typeOfPackaging, aas.SubmodelElement):
                typeOfPackaging = self.TypeOfPackaging(typeOfPackaging)

            # Build a submodel element if a raw value was passed in the argument

            if colorByVisualInspection is not None and not isinstance(colorByVisualInspection, aas.SubmodelElement):
                colorByVisualInspection = self.ColorByVisualInspection(colorByVisualInspection)

            # Build a submodel element if a raw value was passed in the argument

            if form is not None and not isinstance(form, aas.SubmodelElement):
                form = self.Form(form)

            # Build a submodel element if a raw value was passed in the argument

            if tradeName is not None and not isinstance(tradeName, aas.SubmodelElement):
                tradeName = self.TradeName(tradeName)

            # Build a submodel element if a raw value was passed in the argument

            if recycledContent is not None and not isinstance(recycledContent, aas.SubmodelElement):
                recycledContent = self.RecycledContent(recycledContent)

            # Build a submodel element if a raw value was passed in the argument

            if recyclingMethod is not None and not isinstance(recyclingMethod, aas.SubmodelElement):
                recyclingMethod = self.RecyclingMethod(recyclingMethod)

            # Build a submodel element if a raw value was passed in the argument

            if source is not None and not isinstance(source, aas.SubmodelElement):
                source = self.Source(source)

            # A str would be split into its characters
            if isinstance(typesOfFillers, str):
                raise TypeError("typesOfFillers takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if typesOfFillers is not None and not isinstance(typesOfFillers, aas.SubmodelElement):
                typesOfFillers = self.TypesOfFillers(typesOfFillers)

            # Build a submodel element if a raw value was passed in the argument

            if lotNumber is not None and not isinstance(lotNumber, aas.SubmodelElement):
                lotNumber = self.LotNumber(lotNumber)

            # Build a submodel element if a raw value was passed in the argument

            if contentOfTheMainPlasticType is not None and not isinstance(
                contentOfTheMainPlasticType, aas.SubmodelElement
            ):
                contentOfTheMainPlasticType = self.ContentOfTheMainPlasticType(contentOfTheMainPlasticType)

            # Build a submodel element if a raw value was passed in the argument

            if percentConfidenceOfCertificateOfAnalysis is not None and not isinstance(
                percentConfidenceOfCertificateOfAnalysis, aas.SubmodelElement
            ):
                percentConfidenceOfCertificateOfAnalysis = self.PercentConfidenceOfCertificateOfAnalysis(
                    percentConfidenceOfCertificateOfAnalysis
                )

            # Build a submodel element if a raw value was passed in the argument

            if coefficientOfVariationWRTCertificateOfAnalysis is not None and not isinstance(
                coefficientOfVariationWRTCertificateOfAnalysis, aas.SubmodelElement
            ):
                coefficientOfVariationWRTCertificateOfAnalysis = self.CoefficientOfVariationWRTCertificateOfAnalysis(
                    coefficientOfVariationWRTCertificateOfAnalysis
                )

            # A str would be split into its characters
            if isinstance(presenceOfModifyingAdditives, str):
                raise TypeError("presenceOfModifyingAdditives takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if presenceOfModifyingAdditives is not None and not isinstance(
                presenceOfModifyingAdditives, aas.SubmodelElement
            ):
                presenceOfModifyingAdditives = self.PresenceOfModifyingAdditives(presenceOfModifyingAdditives)

            # Build a submodel element if a raw value was passed in the argument

            if originalUseOfMaterial is not None and not isinstance(originalUseOfMaterial, aas.SubmodelElement):
                originalUseOfMaterial = self.OriginalUseOfMaterial(originalUseOfMaterial)

            # Build a submodel element if a raw value was passed in the argument

            if recyclingFeedstockConversionTechnology is not None and not isinstance(
                recyclingFeedstockConversionTechnology, aas.SubmodelElement
            ):
                recyclingFeedstockConversionTechnology = self.RecyclingFeedstockConversionTechnology(
                    recyclingFeedstockConversionTechnology
                )

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                mainMaterialType,
                typeOfPackaging,
                colorByVisualInspection,
                form,
                tradeName,
                recycledContent,
                chainOfCustody,
                recyclingMethod,
                source,
                typesOfFillers,
                lotNumber,
                certificateOfAnalysis,
                contentOfTheMainPlasticType,
                percentConfidenceOfCertificateOfAnalysis,
                coefficientOfVariationWRTCertificateOfAnalysis,
                presenceOfModifyingAdditives,
                originalUseOfMaterial,
                recyclingFeedstockConversionTechnology,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class PropertyCharacteristics(aas.SubmodelElementCollection):

        class Viscosity(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Viscosity",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Viscosity measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Measurements of viscosity (MVR/ MFR, IV, VN) - according to EN ISO 1133 series, EN ISO 307, or EN ISO 1628 series"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/Viscosity/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"1", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class AshContent(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"AshContent",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Ash content measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Measurements of ash content - according to EN ISO 3451 series, or EN ISO 1172"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/AshContent/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ResidualHumidity(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ResidualHumidity",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Residual moisture content measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Measurements of residual moisture content - according to EN ISO 15512, ASTM D6980-17, EN 12099, or EN 15348, Annex B"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/ResidualHumidity/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Density(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"Density",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Density measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Measurements of density - according to EN ISO 1183 series"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/Density/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"2", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class BulkDensity(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"BulkDensity",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Bulk density measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Measurements of bulk density - according to EN ISO 60 or ASTM D1895, Method C, EN 15345, Annex A, or EN 15342, Annex A"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/BulkDensity/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"3", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ParticleSizeDistribution(aas.SubmodelElementCollection):

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuredValue(aas.SubmodelElementCollection):

                class Value(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Value",
                            "value_type": xsd.Float,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                            "category": r"VARIABLE",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"The value of the of measured sensor output"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                        }

                    def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Unit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Unit",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"The unit of the measured value"}),
                            "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Kind(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Kind",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                            "category": r"PARAMETER",
                            "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                            "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                            "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"MeasuredValue",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"This is the measured value of the sensor output"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"),
                    }

                def __init__(
                    self,
                    value_: Union[xsd.Float, Value],
                    unit: Union[str, Unit],
                    kind: Union[str, Kind],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                        value_ = self.Value(value_)

                    # Build a submodel element if a raw value was passed in the argument

                    if unit is not None and not isinstance(unit, aas.SubmodelElement):
                        unit = self.Unit(unit)

                    # Build a submodel element if a raw value was passed in the argument

                    if kind is not None and not isinstance(kind, aas.SubmodelElement):
                        kind = self.Kind(kind)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ParticleSizeDistribution",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Particle size distribution measurements"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Measurements of particle size distribution - according to EN 15346 Annex D, EN 15348 Annex A, ISO 22498, or ASTM D 1921"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/ParticleSizeDistribution/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"4", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValue: MeasuredValue,
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(standardOrNorm, measuredValue)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TensileProperties(aas.SubmodelElementCollection):

            class MeasuredValues(GeneratedSubmodelElementList):

                class Measuredvalues_item(aas.SubmodelElementCollection):

                    class Value(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Value",
                                "value_type": xsd.Float,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Value"}),
                                "category": r"VARIABLE",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"The value of the of measured sensor output"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/measurementvalue/value/1/0"),
                            }

                        def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Unit",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Unit"}),
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"The unit of the measured value"}
                                ),
                                "semantic_id": global_ref(r"0112/2///62720#UBA000"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Kind(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Kind",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Kind"}),
                                "category": r"PARAMETER",
                                "description": aas.MultiLanguageTextType(dict_={r"en": r"Kind of measured value"}),
                                "semantic_id": global_ref(r"0112/2///62683#ACI144"),
                                "supplemental_semantic_id": (global_ref(r"0112/2///62683#ACI144"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"This is the measured value of the sensor output"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value_: Union[xsd.Float, Value],
                        unit: Union[str, Unit],
                        kind: Union[str, Kind],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if value_ is not None and not isinstance(value_, aas.SubmodelElement):
                            value_ = self.Value(value_)

                        # Build a submodel element if a raw value was passed in the argument

                        if unit is not None and not isinstance(unit, aas.SubmodelElement):
                            unit = self.Unit(unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if kind is not None and not isinstance(kind, aas.SubmodelElement):
                            kind = self.Kind(kind)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(value_, unit, kind)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"MeasuredValues",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id_list_element": global_ref(
                            r"https://admin-shell.io/idta/measurementvalue/measuredvalue/1/0"
                        ),
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measured Values"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Template collection to capture a list of measurement values"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/MeasuredValues/1/0"
                        ),
                    }

                def __init__(
                    self,
                    measuredvalues_items: Iterable[Measuredvalues_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(measuredvalues_items, str):
                        raise TypeError("measuredvalues_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(measuredvalues_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class StandardOrNorm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StandardOrNorm",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Application-specific standard"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Standard or norm"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/StandardOrNorm/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"TensileProperties",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Tensile properties measurements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Measurements of tensile properties - according to EN ISO 527-1, EN ISO 527-2, EN ISO 527-3, or EN ISO 527-4"
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/en18065materialdata/TensileProperties/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"4", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                measuredValues: Union[Iterable[MeasuredValues.Measuredvalues_item], MeasuredValues],
                standardOrNorm: Optional[Union[str, StandardOrNorm]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(measuredValues, str):
                    raise TypeError("measuredValues takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if measuredValues is not None and not isinstance(measuredValues, aas.SubmodelElement):
                    measuredValues = self.MeasuredValues(measuredValues)

                # Build a submodel element if a raw value was passed in the argument

                if standardOrNorm is not None and not isinstance(standardOrNorm, aas.SubmodelElement):
                    standardOrNorm = self.StandardOrNorm(standardOrNorm)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(measuredValues, standardOrNorm)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class MaterialIdentification(aas.SubmodelElementCollection):

            class FTIR(aas.SubmodelElementCollection):

                class Documentation(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"Documentation",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Documentation"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/MaterialIdentification/FTIR/Documentation/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/pdf",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"FTIR",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"FTIR"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Material identification - using IR (database comparison) "}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/MaterialIdentification/FTIR/1/0"
                        ),
                    }

                def __init__(
                    self,
                    documentation: Optional[Documentation] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(documentation)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DSC(aas.SubmodelElementCollection):

                class Documentation(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"Documentation",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Documentation"}),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/en18065materialdata/MaterialIdentification/DSC/Documentation/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/pdf",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"DSC",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"DSC"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Material identification - using DSC according to EN ISO 11357-1, EN ISO 11357-2, EN ISO 11357-3"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/en18065materialdata/MaterialIdentification/DSC/1/0"
                        ),
                    }

                def __init__(
                    self, documentation: Iterable[Documentation], **kwargs: Unpack[SubmodelElementCollectionMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(documentation, str):
                        raise TypeError("documentation takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(documentation)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"MaterialIdentification",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Material identification"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Material identification (FTIR or DSC) - using IR (database comparison) or DSC according to EN ISO 11357-1, EN ISO 11357-2, EN ISO 11357-3"
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/en18065materialdata/MaterialIdentification/1/0"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"RequiredAtDQL",
                            value_type=xsd.PositiveInteger,
                            value=xsd.from_xsd(r"4", xsd.PositiveInteger),
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=global_ref(
                                r"https://admin-shell.io/SubmodelTemplates/en18065materialdata/RequiredAtDQL"
                            ),
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(
                self,
                fTIR: Optional[FTIR] = None,
                dSC: Optional[DSC] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(fTIR, dSC)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"PropertyCharacteristics",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Property characteristics"}),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/en18065materialdata/PropertyCharacteristics/1/0"
                ),
            }

        def __init__(
            self,
            viscosity: Optional[Viscosity] = None,
            ashContent: Optional[AshContent] = None,
            residualHumidity: Optional[ResidualHumidity] = None,
            density: Optional[Density] = None,
            bulkDensity: Optional[BulkDensity] = None,
            particleSizeDistribution: Optional[ParticleSizeDistribution] = None,
            tensileProperties: Optional[TensileProperties] = None,
            materialIdentification: Optional[MaterialIdentification] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                viscosity,
                ashContent,
                residualHumidity,
                density,
                bulkDensity,
                particleSizeDistribution,
                tensileProperties,
                materialIdentification,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"MaterialDataForEN18065ClassificationOfPlastics",
            "display_name": aas.MultiLanguageNameType(
                dict_={r"en": r"Material data for classification of plastics according to EN 18065"}
            ),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel template for material data enabling classification of plastics according to EN 18065"
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/IDTA02080-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/en18065materialdata/en18065MaterialData/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        dataQuality: Optional[DataQuality] = None,
        applicationSpecificStandards: Optional[
            Union[
                Iterable[Union[str, ApplicationSpecificStandards.Applicationspecificstandards_item]],
                ApplicationSpecificStandards,
            ]
        ] = None,
        informationCharacteristics: Optional[InformationCharacteristics] = None,
        propertyCharacteristics: Optional[PropertyCharacteristics] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(applicationSpecificStandards, str):
            raise TypeError("applicationSpecificStandards takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if applicationSpecificStandards is not None and not isinstance(
            applicationSpecificStandards, aas.SubmodelElement
        ):
            applicationSpecificStandards = self.ApplicationSpecificStandards(applicationSpecificStandards)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            dataQuality, applicationSpecificStandards, informationCharacteristics, propertyCharacteristics
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
