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


class SISDevice(aas.Submodel):

    class TagInformation(aas.SubmodelElementCollection):

        class TagName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TagName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"tag name"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TagName/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TagDescription(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TagDescription",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"tag description"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TagDescription/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Subsystem(aas.Property):

            ALLOWED_VALUES = (r"input element", r"logic solver", r"final element")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Subsystem",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"subsystem"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Subsystem/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"input element, logic solver, final element",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SafeStateOfDevice(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SafeStateOfDevice",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"safe state of device"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SafeStateOfDevice/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EquipmentType(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EquipmentType",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Equipment type"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/EquipmentType/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToTagGroup(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ReferenceToTagGroup",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to tag group"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToTagGroup/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"TagInformation",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"tag information"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"gives relevant information about the tag that the device represents"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TagInformation/1"),
            }

        def __init__(
            self,
            tagName: Union[str, TagName],
            subsystem: Union[str, Subsystem],
            tagDescription: Optional[Union[str, TagDescription]] = None,
            safeStateOfDevice: Optional[Union[str, SafeStateOfDevice]] = None,
            equipmentType: Optional[Union[str, EquipmentType]] = None,
            referenceToTagGroup: Optional[Iterable[Union[str, ReferenceToTagGroup]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                tagName = self.TagName(tagName)

            # Build a submodel element if a raw value was passed in the argument

            if tagDescription is not None and not isinstance(tagDescription, aas.SubmodelElement):
                tagDescription = self.TagDescription(tagDescription)

            # Build a submodel element if a raw value was passed in the argument

            if subsystem is not None and not isinstance(subsystem, aas.SubmodelElement):
                subsystem = self.Subsystem(subsystem)

            # Build a submodel element if a raw value was passed in the argument

            if safeStateOfDevice is not None and not isinstance(safeStateOfDevice, aas.SubmodelElement):
                safeStateOfDevice = self.SafeStateOfDevice(safeStateOfDevice)

            # Build a submodel element if a raw value was passed in the argument

            if equipmentType is not None and not isinstance(equipmentType, aas.SubmodelElement):
                equipmentType = self.EquipmentType(equipmentType)

            # A str would be split into its characters
            if isinstance(referenceToTagGroup, str):
                raise TypeError("referenceToTagGroup takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if referenceToTagGroup:
                referenceToTagGroup = [
                    i if isinstance(i, aas.SubmodelElement) else self.ReferenceToTagGroup(i)
                    for i in referenceToTagGroup
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                tagName, tagDescription, subsystem, safeStateOfDevice, equipmentType, referenceToTagGroup
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class SRSRequirements(aas.SubmodelElementCollection):

        class SystematicCapabilityRequirement(aas.Property):

            ALLOWED_VALUES = (r"SIL 1", r"SIL 2", r"SIL 3", r"SIL 4")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SystematicCapabilityRequirement",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"systematic capability requirement"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SystematicCapabilityRequirement/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"SIL 1, SIL 2, SIL 3, SIL 4",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PFDBudget(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PFDBudget",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PFD budget"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PFDBudget/1"),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PFHBudget(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PFHBudget",
                    "value_type": xsd.Float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PFH budget"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PFHBudget/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class InternalHFTRequirement(aas.Property):

            ALLOWED_VALUES = (r"0", r"1", r"2", r"3", r"4", r"5", r"6", r"7", r"8")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"InternalHFTRequirement",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"internal HFT requirement"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InternalHFTRequirement/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"0, 1, 2, 3, 4, 5, 6, 7, 8",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProofTest(aas.SubmodelElementCollection):

            class TestCoverage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestCoverage",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test coverage"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestCoverage/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"percentage",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MinimumTestIntervalOperatorSpecification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinimumTestIntervalOperatorSpecification",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"minimum test interval operator specification"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/MinimumTestIntervalOperatorSpecification/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"hours",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaximumTestIntervalForSILCompliance(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumTestIntervalForSILCompliance",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"maximum test interval for SIL compliance"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/MaximumTestIntervalForSILCompliance/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"hours",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestProcedure(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"TestProcedure",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test procedure"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestProcedure/1"),
                    }

                def __init__(
                    self,
                    value: str,
                    content_type: Optional[str] = r"application/octet-stream",
                    **kwargs: Unpack[FileMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class RequirementsForTesting(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"RequirementsForTesting",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"requirements for testing"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RequirementsForTesting/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailCriterion(aas.SubmodelElementCollection):

                class FailCriterionFailureMode(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"FailCriterionFailureMode",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"fail criterion failure mode"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailCriterionFailureMode/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BooleanFailCriterionDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BooleanFailCriterionDescription",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Boolean fail criterion description"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/BooleanFailCriterionDescription/1"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionDescriptionOfMeasurement(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionDescriptionOfMeasurement",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"numeric fail criterion description of measurement"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/NumericFailCriterionDescriptionOfMeasurement/1"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionValue",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"numeric fail criterion value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumericFailCriterionValue/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UnitOfMeasure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UnitOfMeasure",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"unit of measure"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about a measurement"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/UnitOfMeasure/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionOperator(aas.Property):

                    ALLOWED_VALUES = (r">", r">=", r"<", r"<=", r"=")

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionOperator",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"numeric fail criterion operator"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/NumericFailCriterionOperator/1"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"enumeration",
                                    value_type=str,
                                    value=r">, >=, <, <=, =",
                                    value_id=None,
                                    kind=aas.QualifierKind.VALUE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and value not in self.ALLOWED_VALUES:
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CommentsToFailCriterion(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CommentsToFailCriterion",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"comments to fail criterion"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/CommentsToFailCriterion/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"FailCriterion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"fail criterion"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailCriterion/1"),
                    }

                def __init__(
                    self,
                    failCriterionFailureMode: Union[str, FailCriterionFailureMode],
                    booleanFailCriterionDescription: Optional[Union[str, BooleanFailCriterionDescription]] = None,
                    numericFailCriterionDescriptionOfMeasurement: Optional[
                        Union[str, NumericFailCriterionDescriptionOfMeasurement]
                    ] = None,
                    numericFailCriterionValue: Optional[Union[xsd.Decimal, NumericFailCriterionValue]] = None,
                    unitOfMeasure: Optional[Union[str, UnitOfMeasure]] = None,
                    numericFailCriterionOperator: Optional[Union[str, NumericFailCriterionOperator]] = None,
                    commentsToFailCriterion: Optional[Iterable[Union[str, CommentsToFailCriterion]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if failCriterionFailureMode is not None and not isinstance(
                        failCriterionFailureMode, aas.SubmodelElement
                    ):
                        failCriterionFailureMode = self.FailCriterionFailureMode(failCriterionFailureMode)

                    # Build a submodel element if a raw value was passed in the argument

                    if booleanFailCriterionDescription is not None and not isinstance(
                        booleanFailCriterionDescription, aas.SubmodelElement
                    ):
                        booleanFailCriterionDescription = self.BooleanFailCriterionDescription(
                            booleanFailCriterionDescription
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionDescriptionOfMeasurement is not None and not isinstance(
                        numericFailCriterionDescriptionOfMeasurement, aas.SubmodelElement
                    ):
                        numericFailCriterionDescriptionOfMeasurement = (
                            self.NumericFailCriterionDescriptionOfMeasurement(
                                numericFailCriterionDescriptionOfMeasurement
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionValue is not None and not isinstance(
                        numericFailCriterionValue, aas.SubmodelElement
                    ):
                        numericFailCriterionValue = self.NumericFailCriterionValue(numericFailCriterionValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if unitOfMeasure is not None and not isinstance(unitOfMeasure, aas.SubmodelElement):
                        unitOfMeasure = self.UnitOfMeasure(unitOfMeasure)

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionOperator is not None and not isinstance(
                        numericFailCriterionOperator, aas.SubmodelElement
                    ):
                        numericFailCriterionOperator = self.NumericFailCriterionOperator(numericFailCriterionOperator)

                    # A str would be split into its characters
                    if isinstance(commentsToFailCriterion, str):
                        raise TypeError("commentsToFailCriterion takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if commentsToFailCriterion:
                        commentsToFailCriterion = [
                            i if isinstance(i, aas.SubmodelElement) else self.CommentsToFailCriterion(i)
                            for i in commentsToFailCriterion
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        failCriterionFailureMode,
                        booleanFailCriterionDescription,
                        numericFailCriterionDescriptionOfMeasurement,
                        numericFailCriterionValue,
                        unitOfMeasure,
                        numericFailCriterionOperator,
                        commentsToFailCriterion,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProofTest",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"proof test"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProofTest/1"),
                }

            def __init__(
                self,
                testCoverage: Union[xsd.Decimal, TestCoverage],
                minimumTestIntervalOperatorSpecification: Union[int, MinimumTestIntervalOperatorSpecification],
                maximumTestIntervalForSILCompliance: Union[int, MaximumTestIntervalForSILCompliance],
                failCriterion: Iterable[FailCriterion],
                testProcedure: Optional[Iterable[TestProcedure]] = None,
                requirementsForTesting: Optional[Iterable[Union[str, RequirementsForTesting]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if testCoverage is not None and not isinstance(testCoverage, aas.SubmodelElement):
                    testCoverage = self.TestCoverage(testCoverage)

                # Build a submodel element if a raw value was passed in the argument

                if minimumTestIntervalOperatorSpecification is not None and not isinstance(
                    minimumTestIntervalOperatorSpecification, aas.SubmodelElement
                ):
                    minimumTestIntervalOperatorSpecification = self.MinimumTestIntervalOperatorSpecification(
                        minimumTestIntervalOperatorSpecification
                    )

                # Build a submodel element if a raw value was passed in the argument

                if maximumTestIntervalForSILCompliance is not None and not isinstance(
                    maximumTestIntervalForSILCompliance, aas.SubmodelElement
                ):
                    maximumTestIntervalForSILCompliance = self.MaximumTestIntervalForSILCompliance(
                        maximumTestIntervalForSILCompliance
                    )

                # A str would be split into its characters
                if isinstance(testProcedure, str):
                    raise TypeError("testProcedure takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(requirementsForTesting, str):
                    raise TypeError("requirementsForTesting takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if requirementsForTesting:
                    requirementsForTesting = [
                        i if isinstance(i, aas.SubmodelElement) else self.RequirementsForTesting(i)
                        for i in requirementsForTesting
                    ]

                # A str would be split into its characters
                if isinstance(failCriterion, str):
                    raise TypeError("failCriterion takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    testCoverage,
                    minimumTestIntervalOperatorSpecification,
                    maximumTestIntervalForSILCompliance,
                    testProcedure,
                    requirementsForTesting,
                    failCriterion,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class PartialStrokeTest(aas.SubmodelElementCollection):

            class TestCoverage(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestCoverage",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test coverage"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestCoverage/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"percentage",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MinimumTestIntervalOperatorSpecification(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinimumTestIntervalOperatorSpecification",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"minimum test interval operator specification"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/MinimumTestIntervalOperatorSpecification/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"hours",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaximumTestIntervalForSILCompliance(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumTestIntervalForSILCompliance",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"maximum test interval for SIL compliance"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/MaximumTestIntervalForSILCompliance/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"hours",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestProcedure(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"TestProcedure",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test procedure"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestProcedure/1"),
                    }

                def __init__(
                    self,
                    value: str,
                    content_type: Optional[str] = r"application/octet-stream",
                    **kwargs: Unpack[FileMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class FailCriterion(aas.SubmodelElementCollection):

                class FailCriterionFailureMode(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"FailCriterionFailureMode",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"fail criterion failure mode"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailCriterionFailureMode/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class BooleanFailCriterionDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"BooleanFailCriterionDescription",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Boolean fail criterion description"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/BooleanFailCriterionDescription/1"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionDescriptionOfMeasurement(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionDescriptionOfMeasurement",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"numeric fail criterion description of measurement"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/NumericFailCriterionDescriptionOfMeasurement/1"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionValue",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"numeric fail criterion value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumericFailCriterionValue/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UnitOfMeasure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UnitOfMeasure",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"unit of measure"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about a measurement"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/UnitOfMeasure/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NumericFailCriterionComparison(aas.Property):

                    ALLOWED_VALUES = (r">", r">=", r"<", r"<=", r"=")

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NumericFailCriterionComparison",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"numeric fail criterion operator"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/SISDevice/NumericFailCriterionOperator/1/0"
                            ),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"enumeration",
                                    value_type=str,
                                    value=r">, >=, <, <=, =",
                                    value_id=None,
                                    kind=aas.QualifierKind.VALUE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and value not in self.ALLOWED_VALUES:
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CommentsToFailCriterion(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CommentsToFailCriterion",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"comments to fail criterion"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/CommentsToFailCriterion/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"FailCriterion",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"fail criterion"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailCriterion/1"),
                    }

                def __init__(
                    self,
                    failCriterionFailureMode: Union[str, FailCriterionFailureMode],
                    booleanFailCriterionDescription: Optional[Union[str, BooleanFailCriterionDescription]] = None,
                    numericFailCriterionDescriptionOfMeasurement: Optional[
                        Union[str, NumericFailCriterionDescriptionOfMeasurement]
                    ] = None,
                    numericFailCriterionValue: Optional[Union[xsd.Decimal, NumericFailCriterionValue]] = None,
                    unitOfMeasure: Optional[Union[str, UnitOfMeasure]] = None,
                    numericFailCriterionComparison: Optional[Union[str, NumericFailCriterionComparison]] = None,
                    commentsToFailCriterion: Optional[Iterable[Union[str, CommentsToFailCriterion]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if failCriterionFailureMode is not None and not isinstance(
                        failCriterionFailureMode, aas.SubmodelElement
                    ):
                        failCriterionFailureMode = self.FailCriterionFailureMode(failCriterionFailureMode)

                    # Build a submodel element if a raw value was passed in the argument

                    if booleanFailCriterionDescription is not None and not isinstance(
                        booleanFailCriterionDescription, aas.SubmodelElement
                    ):
                        booleanFailCriterionDescription = self.BooleanFailCriterionDescription(
                            booleanFailCriterionDescription
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionDescriptionOfMeasurement is not None and not isinstance(
                        numericFailCriterionDescriptionOfMeasurement, aas.SubmodelElement
                    ):
                        numericFailCriterionDescriptionOfMeasurement = (
                            self.NumericFailCriterionDescriptionOfMeasurement(
                                numericFailCriterionDescriptionOfMeasurement
                            )
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionValue is not None and not isinstance(
                        numericFailCriterionValue, aas.SubmodelElement
                    ):
                        numericFailCriterionValue = self.NumericFailCriterionValue(numericFailCriterionValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if unitOfMeasure is not None and not isinstance(unitOfMeasure, aas.SubmodelElement):
                        unitOfMeasure = self.UnitOfMeasure(unitOfMeasure)

                    # Build a submodel element if a raw value was passed in the argument

                    if numericFailCriterionComparison is not None and not isinstance(
                        numericFailCriterionComparison, aas.SubmodelElement
                    ):
                        numericFailCriterionComparison = self.NumericFailCriterionComparison(
                            numericFailCriterionComparison
                        )

                    # A str would be split into its characters
                    if isinstance(commentsToFailCriterion, str):
                        raise TypeError("commentsToFailCriterion takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if commentsToFailCriterion:
                        commentsToFailCriterion = [
                            i if isinstance(i, aas.SubmodelElement) else self.CommentsToFailCriterion(i)
                            for i in commentsToFailCriterion
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        failCriterionFailureMode,
                        booleanFailCriterionDescription,
                        numericFailCriterionDescriptionOfMeasurement,
                        numericFailCriterionValue,
                        unitOfMeasure,
                        numericFailCriterionComparison,
                        commentsToFailCriterion,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"PartialStrokeTest",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"partial stroke test"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PartialStrokeTest/1"),
                }

            def __init__(
                self,
                testCoverage: Union[xsd.Decimal, TestCoverage],
                minimumTestIntervalOperatorSpecification: Union[int, MinimumTestIntervalOperatorSpecification],
                maximumTestIntervalForSILCompliance: Union[int, MaximumTestIntervalForSILCompliance],
                failCriterion: Iterable[FailCriterion],
                testProcedure: Optional[Iterable[TestProcedure]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if testCoverage is not None and not isinstance(testCoverage, aas.SubmodelElement):
                    testCoverage = self.TestCoverage(testCoverage)

                # Build a submodel element if a raw value was passed in the argument

                if minimumTestIntervalOperatorSpecification is not None and not isinstance(
                    minimumTestIntervalOperatorSpecification, aas.SubmodelElement
                ):
                    minimumTestIntervalOperatorSpecification = self.MinimumTestIntervalOperatorSpecification(
                        minimumTestIntervalOperatorSpecification
                    )

                # Build a submodel element if a raw value was passed in the argument

                if maximumTestIntervalForSILCompliance is not None and not isinstance(
                    maximumTestIntervalForSILCompliance, aas.SubmodelElement
                ):
                    maximumTestIntervalForSILCompliance = self.MaximumTestIntervalForSILCompliance(
                        maximumTestIntervalForSILCompliance
                    )

                # A str would be split into its characters
                if isinstance(testProcedure, str):
                    raise TypeError("testProcedure takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(failCriterion, str):
                    raise TypeError("failCriterion takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    testCoverage,
                    minimumTestIntervalOperatorSpecification,
                    maximumTestIntervalForSILCompliance,
                    testProcedure,
                    failCriterion,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class MaximumAllowableSISDeviceResponseTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaximumAllowableSISDeviceResponseTime",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"maximum allowable SIS device response time"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/cds/MaximumAllowableSISDeviceResponseTime/1"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"seconds",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MinimumAllowableSISDeviceResponseTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MinimumAllowableSISDeviceResponseTime",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"minimum allowable SIS device response time"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/cds/MinimumAllowableSISDeviceResponseTime/1"
                    ),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"seconds",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaximumPermittedRepairTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaximumPermittedRepairTime",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maximum permitted repair time"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaximumPermittedRepairTime/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"seconds",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BypassRequirements(aas.SubmodelElementCollection):

            class MaximumAllowableBypassTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumAllowableBypassTime",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maximum allowable bypass time"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaximumAllowableBypassTime/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"seconds",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BypassAdministrativeControlIsRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BypassAdministrativeControlIsRequired",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"bypass administrative control is required"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/BypassAdministrativeControlIsRequired/1"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceToBypassGroup(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ReferenceToBypassGroup",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to bypass group"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToBypassGroup/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"BypassRequirements",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"bypass requirements"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/BypassRequirements/1"),
                }

            def __init__(
                self,
                maximumAllowableBypassTime: Union[xsd.Float, MaximumAllowableBypassTime],
                bypassAdministrativeControlIsRequired: Union[bool, BypassAdministrativeControlIsRequired],
                referenceToBypassGroup: Optional[Iterable[Union[str, ReferenceToBypassGroup]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if maximumAllowableBypassTime is not None and not isinstance(
                    maximumAllowableBypassTime, aas.SubmodelElement
                ):
                    maximumAllowableBypassTime = self.MaximumAllowableBypassTime(maximumAllowableBypassTime)

                # Build a submodel element if a raw value was passed in the argument

                if bypassAdministrativeControlIsRequired is not None and not isinstance(
                    bypassAdministrativeControlIsRequired, aas.SubmodelElement
                ):
                    bypassAdministrativeControlIsRequired = self.BypassAdministrativeControlIsRequired(
                        bypassAdministrativeControlIsRequired
                    )

                # A str would be split into its characters
                if isinstance(referenceToBypassGroup, str):
                    raise TypeError("referenceToBypassGroup takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if referenceToBypassGroup:
                    referenceToBypassGroup = [
                        i if isinstance(i, aas.SubmodelElement) else self.ReferenceToBypassGroup(i)
                        for i in referenceToBypassGroup
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    maximumAllowableBypassTime, bypassAdministrativeControlIsRequired, referenceToBypassGroup
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TripEnergyMode(aas.Property):

            ALLOWED_VALUES = (r"energized", r"de-energized")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TripEnergyMode",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"trip energy mode"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripEnergyMode/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"energized, de-energized",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RequirementIfEnergizedToTrip(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RequirementIfEnergizedToTrip",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"requirement if energized to trip"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RequirementIfEnergizedToTrip/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TripAction(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TripAction",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"trip action"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripAction/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SurvivabilityRequirement(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SurvivabilityRequirement",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"survivability requirement"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SurvivabilityRequirement/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DiagnosticRequired(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DiagnosticRequired",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostic required"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DiagnosticRequired/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AdditionalDiagnosticRequirementForImplementation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AdditionalDiagnosticRequirementForImplementation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"additional diagnostic requirement for implementation"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/cds/AdditionalDiagnosticRequirementForImplementation/1"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TimeDelayOfAction(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TimeDelayOfAction",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time delay of action"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TimeDelayOfAction/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"seconds",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EnvironmentalExtremes(aas.SubmodelElementCollection):

            class MinimumAllowableTemperature(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinimumAllowableTemperature",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"minimum allowable temperature"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MinimumAllowableTemperature/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"degrees Celcius",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaximumAllowableTemperature(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumAllowableTemperature",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maximum allowable temperature"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaximumAllowableTemperature/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"degrees Celcius",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MinimumAllowableHumidity(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MinimumAllowableHumidity",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"minimum allowable humidity"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MinimumAllowableHumidity/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"percentage",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaximumAllowableHumidity(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumAllowableHumidity",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maximum allowable humidity"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaximumAllowableHumidity/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"percentage",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContaminantRequirement(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ContaminantRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"contaminant requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ContaminantRequirement/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class GroundingRequirement(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"GroundingRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"grounding requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/GroundingRequirement/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MaximumElectromagneticInterference(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumElectromagneticInterference",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Maximum electromagnetic interference"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/MaximumElectromagneticInterference/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"dBµV/m",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ShockResistance(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ShockResistance",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"mechanical shock resistance"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ShockResistance/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class VibrationResistance(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"VibrationResistance",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"vibration restistance"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/VibrationResistance/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ElectrostaticDischargeProtection(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ElectrostaticDischargeProtection",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"protection against static discharge"}
                        ),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/ElectrostaticDischargeProtection/1"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ATEXZone(aas.Property):

                ALLOWED_VALUES = (r"Zone 0", r"Zone 1", r"Zone 2", r"Zone 20", r"Zone 21", r"Zone 22")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ATEXZone",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"ATEX zone"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ATEXZone/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"Zone 0, Zone 1, Zone 2, Zone 20, Zone 21, Zone 22",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class GasGroup(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"GasGroup",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"gas group/explosion group"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/GasGroup/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TemperatureClass(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TemperatureClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"temperature class"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TemperatureClass/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FloodingRequirement(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FloodingRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"flooding requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FloodingRequirement/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LightningExposureRequirement(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LightningExposureRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lightning exposure requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LightningExposureRequirement/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OtherEnvironmentalRequirement(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OtherEnvironmentalRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"other environmental requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/OtherEnvironmentalRequirement/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"EnvironmentalExtremes",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Limiting environmental conditions"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"environmental extreme value"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/EnvironmentalExtremes/1"),
                }

            def __init__(
                self,
                minimumAllowableTemperature: Optional[Union[int, MinimumAllowableTemperature]] = None,
                maximumAllowableTemperature: Optional[Union[int, MaximumAllowableTemperature]] = None,
                minimumAllowableHumidity: Optional[Union[int, MinimumAllowableHumidity]] = None,
                maximumAllowableHumidity: Optional[Union[int, MaximumAllowableHumidity]] = None,
                contaminantRequirement: Optional[Iterable[Union[str, ContaminantRequirement]]] = None,
                groundingRequirement: Optional[Iterable[Union[str, GroundingRequirement]]] = None,
                maximumElectromagneticInterference: Optional[
                    Union[xsd.Decimal, MaximumElectromagneticInterference]
                ] = None,
                shockResistance: Optional[Union[str, ShockResistance]] = None,
                vibrationResistance: Optional[Union[str, VibrationResistance]] = None,
                electrostaticDischargeProtection: Optional[
                    Iterable[Union[str, ElectrostaticDischargeProtection]]
                ] = None,
                aTEXZone: Optional[Union[str, ATEXZone]] = None,
                gasGroup: Optional[Union[str, GasGroup]] = None,
                temperatureClass: Optional[Union[str, TemperatureClass]] = None,
                floodingRequirement: Optional[Iterable[Union[str, FloodingRequirement]]] = None,
                lightningExposureRequirement: Optional[Iterable[Union[str, LightningExposureRequirement]]] = None,
                otherEnvironmentalRequirement: Optional[Iterable[Union[str, OtherEnvironmentalRequirement]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if minimumAllowableTemperature is not None and not isinstance(
                    minimumAllowableTemperature, aas.SubmodelElement
                ):
                    minimumAllowableTemperature = self.MinimumAllowableTemperature(minimumAllowableTemperature)

                # Build a submodel element if a raw value was passed in the argument

                if maximumAllowableTemperature is not None and not isinstance(
                    maximumAllowableTemperature, aas.SubmodelElement
                ):
                    maximumAllowableTemperature = self.MaximumAllowableTemperature(maximumAllowableTemperature)

                # Build a submodel element if a raw value was passed in the argument

                if minimumAllowableHumidity is not None and not isinstance(
                    minimumAllowableHumidity, aas.SubmodelElement
                ):
                    minimumAllowableHumidity = self.MinimumAllowableHumidity(minimumAllowableHumidity)

                # Build a submodel element if a raw value was passed in the argument

                if maximumAllowableHumidity is not None and not isinstance(
                    maximumAllowableHumidity, aas.SubmodelElement
                ):
                    maximumAllowableHumidity = self.MaximumAllowableHumidity(maximumAllowableHumidity)

                # A str would be split into its characters
                if isinstance(contaminantRequirement, str):
                    raise TypeError("contaminantRequirement takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if contaminantRequirement:
                    contaminantRequirement = [
                        i if isinstance(i, aas.SubmodelElement) else self.ContaminantRequirement(i)
                        for i in contaminantRequirement
                    ]

                # A str would be split into its characters
                if isinstance(groundingRequirement, str):
                    raise TypeError("groundingRequirement takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if groundingRequirement:
                    groundingRequirement = [
                        i if isinstance(i, aas.SubmodelElement) else self.GroundingRequirement(i)
                        for i in groundingRequirement
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if maximumElectromagneticInterference is not None and not isinstance(
                    maximumElectromagneticInterference, aas.SubmodelElement
                ):
                    maximumElectromagneticInterference = self.MaximumElectromagneticInterference(
                        maximumElectromagneticInterference
                    )

                # Build a submodel element if a raw value was passed in the argument

                if shockResistance is not None and not isinstance(shockResistance, aas.SubmodelElement):
                    shockResistance = self.ShockResistance(shockResistance)

                # Build a submodel element if a raw value was passed in the argument

                if vibrationResistance is not None and not isinstance(vibrationResistance, aas.SubmodelElement):
                    vibrationResistance = self.VibrationResistance(vibrationResistance)

                # A str would be split into its characters
                if isinstance(electrostaticDischargeProtection, str):
                    raise TypeError("electrostaticDischargeProtection takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if electrostaticDischargeProtection:
                    electrostaticDischargeProtection = [
                        i if isinstance(i, aas.SubmodelElement) else self.ElectrostaticDischargeProtection(i)
                        for i in electrostaticDischargeProtection
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if aTEXZone is not None and not isinstance(aTEXZone, aas.SubmodelElement):
                    aTEXZone = self.ATEXZone(aTEXZone)

                # Build a submodel element if a raw value was passed in the argument

                if gasGroup is not None and not isinstance(gasGroup, aas.SubmodelElement):
                    gasGroup = self.GasGroup(gasGroup)

                # Build a submodel element if a raw value was passed in the argument

                if temperatureClass is not None and not isinstance(temperatureClass, aas.SubmodelElement):
                    temperatureClass = self.TemperatureClass(temperatureClass)

                # A str would be split into its characters
                if isinstance(floodingRequirement, str):
                    raise TypeError("floodingRequirement takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if floodingRequirement:
                    floodingRequirement = [
                        i if isinstance(i, aas.SubmodelElement) else self.FloodingRequirement(i)
                        for i in floodingRequirement
                    ]

                # A str would be split into its characters
                if isinstance(lightningExposureRequirement, str):
                    raise TypeError("lightningExposureRequirement takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if lightningExposureRequirement:
                    lightningExposureRequirement = [
                        i if isinstance(i, aas.SubmodelElement) else self.LightningExposureRequirement(i)
                        for i in lightningExposureRequirement
                    ]

                # A str would be split into its characters
                if isinstance(otherEnvironmentalRequirement, str):
                    raise TypeError("otherEnvironmentalRequirement takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if otherEnvironmentalRequirement:
                    otherEnvironmentalRequirement = [
                        i if isinstance(i, aas.SubmodelElement) else self.OtherEnvironmentalRequirement(i)
                        for i in otherEnvironmentalRequirement
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    minimumAllowableTemperature,
                    maximumAllowableTemperature,
                    minimumAllowableHumidity,
                    maximumAllowableHumidity,
                    contaminantRequirement,
                    groundingRequirement,
                    maximumElectromagneticInterference,
                    shockResistance,
                    vibrationResistance,
                    electrostaticDischargeProtection,
                    aTEXZone,
                    gasGroup,
                    temperatureClass,
                    floodingRequirement,
                    lightningExposureRequirement,
                    otherEnvironmentalRequirement,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FailureModeResponses(aas.SubmodelElementCollection):

            class FailureModeAbbreviation(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureModeAbbreviation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure mode abbreviation"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureModeAbbreviation/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureModeName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureModeName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure mode name"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureModeName/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SafeAutomaticResponse(aas.SubmodelElementCollection):

                class FailurePhilosophy(aas.Property):

                    ALLOWED_VALUES = (r"fail-safe", r"fail as-is")

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"FailurePhilosophy",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure philosophy"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailurePhilosophy/1"),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"enumeration",
                                    value_type=str,
                                    value=r"fail-safe, fail as-is",
                                    value_id=None,
                                    kind=aas.QualifierKind.VALUE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and value not in self.ALLOWED_VALUES:
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReferenceToAlarm(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ReferenceToAlarm",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to alarm"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToAlarm/1"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SafeAutomaticResponse",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"safe automatic response"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SafeAutomaticResponse/1"),
                    }

                def __init__(
                    self,
                    failurePhilosophy: Union[str, FailurePhilosophy],
                    referenceToAlarm: Optional[Iterable[Union[aas.Reference, ReferenceToAlarm]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if failurePhilosophy is not None and not isinstance(failurePhilosophy, aas.SubmodelElement):
                        failurePhilosophy = self.FailurePhilosophy(failurePhilosophy)

                    # A str would be split into its characters
                    if isinstance(referenceToAlarm, str):
                        raise TypeError("referenceToAlarm takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if referenceToAlarm:
                        referenceToAlarm = [
                            i if isinstance(i, aas.SubmodelElement) else self.ReferenceToAlarm(i)
                            for i in referenceToAlarm
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(failurePhilosophy, referenceToAlarm)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ManualResponse(aas.SubmodelElementCollection):

                class ManualResponseActionDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ManualResponseActionDescription",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"manual response action description"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/cds/ManualResponseActionDescription/1"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Document(aas.File):

                    @staticmethod
                    def template_defaults() -> FileMetadata:
                        return {
                            "id_short": r"Document",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"URL of document"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about relevant document(s)"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Document/1"),
                        }

                    def __init__(
                        self,
                        value: str,
                        content_type: Optional[str] = r"application/octet-stream",
                        **kwargs: Unpack[FileMetadata],
                    ):

                        super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ManualResponse",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"manual response"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ManualResponse/1"),
                    }

                def __init__(
                    self,
                    manualResponseActionDescription: Union[str, ManualResponseActionDescription],
                    document: Optional[Iterable[Document]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if manualResponseActionDescription is not None and not isinstance(
                        manualResponseActionDescription, aas.SubmodelElement
                    ):
                        manualResponseActionDescription = self.ManualResponseActionDescription(
                            manualResponseActionDescription
                        )

                    # A str would be split into its characters
                    if isinstance(document, str):
                        raise TypeError("document takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(manualResponseActionDescription, document)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FailureModeResponses",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure mode responses"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureModeResponses/1"),
                }

            def __init__(
                self,
                failureModeAbbreviation: Union[str, FailureModeAbbreviation],
                failureModeName: Union[str, FailureModeName],
                safeAutomaticResponse: Optional[SafeAutomaticResponse] = None,
                manualResponse: Optional[ManualResponse] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if failureModeAbbreviation is not None and not isinstance(failureModeAbbreviation, aas.SubmodelElement):
                    failureModeAbbreviation = self.FailureModeAbbreviation(failureModeAbbreviation)

                # Build a submodel element if a raw value was passed in the argument

                if failureModeName is not None and not isinstance(failureModeName, aas.SubmodelElement):
                    failureModeName = self.FailureModeName(failureModeName)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    failureModeAbbreviation, failureModeName, safeAutomaticResponse, manualResponse
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InputDevice(aas.SubmodelElementCollection):

            class ProcessMeasurement(aas.SubmodelElementCollection):

                class UnitOfMeasure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UnitOfMeasure",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"unit of measure for trip point"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about the device diagnostics"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/UnitOfMeasure/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RangeMin(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"RangeMin",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"lower range-limit of other variable"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RangeMin/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RangeMax(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"RangeMax",
                            "value_type": xsd.NonNegativeInteger,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"upper range-limit of other variable"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RangeMax/1"),
                        }

                    def __init__(self, value: xsd.NonNegativeInteger, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Accuracy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Accuracy",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"accuracy expressed as percentage"}
                            ),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Accuracy/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SubstistuteValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SubstistuteValue",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"substitute value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/SISDevice/SubstituteValue/1/0"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ProcessMeasurement",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"process measurement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProcessMeasurement/1"),
                    }

                def __init__(
                    self,
                    unitOfMeasure: Union[str, UnitOfMeasure],
                    rangeMin: Union[xsd.Decimal, RangeMin],
                    rangeMax: Union[xsd.NonNegativeInteger, RangeMax],
                    accuracy: Union[xsd.Decimal, Accuracy],
                    substistuteValue: Union[xsd.Decimal, SubstistuteValue],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if unitOfMeasure is not None and not isinstance(unitOfMeasure, aas.SubmodelElement):
                        unitOfMeasure = self.UnitOfMeasure(unitOfMeasure)

                    # Build a submodel element if a raw value was passed in the argument

                    if rangeMin is not None and not isinstance(rangeMin, aas.SubmodelElement):
                        rangeMin = self.RangeMin(rangeMin)

                    # Build a submodel element if a raw value was passed in the argument

                    if rangeMax is not None and not isinstance(rangeMax, aas.SubmodelElement):
                        rangeMax = self.RangeMax(rangeMax)

                    # Build a submodel element if a raw value was passed in the argument

                    if accuracy is not None and not isinstance(accuracy, aas.SubmodelElement):
                        accuracy = self.Accuracy(accuracy)

                    # Build a submodel element if a raw value was passed in the argument

                    if substistuteValue is not None and not isinstance(substistuteValue, aas.SubmodelElement):
                        substistuteValue = self.SubstistuteValue(substistuteValue)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        unitOfMeasure, rangeMin, rangeMax, accuracy, substistuteValue
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TripPoint(aas.SubmodelElementCollection):

                class TripPointName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TripPointName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"designation of trip point"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about the device diagnostics"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripPointName/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TripPointValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TripPointValue",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"value of trip point"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about the device diagnostics"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripPointValue/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class HysteresisOfTripPoint(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"HysteresisOfTripPoint",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hysteresis of trip value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"gives information about the device diagnostics"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/HysteresisOfTripPoint/1"),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"unit",
                                    value_type=str,
                                    value=r"percentage",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TripDeadTime(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TripDeadTime",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"trip dead time"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripDeadTime/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReferenceToAlarm(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ReferenceToAlarm",
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to alarm"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToAlarm/1"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"TripPoint",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Trip point"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the device diagnostics"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TripPoint/1"),
                    }

                def __init__(
                    self,
                    tripPointName: Union[str, TripPointName],
                    tripPointValue: Union[xsd.Decimal, TripPointValue],
                    hysteresisOfTripPoint: Optional[Union[xsd.Decimal, HysteresisOfTripPoint]] = None,
                    tripDeadTime: Optional[Union[xsd.Decimal, TripDeadTime]] = None,
                    referenceToAlarm: Optional[Union[aas.Reference, ReferenceToAlarm]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if tripPointName is not None and not isinstance(tripPointName, aas.SubmodelElement):
                        tripPointName = self.TripPointName(tripPointName)

                    # Build a submodel element if a raw value was passed in the argument

                    if tripPointValue is not None and not isinstance(tripPointValue, aas.SubmodelElement):
                        tripPointValue = self.TripPointValue(tripPointValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if hysteresisOfTripPoint is not None and not isinstance(hysteresisOfTripPoint, aas.SubmodelElement):
                        hysteresisOfTripPoint = self.HysteresisOfTripPoint(hysteresisOfTripPoint)

                    # Build a submodel element if a raw value was passed in the argument

                    if tripDeadTime is not None and not isinstance(tripDeadTime, aas.SubmodelElement):
                        tripDeadTime = self.TripDeadTime(tripDeadTime)

                    # Build a submodel element if a raw value was passed in the argument

                    if referenceToAlarm is not None and not isinstance(referenceToAlarm, aas.SubmodelElement):
                        referenceToAlarm = self.ReferenceToAlarm(referenceToAlarm)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        tripPointName, tripPointValue, hysteresisOfTripPoint, tripDeadTime, referenceToAlarm
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class DiagnosticAlarm(aas.SubmodelElementCollection):

                class AlarmName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AlarmName",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm name"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmName/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AlarmValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AlarmValue",
                            "value_type": xsd.Decimal,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm value"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmValue/1"),
                        }

                    def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AlarmType(aas.Property):

                    ALLOWED_VALUES = (
                        r"analogue low",
                        r"analogue low low",
                        r"analogue high",
                        r"analogue high high",
                        r"digital high",
                        r"level to level",
                        r"other",
                    )

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AlarmType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm type"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmType/1"),
                            "qualifier": (
                                aas.Qualifier(
                                    type_=r"enumeration",
                                    value_type=str,
                                    value=r"analogue low, analogue low low, analogue high, analogue high high, digital high, level to level, other",
                                    value_id=None,
                                    kind=aas.QualifierKind.VALUE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        if value is not None and value not in self.ALLOWED_VALUES:
                            raise ValueError(
                                f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                            )

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OtherAlarmType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"OtherAlarmType",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"other alarm type"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/OtherAlarmType/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AlarmMessage(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AlarmMessage",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm message"}),
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmMessage/1"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"DiagnosticAlarm",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostic alarm"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DiagnosticAlarm/1"),
                    }

                def __init__(
                    self,
                    alarmName: Union[str, AlarmName],
                    alarmValue: Union[xsd.Decimal, AlarmValue],
                    alarmType: Optional[Iterable[Union[str, AlarmType]]] = None,
                    otherAlarmType: Optional[Iterable[Union[str, OtherAlarmType]]] = None,
                    alarmMessage: Optional[Union[str, AlarmMessage]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if alarmName is not None and not isinstance(alarmName, aas.SubmodelElement):
                        alarmName = self.AlarmName(alarmName)

                    # Build a submodel element if a raw value was passed in the argument

                    if alarmValue is not None and not isinstance(alarmValue, aas.SubmodelElement):
                        alarmValue = self.AlarmValue(alarmValue)

                    # A str would be split into its characters
                    if isinstance(alarmType, str):
                        raise TypeError("alarmType takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if alarmType:
                        alarmType = [i if isinstance(i, aas.SubmodelElement) else self.AlarmType(i) for i in alarmType]

                    # A str would be split into its characters
                    if isinstance(otherAlarmType, str):
                        raise TypeError("otherAlarmType takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if otherAlarmType:
                        otherAlarmType = [
                            i if isinstance(i, aas.SubmodelElement) else self.OtherAlarmType(i) for i in otherAlarmType
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if alarmMessage is not None and not isinstance(alarmMessage, aas.SubmodelElement):
                        alarmMessage = self.AlarmMessage(alarmMessage)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        alarmName, alarmValue, alarmType, otherAlarmType, alarmMessage
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class AlarmResetAfterShutdownIsRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlarmResetAfterShutdownIsRequired",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"alarm reset after shutdown is required"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/AlarmResetAfterShutdownIsRequired/1"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasurementComparisonIsRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MeasurementComparisonIsRequired",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"measurement comparison is required"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MeasurementComparisonIsRequired/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InputDevice",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"input device"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the input device subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InputDevice/1"),
                }

            def __init__(
                self,
                processMeasurement: Optional[ProcessMeasurement] = None,
                tripPoint: Optional[Iterable[TripPoint]] = None,
                diagnosticAlarm: Optional[Iterable[DiagnosticAlarm]] = None,
                alarmResetAfterShutdownIsRequired: Optional[Union[bool, AlarmResetAfterShutdownIsRequired]] = None,
                measurementComparisonIsRequired: Optional[Union[bool, MeasurementComparisonIsRequired]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(tripPoint, str):
                    raise TypeError("tripPoint takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(diagnosticAlarm, str):
                    raise TypeError("diagnosticAlarm takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if alarmResetAfterShutdownIsRequired is not None and not isinstance(
                    alarmResetAfterShutdownIsRequired, aas.SubmodelElement
                ):
                    alarmResetAfterShutdownIsRequired = self.AlarmResetAfterShutdownIsRequired(
                        alarmResetAfterShutdownIsRequired
                    )

                # Build a submodel element if a raw value was passed in the argument

                if measurementComparisonIsRequired is not None and not isinstance(
                    measurementComparisonIsRequired, aas.SubmodelElement
                ):
                    measurementComparisonIsRequired = self.MeasurementComparisonIsRequired(
                        measurementComparisonIsRequired
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    processMeasurement,
                    tripPoint,
                    diagnosticAlarm,
                    alarmResetAfterShutdownIsRequired,
                    measurementComparisonIsRequired,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LogicSolver(aas.SubmodelElementCollection):

            class LogicSolverResetAfterShutdownIsRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"LogicSolverResetAfterShutdownIsRequired",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"logic solver reset after shutdown is required"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/LogicSolverResetAfterShutdownIsRequired/1"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"LogicSolver",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"logic solver"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the logic solver subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LogicSolver/1"),
                }

            def __init__(
                self,
                logicSolverResetAfterShutdownIsRequired: Optional[
                    Union[bool, LogicSolverResetAfterShutdownIsRequired]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if logicSolverResetAfterShutdownIsRequired is not None and not isinstance(
                    logicSolverResetAfterShutdownIsRequired, aas.SubmodelElement
                ):
                    logicSolverResetAfterShutdownIsRequired = self.LogicSolverResetAfterShutdownIsRequired(
                        logicSolverResetAfterShutdownIsRequired
                    )

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(logicSolverResetAfterShutdownIsRequired)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FinalElement(aas.SubmodelElementCollection):

            class MaximumAllowableLeakageRate(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MaximumAllowableLeakageRate",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maximum allowable leakage rate"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaximumAllowableLeakageRate/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"kg/s",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TightShutOffIsRequired(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TightShutOffIsRequired",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"tight shutoff is required"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TightShutoffIsRequired/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ManualOperationIsPossible(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ManualOperationIsPossible",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"manual operation is possible"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ManualOperationIsPossible/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ResetAfterShutdownRequirement(aas.Property):

                ALLOWED_VALUES = (r"reset in logic solver", r"reset in field")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ResetAfterShutdownRequirement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reset after shutdown requirement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ResetAfterShutdownRequirement/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"reset in logic solver, reset in field",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FinalElementFunction(aas.Property):

                ALLOWED_VALUES = (
                    r"start/open/connect/activate",
                    r"stop/close/disconnect/deactivate",
                    r"level to level",
                    r"other",
                )

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FinalElementFunction",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"final element function"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives input to the description of the SIS device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FinalElementFunction/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"start/open/connect/activate, stop/close/disconnect/deactivate, level to level, other",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FinalElement",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"final element"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the final element subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FinalElement/1"),
                }

            def __init__(
                self,
                manualOperationIsPossible: Union[bool, ManualOperationIsPossible],
                maximumAllowableLeakageRate: Optional[Union[str, MaximumAllowableLeakageRate]] = None,
                tightShutOffIsRequired: Optional[Union[bool, TightShutOffIsRequired]] = None,
                resetAfterShutdownRequirement: Optional[Union[str, ResetAfterShutdownRequirement]] = None,
                finalElementFunction: Optional[Union[str, FinalElementFunction]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if maximumAllowableLeakageRate is not None and not isinstance(
                    maximumAllowableLeakageRate, aas.SubmodelElement
                ):
                    maximumAllowableLeakageRate = self.MaximumAllowableLeakageRate(maximumAllowableLeakageRate)

                # Build a submodel element if a raw value was passed in the argument

                if tightShutOffIsRequired is not None and not isinstance(tightShutOffIsRequired, aas.SubmodelElement):
                    tightShutOffIsRequired = self.TightShutOffIsRequired(tightShutOffIsRequired)

                # Build a submodel element if a raw value was passed in the argument

                if manualOperationIsPossible is not None and not isinstance(
                    manualOperationIsPossible, aas.SubmodelElement
                ):
                    manualOperationIsPossible = self.ManualOperationIsPossible(manualOperationIsPossible)

                # Build a submodel element if a raw value was passed in the argument

                if resetAfterShutdownRequirement is not None and not isinstance(
                    resetAfterShutdownRequirement, aas.SubmodelElement
                ):
                    resetAfterShutdownRequirement = self.ResetAfterShutdownRequirement(resetAfterShutdownRequirement)

                # Build a submodel element if a raw value was passed in the argument

                if finalElementFunction is not None and not isinstance(finalElementFunction, aas.SubmodelElement):
                    finalElementFunction = self.FinalElementFunction(finalElementFunction)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    maximumAllowableLeakageRate,
                    tightShutOffIsRequired,
                    manualOperationIsPossible,
                    resetAfterShutdownRequirement,
                    finalElementFunction,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SharedUseIsAllowed(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SharedUseIsAllowed",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"shared use is allowed"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SharedUseIsAllowed/1"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToSIF(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ReferenceToSIF",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to SIF"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToSIF/1"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class UsefulLife(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"UsefulLife",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"useful life"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/UsefulLife/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"SRSRequirements",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"SRS requirements"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SRSRequirements/1"),
            }

        def __init__(
            self,
            systematicCapabilityRequirement: Union[str, SystematicCapabilityRequirement],
            proofTest: ProofTest,
            maximumAllowableSISDeviceResponseTime: Union[xsd.Decimal, MaximumAllowableSISDeviceResponseTime],
            maximumPermittedRepairTime: Union[xsd.Decimal, MaximumPermittedRepairTime],
            bypassRequirements: BypassRequirements,
            tripEnergyMode: Union[str, TripEnergyMode],
            tripAction: Union[str, TripAction],
            sharedUseIsAllowed: Union[bool, SharedUseIsAllowed],
            referenceToSIF: Union[aas.Reference, ReferenceToSIF],
            pFDBudget: Optional[Union[xsd.Float, PFDBudget]] = None,
            pFHBudget: Optional[Union[xsd.Float, PFHBudget]] = None,
            internalHFTRequirement: Optional[Union[str, InternalHFTRequirement]] = None,
            partialStrokeTest: Optional[PartialStrokeTest] = None,
            minimumAllowableSISDeviceResponseTime: Optional[
                Union[xsd.Decimal, MinimumAllowableSISDeviceResponseTime]
            ] = None,
            requirementIfEnergizedToTrip: Optional[Iterable[Union[str, RequirementIfEnergizedToTrip]]] = None,
            survivabilityRequirement: Optional[Iterable[Union[str, SurvivabilityRequirement]]] = None,
            diagnosticRequired: Optional[Iterable[Union[str, DiagnosticRequired]]] = None,
            additionalDiagnosticRequirementForImplementation: Optional[
                Iterable[Union[str, AdditionalDiagnosticRequirementForImplementation]]
            ] = None,
            timeDelayOfAction: Optional[Iterable[Union[xsd.Decimal, TimeDelayOfAction]]] = None,
            environmentalExtremes: Optional[EnvironmentalExtremes] = None,
            failureModeResponses: Optional[Iterable[FailureModeResponses]] = None,
            inputDevice: Optional[InputDevice] = None,
            logicSolver: Optional[LogicSolver] = None,
            finalElement: Optional[FinalElement] = None,
            usefulLife: Optional[Union[str, UsefulLife]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if systematicCapabilityRequirement is not None and not isinstance(
                systematicCapabilityRequirement, aas.SubmodelElement
            ):
                systematicCapabilityRequirement = self.SystematicCapabilityRequirement(systematicCapabilityRequirement)

            # Build a submodel element if a raw value was passed in the argument

            if pFDBudget is not None and not isinstance(pFDBudget, aas.SubmodelElement):
                pFDBudget = self.PFDBudget(pFDBudget)

            # Build a submodel element if a raw value was passed in the argument

            if pFHBudget is not None and not isinstance(pFHBudget, aas.SubmodelElement):
                pFHBudget = self.PFHBudget(pFHBudget)

            # Build a submodel element if a raw value was passed in the argument

            if internalHFTRequirement is not None and not isinstance(internalHFTRequirement, aas.SubmodelElement):
                internalHFTRequirement = self.InternalHFTRequirement(internalHFTRequirement)

            # Build a submodel element if a raw value was passed in the argument

            if maximumAllowableSISDeviceResponseTime is not None and not isinstance(
                maximumAllowableSISDeviceResponseTime, aas.SubmodelElement
            ):
                maximumAllowableSISDeviceResponseTime = self.MaximumAllowableSISDeviceResponseTime(
                    maximumAllowableSISDeviceResponseTime
                )

            # Build a submodel element if a raw value was passed in the argument

            if minimumAllowableSISDeviceResponseTime is not None and not isinstance(
                minimumAllowableSISDeviceResponseTime, aas.SubmodelElement
            ):
                minimumAllowableSISDeviceResponseTime = self.MinimumAllowableSISDeviceResponseTime(
                    minimumAllowableSISDeviceResponseTime
                )

            # Build a submodel element if a raw value was passed in the argument

            if maximumPermittedRepairTime is not None and not isinstance(
                maximumPermittedRepairTime, aas.SubmodelElement
            ):
                maximumPermittedRepairTime = self.MaximumPermittedRepairTime(maximumPermittedRepairTime)

            # Build a submodel element if a raw value was passed in the argument

            if tripEnergyMode is not None and not isinstance(tripEnergyMode, aas.SubmodelElement):
                tripEnergyMode = self.TripEnergyMode(tripEnergyMode)

            # A str would be split into its characters
            if isinstance(requirementIfEnergizedToTrip, str):
                raise TypeError("requirementIfEnergizedToTrip takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if requirementIfEnergizedToTrip:
                requirementIfEnergizedToTrip = [
                    i if isinstance(i, aas.SubmodelElement) else self.RequirementIfEnergizedToTrip(i)
                    for i in requirementIfEnergizedToTrip
                ]

            # Build a submodel element if a raw value was passed in the argument

            if tripAction is not None and not isinstance(tripAction, aas.SubmodelElement):
                tripAction = self.TripAction(tripAction)

            # A str would be split into its characters
            if isinstance(survivabilityRequirement, str):
                raise TypeError("survivabilityRequirement takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if survivabilityRequirement:
                survivabilityRequirement = [
                    i if isinstance(i, aas.SubmodelElement) else self.SurvivabilityRequirement(i)
                    for i in survivabilityRequirement
                ]

            # A str would be split into its characters
            if isinstance(diagnosticRequired, str):
                raise TypeError("diagnosticRequired takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if diagnosticRequired:
                diagnosticRequired = [
                    i if isinstance(i, aas.SubmodelElement) else self.DiagnosticRequired(i) for i in diagnosticRequired
                ]

            # A str would be split into its characters
            if isinstance(additionalDiagnosticRequirementForImplementation, str):
                raise TypeError("additionalDiagnosticRequirementForImplementation takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if additionalDiagnosticRequirementForImplementation:
                additionalDiagnosticRequirementForImplementation = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.AdditionalDiagnosticRequirementForImplementation(i)
                    )
                    for i in additionalDiagnosticRequirementForImplementation
                ]

            # A str would be split into its characters
            if isinstance(timeDelayOfAction, str):
                raise TypeError("timeDelayOfAction takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if timeDelayOfAction:
                timeDelayOfAction = [
                    i if isinstance(i, aas.SubmodelElement) else self.TimeDelayOfAction(i) for i in timeDelayOfAction
                ]

            # A str would be split into its characters
            if isinstance(failureModeResponses, str):
                raise TypeError("failureModeResponses takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if sharedUseIsAllowed is not None and not isinstance(sharedUseIsAllowed, aas.SubmodelElement):
                sharedUseIsAllowed = self.SharedUseIsAllowed(sharedUseIsAllowed)

            # Build a submodel element if a raw value was passed in the argument

            if referenceToSIF is not None and not isinstance(referenceToSIF, aas.SubmodelElement):
                referenceToSIF = self.ReferenceToSIF(referenceToSIF)

            # Build a submodel element if a raw value was passed in the argument

            if usefulLife is not None and not isinstance(usefulLife, aas.SubmodelElement):
                usefulLife = self.UsefulLife(usefulLife)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                systematicCapabilityRequirement,
                pFDBudget,
                pFHBudget,
                internalHFTRequirement,
                proofTest,
                partialStrokeTest,
                maximumAllowableSISDeviceResponseTime,
                minimumAllowableSISDeviceResponseTime,
                maximumPermittedRepairTime,
                bypassRequirements,
                tripEnergyMode,
                requirementIfEnergizedToTrip,
                tripAction,
                survivabilityRequirement,
                diagnosticRequired,
                additionalDiagnosticRequirementForImplementation,
                timeDelayOfAction,
                environmentalExtremes,
                failureModeResponses,
                inputDevice,
                logicSolver,
                finalElement,
                sharedUseIsAllowed,
                referenceToSIF,
                usefulLife,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DeviceModelSpecification(aas.SubmodelElementCollection):

        class InstrumentDataSheet(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"InstrumentDataSheet",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"instrument data sheet"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InstrumentDataSheet/1"),
                }

            def __init__(
                self,
                value: str,
                content_type: Optional[str] = r"application/octet-stream",
                **kwargs: Unpack[FileMetadata],
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class SafetyManual(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {
                    "id_short": r"SafetyManual",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"safety manual"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SafetyManual/1"),
                }

            def __init__(
                self,
                value: str,
                content_type: Optional[str] = r"application/octet-stream",
                **kwargs: Unpack[FileMetadata],
            ):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        class ProductTypeName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductTypeName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"type name of product"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProductTypeName/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductFamilyName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductFamilyName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"family name of product"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProductFamilyName/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductModelName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductModelName",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"model name of product"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProductModelName/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NameOfManufacturer(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NameOfManufacturer",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"name of component manufacturer"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NameOfManufacturer/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeviceDescription(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DeviceDescription",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device description"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceDescription/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeviceBoundary(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DeviceBoundary",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device boundary"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceBoundary/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MaintainableItem(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaintainableItem",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"maintainable item"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MaintainableItem/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SystematicCapabilitySpecified(aas.Property):

            ALLOWED_VALUES = (r"SIL 4", r"SIL 3", r"SIL 2", r"SIL 1", r"no SIL")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SystematicCapabilitySpecified",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"systematic capability specified"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SystematicCapabilitySpecified/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"SIL 4, SIL 3, SIL 2, SIL 1, no SIL",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class InternalHFTSpecified(aas.Property):

            ALLOWED_VALUES = (r"0", r"1", r"2", r"3", r"4", r"5", r"6", r"7", r"8")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"InternalHFTSpecified",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"internal HFT specified"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InternalHFTSpecified/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"0, 1, 2, 3, 4, 5, 6, 7, 8",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsPriorUse(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsPriorUse",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is prior use"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/IsPriorUse/1"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class IsProvenInUse(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"IsProvenInUse",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is proven in use"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/IsProvenInUse/1"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MeanTimeToRestoration(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MeanTimeToRestoration",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"mean time to restoration"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MeanTimeToRestoration/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FinalElement(aas.SubmodelElementCollection):

            class EnergizeSource(aas.Property):

                ALLOWED_VALUES = (r"electrical", r"pneumatic", r"hydraulic")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EnergizeSource",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"energize source"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the model of the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/EnergizeSource/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"electrical, pneumatic, hydraulic",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FinalElement",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"final element"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the final element subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FinalElement/1"),
                }

            def __init__(
                self,
                energizeSource: Optional[Union[str, EnergizeSource]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if energizeSource is not None and not isinstance(energizeSource, aas.SubmodelElement):
                    energizeSource = self.EnergizeSource(energizeSource)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(energizeSource)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LogicSolver(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"LogicSolver",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"logic solver"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the logic solver subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LogicSolver/1"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InputDevice(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InputDevice",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"input device"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the input device subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InputDevice/1"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class TypeAOrB(aas.Property):

            ALLOWED_VALUES = (r"A", r"B", r"other")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TypeAOrB",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"type A or B"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the model of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TypeAOrB/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"A, B, other",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class HardwareVersion(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"HardwareVersion",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"hardware version"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/HardwareVersion/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SoftwareVersion(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SoftwareVersion",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"software version"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SoftwareVersion/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DeviceModelSpecification",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device model specification"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"gives information about the model of the device"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceModelSpecification/1"),
            }

        def __init__(
            self,
            instrumentDataSheet: InstrumentDataSheet,
            safetyManual: SafetyManual,
            productTypeName: Union[str, ProductTypeName],
            nameOfManufacturer: Union[str, NameOfManufacturer],
            systematicCapabilitySpecified: Union[str, SystematicCapabilitySpecified],
            isPriorUse: Union[bool, IsPriorUse],
            isProvenInUse: Union[bool, IsProvenInUse],
            meanTimeToRestoration: Union[float, MeanTimeToRestoration],
            productFamilyName: Optional[Union[str, ProductFamilyName]] = None,
            productModelName: Optional[Union[str, ProductModelName]] = None,
            deviceDescription: Optional[Union[str, DeviceDescription]] = None,
            deviceBoundary: Optional[Union[str, DeviceBoundary]] = None,
            maintainableItem: Optional[Iterable[Union[str, MaintainableItem]]] = None,
            internalHFTSpecified: Optional[Union[str, InternalHFTSpecified]] = None,
            finalElement: Optional[FinalElement] = None,
            logicSolver: Optional[LogicSolver] = None,
            inputDevice: Optional[InputDevice] = None,
            typeAOrB: Optional[Union[str, TypeAOrB]] = None,
            hardwareVersion: Optional[Union[str, HardwareVersion]] = None,
            softwareVersion: Optional[Union[str, SoftwareVersion]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if productTypeName is not None and not isinstance(productTypeName, aas.SubmodelElement):
                productTypeName = self.ProductTypeName(productTypeName)

            # Build a submodel element if a raw value was passed in the argument

            if productFamilyName is not None and not isinstance(productFamilyName, aas.SubmodelElement):
                productFamilyName = self.ProductFamilyName(productFamilyName)

            # Build a submodel element if a raw value was passed in the argument

            if productModelName is not None and not isinstance(productModelName, aas.SubmodelElement):
                productModelName = self.ProductModelName(productModelName)

            # Build a submodel element if a raw value was passed in the argument

            if nameOfManufacturer is not None and not isinstance(nameOfManufacturer, aas.SubmodelElement):
                nameOfManufacturer = self.NameOfManufacturer(nameOfManufacturer)

            # Build a submodel element if a raw value was passed in the argument

            if deviceDescription is not None and not isinstance(deviceDescription, aas.SubmodelElement):
                deviceDescription = self.DeviceDescription(deviceDescription)

            # Build a submodel element if a raw value was passed in the argument

            if deviceBoundary is not None and not isinstance(deviceBoundary, aas.SubmodelElement):
                deviceBoundary = self.DeviceBoundary(deviceBoundary)

            # A str would be split into its characters
            if isinstance(maintainableItem, str):
                raise TypeError("maintainableItem takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if maintainableItem:
                maintainableItem = [
                    i if isinstance(i, aas.SubmodelElement) else self.MaintainableItem(i) for i in maintainableItem
                ]

            # Build a submodel element if a raw value was passed in the argument

            if systematicCapabilitySpecified is not None and not isinstance(
                systematicCapabilitySpecified, aas.SubmodelElement
            ):
                systematicCapabilitySpecified = self.SystematicCapabilitySpecified(systematicCapabilitySpecified)

            # Build a submodel element if a raw value was passed in the argument

            if internalHFTSpecified is not None and not isinstance(internalHFTSpecified, aas.SubmodelElement):
                internalHFTSpecified = self.InternalHFTSpecified(internalHFTSpecified)

            # Build a submodel element if a raw value was passed in the argument

            if isPriorUse is not None and not isinstance(isPriorUse, aas.SubmodelElement):
                isPriorUse = self.IsPriorUse(isPriorUse)

            # Build a submodel element if a raw value was passed in the argument

            if isProvenInUse is not None and not isinstance(isProvenInUse, aas.SubmodelElement):
                isProvenInUse = self.IsProvenInUse(isProvenInUse)

            # Build a submodel element if a raw value was passed in the argument

            if meanTimeToRestoration is not None and not isinstance(meanTimeToRestoration, aas.SubmodelElement):
                meanTimeToRestoration = self.MeanTimeToRestoration(meanTimeToRestoration)

            # Build a submodel element if a raw value was passed in the argument

            if typeAOrB is not None and not isinstance(typeAOrB, aas.SubmodelElement):
                typeAOrB = self.TypeAOrB(typeAOrB)

            # Build a submodel element if a raw value was passed in the argument

            if hardwareVersion is not None and not isinstance(hardwareVersion, aas.SubmodelElement):
                hardwareVersion = self.HardwareVersion(hardwareVersion)

            # Build a submodel element if a raw value was passed in the argument

            if softwareVersion is not None and not isinstance(softwareVersion, aas.SubmodelElement):
                softwareVersion = self.SoftwareVersion(softwareVersion)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                instrumentDataSheet,
                safetyManual,
                productTypeName,
                productFamilyName,
                productModelName,
                nameOfManufacturer,
                deviceDescription,
                deviceBoundary,
                maintainableItem,
                systematicCapabilitySpecified,
                internalHFTSpecified,
                isPriorUse,
                isProvenInUse,
                meanTimeToRestoration,
                finalElement,
                logicSolver,
                inputDevice,
                typeAOrB,
                hardwareVersion,
                softwareVersion,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ReliabilityDataDesign(aas.SubmodelElementCollection):

        class MeanTimeBetweenFailures(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MeanTimeBetweenFailures",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"mean time between failures"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MeanTimeBetweenFailures/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"years",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaDUDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaDUDesign",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda DU design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaDUDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaDDDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaDDDesign",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda DD design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaDDDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaSUDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaSUDesign",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda SU design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaSUDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaSDDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaSDDesign",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda SD design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaSDDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Beta(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Beta",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"beta"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Beta/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"percentage",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SafeFailureFractionDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SafeFailureFractionDesign",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"safe failure fraction design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SafeFailureFractionDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"percentage",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DiagnosticCoverageDesign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DiagnosticCoverageDesign",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostic coverage design"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DiagnosticCoverageDesign/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"percentage",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DataSource(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DataSource",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"data source"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"source of the reliability data in this SMC"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DataSource/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ReliabilityDataDesign",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reliability data design"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"reliability data parameter(s) with design data value(s)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReliabilityDataDesign/1"),
            }

        def __init__(
            self,
            lambdaDUDesign: Union[float, LambdaDUDesign],
            safeFailureFractionDesign: Union[xsd.Decimal, SafeFailureFractionDesign],
            diagnosticCoverageDesign: Union[xsd.Decimal, DiagnosticCoverageDesign],
            dataSource: Iterable[Union[str, DataSource]],
            meanTimeBetweenFailures: Optional[Union[xsd.Decimal, MeanTimeBetweenFailures]] = None,
            lambdaDDDesign: Optional[Union[float, LambdaDDDesign]] = None,
            lambdaSUDesign: Optional[Union[float, LambdaSUDesign]] = None,
            lambdaSDDesign: Optional[Union[float, LambdaSDDesign]] = None,
            beta: Optional[Union[xsd.Decimal, Beta]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if meanTimeBetweenFailures is not None and not isinstance(meanTimeBetweenFailures, aas.SubmodelElement):
                meanTimeBetweenFailures = self.MeanTimeBetweenFailures(meanTimeBetweenFailures)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaDUDesign is not None and not isinstance(lambdaDUDesign, aas.SubmodelElement):
                lambdaDUDesign = self.LambdaDUDesign(lambdaDUDesign)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaDDDesign is not None and not isinstance(lambdaDDDesign, aas.SubmodelElement):
                lambdaDDDesign = self.LambdaDDDesign(lambdaDDDesign)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaSUDesign is not None and not isinstance(lambdaSUDesign, aas.SubmodelElement):
                lambdaSUDesign = self.LambdaSUDesign(lambdaSUDesign)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaSDDesign is not None and not isinstance(lambdaSDDesign, aas.SubmodelElement):
                lambdaSDDesign = self.LambdaSDDesign(lambdaSDDesign)

            # Build a submodel element if a raw value was passed in the argument

            if beta is not None and not isinstance(beta, aas.SubmodelElement):
                beta = self.Beta(beta)

            # Build a submodel element if a raw value was passed in the argument

            if safeFailureFractionDesign is not None and not isinstance(safeFailureFractionDesign, aas.SubmodelElement):
                safeFailureFractionDesign = self.SafeFailureFractionDesign(safeFailureFractionDesign)

            # Build a submodel element if a raw value was passed in the argument

            if diagnosticCoverageDesign is not None and not isinstance(diagnosticCoverageDesign, aas.SubmodelElement):
                diagnosticCoverageDesign = self.DiagnosticCoverageDesign(diagnosticCoverageDesign)

            # A str would be split into its characters
            if isinstance(dataSource, str):
                raise TypeError("dataSource takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if dataSource:
                dataSource = [i if isinstance(i, aas.SubmodelElement) else self.DataSource(i) for i in dataSource]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                meanTimeBetweenFailures,
                lambdaDUDesign,
                lambdaDDDesign,
                lambdaSUDesign,
                lambdaSDDesign,
                beta,
                safeFailureFractionDesign,
                diagnosticCoverageDesign,
                dataSource,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ReliabilityInfluencingProperties(aas.SubmodelElementCollection):

        class Application(aas.Property):

            ALLOWED_VALUES = (
                r"ESD",
                r"PSD",
                r"ESD/PSD",
                r"F&G",
                r"HVAC",
                r"EDP",
                r"BPCS",
                r"HIPPS",
                r"PPS",
                r"Equipment protection",
                r"Offloading",
                r"Monitoring",
            )

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Application",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"application description"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Application/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"ESD, PSD, ESD/PSD, F&G, HVAC, EDP, BPCS, HIPPS, PPS, Equipment protection, Offloading, Monitoring",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ExternalExposure(aas.Property):

            ALLOWED_VALUES = (r"severe", r"moderate", r"shielded", r"indoor", r"outdoor")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExternalExposure",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"external exposure"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ExternalExposure/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"severe, moderate, shielded, indoor, outdoor",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FluidSeverity(aas.Property):

            ALLOWED_VALUES = (r"clean", r"medium", r"dirty")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FluidSeverity",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"fluid severity"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FluidSeverity/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"clean, medium, dirty",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class Fluid(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"Fluid",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"type of fluid"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Fluid/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class InputDevice(aas.SubmodelElementCollection):

            class MeasuringPrinciple(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MeasuringPrinciple",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"measuring principle"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MeasuringPrinciple/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InterfaceMeasurement(aas.Property):

                ALLOWED_VALUES = (r"liquid-gas", r"liquid-liquid", r"solid")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InterfaceMeasurement",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"interface measurement"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InterfaceMeasurement/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"liquid-gas, liquid-liquid, solid",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Function(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Function",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"function"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Function/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"InputDevice",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"input device"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the input device subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InputDevice/1"),
                }

            def __init__(
                self,
                measuringPrinciple: Optional[Union[str, MeasuringPrinciple]] = None,
                interfaceMeasurement: Optional[Union[str, InterfaceMeasurement]] = None,
                function: Optional[Union[str, Function]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if measuringPrinciple is not None and not isinstance(measuringPrinciple, aas.SubmodelElement):
                    measuringPrinciple = self.MeasuringPrinciple(measuringPrinciple)

                # Build a submodel element if a raw value was passed in the argument

                if interfaceMeasurement is not None and not isinstance(interfaceMeasurement, aas.SubmodelElement):
                    interfaceMeasurement = self.InterfaceMeasurement(interfaceMeasurement)

                # Build a submodel element if a raw value was passed in the argument

                if function is not None and not isinstance(function, aas.SubmodelElement):
                    function = self.Function(function)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    measuringPrinciple, interfaceMeasurement, function
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LogicSolver(aas.SubmodelElementCollection):

            class DesignPrinciple(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignPrinciple",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"design principle"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DesignPrinciple/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DeviceType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DeviceType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device type"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceType/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Application(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Application",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"application description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Application/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class StyleOfFailSafe(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"StyleOfFailSafe",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"style of failsafe"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/StyleOfFailSafe/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"LogicSolver",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"logic solver"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the logic solver subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LogicSolver/1"),
                }

            def __init__(
                self,
                designPrinciple: Optional[Union[str, DesignPrinciple]] = None,
                deviceType: Optional[Union[str, DeviceType]] = None,
                application: Optional[Union[str, Application]] = None,
                styleOfFailSafe: Optional[Union[str, StyleOfFailSafe]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if designPrinciple is not None and not isinstance(designPrinciple, aas.SubmodelElement):
                    designPrinciple = self.DesignPrinciple(designPrinciple)

                # Build a submodel element if a raw value was passed in the argument

                if deviceType is not None and not isinstance(deviceType, aas.SubmodelElement):
                    deviceType = self.DeviceType(deviceType)

                # Build a submodel element if a raw value was passed in the argument

                if application is not None and not isinstance(application, aas.SubmodelElement):
                    application = self.Application(application)

                # Build a submodel element if a raw value was passed in the argument

                if styleOfFailSafe is not None and not isinstance(styleOfFailSafe, aas.SubmodelElement):
                    styleOfFailSafe = self.StyleOfFailSafe(styleOfFailSafe)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    designPrinciple, deviceType, application, styleOfFailSafe
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FinalElement(aas.SubmodelElementCollection):

            class DeviceType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DeviceType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device type"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceType/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DesignPrinciple(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DesignPrinciple",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"design principle"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DesignPrinciple/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ActuationPrinciple(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ActuationPrinciple",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"actuation principle"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ActuationPrinciple/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ValveSize(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ValveSize",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"valve size"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ValveSize/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"inches",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DamperLength(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DamperLength",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"damper length"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DamperLength/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"cm",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DamperWidth(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DamperWidth",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"damper width"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DamperWidth/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"cm",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MountingPrinciple(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MountingPrinciple",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"mounting principle"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MountingPrinciple/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DoorHasPersonnelProtectionSystem(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DoorHasPersonnelProtectionSystem",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"door has personnel protection system"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/DoorHasPersonnelProtectionSystem/1"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class VoltageClass(aas.Property):

                ALLOWED_VALUES = (r"high", r"medium", r"low")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"VoltageClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"voltage class"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"reliability influencing property for the device"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/VoltageClass/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"high, medium, low",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FinalElement",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"final element"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the final element subsystem of the SIF"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FinalElement/1"),
                }

            def __init__(
                self,
                deviceType: Optional[Union[str, DeviceType]] = None,
                designPrinciple: Optional[Union[str, DesignPrinciple]] = None,
                actuationPrinciple: Optional[Union[str, ActuationPrinciple]] = None,
                valveSize: Optional[Union[xsd.Decimal, ValveSize]] = None,
                damperLength: Optional[Union[xsd.Decimal, DamperLength]] = None,
                damperWidth: Optional[Union[xsd.Decimal, DamperWidth]] = None,
                mountingPrinciple: Optional[Union[str, MountingPrinciple]] = None,
                doorHasPersonnelProtectionSystem: Optional[Union[bool, DoorHasPersonnelProtectionSystem]] = None,
                voltageClass: Optional[Union[str, VoltageClass]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if deviceType is not None and not isinstance(deviceType, aas.SubmodelElement):
                    deviceType = self.DeviceType(deviceType)

                # Build a submodel element if a raw value was passed in the argument

                if designPrinciple is not None and not isinstance(designPrinciple, aas.SubmodelElement):
                    designPrinciple = self.DesignPrinciple(designPrinciple)

                # Build a submodel element if a raw value was passed in the argument

                if actuationPrinciple is not None and not isinstance(actuationPrinciple, aas.SubmodelElement):
                    actuationPrinciple = self.ActuationPrinciple(actuationPrinciple)

                # Build a submodel element if a raw value was passed in the argument

                if valveSize is not None and not isinstance(valveSize, aas.SubmodelElement):
                    valveSize = self.ValveSize(valveSize)

                # Build a submodel element if a raw value was passed in the argument

                if damperLength is not None and not isinstance(damperLength, aas.SubmodelElement):
                    damperLength = self.DamperLength(damperLength)

                # Build a submodel element if a raw value was passed in the argument

                if damperWidth is not None and not isinstance(damperWidth, aas.SubmodelElement):
                    damperWidth = self.DamperWidth(damperWidth)

                # Build a submodel element if a raw value was passed in the argument

                if mountingPrinciple is not None and not isinstance(mountingPrinciple, aas.SubmodelElement):
                    mountingPrinciple = self.MountingPrinciple(mountingPrinciple)

                # Build a submodel element if a raw value was passed in the argument

                if doorHasPersonnelProtectionSystem is not None and not isinstance(
                    doorHasPersonnelProtectionSystem, aas.SubmodelElement
                ):
                    doorHasPersonnelProtectionSystem = self.DoorHasPersonnelProtectionSystem(
                        doorHasPersonnelProtectionSystem
                    )

                # Build a submodel element if a raw value was passed in the argument

                if voltageClass is not None and not isinstance(voltageClass, aas.SubmodelElement):
                    voltageClass = self.VoltageClass(voltageClass)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    deviceType,
                    designPrinciple,
                    actuationPrinciple,
                    valveSize,
                    damperLength,
                    damperWidth,
                    mountingPrinciple,
                    doorHasPersonnelProtectionSystem,
                    voltageClass,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class InternalDiagnostic(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"InternalDiagnostic",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"internal diagnostic"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/InternalDiagnostic/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ExternalDiagnostic(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ExternalDiagnostic",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"external diagnostic"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability influencing property for the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ExternalDiagnostic/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ReliabilityInfluencingProperties",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reliability influencing property"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"reliability influencing property for the device"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReliabilityInfluencingProperties/1"),
            }

        def __init__(
            self,
            application: Optional[Iterable[Union[str, Application]]] = None,
            externalExposure: Optional[Union[str, ExternalExposure]] = None,
            fluidSeverity: Optional[Union[str, FluidSeverity]] = None,
            fluid: Optional[Union[str, Fluid]] = None,
            inputDevice: Optional[InputDevice] = None,
            logicSolver: Optional[LogicSolver] = None,
            finalElement: Optional[FinalElement] = None,
            internalDiagnostic: Optional[Iterable[Union[str, InternalDiagnostic]]] = None,
            externalDiagnostic: Optional[Iterable[Union[str, ExternalDiagnostic]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(application, str):
                raise TypeError("application takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if application:
                application = [i if isinstance(i, aas.SubmodelElement) else self.Application(i) for i in application]

            # Build a submodel element if a raw value was passed in the argument

            if externalExposure is not None and not isinstance(externalExposure, aas.SubmodelElement):
                externalExposure = self.ExternalExposure(externalExposure)

            # Build a submodel element if a raw value was passed in the argument

            if fluidSeverity is not None and not isinstance(fluidSeverity, aas.SubmodelElement):
                fluidSeverity = self.FluidSeverity(fluidSeverity)

            # Build a submodel element if a raw value was passed in the argument

            if fluid is not None and not isinstance(fluid, aas.SubmodelElement):
                fluid = self.Fluid(fluid)

            # A str would be split into its characters
            if isinstance(internalDiagnostic, str):
                raise TypeError("internalDiagnostic takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if internalDiagnostic:
                internalDiagnostic = [
                    i if isinstance(i, aas.SubmodelElement) else self.InternalDiagnostic(i) for i in internalDiagnostic
                ]

            # A str would be split into its characters
            if isinstance(externalDiagnostic, str):
                raise TypeError("externalDiagnostic takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if externalDiagnostic:
                externalDiagnostic = [
                    i if isinstance(i, aas.SubmodelElement) else self.ExternalDiagnostic(i) for i in externalDiagnostic
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                application,
                externalExposure,
                fluidSeverity,
                fluid,
                inputDevice,
                logicSolver,
                finalElement,
                internalDiagnostic,
                externalDiagnostic,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DeviceInstanceSpecification(aas.SubmodelElementCollection):

        class EquipmentNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EquipmentNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"equipment number"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/EquipmentNumber/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SerialNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SerialNumber",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"serial number"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SerialNumber/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DateOfProduction(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DateOfProduction",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"date of manufacture"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DateOfProduction/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class StartDateOperation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"StartDateOperation",
                    "value_type": xsd.Date,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"start date operation"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/StartDateOperation/1"),
                }

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class EndDateOperation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"EndDateOperation",
                    "value_type": xsd.Date,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"end date operation"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/EndDateOperation/1"),
                }

            def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PhysicalLocation(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PhysicalLocation",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"description of physical location"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the tag that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PhysicalLocation/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToAssociatedDevice(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ReferenceToAssociatedDevice",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to associated device"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToAssociatedDevice/1"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToModelNumber(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ReferenceToModelNumber",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to model number"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives relevant information about the instance that the device represents"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToModelNumber/1"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToTag(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ReferenceToTag",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to tag"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the instance of the device"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToTag/1"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DeviceInstanceSpecification",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device instance specification"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"gives information about the instance of the device"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceInstanceSpecification/1"),
            }

        def __init__(
            self,
            serialNumber: Union[str, SerialNumber],
            dateOfProduction: Union[str, DateOfProduction],
            referenceToModelNumber: Union[aas.Reference, ReferenceToModelNumber],
            referenceToTag: Union[aas.Reference, ReferenceToTag],
            equipmentNumber: Optional[Union[str, EquipmentNumber]] = None,
            startDateOperation: Optional[Union[xsd.Date, StartDateOperation]] = None,
            endDateOperation: Optional[Union[xsd.Date, EndDateOperation]] = None,
            physicalLocation: Optional[Union[str, PhysicalLocation]] = None,
            referenceToAssociatedDevice: Optional[Iterable[Union[aas.Reference, ReferenceToAssociatedDevice]]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if equipmentNumber is not None and not isinstance(equipmentNumber, aas.SubmodelElement):
                equipmentNumber = self.EquipmentNumber(equipmentNumber)

            # Build a submodel element if a raw value was passed in the argument

            if serialNumber is not None and not isinstance(serialNumber, aas.SubmodelElement):
                serialNumber = self.SerialNumber(serialNumber)

            # Build a submodel element if a raw value was passed in the argument

            if dateOfProduction is not None and not isinstance(dateOfProduction, aas.SubmodelElement):
                dateOfProduction = self.DateOfProduction(dateOfProduction)

            # Build a submodel element if a raw value was passed in the argument

            if startDateOperation is not None and not isinstance(startDateOperation, aas.SubmodelElement):
                startDateOperation = self.StartDateOperation(startDateOperation)

            # Build a submodel element if a raw value was passed in the argument

            if endDateOperation is not None and not isinstance(endDateOperation, aas.SubmodelElement):
                endDateOperation = self.EndDateOperation(endDateOperation)

            # Build a submodel element if a raw value was passed in the argument

            if physicalLocation is not None and not isinstance(physicalLocation, aas.SubmodelElement):
                physicalLocation = self.PhysicalLocation(physicalLocation)

            # A str would be split into its characters
            if isinstance(referenceToAssociatedDevice, str):
                raise TypeError("referenceToAssociatedDevice takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if referenceToAssociatedDevice:
                referenceToAssociatedDevice = [
                    i if isinstance(i, aas.SubmodelElement) else self.ReferenceToAssociatedDevice(i)
                    for i in referenceToAssociatedDevice
                ]

            # Build a submodel element if a raw value was passed in the argument

            if referenceToModelNumber is not None and not isinstance(referenceToModelNumber, aas.SubmodelElement):
                referenceToModelNumber = self.ReferenceToModelNumber(referenceToModelNumber)

            # Build a submodel element if a raw value was passed in the argument

            if referenceToTag is not None and not isinstance(referenceToTag, aas.SubmodelElement):
                referenceToTag = self.ReferenceToTag(referenceToTag)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                equipmentNumber,
                serialNumber,
                dateOfProduction,
                startDateOperation,
                endDateOperation,
                physicalLocation,
                referenceToAssociatedDevice,
                referenceToModelNumber,
                referenceToTag,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BypassData(aas.SubmodelElementCollection):

        class NumberOfBypasses(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfBypasses",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of bypasses"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred bypass(es)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfBypasses/1"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TotalBypassDuration(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TotalBypassDuration",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"total bypass duration"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred bypass(es)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TotalBypassDuration/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"hours",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BypassEvent(aas.SubmodelElementCollection):

            class TimeStampDateAndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStampDateAndTime",
                        "value_type": xsd.Time,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time stamp (date and time)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date of the event given within the current SMC"}
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABN627#001"),
                    }

                def __init__(self, value: xsd.Time, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BypassDescription(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BypassDescription",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"bypass description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred bypass(es)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/BypassDescription/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BypassDuration(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BypassDuration",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"bypass duration"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred bypass(es)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/BypassDuration/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"hours",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"BypassEvent",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"bypass event"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred bypass(es)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/BypassEvent/1"),
                }

            def __init__(
                self,
                timeStampDateAndTime: Union[xsd.Time, TimeStampDateAndTime],
                bypassDuration: Union[int, BypassDuration],
                bypassDescription: Optional[Union[str, BypassDescription]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if timeStampDateAndTime is not None and not isinstance(timeStampDateAndTime, aas.SubmodelElement):
                    timeStampDateAndTime = self.TimeStampDateAndTime(timeStampDateAndTime)

                # Build a submodel element if a raw value was passed in the argument

                if bypassDescription is not None and not isinstance(bypassDescription, aas.SubmodelElement):
                    bypassDescription = self.BypassDescription(bypassDescription)

                # Build a submodel element if a raw value was passed in the argument

                if bypassDuration is not None and not isinstance(bypassDuration, aas.SubmodelElement):
                    bypassDuration = self.BypassDuration(bypassDuration)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    timeStampDateAndTime, bypassDescription, bypassDuration
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BypassData",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"bypass data"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about occurred bypass(es)"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/BypassData/1"),
            }

        def __init__(
            self,
            numberOfBypasses: Union[int, NumberOfBypasses],
            totalBypassDuration: Union[int, TotalBypassDuration],
            bypassEvent: Optional[Iterable[BypassEvent]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if numberOfBypasses is not None and not isinstance(numberOfBypasses, aas.SubmodelElement):
                numberOfBypasses = self.NumberOfBypasses(numberOfBypasses)

            # Build a submodel element if a raw value was passed in the argument

            if totalBypassDuration is not None and not isinstance(totalBypassDuration, aas.SubmodelElement):
                totalBypassDuration = self.TotalBypassDuration(totalBypassDuration)

            # A str would be split into its characters
            if isinstance(bypassEvent, str):
                raise TypeError("bypassEvent takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(numberOfBypasses, totalBypassDuration, bypassEvent)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Diagnostics(aas.SubmodelElementCollection):

        class DiagnosticFunction(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DiagnosticFunction",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostic function"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the device diagnostics"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DiagnosticFunction/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToDiagnosticAlarm(aas.RelationshipElement):

            @staticmethod
            def template_defaults() -> RelationshipElementMetadata:
                return {
                    "id_short": r"ReferenceToDiagnosticAlarm",
                    "first": aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/cds/DiagnosticFunction/1",
                            ),
                        ),
                        referred_semantic_id=global_ref(r"https://admin-shell.io/idta/cds/DiagnosticFunction/1"),
                    ),
                    "second": aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/cds/AlarmEventData/1",
                            ),
                        ),
                        referred_semantic_id=global_ref(r"https://admin-shell.io/idta/cds/AlarmEventData/1"),
                    ),
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to diagnostic alarm"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the device diagnostics"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToDiagnosticAlarm/1"),
                }

            def __init__(self, **kwargs: Unpack[RelationshipElementMetadata]):

                super().__init__(**(self.template_defaults() | kwargs))

        class AlarmEventData(aas.SubmodelElementCollection):

            class AlarmDescription(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlarmDescription",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the device diagnostics"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmDescription/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TimeStampDateAndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStampDateAndTime",
                        "value_type": xsd.Time,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time stamp (date and time)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date of the event given within the current SMC"}
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABN627#001"),
                    }

                def __init__(self, value: xsd.Time, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AlarmSource(aas.Property):

                ALLOWED_VALUES = (r"ASR", r"SAS", r"IMS", r"other")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlarmSource",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm source"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the device diagnostics"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmSource/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"ASR, SAS, IMS, other",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AlarmState(aas.Property):

                ALLOWED_VALUES = (
                    r"unacknowledged",
                    r"acknowledged",
                    r"return to normal unacknowledged",
                    r"shelved",
                    r"suppressed by design",
                    r"out of service",
                )

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlarmState",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm state"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the device diagnostics"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmState/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"unacknowledged, acknowledged, return to normal unacknowledged, shelved, suppressed by design, out of service",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AlarmStatus(aas.Property):

                ALLOWED_VALUES = (r"active", r"not active")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AlarmStatus",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm status"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about the device diagnostics"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmStatus/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"active, not active",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceToFailureEvent(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ReferenceToFailureEvent",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to failure event"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred test(s) or alarm(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToFailureEvent/1"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"AlarmEventData",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"alarm event data"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the device diagnostics"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/AlarmEventData/1"),
                }

            def __init__(
                self,
                timeStampDateAndTime: Union[xsd.Time, TimeStampDateAndTime],
                alarmSource: Union[str, AlarmSource],
                alarmDescription: Optional[Union[str, AlarmDescription]] = None,
                alarmState: Optional[Union[str, AlarmState]] = None,
                alarmStatus: Optional[Union[str, AlarmStatus]] = None,
                referenceToFailureEvent: Optional[Union[aas.Reference, ReferenceToFailureEvent]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if alarmDescription is not None and not isinstance(alarmDescription, aas.SubmodelElement):
                    alarmDescription = self.AlarmDescription(alarmDescription)

                # Build a submodel element if a raw value was passed in the argument

                if timeStampDateAndTime is not None and not isinstance(timeStampDateAndTime, aas.SubmodelElement):
                    timeStampDateAndTime = self.TimeStampDateAndTime(timeStampDateAndTime)

                # Build a submodel element if a raw value was passed in the argument

                if alarmSource is not None and not isinstance(alarmSource, aas.SubmodelElement):
                    alarmSource = self.AlarmSource(alarmSource)

                # Build a submodel element if a raw value was passed in the argument

                if alarmState is not None and not isinstance(alarmState, aas.SubmodelElement):
                    alarmState = self.AlarmState(alarmState)

                # Build a submodel element if a raw value was passed in the argument

                if alarmStatus is not None and not isinstance(alarmStatus, aas.SubmodelElement):
                    alarmStatus = self.AlarmStatus(alarmStatus)

                # Build a submodel element if a raw value was passed in the argument

                if referenceToFailureEvent is not None and not isinstance(referenceToFailureEvent, aas.SubmodelElement):
                    referenceToFailureEvent = self.ReferenceToFailureEvent(referenceToFailureEvent)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    alarmDescription,
                    timeStampDateAndTime,
                    alarmSource,
                    alarmState,
                    alarmStatus,
                    referenceToFailureEvent,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Diagnostics",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostics"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"gives information about the device diagnostics"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Diagnostics/1"),
            }

        def __init__(
            self,
            diagnosticFunction: Union[str, DiagnosticFunction],
            referenceToDiagnosticAlarm: Optional[Iterable[ReferenceToDiagnosticAlarm]] = None,
            alarmEventData: Optional[Iterable[AlarmEventData]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if diagnosticFunction is not None and not isinstance(diagnosticFunction, aas.SubmodelElement):
                diagnosticFunction = self.DiagnosticFunction(diagnosticFunction)

            # A str would be split into its characters
            if isinstance(referenceToDiagnosticAlarm, str):
                raise TypeError("referenceToDiagnosticAlarm takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(alarmEventData, str):
                raise TypeError("alarmEventData takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                diagnosticFunction, referenceToDiagnosticAlarm, alarmEventData
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DeviceOperationData(aas.SubmodelElementCollection):

        class OperatingTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OperatingTime",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"operating time"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/OperatingTime/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SurveillanceTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SurveillanceTime",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"surveillance time"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SurveillanceTime/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeviceOperationalStatus(aas.Property):

            ALLOWED_VALUES = (r"activated / normally running", r"standby", r"blocked", r"degraded", r"failed")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DeviceOperationalStatus",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device operational status"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceOperationalStatus/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"activated / normally running, standby, blocked, degraded, failed",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ConditionMonitoringData(aas.SubmodelElementCollection):

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ConditionMonitoringData",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"condition monitoring data"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ConditionMonitoringData/1"),
                }

            def __init__(self, **kwargs: Unpack[SubmodelElementCollectionMetadata]):

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements()

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class FailureStatusSignal(aas.Property):

            ALLOWED_VALUES = (r"failure", r"function check", r"out of specificatoin", r"maintenance request")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FailureStatusSignal",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure status signal"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureStatusSignal/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"failure, function check, out of specificatoin, maintenance request",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PresentTestInterval(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PresentTestInterval",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"present test interval"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PresentTestInterval/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ActualMeanRepairTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ActualMeanRepairTime",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"actual mean repair time"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred failure(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ActualMeanRepairTime/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"hours",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MissionTime(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MissionTime",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"mission time"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"operational data of the device"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MissionTime/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DeviceOperationData",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device operation data"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceOperationData/1"),
            }

        def __init__(
            self,
            operatingTime: Union[float, OperatingTime],
            surveillanceTime: Union[float, SurveillanceTime],
            deviceOperationalStatus: Union[str, DeviceOperationalStatus],
            failureStatusSignal: Union[str, FailureStatusSignal],
            actualMeanRepairTime: Union[float, ActualMeanRepairTime],
            conditionMonitoringData: Optional[Iterable[ConditionMonitoringData]] = None,
            presentTestInterval: Optional[Union[str, PresentTestInterval]] = None,
            missionTime: Optional[Union[str, MissionTime]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if operatingTime is not None and not isinstance(operatingTime, aas.SubmodelElement):
                operatingTime = self.OperatingTime(operatingTime)

            # Build a submodel element if a raw value was passed in the argument

            if surveillanceTime is not None and not isinstance(surveillanceTime, aas.SubmodelElement):
                surveillanceTime = self.SurveillanceTime(surveillanceTime)

            # Build a submodel element if a raw value was passed in the argument

            if deviceOperationalStatus is not None and not isinstance(deviceOperationalStatus, aas.SubmodelElement):
                deviceOperationalStatus = self.DeviceOperationalStatus(deviceOperationalStatus)

            # A str would be split into its characters
            if isinstance(conditionMonitoringData, str):
                raise TypeError("conditionMonitoringData takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if failureStatusSignal is not None and not isinstance(failureStatusSignal, aas.SubmodelElement):
                failureStatusSignal = self.FailureStatusSignal(failureStatusSignal)

            # Build a submodel element if a raw value was passed in the argument

            if presentTestInterval is not None and not isinstance(presentTestInterval, aas.SubmodelElement):
                presentTestInterval = self.PresentTestInterval(presentTestInterval)

            # Build a submodel element if a raw value was passed in the argument

            if actualMeanRepairTime is not None and not isinstance(actualMeanRepairTime, aas.SubmodelElement):
                actualMeanRepairTime = self.ActualMeanRepairTime(actualMeanRepairTime)

            # Build a submodel element if a raw value was passed in the argument

            if missionTime is not None and not isinstance(missionTime, aas.SubmodelElement):
                missionTime = self.MissionTime(missionTime)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                operatingTime,
                surveillanceTime,
                deviceOperationalStatus,
                conditionMonitoringData,
                failureStatusSignal,
                presentTestInterval,
                actualMeanRepairTime,
                missionTime,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DemandData(aas.SubmodelElementCollection):

        class OperationalDemandRate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OperationalDemandRate",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"operational demand rate"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred demand(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/OperationalDemandRate/1"),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfDemands(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfDemands",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of demands"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred demand(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfDemands/1"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DeviceDemandEvent(aas.SubmodelElementCollection):

            class TimeStampDateAndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStampDateAndTime",
                        "value_type": xsd.Time,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time stamp (date and time)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date of the event given within the current SMC"}
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABN627#001"),
                    }

                def __init__(self, value: xsd.Time, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DemandDescription(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DemandDescription",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"demand description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred demand(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DemandDescription/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DemandClass(aas.Property):

                ALLOWED_VALUES = (r"true demand", r"false demand", r"nuisance demand", r"spurious demand")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DemandClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"demand class"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred demand(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DemandClass/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"true demand, false demand, nuisance demand, spurious demand",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SISDeviceResponseTimeActual(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SISDeviceResponseTimeActual",
                        "value_type": xsd.Decimal,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"SIS device response time actual"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred demand(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SISDeviceResponseTimeActual/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"unit",
                                value_type=str,
                                value=r"seconds",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceToFailureEvent(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ReferenceToFailureEvent",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to failure event"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred test(s) or alarm(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToFailureEvent/1"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsSIFDemand(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsSIFDemand",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is SIF demand"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred demand(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/IsSIFDemand/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DeviceDemandEvent",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"device demand event"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred demand(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DeviceDemandEvent/1"),
                }

            def __init__(
                self,
                timeStampDateAndTime: Union[xsd.Time, TimeStampDateAndTime],
                isSIFDemand: Union[bool, IsSIFDemand],
                demandDescription: Optional[Union[str, DemandDescription]] = None,
                demandClass: Optional[Union[str, DemandClass]] = None,
                sISDeviceResponseTimeActual: Optional[Union[xsd.Decimal, SISDeviceResponseTimeActual]] = None,
                referenceToFailureEvent: Optional[Union[aas.Reference, ReferenceToFailureEvent]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if timeStampDateAndTime is not None and not isinstance(timeStampDateAndTime, aas.SubmodelElement):
                    timeStampDateAndTime = self.TimeStampDateAndTime(timeStampDateAndTime)

                # Build a submodel element if a raw value was passed in the argument

                if demandDescription is not None and not isinstance(demandDescription, aas.SubmodelElement):
                    demandDescription = self.DemandDescription(demandDescription)

                # Build a submodel element if a raw value was passed in the argument

                if demandClass is not None and not isinstance(demandClass, aas.SubmodelElement):
                    demandClass = self.DemandClass(demandClass)

                # Build a submodel element if a raw value was passed in the argument

                if sISDeviceResponseTimeActual is not None and not isinstance(
                    sISDeviceResponseTimeActual, aas.SubmodelElement
                ):
                    sISDeviceResponseTimeActual = self.SISDeviceResponseTimeActual(sISDeviceResponseTimeActual)

                # Build a submodel element if a raw value was passed in the argument

                if referenceToFailureEvent is not None and not isinstance(referenceToFailureEvent, aas.SubmodelElement):
                    referenceToFailureEvent = self.ReferenceToFailureEvent(referenceToFailureEvent)

                # Build a submodel element if a raw value was passed in the argument

                if isSIFDemand is not None and not isinstance(isSIFDemand, aas.SubmodelElement):
                    isSIFDemand = self.IsSIFDemand(isSIFDemand)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    timeStampDateAndTime,
                    demandDescription,
                    demandClass,
                    sISDeviceResponseTimeActual,
                    referenceToFailureEvent,
                    isSIFDemand,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DemandData",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"demand data"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about occurred demand(s)"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DemandData/1"),
            }

        def __init__(
            self,
            operationalDemandRate: Union[xsd.Decimal, OperationalDemandRate],
            numberOfDemands: Union[int, NumberOfDemands],
            deviceDemandEvent: Optional[Iterable[DeviceDemandEvent]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if operationalDemandRate is not None and not isinstance(operationalDemandRate, aas.SubmodelElement):
                operationalDemandRate = self.OperationalDemandRate(operationalDemandRate)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfDemands is not None and not isinstance(numberOfDemands, aas.SubmodelElement):
                numberOfDemands = self.NumberOfDemands(numberOfDemands)

            # A str would be split into its characters
            if isinstance(deviceDemandEvent, str):
                raise TypeError("deviceDemandEvent takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                operationalDemandRate, numberOfDemands, deviceDemandEvent
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class FailureData(aas.SubmodelElementCollection):

        class NumberOfFailures(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfFailures",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of failures"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred failure(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfFailures/1"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfDUFailures(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfDUFailures",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of DU failures"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred failure(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfDUFailures/1"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfSpuriousTrips(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfSpuriousTrips",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of spurious trips"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred failure(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfSpuriousTrips/1"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FailureEvent(aas.SubmodelElementCollection):

            class TimeStampDateAndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStampDateAndTime",
                        "value_type": xsd.Time,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time stamp (date and time)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date of the event given within the current SMC"}
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABN627#001"),
                    }

                def __init__(self, value: xsd.Time, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DetectionMethod(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DetectionMethod",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"detection method"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DetectionMethod/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"TBD according to APOS H1",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DetectionMode(aas.Property):

                ALLOWED_VALUES = (r"detected", r"undetected")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DetectionMode",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"detection mode"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DetectionMode/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"detected, undetected",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureMode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureMode",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure mode"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureMode/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"TBD according to APOS L2 group",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureClass(aas.Property):

                ALLOWED_VALUES = (r"DU", r"DD", r"SU", r"SD", r"S", r"Spurious", r"NONC", r"NA")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureClass",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure class"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureClass/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"DU, DD, SU, SD, S, Spurious, NONC, NA",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsSpuriousTrip(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsSpuriousTrip",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is spurious trip"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/IsSpuriousTrip/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureMechanism(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureMechanism",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure mechanism"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureMechanism/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsSystematicOrRandomHardwareFailure(aas.Property):

                ALLOWED_VALUES = (r"systematic", r"random hardware")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsSystematicOrRandomHardwareFailure",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"is systematic or random hardware failure"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/cds/IsSystematicOrRandomHardwareFailure/1"
                        ),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"systematic, random hardware",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureDescription(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureDescription",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure description"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureDescription/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureCause(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureCause",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure cause"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureCause/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class FailureIndependencyType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FailureIndependencyType",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure independency type"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureIndependencyType/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IsSIFFailure(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IsSIFFailure",
                        "value_type": bool,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"is SIF failure"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/IsSIFFailure/1"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ExpectedRepairTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ExpectedRepairTime",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"expected repair time"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ExpectedRepairTime/1"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ActualRepairTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ActualRepairTime",
                        "value_type": float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"actual repair time"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ActualRepairTime/1"),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NotificationNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"NotificationNumber",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"notification number"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NotificationNumber/1"),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class WorkOrderNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WorkOrderNumber",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"work order number"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/WorkOrderNumber/1"),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Measure(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Measure",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Measure"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred failure(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/Measure/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"FailureEvent",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure event"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred failure(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureEvent/1"),
                }

            def __init__(
                self,
                timeStampDateAndTime: Union[xsd.Time, TimeStampDateAndTime],
                detectionMode: Union[str, DetectionMode],
                failureClass: Union[str, FailureClass],
                isSpuriousTrip: Union[bool, IsSpuriousTrip],
                failureDescription: Iterable[Union[str, FailureDescription]],
                actualRepairTime: Union[float, ActualRepairTime],
                notificationNumber: Union[int, NotificationNumber],
                detectionMethod: Optional[Union[str, DetectionMethod]] = None,
                failureMode: Optional[Union[str, FailureMode]] = None,
                failureMechanism: Optional[Iterable[Union[str, FailureMechanism]]] = None,
                isSystematicOrRandomHardwareFailure: Optional[Union[str, IsSystematicOrRandomHardwareFailure]] = None,
                failureCause: Optional[Union[str, FailureCause]] = None,
                failureIndependencyType: Optional[Union[str, FailureIndependencyType]] = None,
                isSIFFailure: Optional[Union[bool, IsSIFFailure]] = None,
                expectedRepairTime: Optional[Union[float, ExpectedRepairTime]] = None,
                workOrderNumber: Optional[Union[int, WorkOrderNumber]] = None,
                measure: Optional[Iterable[Union[str, Measure]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if timeStampDateAndTime is not None and not isinstance(timeStampDateAndTime, aas.SubmodelElement):
                    timeStampDateAndTime = self.TimeStampDateAndTime(timeStampDateAndTime)

                # Build a submodel element if a raw value was passed in the argument

                if detectionMethod is not None and not isinstance(detectionMethod, aas.SubmodelElement):
                    detectionMethod = self.DetectionMethod(detectionMethod)

                # Build a submodel element if a raw value was passed in the argument

                if detectionMode is not None and not isinstance(detectionMode, aas.SubmodelElement):
                    detectionMode = self.DetectionMode(detectionMode)

                # Build a submodel element if a raw value was passed in the argument

                if failureMode is not None and not isinstance(failureMode, aas.SubmodelElement):
                    failureMode = self.FailureMode(failureMode)

                # Build a submodel element if a raw value was passed in the argument

                if failureClass is not None and not isinstance(failureClass, aas.SubmodelElement):
                    failureClass = self.FailureClass(failureClass)

                # Build a submodel element if a raw value was passed in the argument

                if isSpuriousTrip is not None and not isinstance(isSpuriousTrip, aas.SubmodelElement):
                    isSpuriousTrip = self.IsSpuriousTrip(isSpuriousTrip)

                # A str would be split into its characters
                if isinstance(failureMechanism, str):
                    raise TypeError("failureMechanism takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if failureMechanism:
                    failureMechanism = [
                        i if isinstance(i, aas.SubmodelElement) else self.FailureMechanism(i) for i in failureMechanism
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if isSystematicOrRandomHardwareFailure is not None and not isinstance(
                    isSystematicOrRandomHardwareFailure, aas.SubmodelElement
                ):
                    isSystematicOrRandomHardwareFailure = self.IsSystematicOrRandomHardwareFailure(
                        isSystematicOrRandomHardwareFailure
                    )

                # A str would be split into its characters
                if isinstance(failureDescription, str):
                    raise TypeError("failureDescription takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if failureDescription:
                    failureDescription = [
                        i if isinstance(i, aas.SubmodelElement) else self.FailureDescription(i)
                        for i in failureDescription
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if failureCause is not None and not isinstance(failureCause, aas.SubmodelElement):
                    failureCause = self.FailureCause(failureCause)

                # Build a submodel element if a raw value was passed in the argument

                if failureIndependencyType is not None and not isinstance(failureIndependencyType, aas.SubmodelElement):
                    failureIndependencyType = self.FailureIndependencyType(failureIndependencyType)

                # Build a submodel element if a raw value was passed in the argument

                if isSIFFailure is not None and not isinstance(isSIFFailure, aas.SubmodelElement):
                    isSIFFailure = self.IsSIFFailure(isSIFFailure)

                # Build a submodel element if a raw value was passed in the argument

                if expectedRepairTime is not None and not isinstance(expectedRepairTime, aas.SubmodelElement):
                    expectedRepairTime = self.ExpectedRepairTime(expectedRepairTime)

                # Build a submodel element if a raw value was passed in the argument

                if actualRepairTime is not None and not isinstance(actualRepairTime, aas.SubmodelElement):
                    actualRepairTime = self.ActualRepairTime(actualRepairTime)

                # Build a submodel element if a raw value was passed in the argument

                if notificationNumber is not None and not isinstance(notificationNumber, aas.SubmodelElement):
                    notificationNumber = self.NotificationNumber(notificationNumber)

                # Build a submodel element if a raw value was passed in the argument

                if workOrderNumber is not None and not isinstance(workOrderNumber, aas.SubmodelElement):
                    workOrderNumber = self.WorkOrderNumber(workOrderNumber)

                # A str would be split into its characters
                if isinstance(measure, str):
                    raise TypeError("measure takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if measure:
                    measure = [i if isinstance(i, aas.SubmodelElement) else self.Measure(i) for i in measure]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    timeStampDateAndTime,
                    detectionMethod,
                    detectionMode,
                    failureMode,
                    failureClass,
                    isSpuriousTrip,
                    failureMechanism,
                    isSystematicOrRandomHardwareFailure,
                    failureDescription,
                    failureCause,
                    failureIndependencyType,
                    isSIFFailure,
                    expectedRepairTime,
                    actualRepairTime,
                    notificationNumber,
                    workOrderNumber,
                    measure,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"FailureData",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"failure data"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"gives relevant information about the occurred failure(s)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/FailureData/1"),
            }

        def __init__(
            self,
            numberOfFailures: Union[int, NumberOfFailures],
            numberOfDUFailures: Union[int, NumberOfDUFailures],
            numberOfSpuriousTrips: Union[int, NumberOfSpuriousTrips],
            failureEvent: Optional[Iterable[FailureEvent]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if numberOfFailures is not None and not isinstance(numberOfFailures, aas.SubmodelElement):
                numberOfFailures = self.NumberOfFailures(numberOfFailures)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfDUFailures is not None and not isinstance(numberOfDUFailures, aas.SubmodelElement):
                numberOfDUFailures = self.NumberOfDUFailures(numberOfDUFailures)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfSpuriousTrips is not None and not isinstance(numberOfSpuriousTrips, aas.SubmodelElement):
                numberOfSpuriousTrips = self.NumberOfSpuriousTrips(numberOfSpuriousTrips)

            # A str would be split into its characters
            if isinstance(failureEvent, str):
                raise TypeError("failureEvent takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                numberOfFailures, numberOfDUFailures, numberOfSpuriousTrips, failureEvent
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ReliabilityDataOperational(aas.SubmodelElementCollection):

        class LambdaDUOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaDUOperational",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda DU operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaDUOperational/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PFHAverageBasedOnOperationalData(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PFHAverageBasedOnOperationalData",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PFH average based on operational data"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"performance measure(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PFHAverageBasedOnOperationalData/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PFDAverageBasedOnOperationalData(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PFDAverageBasedOnOperationalData",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"PFD average based on operational data"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PFDAverageBasedOnOperationalData/1"),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaDDOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaDDOperational",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda DD operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaDDOperational/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaSUOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaSUOperational",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda SU operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/LambdaSUOperational/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SpuriousTripRateOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SpuriousTripRateOperational",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"spurious trip rate operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about occurred demand(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SpuriousTripRateOperational/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LambdaSDOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"lambdaSDOperational",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"lambda SD operatoinal"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/SISDevice/LambdaSDOperatoinal/1/0"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"per hour",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SafeFailureFractionOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SafeFailureFractionOperational",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"safe failure fraction operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SafeFailureFractionOperational/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"percentage",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DiagnosticCoverageOperational(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DiagnosticCoverageOperational",
                    "value_type": xsd.Decimal,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"diagnostic coverage operational"}),
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/DiagnosticCoverageOperational/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"percentage",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: xsd.Decimal, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ReliabilityDataOperational",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reliability data operational"}),
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"reliability data parameter(s) with operational data value(s)"}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReliabilityDataOperational/1"),
            }

        def __init__(
            self,
            lambdaDUOperational: Union[float, LambdaDUOperational],
            spuriousTripRateOperational: Union[float, SpuriousTripRateOperational],
            pFHAverageBasedOnOperationalData: Optional[Union[float, PFHAverageBasedOnOperationalData]] = None,
            pFDAverageBasedOnOperationalData: Optional[Union[xsd.Decimal, PFDAverageBasedOnOperationalData]] = None,
            lambdaDDOperational: Optional[Union[float, LambdaDDOperational]] = None,
            lambdaSUOperational: Optional[Union[float, LambdaSUOperational]] = None,
            lambdaSDOperational: Optional[Union[float, LambdaSDOperational]] = None,
            safeFailureFractionOperational: Optional[Union[xsd.Decimal, SafeFailureFractionOperational]] = None,
            diagnosticCoverageOperational: Optional[Union[xsd.Decimal, DiagnosticCoverageOperational]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if lambdaDUOperational is not None and not isinstance(lambdaDUOperational, aas.SubmodelElement):
                lambdaDUOperational = self.LambdaDUOperational(lambdaDUOperational)

            # Build a submodel element if a raw value was passed in the argument

            if pFHAverageBasedOnOperationalData is not None and not isinstance(
                pFHAverageBasedOnOperationalData, aas.SubmodelElement
            ):
                pFHAverageBasedOnOperationalData = self.PFHAverageBasedOnOperationalData(
                    pFHAverageBasedOnOperationalData
                )

            # Build a submodel element if a raw value was passed in the argument

            if pFDAverageBasedOnOperationalData is not None and not isinstance(
                pFDAverageBasedOnOperationalData, aas.SubmodelElement
            ):
                pFDAverageBasedOnOperationalData = self.PFDAverageBasedOnOperationalData(
                    pFDAverageBasedOnOperationalData
                )

            # Build a submodel element if a raw value was passed in the argument

            if lambdaDDOperational is not None and not isinstance(lambdaDDOperational, aas.SubmodelElement):
                lambdaDDOperational = self.LambdaDDOperational(lambdaDDOperational)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaSUOperational is not None and not isinstance(lambdaSUOperational, aas.SubmodelElement):
                lambdaSUOperational = self.LambdaSUOperational(lambdaSUOperational)

            # Build a submodel element if a raw value was passed in the argument

            if spuriousTripRateOperational is not None and not isinstance(
                spuriousTripRateOperational, aas.SubmodelElement
            ):
                spuriousTripRateOperational = self.SpuriousTripRateOperational(spuriousTripRateOperational)

            # Build a submodel element if a raw value was passed in the argument

            if lambdaSDOperational is not None and not isinstance(lambdaSDOperational, aas.SubmodelElement):
                lambdaSDOperational = self.LambdaSDOperational(lambdaSDOperational)

            # Build a submodel element if a raw value was passed in the argument

            if safeFailureFractionOperational is not None and not isinstance(
                safeFailureFractionOperational, aas.SubmodelElement
            ):
                safeFailureFractionOperational = self.SafeFailureFractionOperational(safeFailureFractionOperational)

            # Build a submodel element if a raw value was passed in the argument

            if diagnosticCoverageOperational is not None and not isinstance(
                diagnosticCoverageOperational, aas.SubmodelElement
            ):
                diagnosticCoverageOperational = self.DiagnosticCoverageOperational(diagnosticCoverageOperational)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                lambdaDUOperational,
                pFHAverageBasedOnOperationalData,
                pFDAverageBasedOnOperationalData,
                lambdaDDOperational,
                lambdaSUOperational,
                spuriousTripRateOperational,
                lambdaSDOperational,
                safeFailureFractionOperational,
                diagnosticCoverageOperational,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ProofTestData(aas.SubmodelElementCollection):

        class TypeOfTest(aas.Property):

            ALLOWED_VALUES = (r"complete test", r"partial stroke test", r"leakage test")

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TypeOfTest",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"type of test"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TypeOfTest/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"enumeration",
                            value_type=str,
                            value=r"complete test, partial stroke test, leakage test",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                if value is not None and value not in self.ALLOWED_VALUES:
                    raise ValueError(
                        f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                    )

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TestDescription(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TestDescription",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test description"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestDescription/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ShutdownIsNeededForTesting(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ShutdownIsNeededForTesting",
                    "value_type": bool,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"shutdown is needed for testing"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ShutdownIsNeededForTesting/1"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MinimumTimeRequiredForTesting(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MinimumTimeRequiredForTesting",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"minimum time required for testing"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/MinimumTimeRequiredForTesting/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class RequiredResources(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"RequiredResources",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"required resources"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/RequiredResources/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PresentTestInterval(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PresentTestInterval",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"present test interval"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/PresentTestInterval/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"hours",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SourceOfPresentTestInterval(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SourceOfPresentTestInterval",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"source of present test interval"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/SourceOfPresentTestInterval/1"),
                    "qualifier": (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"hours",
                            value_id=None,
                            kind=aas.QualifierKind.VALUE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TestDuration(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TestDuration",
                    "value_type": float,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"duration of test"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestDuration/1"),
                }

            def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfPerformedTests(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfPerformedTests",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of performed tests"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfPerformedTests/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class NumberOfFailedTests(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"NumberOfFailedTests",
                    "value_type": str,
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"number of failed tests"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/NumberOfFailedTests/1"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ReferenceToFailCriterion(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"ReferenceToFailCriterion",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to fail criterion"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToFailCriterion/1"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProofTestEvent(aas.SubmodelElementCollection):

            class TimeStampDateAndTime(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TimeStampDateAndTime",
                        "value_type": xsd.Time,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"time stamp (date and time)"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"date of the event given within the current SMC"}
                        ),
                        "semantic_id": global_ref(r"0112/2///61987#ABN627#001"),
                    }

                def __init__(self, value: xsd.Time, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestLocation(aas.Property):

                ALLOWED_VALUES = (r"in field", r"workshop", r"other")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestLocation",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test location"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestLocation/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"in field, workshop, other",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestResultFailedOrPassed(aas.Property):

                ALLOWED_VALUES = (r"failed", r"passed")

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestResultFailedOrPassed",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test result failed or passed"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestResultFailedOrPassed/1"),
                        "qualifier": (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"failed, passed",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestResultNumeric(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestResultNumeric",
                        "value_type": xsd.Float,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test result numeric"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestResultNumeric/1"),
                    }

                def __init__(self, value: xsd.Float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TestResultText(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TestResultText",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"test result text"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/TestResultText/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CommentToTestResult(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"CommentToTestResult",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"comment to test result"}),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/CommentToTestResult/1"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ReferenceToFailureEvent(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ReferenceToFailureEvent",
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"reference to failure event"}),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"gives information about occurred test(s) or alarm(s)"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ReferenceToFailureEvent/1"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProofTestEvent",
                    "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Proof test event"}),
                    "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProofTestEvent/1"),
                }

            def __init__(
                self,
                timeStampDateAndTime: Union[xsd.Time, TimeStampDateAndTime],
                testResultFailedOrPassed: Union[str, TestResultFailedOrPassed],
                testLocation: Optional[Union[str, TestLocation]] = None,
                testResultNumeric: Optional[Union[xsd.Float, TestResultNumeric]] = None,
                testResultText: Optional[Union[str, TestResultText]] = None,
                commentToTestResult: Optional[Union[str, CommentToTestResult]] = None,
                referenceToFailureEvent: Optional[Union[aas.Reference, ReferenceToFailureEvent]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if timeStampDateAndTime is not None and not isinstance(timeStampDateAndTime, aas.SubmodelElement):
                    timeStampDateAndTime = self.TimeStampDateAndTime(timeStampDateAndTime)

                # Build a submodel element if a raw value was passed in the argument

                if testLocation is not None and not isinstance(testLocation, aas.SubmodelElement):
                    testLocation = self.TestLocation(testLocation)

                # Build a submodel element if a raw value was passed in the argument

                if testResultFailedOrPassed is not None and not isinstance(
                    testResultFailedOrPassed, aas.SubmodelElement
                ):
                    testResultFailedOrPassed = self.TestResultFailedOrPassed(testResultFailedOrPassed)

                # Build a submodel element if a raw value was passed in the argument

                if testResultNumeric is not None and not isinstance(testResultNumeric, aas.SubmodelElement):
                    testResultNumeric = self.TestResultNumeric(testResultNumeric)

                # Build a submodel element if a raw value was passed in the argument

                if testResultText is not None and not isinstance(testResultText, aas.SubmodelElement):
                    testResultText = self.TestResultText(testResultText)

                # Build a submodel element if a raw value was passed in the argument

                if commentToTestResult is not None and not isinstance(commentToTestResult, aas.SubmodelElement):
                    commentToTestResult = self.CommentToTestResult(commentToTestResult)

                # Build a submodel element if a raw value was passed in the argument

                if referenceToFailureEvent is not None and not isinstance(referenceToFailureEvent, aas.SubmodelElement):
                    referenceToFailureEvent = self.ReferenceToFailureEvent(referenceToFailureEvent)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    timeStampDateAndTime,
                    testLocation,
                    testResultFailedOrPassed,
                    testResultNumeric,
                    testResultText,
                    commentToTestResult,
                    referenceToFailureEvent,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ProofTestData",
                "display_name": aas.MultiLanguageNameType(dict_={r"en": r"proof test data"}),
                "description": aas.MultiLanguageTextType(dict_={r"en": r"gives information about test(s)"}),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/cds/ProofTestData/1"),
            }

        def __init__(
            self,
            typeOfTest: Union[str, TypeOfTest],
            shutdownIsNeededForTesting: Union[bool, ShutdownIsNeededForTesting],
            presentTestInterval: Union[str, PresentTestInterval],
            sourceOfPresentTestInterval: Iterable[Union[str, SourceOfPresentTestInterval]],
            numberOfPerformedTests: Union[str, NumberOfPerformedTests],
            numberOfFailedTests: Union[str, NumberOfFailedTests],
            testDescription: Optional[Union[str, TestDescription]] = None,
            minimumTimeRequiredForTesting: Optional[Union[float, MinimumTimeRequiredForTesting]] = None,
            requiredResources: Optional[Union[str, RequiredResources]] = None,
            testDuration: Optional[Union[float, TestDuration]] = None,
            referenceToFailCriterion: Optional[Union[aas.Reference, ReferenceToFailCriterion]] = None,
            proofTestEvent: Optional[Iterable[ProofTestEvent]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if typeOfTest is not None and not isinstance(typeOfTest, aas.SubmodelElement):
                typeOfTest = self.TypeOfTest(typeOfTest)

            # Build a submodel element if a raw value was passed in the argument

            if testDescription is not None and not isinstance(testDescription, aas.SubmodelElement):
                testDescription = self.TestDescription(testDescription)

            # Build a submodel element if a raw value was passed in the argument

            if shutdownIsNeededForTesting is not None and not isinstance(
                shutdownIsNeededForTesting, aas.SubmodelElement
            ):
                shutdownIsNeededForTesting = self.ShutdownIsNeededForTesting(shutdownIsNeededForTesting)

            # Build a submodel element if a raw value was passed in the argument

            if minimumTimeRequiredForTesting is not None and not isinstance(
                minimumTimeRequiredForTesting, aas.SubmodelElement
            ):
                minimumTimeRequiredForTesting = self.MinimumTimeRequiredForTesting(minimumTimeRequiredForTesting)

            # Build a submodel element if a raw value was passed in the argument

            if requiredResources is not None and not isinstance(requiredResources, aas.SubmodelElement):
                requiredResources = self.RequiredResources(requiredResources)

            # Build a submodel element if a raw value was passed in the argument

            if presentTestInterval is not None and not isinstance(presentTestInterval, aas.SubmodelElement):
                presentTestInterval = self.PresentTestInterval(presentTestInterval)

            # A str would be split into its characters
            if isinstance(sourceOfPresentTestInterval, str):
                raise TypeError("sourceOfPresentTestInterval takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if sourceOfPresentTestInterval:
                sourceOfPresentTestInterval = [
                    i if isinstance(i, aas.SubmodelElement) else self.SourceOfPresentTestInterval(i)
                    for i in sourceOfPresentTestInterval
                ]

            # Build a submodel element if a raw value was passed in the argument

            if testDuration is not None and not isinstance(testDuration, aas.SubmodelElement):
                testDuration = self.TestDuration(testDuration)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfPerformedTests is not None and not isinstance(numberOfPerformedTests, aas.SubmodelElement):
                numberOfPerformedTests = self.NumberOfPerformedTests(numberOfPerformedTests)

            # Build a submodel element if a raw value was passed in the argument

            if numberOfFailedTests is not None and not isinstance(numberOfFailedTests, aas.SubmodelElement):
                numberOfFailedTests = self.NumberOfFailedTests(numberOfFailedTests)

            # Build a submodel element if a raw value was passed in the argument

            if referenceToFailCriterion is not None and not isinstance(referenceToFailCriterion, aas.SubmodelElement):
                referenceToFailCriterion = self.ReferenceToFailCriterion(referenceToFailCriterion)

            # A str would be split into its characters
            if isinstance(proofTestEvent, str):
                raise TypeError("proofTestEvent takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                typeOfTest,
                testDescription,
                shutdownIsNeededForTesting,
                minimumTimeRequiredForTesting,
                requiredResources,
                presentTestInterval,
                sourceOfPresentTestInterval,
                testDuration,
                numberOfPerformedTests,
                numberOfFailedTests,
                referenceToFailCriterion,
                proofTestEvent,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"SISDevice",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The submodel SIS device is a collection of properties about the functional safety requirements and information for the lifecycle of a device of a safety instrumented system (SIS) realising one or more safety instrumented functions."
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02079-1-0",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/SubmodelTemplate/SISDevice/1/0"),
        }

    def __init__(
        self,
        id_: str,
        tagInformation: TagInformation,
        sRSRequirements: Iterable[SRSRequirements],
        deviceModelSpecification: DeviceModelSpecification,
        reliabilityDataDesign: ReliabilityDataDesign,
        deviceInstanceSpecification: DeviceInstanceSpecification,
        reliabilityInfluencingProperties: Optional[ReliabilityInfluencingProperties] = None,
        bypassData: Optional[BypassData] = None,
        diagnostics: Optional[Iterable[Diagnostics]] = None,
        deviceOperationData: Optional[DeviceOperationData] = None,
        demandData: Optional[DemandData] = None,
        failureData: Optional[FailureData] = None,
        reliabilityDataOperational: Optional[ReliabilityDataOperational] = None,
        proofTestData: Optional[Iterable[ProofTestData]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(sRSRequirements, str):
            raise TypeError("sRSRequirements takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(diagnostics, str):
            raise TypeError("diagnostics takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(proofTestData, str):
            raise TypeError("proofTestData takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            tagInformation,
            sRSRequirements,
            deviceModelSpecification,
            reliabilityDataDesign,
            reliabilityInfluencingProperties,
            deviceInstanceSpecification,
            bypassData,
            diagnostics,
            deviceOperationData,
            demandData,
            failureData,
            reliabilityDataOperational,
            proofTestData,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
