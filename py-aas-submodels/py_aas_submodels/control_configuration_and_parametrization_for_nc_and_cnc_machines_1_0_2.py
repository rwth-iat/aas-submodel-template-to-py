from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class ControlConfig(aas.Submodel):

    class DigitalNameplate(aas.ReferenceElement):

        def __init__(
            self,
            value: aas.Reference,
            id_short: Optional[str] = r"DigitalNameplate",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/nameplate/3/0/Nameplate",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Reference to the digital nameplate of the controller."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"DigitalNameplate",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Submodel Element reference to the digital nameplate of the control.",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class ControllerType(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"ControllerType",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"PARAMETER",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/ControllerType/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The Controller Type describes the type of controller"
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"ControllerType",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"List of controller types.",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormChoices",
                        value_type=str,
                        value=r"Path controlled; Point controlled, Track controlled",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class TimeUnit(aas.Property):

        def __init__(
            self,
            value: xsd.Float,
            id_short: Optional[str] = r"TimeUnit",
            value_type: aas.DataTypeDefXsd = xsd.Float,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"VARIABLE",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/TimeUnit/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Time unit of the control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"TimeUnit",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Time unit (s, ms, us)",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class LengthUnit(aas.Property):

        def __init__(
            self,
            value: float,
            id_short: Optional[str] = r"LengthUnit",
            value_type: aas.DataTypeDefXsd = float,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/LengthUnit/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Length Unit of the control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"LengthType",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Length type of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class FieldbusType(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"FieldbusType",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/FieldbusType/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Fieldbus Type of the control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"FieldbusType",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Fieldbus type of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class CNCCycleTime(aas.Property):

        def __init__(
            self,
            value: float,
            id_short: Optional[str] = r"CNCCycleTime",
            value_type: aas.DataTypeDefXsd = float,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"VARIABLE",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/CNCCycleTime/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the cycle time of the CNC control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"CNCCycleTime",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Cycle time of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class PLCCycleTime(aas.Property):

        def __init__(
            self,
            value: float,
            id_short: Optional[str] = r"PLCCycleTime",
            value_type: aas.DataTypeDefXsd = float,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"VARIABLE",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/PLCCycleTime/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the cycle time of the PLC control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"PLCCycleTime",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Cycle time of the PLC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class FieldbusCycleTime(aas.Property):

        def __init__(
            self,
            value: float,
            id_short: Optional[str] = r"FieldbusCycleTime",
            value_type: aas.DataTypeDefXsd = float,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"VARIABLE",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/FieldbusCycleTime/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the cycle time of the fieldbus control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"FieldbusCycleTime",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Cycle time of the fieldbus",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class VelocityUnit(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"VelocityUnit",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/VelocityType/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the velocity unit of the CNC control "}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Velocity unit",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Velocity unit of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class AccelerationUnit(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"AccelerationUnit",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/AccelerationUnit/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Defines the acceleration unit unit of the CNC control"
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Acceleration unit",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Acceleration unit of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class JerkUnit(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"JerkUnit",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/JerkUnit/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Defines the jerk unit of the CNC control "}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Jerk unit",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Jerk unit of the CNC",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class ControlConfigData(aas.SubmodelElementCollection):

        class ControlConfigFileName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ControlConfigFileName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/ControlConfigFileName/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Name of the control configuration file"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"ControlConfigFileName",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Filename of the configuration file.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class ControlConfigFile(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ControlConfigFile",
                content_type: Optional[str] = r"application/json",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/ControlConfigFile/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"File to configure the control"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"ConfigurationFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Configuration file of the controler.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    content_type=content_type,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            controlConfigFileName: Union[str, ControlConfigFileName],
            controlConfigFile: ControlConfigFile,
            id_short: Optional[str] = r"ControlConfigData",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/ControlConfigData/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Control configuration data",
                        r"de": r"Steuerungskonfigurationsdaten",
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"ControlerConfigData",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Provide the configuration data for the controler.",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToMany",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if controlConfigFileName is not None and not isinstance(
                controlConfigFileName, aas.SubmodelElement
            ):
                controlConfigFileName = self.ControlConfigFileName(
                    controlConfigFileName
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [controlConfigFileName, controlConfigFile]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class Channels(aas.SubmodelElementCollection):

        class Channel(aas.SubmodelElementCollection):

            class ChannelIdentification(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ChannelIdentification",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"VARIABLE",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Channels/ChannelIdentification/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"This describes the unique channel identification of the specific channel"
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"ChannelIdentification",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Identification number of the channel",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AxesReference(aas.SubmodelElementCollection):

                class AxisName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AxisName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Channels/AxesReference/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Unique axis name"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"AxisName",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Unique axis name",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class ReferenceToAxis(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"ReferenceToAxis",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Channels/ReferenceToAxis/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Reference to the axis"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"ReferenceToAxis",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Reference to the axis",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    axisName: Union[str, AxisName],
                    referenceToAxis: Union[aas.Reference, ReferenceToAxis],
                    id_short: Optional[str] = r"AxesReference",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Channels/AxesReference/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “AxesReference” is a collection of referenced axes for the specific channel."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"AxesReference",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Collection of referenced axes for the specific channel",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if axisName is not None and not isinstance(
                        axisName, aas.SubmodelElement
                    ):
                        axisName = self.AxisName(axisName)

                    # Build a submodel element if a raw value was passed in the argument

                    if referenceToAxis is not None and not isinstance(
                        referenceToAxis, aas.SubmodelElement
                    ):
                        referenceToAxis = self.ReferenceToAxis(referenceToAxis)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [axisName, referenceToAxis]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                channelIdentification: Union[str, ChannelIdentification],
                axesReference: Optional[Iterable[AxesReference]] = None,
                id_short: Optional[str] = r"Channel",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/Channel/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Configuration information of a specific channel"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Channel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Channel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if channelIdentification is not None and not isinstance(
                    channelIdentification, aas.SubmodelElement
                ):
                    channelIdentification = self.ChannelIdentification(
                        channelIdentification
                    )

                # A str would be split into its characters
                if isinstance(axesReference, str):
                    raise TypeError("axesReference takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [channelIdentification, axesReference]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            channel: Channel,
            id_short: Optional[str] = r"Channels",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/Channels/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of channels of the control"}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Channels",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Provides access to the paramtization of the channels/axes/drives",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToMany",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [channel]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class Axes(aas.SubmodelElementCollection):

        class Axis(aas.SubmodelElementCollection):

            class AxisName(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AxisName",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/AxisName/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Name of the axis"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"AxisName",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Name of the specific axis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AxisType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AxisType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/AxisType/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Type of the axis"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"AxisType",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Type of the specific axis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SimulationAxis(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SimulationAxis",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchPos/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Axis is a simulated or real one"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"SimulationAxis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Axis is a simulated or real one",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SwLimitSwitchNeg(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"SwLimitSwitchNeg",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchNeg/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Positive software limit switch"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"SwLimitSwitchNeg",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Software limit switch negative",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class SwLimitSwitchPos(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SwLimitSwitchPos",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/SwLimitSwitchPos/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Negative software limit switch"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"SwLimitSwitchPos",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Software limit switch positive",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class VelocityLimit(aas.Property):

                def __init__(
                    self,
                    value: xsd.Long,
                    id_short: Optional[str] = r"VelocityLimit",
                    value_type: aas.DataTypeDefXsd = xsd.Long,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/VelocityLimit/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Velocity limit of the axis"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"VelocityLimit",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Velocity limit of the axis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AccelerationLimit(aas.Property):

                def __init__(
                    self,
                    value: xsd.Long,
                    id_short: Optional[str] = r"AccelerationLimit",
                    value_type: aas.DataTypeDefXsd = xsd.Long,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/AccelerationLimit/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Accelerationlimit of the axis"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"AccelerationLimit",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Acceleration limit of the axis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class JerkLimit(aas.Property):

                def __init__(
                    self,
                    value: xsd.Long,
                    id_short: Optional[str] = r"JerkLimit",
                    value_type: aas.DataTypeDefXsd = xsd.Long,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/JerkLimit/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Jerk limit of the axis"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"JerkLimit",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Jerk limit of the axis",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class AxisConfigData(aas.SubmodelElementCollection):

                class AxisConfigFileName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AxisConfigFileName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigFileName/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Axis configuration file name"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"AxisConfigFilename",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Configuration filename of the axis",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class AxisConfigFile(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AxisConfigFile",
                        content_type: Optional[str] = r"application/json",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigFile/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Configuration file of the axis"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"AxisConfigFile",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Axis configuration file",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            content_type=content_type,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    axisConfigFileName: Optional[Union[str, AxisConfigFileName]] = None,
                    axisConfigFile: Optional[AxisConfigFile] = None,
                    id_short: Optional[str] = r"AxisConfigData",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Channels/Axes/AxisConfigData/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “AxisConfigData” is a collection of axis configuration data."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"AxisConfigData",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Collection of axis configuration data",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if axisConfigFileName is not None and not isinstance(
                        axisConfigFileName, aas.SubmodelElement
                    ):
                        axisConfigFileName = self.AxisConfigFileName(axisConfigFileName)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [axisConfigFileName, axisConfigFile]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class Drive(aas.SubmodelElementCollection):

                class Manual(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Manual",
                        content_type: Optional[str] = r"application/json",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Manual/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"The manual file of the drive "}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"DriveManual",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Manual file of the drive",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            content_type=content_type,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class TechnicalData(aas.ReferenceElement):

                    def __init__(
                        self,
                        value: aas.Reference,
                        id_short: Optional[str] = r"TechnicalData",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/IDTA/TechnicalData/Submodel/2/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to the Submodel Technical Specification of the axis to gather more information"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"TechnicalData",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Reference to the technical Data of the drive",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                class DriveConfigData(aas.SubmodelElementCollection):

                    class DriveConfigFileName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DriveConfigFileName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"CONSTANT",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/DriveConfigFileName/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of the configuration file of the drive "
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"DriveConfigFileName",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Filename of of the configuration file",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                value_type=value_type,
                                value_id=value_id,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    class DriveConfigFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"DriveConfigFile",
                            content_type: Optional[str] = r"application/json",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/DriveConfigFile/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Configuration File of the drive"}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"DriveConfigFile",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Drive configuration file",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            super().__init__(
                                value=value,
                                id_short=id_short,
                                content_type=content_type,
                                display_name=display_name,
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                extension=extension,
                                supplemental_semantic_id=supplemental_semantic_id,
                                embedded_data_specifications=embedded_data_specifications,
                            )

                    def __init__(
                        self,
                        driveConfigFileName: Optional[
                            Union[str, DriveConfigFileName]
                        ] = None,
                        driveConfigFile: Optional[DriveConfigFile] = None,
                        id_short: Optional[str] = r"DriveConfigData",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/DriveConfigData/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[
                            aas.EmbeddedDataSpecification
                        ] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"The SMC “DriveConfigData” is a collection of drive configuration data."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"DriveConfigData",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Drive configuration data",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if driveConfigFileName is not None and not isinstance(
                            driveConfigFileName, aas.SubmodelElement
                        ):
                            driveConfigFileName = self.DriveConfigFileName(
                                driveConfigFileName
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [driveConfigFileName, driveConfigFile]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, aas.SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(
                                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                                )

                        super().__init__(
                            value=embedded_submodel_elements,
                            id_short=id_short,
                            display_name=display_name,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            extension=extension,
                            supplemental_semantic_id=supplemental_semantic_id,
                            embedded_data_specifications=embedded_data_specifications,
                        )

                def __init__(
                    self,
                    manual: Optional[Manual] = None,
                    technicalData: Optional[Union[aas.Reference, TechnicalData]] = None,
                    driveConfigData: Optional[DriveConfigData] = None,
                    id_short: Optional[str] = r"Drive",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ControlConfig/Axes/Axis/Drive/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The SMC “Drive” is a collection of drive configuration information."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"Drive",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"To be filled; longer explanation",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if technicalData is not None and not isinstance(
                        technicalData, aas.SubmodelElement
                    ):
                        technicalData = self.TechnicalData(technicalData)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [manual, technicalData, driveConfigData]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                axisName: Optional[Union[str, AxisName]] = None,
                axisType: Optional[Union[str, AxisType]] = None,
                simulationAxis: Optional[Union[str, SimulationAxis]] = None,
                swLimitSwitchNeg: Optional[Union[float, SwLimitSwitchNeg]] = None,
                swLimitSwitchPos: Optional[Union[str, SwLimitSwitchPos]] = None,
                velocityLimit: Optional[Union[xsd.Long, VelocityLimit]] = None,
                accelerationLimit: Optional[Union[xsd.Long, AccelerationLimit]] = None,
                jerkLimit: Optional[Union[xsd.Long, JerkLimit]] = None,
                axisConfigData: Optional[AxisConfigData] = None,
                drive: Optional[Drive] = None,
                id_short: Optional[str] = r"Axis",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/Channel/Axis/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The SMC “Axis” is a collection of axis configuration information."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Axis",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of axis specific configuration data",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if axisName is not None and not isinstance(
                    axisName, aas.SubmodelElement
                ):
                    axisName = self.AxisName(axisName)

                # Build a submodel element if a raw value was passed in the argument

                if axisType is not None and not isinstance(
                    axisType, aas.SubmodelElement
                ):
                    axisType = self.AxisType(axisType)

                # Build a submodel element if a raw value was passed in the argument

                if simulationAxis is not None and not isinstance(
                    simulationAxis, aas.SubmodelElement
                ):
                    simulationAxis = self.SimulationAxis(simulationAxis)

                # Build a submodel element if a raw value was passed in the argument

                if swLimitSwitchNeg is not None and not isinstance(
                    swLimitSwitchNeg, aas.SubmodelElement
                ):
                    swLimitSwitchNeg = self.SwLimitSwitchNeg(swLimitSwitchNeg)

                # Build a submodel element if a raw value was passed in the argument

                if swLimitSwitchPos is not None and not isinstance(
                    swLimitSwitchPos, aas.SubmodelElement
                ):
                    swLimitSwitchPos = self.SwLimitSwitchPos(swLimitSwitchPos)

                # Build a submodel element if a raw value was passed in the argument

                if velocityLimit is not None and not isinstance(
                    velocityLimit, aas.SubmodelElement
                ):
                    velocityLimit = self.VelocityLimit(velocityLimit)

                # Build a submodel element if a raw value was passed in the argument

                if accelerationLimit is not None and not isinstance(
                    accelerationLimit, aas.SubmodelElement
                ):
                    accelerationLimit = self.AccelerationLimit(accelerationLimit)

                # Build a submodel element if a raw value was passed in the argument

                if jerkLimit is not None and not isinstance(
                    jerkLimit, aas.SubmodelElement
                ):
                    jerkLimit = self.JerkLimit(jerkLimit)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    axisName,
                    axisType,
                    simulationAxis,
                    swLimitSwitchNeg,
                    swLimitSwitchPos,
                    velocityLimit,
                    accelerationLimit,
                    jerkLimit,
                    axisConfigData,
                    drive,
                ]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            axis: Optional[Axis] = None,
            id_short: Optional[str] = r"Axes",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/Axes/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The SMC “Axes” is a collection of axes of the CNC controller."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Axes",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"List of axes of the specific channel",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"OneToMany",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [axis]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class NCProgramConfig(aas.SubmodelElementCollection):

        class NCProgramFileType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"NCProgramFileType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/NCProgramFileType/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"NC program file type, which the CNC control can work with"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"NCProgramFileType",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"File type (extension) of the NC program file",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class NCProgramSyntaxType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"NCProgramSyntaxType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/NCProgramSyntaxType/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"NC program syntax type"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"NCProgramSyntax",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Syntax of the NC program",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class NCProgramSyntaxManual(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"NCProgramSyntaxManual",
                content_type: Optional[str] = r"application/json",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/NCProgramSyntaxManual/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Manual file of the syntax of the NC program"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Machine code syntax manual file",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"The description of the synatx of the machine code implementation of the cnc machine",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    content_type=content_type,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            nCProgramFileType: Optional[Union[str, NCProgramFileType]] = None,
            nCProgramSyntaxType: Optional[Union[str, NCProgramSyntaxType]] = None,
            nCProgramSyntaxManual: Optional[Iterable[NCProgramSyntaxManual]] = None,
            id_short: Optional[str] = r"NCProgramConfig",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/NCProgramConfig/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The SMC “NCProgramConfig” is a collection of NC program configuration information."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"NCProgramConfig",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Provides NC program informations",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if nCProgramFileType is not None and not isinstance(
                nCProgramFileType, aas.SubmodelElement
            ):
                nCProgramFileType = self.NCProgramFileType(nCProgramFileType)

            # Build a submodel element if a raw value was passed in the argument

            if nCProgramSyntaxType is not None and not isinstance(
                nCProgramSyntaxType, aas.SubmodelElement
            ):
                nCProgramSyntaxType = self.NCProgramSyntaxType(nCProgramSyntaxType)

            # A str would be split into its characters
            if isinstance(nCProgramSyntaxManual, str):
                raise TypeError(
                    "nCProgramSyntaxManual takes several elements, got a str"
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                nCProgramFileType,
                nCProgramSyntaxType,
                nCProgramSyntaxManual,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class CommunicationConfig(aas.SubmodelElementCollection):

        class CommunicationType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CommunicationType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/CommunicationType/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Type of communication to the control"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"CommunicationType",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Type of the communication access to the CNC.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class CommunicationAdress(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CommunicationAdress",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/CommunicationAdress/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Communication address into the control"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"CommunicationAdress",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Type of the communication access to the CNC.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class CommunicationInformationModel(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CommunicationInformationModel",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/CommunicationInformationModel/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Communication information model if ones exist like OPCUA"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"CommunicationInformationModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Information model of the communication configuration",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    value_type=value_type,
                    value_id=value_id,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class OPCUAServerDataSheet(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"OPCUAServerDataSheet",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/opcua-server-datasheet/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to the OPCUA server datasheet Submodel"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"OPCUAServerDataSheet",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Reference to the OPCUA server datasheet Submodel",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    value=value,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            communicationType: Optional[Union[str, CommunicationType]] = None,
            communicationAdress: Optional[Union[str, CommunicationAdress]] = None,
            communicationInformationModel: Optional[
                Union[str, CommunicationInformationModel]
            ] = None,
            oPCUAServerDataSheet: Optional[
                Union[aas.Reference, OPCUAServerDataSheet]
            ] = None,
            id_short: Optional[str] = r"CommunicationConfig",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/CommunicationConfig/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"The SMC “CommunicationConfig” is a collection of communication configuration information."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"CommunicationConfig",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Provides the communication information to access the CNC.",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if communicationType is not None and not isinstance(
                communicationType, aas.SubmodelElement
            ):
                communicationType = self.CommunicationType(communicationType)

            # Build a submodel element if a raw value was passed in the argument

            if communicationAdress is not None and not isinstance(
                communicationAdress, aas.SubmodelElement
            ):
                communicationAdress = self.CommunicationAdress(communicationAdress)

            # Build a submodel element if a raw value was passed in the argument

            if communicationInformationModel is not None and not isinstance(
                communicationInformationModel, aas.SubmodelElement
            ):
                communicationInformationModel = self.CommunicationInformationModel(
                    communicationInformationModel
                )

            # Build a submodel element if a raw value was passed in the argument

            if oPCUAServerDataSheet is not None and not isinstance(
                oPCUAServerDataSheet, aas.SubmodelElement
            ):
                oPCUAServerDataSheet = self.OPCUAServerDataSheet(oPCUAServerDataSheet)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                communicationType,
                communicationAdress,
                communicationInformationModel,
                oPCUAServerDataSheet,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class Tools(aas.SubmodelElementCollection):

        class Tool(aas.SubmodelElementCollection):

            class ToolDescription(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"ToolDescription",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/ToolDescription/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to the tool description Submodel of the specific tool."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"ToolDescription",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Reference to the tool description Submodel of the specific tool.",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            def __init__(
                self,
                toolDescription: Optional[Union[aas.Reference, ToolDescription]] = None,
                id_short: Optional[str] = r"Tool",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/ControlConfig/Tool/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The SMC “Tool” is a collection of tool configuration information."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"Tool",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"One tool of the CNC",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if toolDescription is not None and not isinstance(
                    toolDescription, aas.SubmodelElement
                ):
                    toolDescription = self.ToolDescription(toolDescription)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [toolDescription]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        def __init__(
            self,
            tool: Optional[Iterable[Tool]] = None,
            id_short: Optional[str] = r"Tools",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/ControlConfig/Tools/1/0",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Explanation: The SMC “Tools” is a collection of tools of the CNC controller."
                    }
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"Tools",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"List of tools",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"OneToMany",
                        value_id=None,
                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(tool, str):
                raise TypeError("tool takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [tool]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                    )

            super().__init__(
                value=embedded_submodel_elements,
                id_short=id_short,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    def __init__(
        self,
        id_: str,
        digitalNameplate: Union[aas.Reference, DigitalNameplate],
        controllerType: Union[str, ControllerType],
        timeUnit: Union[xsd.Float, TimeUnit],
        axes: Iterable[Axes],
        tools: Iterable[Tools],
        lengthUnit: Optional[Union[float, LengthUnit]] = None,
        fieldbusType: Optional[Union[str, FieldbusType]] = None,
        cNCCycleTime: Optional[Union[float, CNCCycleTime]] = None,
        pLCCycleTime: Optional[Union[float, PLCCycleTime]] = None,
        fieldbusCycleTime: Optional[Union[float, FieldbusCycleTime]] = None,
        velocityUnit: Optional[Union[str, VelocityUnit]] = None,
        accelerationUnit: Optional[Union[str, AccelerationUnit]] = None,
        jerkUnit: Optional[Union[str, JerkUnit]] = None,
        controlConfigData: Optional[Iterable[ControlConfigData]] = None,
        channels: Optional[Iterable[Channels]] = None,
        nCProgramConfig: Optional[NCProgramConfig] = None,
        communicationConfig: Optional[CommunicationConfig] = None,
        id_short: Optional[str] = r"ControlConfig",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/ControlConfig/1/0",
                ),
            ),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel “ControlConfig” is the collection for various parametrizations for the control of CNC machines "
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02053-1-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if digitalNameplate is not None and not isinstance(
            digitalNameplate, aas.SubmodelElement
        ):
            digitalNameplate = self.DigitalNameplate(digitalNameplate)

        # Build a submodel element if a raw value was passed in the argument

        if controllerType is not None and not isinstance(
            controllerType, aas.SubmodelElement
        ):
            controllerType = self.ControllerType(controllerType)

        # Build a submodel element if a raw value was passed in the argument

        if timeUnit is not None and not isinstance(timeUnit, aas.SubmodelElement):
            timeUnit = self.TimeUnit(timeUnit)

        # Build a submodel element if a raw value was passed in the argument

        if lengthUnit is not None and not isinstance(lengthUnit, aas.SubmodelElement):
            lengthUnit = self.LengthUnit(lengthUnit)

        # Build a submodel element if a raw value was passed in the argument

        if fieldbusType is not None and not isinstance(
            fieldbusType, aas.SubmodelElement
        ):
            fieldbusType = self.FieldbusType(fieldbusType)

        # Build a submodel element if a raw value was passed in the argument

        if cNCCycleTime is not None and not isinstance(
            cNCCycleTime, aas.SubmodelElement
        ):
            cNCCycleTime = self.CNCCycleTime(cNCCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if pLCCycleTime is not None and not isinstance(
            pLCCycleTime, aas.SubmodelElement
        ):
            pLCCycleTime = self.PLCCycleTime(pLCCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if fieldbusCycleTime is not None and not isinstance(
            fieldbusCycleTime, aas.SubmodelElement
        ):
            fieldbusCycleTime = self.FieldbusCycleTime(fieldbusCycleTime)

        # Build a submodel element if a raw value was passed in the argument

        if velocityUnit is not None and not isinstance(
            velocityUnit, aas.SubmodelElement
        ):
            velocityUnit = self.VelocityUnit(velocityUnit)

        # Build a submodel element if a raw value was passed in the argument

        if accelerationUnit is not None and not isinstance(
            accelerationUnit, aas.SubmodelElement
        ):
            accelerationUnit = self.AccelerationUnit(accelerationUnit)

        # Build a submodel element if a raw value was passed in the argument

        if jerkUnit is not None and not isinstance(jerkUnit, aas.SubmodelElement):
            jerkUnit = self.JerkUnit(jerkUnit)

        # A str would be split into its characters
        if isinstance(controlConfigData, str):
            raise TypeError("controlConfigData takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(channels, str):
            raise TypeError("channels takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(axes, str):
            raise TypeError("axes takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(tools, str):
            raise TypeError("tools takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            digitalNameplate,
            controllerType,
            timeUnit,
            lengthUnit,
            fieldbusType,
            cNCCycleTime,
            pLCCycleTime,
            fieldbusCycleTime,
            velocityUnit,
            accelerationUnit,
            jerkUnit,
            controlConfigData,
            channels,
            axes,
            nCProgramConfig,
            communicationConfig,
            tools,
        ]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, aas.SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                )

        super().__init__(
            submodel_element=embedded_submodel_elements,
            id_=id_,
            id_short=id_short,
            display_name=display_name,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
            extension=extension,
            supplemental_semantic_id=supplemental_semantic_id,
            embedded_data_specifications=embedded_data_specifications,
        )
