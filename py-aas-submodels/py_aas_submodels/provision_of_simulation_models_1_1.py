from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class SimulationModels(aas.Submodel):

    class SimulationModel(aas.SubmodelElementCollection):

        class Summary(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"Summary",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/Summary/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Summary"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Specifies Summary."}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"summary",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Summary of the contents of the simulation model in text form. ",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"summary",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
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

        class SimPurpose(aas.SubmodelElementCollection):

            class PosSimPurpose(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PosSimPurpose",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/PosSimPurpose/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Pos Sim Purpose"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of simulation purposes for which the model is intended."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"posSimPurpose",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"List of simulation purposes for which the model is intended.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="posSimPurpose'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"Concept evaluation; Sizing; Energy consumption; Control design; Behaviour in fault condition; Validation and testing; Virtual commissioning; Condition monitoring; Predictive maintenance; Operator Training; Teaching",
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

            class NegSimPurpose(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NegSimPurpose",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/NegSimPurpose/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Neg Sim Purpose"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of simulation purposes for which the model is explicitly not suitable."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"negSimPurpose",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"List of simulation purposes for which the model is explicitly not suitable. ",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="negSimPurpose'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"Concept evaluation; Sizing; Energy consumption; Control design; Behaviour in fault condition; Validation and testing; Virtual commissioning; Condition monitoring; Predictive maintenance; Operator Training; Teaching",
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

            def __init__(
                self,
                posSimPurpose: Iterable[Union[str, PosSimPurpose]],
                negSimPurpose: Optional[Iterable[Union[str, NegSimPurpose]]] = None,
                id_short: Optional[str] = r"SimPurpose",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/SimPurpose/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Sim Purpose"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"This characteristic describes the simulation purpose or suitability for different simulation goals."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"simPurpose",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"This characteristic describes the simulation purpose or suitability for different simulation goals.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"simPurpose",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(posSimPurpose, str):
                    raise TypeError("posSimPurpose takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if posSimPurpose:
                    posSimPurpose = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.PosSimPurpose(i)
                        )
                        for i in posSimPurpose
                    ]

                # A str would be split into its characters
                if isinstance(negSimPurpose, str):
                    raise TypeError("negSimPurpose takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if negSimPurpose:
                    negSimPurpose = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.NegSimPurpose(i)
                        )
                        for i in negSimPurpose
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [posSimPurpose, negSimPurpose]:
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

        class TypeOfModel(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TypeOfModel",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/TypeOfModel/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Type Of Model"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of modeling approaches used for the model."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"typeOfModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of modeling approaches used for the model.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"typeOfModelDesc",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"Linear model; Nonlinear model; Data-driven model; Lumped element model; Fixed causality model; Acausal model ",
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

        class ScopeOfModel(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ScopeOfModel",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/ScopeOfModel/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Scope Of Model"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of basic physical characteristics which are represented by the model."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"scopeOfModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of basic physical characteristics which are represented by the model.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"scopeOfModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"Logic and timing behaviour; Geometry; Kinematics; Dynamics; Distribution networks; Network communication; Visualization",
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

        class LicenseModel(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"LicenseModel",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/LicenseModel/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"License Model"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"If a simulation model usage will be charged and how it will be charged."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"licenseModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"If a simulation model usage will be charged and how it will be charged.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"licenseModel",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"free; perpetual; subscription; volume-based",
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

        class EngineeringDomain(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"EngineeringDomain",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/EngineeringDomain/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Engineering Domain"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of engineering disciplines supported or mapped with the model."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"engineeringDomainList",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"List of engineering disciplines supported or mapped with the model. ",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value="engineeringDomainList'{0:00}'",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"Hydraulic Engineering; Electrical Engineering; Pneumatic Engineering; Mechanical Engineering; Material Flow; Robotics; Image Processing; Data Engineering; Process Engineering; Workflow Engineering; HMI Engineering; Control Engineering",
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

        class Environment(aas.SubmodelElementCollection):

            class OperatingSystem(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"OperatingSystem",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/OperatingSystem/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Operating System"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Name of the operating system including version and architecture (e.g. Windows 10 64bit)"
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"operatingSystem",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Name of the operating system including version and architecture (e.g. Windows 10 64bit)",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="operatingSystem'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class ToolEnvironment(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ToolEnvironment",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/ToolEnvironment/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Tool Environment"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List with required simulation tools, interpreters, model libraries or runtime libraries. In each case the exact designation of the software producer is given as free text."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"toolEnvironment",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"List with required simulation tools, interpreters, model libraries or runtime libraries. In each case the exact designation of the software producer is given as free text.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="toolEnvironment'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
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

            class DependencyEnvironment(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"DependencyEnvironment",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/DependencyEnvironment/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Dependency Environment"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of dependencies to associated hardware and software."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"dependencyEnvironment",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Description of dependencies to associated hardware and software. ",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"dependencyEnvironment",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
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

            class VisualizationInformation(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"VisualizationInformation",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/VisualizationInformation/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Visualization Information"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Ability to use a visualization. This can be integrated in a model or the model offers capabilities for connection. The connection can be described in more detail under Ports."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"visualizationInformation",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Ability to use a visualization. This can be integrated in a model or the model offers capabilities for connection. The connection can be described in more detail under ports.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"visualizationInformation",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormChoices",
                                value_type=str,
                                value=r"separately; integrated; none",
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

            class SimulationTool(aas.SubmodelElementCollection):

                class SimToolName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"SimToolName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/SimToolName/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Sim Tool Name"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Specifies Sim Tool Name."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"simToolName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Name of the simulation tool including version.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"simToolName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class DependencySimTool(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DependencySimTool",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/DependencySimTool/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Dependency Sim Tool"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Dependencies of Simulation Tools"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"dependencySimTool",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Dependencies of Simulation Tools",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value="dependencySimTool'{0:00}'",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToMany",
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

                class Compiler(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Compiler",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/Compiler/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Compiler"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name of necessary compiler including version"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"compiler",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Name of necessary compiler including version",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value="compiler'{0:00}'",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToMany",
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

                class SolverAndTolerances(aas.SubmodelElementCollection):

                    class StepSizeControlNeeded(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"StepSizeControlNeeded",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/StepSizeControlNeeded/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Step Size Control Needed"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Solver with step size control recommended."
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"stepSizeControlNeeded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Solver with step size control recommended.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"stepSizeControlNeeded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"True; False",
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

                    class FixedStepSize(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Float,
                            id_short: Optional[str] = r"FixedStepSize",
                            value_type: aas.DataTypeDefXsd = xsd.Float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/FixedStepSize/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Fixed Step Size"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Fixed integration step size, if there is no adaptive step size"
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"fixedStepSize",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Fixed integration step size, if there is no adaptive step size ",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"fixedStepSize",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToOne",
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

                    class StiffSolverNeeded(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"StiffSolverNeeded",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/StiffSolverNeeded/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Stiff Solver Needed"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Stiff solver needed."}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"stiffSolverNeeded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Stiff solver needed.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"stiffSolverNeeded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"True; False",
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

                    class SolverIncluded(aas.Property):

                        def __init__(
                            self,
                            value: bool,
                            id_short: Optional[str] = r"SolverIncluded",
                            value_type: aas.DataTypeDefXsd = bool,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/SolverIncluded/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Solver Included"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Solver is integrated in the model (e.g. FMU for co-simulation)"
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"solverIncluded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Solver is integrated in the model (e.g. FMU for co-simulation)",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"solverIncluded",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"True; False",
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

                    class TestedToolSolverAlgorithm(aas.SubmodelElementCollection):

                        class SolverAlgorithm(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"SolverAlgorithm",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/SimulationModels/SolverAlgorithm/1/0",
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Solver Algorithm"}
                                    )

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={r"en": r"validated solver"}
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"FormTitle",
                                            value_type=str,
                                            value=r"solverAlgorithm",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"FormInfo",
                                            value_type=str,
                                            value=r"validated solver",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"PresetIdShort",
                                            value_type=str,
                                            value=r"solverAlgorithm",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Multiplicity",
                                            value_type=str,
                                            value=r"One",
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

                        class ToolSolverFurtherDescription(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[
                                    str
                                ] = r"ToolSolverFurtherDescription",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/SimulationModels/ToolSolverFurtherDescription/1/0",
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={
                                            r"en": r"Tool Solver Further Description"
                                        }
                                    )

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Further tool- and solver-specific information"
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"FormTitle",
                                            value_type=str,
                                            value=r"toolSolverFurtherDescription",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"FormInfo",
                                            value_type=str,
                                            value=r"Further tool- and solver-specific information",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"PresetIdShort",
                                            value_type=str,
                                            value=r"toolSolverFurtherDescription",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Multiplicity",
                                            value_type=str,
                                            value=r"ZeroToOne",
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

                        class Tolerance(aas.Property):

                            def __init__(
                                self,
                                value: xsd.Float,
                                id_short: Optional[str] = r"Tolerance",
                                value_type: aas.DataTypeDefXsd = xsd.Float,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[
                                    aas.MultiLanguageNameType
                                ] = None,
                                category: Optional[str] = None,
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[
                                    aas.Reference
                                ] = aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/SimulationModels/Tolerance/1/0",
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

                                if display_name is None:
                                    display_name = aas.MultiLanguageNameType(
                                        dict_={r"en": r"Tolerance"}
                                    )

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"(relative) tolerance for theadaptive step size"
                                        }
                                    )

                                if qualifier is None:
                                    qualifier = (
                                        aas.Qualifier(
                                            type_=r"FormTitle",
                                            value_type=str,
                                            value=r"tolerance",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"FormInfo",
                                            value_type=str,
                                            value=r"(relative) tolerance for theadaptive step size ",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"PresetIdShort",
                                            value_type=str,
                                            value=r"tolerance",
                                            value_id=None,
                                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                            semantic_id=None,
                                            supplemental_semantic_id=(),
                                        ),
                                        aas.Qualifier(
                                            type_=r"Multiplicity",
                                            value_type=str,
                                            value=r"ZeroToOne",
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

                        def __init__(
                            self,
                            solverAlgorithm: Union[str, SolverAlgorithm],
                            toolSolverFurtherDescription: Optional[
                                Union[str, ToolSolverFurtherDescription]
                            ] = None,
                            tolerance: Optional[Union[xsd.Float, Tolerance]] = None,
                            id_short: Optional[str] = r"TestedToolSolverAlgorithm",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/TestedToolSolverAlgorithm/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Tested Tool Solver Algorithm"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"List of validated tool-solver combinations"
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"testedToolSolverAlgorithm",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"List of validated tool-solver combinations",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value="testedToolSolverAlgorithm'{0:00}'",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToMany",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                )

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if solverAlgorithm is not None and not isinstance(
                                solverAlgorithm, aas.SubmodelElement
                            ):
                                solverAlgorithm = self.SolverAlgorithm(solverAlgorithm)

                            # Build a submodel element if a raw value was passed in the argument

                            if (
                                toolSolverFurtherDescription is not None
                                and not isinstance(
                                    toolSolverFurtherDescription, aas.SubmodelElement
                                )
                            ):
                                toolSolverFurtherDescription = (
                                    self.ToolSolverFurtherDescription(
                                        toolSolverFurtherDescription
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument

                            if tolerance is not None and not isinstance(
                                tolerance, aas.SubmodelElement
                            ):
                                tolerance = self.Tolerance(tolerance)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                solverAlgorithm,
                                toolSolverFurtherDescription,
                                tolerance,
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
                        stepSizeControlNeeded: Union[bool, StepSizeControlNeeded],
                        stiffSolverNeeded: Union[bool, StiffSolverNeeded],
                        solverIncluded: Union[bool, SolverIncluded],
                        fixedStepSize: Optional[Union[xsd.Float, FixedStepSize]] = None,
                        testedToolSolverAlgorithm: Optional[
                            Iterable[TestedToolSolverAlgorithm]
                        ] = None,
                        id_short: Optional[str] = r"SolverAndTolerances",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/SolverAndTolerances/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Solver And Tolerances"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Useful settings of the simulation environment. Includes e.g. solver settings."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"solverAndTolerances",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Useful settings of the simulation environment. Includes e.g. solver settings. ",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"solverAndTolerances",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if stepSizeControlNeeded is not None and not isinstance(
                            stepSizeControlNeeded, aas.SubmodelElement
                        ):
                            stepSizeControlNeeded = self.StepSizeControlNeeded(
                                stepSizeControlNeeded
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if fixedStepSize is not None and not isinstance(
                            fixedStepSize, aas.SubmodelElement
                        ):
                            fixedStepSize = self.FixedStepSize(fixedStepSize)

                        # Build a submodel element if a raw value was passed in the argument

                        if stiffSolverNeeded is not None and not isinstance(
                            stiffSolverNeeded, aas.SubmodelElement
                        ):
                            stiffSolverNeeded = self.StiffSolverNeeded(
                                stiffSolverNeeded
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if solverIncluded is not None and not isinstance(
                            solverIncluded, aas.SubmodelElement
                        ):
                            solverIncluded = self.SolverIncluded(solverIncluded)

                        # A str would be split into its characters
                        if isinstance(testedToolSolverAlgorithm, str):
                            raise TypeError(
                                "testedToolSolverAlgorithm takes several elements, got a str"
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            stepSizeControlNeeded,
                            fixedStepSize,
                            stiffSolverNeeded,
                            solverIncluded,
                            testedToolSolverAlgorithm,
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
                    simToolName: Union[str, SimToolName],
                    solverAndTolerances: SolverAndTolerances,
                    dependencySimTool: Optional[
                        Iterable[Union[str, DependencySimTool]]
                    ] = None,
                    compiler: Optional[Iterable[Union[str, Compiler]]] = None,
                    id_short: Optional[str] = r"SimulationTool",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/SimulationTool/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Simulation Tool"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Properties of the model with regarding to concrete simulation tools"
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"simulationTool",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Eigenschaften des Modells bezüglich konkreter Simulationswerkzeuge.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="simulationTool'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if simToolName is not None and not isinstance(
                        simToolName, aas.SubmodelElement
                    ):
                        simToolName = self.SimToolName(simToolName)

                    # A str would be split into its characters
                    if isinstance(dependencySimTool, str):
                        raise TypeError(
                            "dependencySimTool takes several elements, got a str"
                        )

                    # Build submodel elements from raw values passed in the argument
                    if dependencySimTool:
                        dependencySimTool = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.DependencySimTool(i)
                            )
                            for i in dependencySimTool
                        ]

                    # A str would be split into its characters
                    if isinstance(compiler, str):
                        raise TypeError("compiler takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if compiler:
                        compiler = [
                            (
                                i
                                if isinstance(i, aas.SubmodelElement)
                                else self.Compiler(i)
                            )
                            for i in compiler
                        ]

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        simToolName,
                        dependencySimTool,
                        compiler,
                        solverAndTolerances,
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
                operatingSystem: Union[str, OperatingSystem],
                simulationTool: Iterable[SimulationTool],
                toolEnvironment: Optional[Iterable[Union[str, ToolEnvironment]]] = None,
                dependencyEnvironment: Optional[
                    Union[aas.LangStringSet, DependencyEnvironment]
                ] = None,
                visualizationInformation: Optional[
                    Union[str, VisualizationInformation]
                ] = None,
                id_short: Optional[str] = r"Environment",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/Environment/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Environment"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about prerequisite environments or dependencies of underlying components on the target system."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"environment",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Information about prerequisite environments or dependencies of underlying components on the target system.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"environment",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if operatingSystem is not None and not isinstance(
                    operatingSystem, aas.SubmodelElement
                ):
                    operatingSystem = self.OperatingSystem(operatingSystem)

                # A str would be split into its characters
                if isinstance(toolEnvironment, str):
                    raise TypeError("toolEnvironment takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if toolEnvironment:
                    toolEnvironment = [
                        (
                            i
                            if isinstance(i, aas.SubmodelElement)
                            else self.ToolEnvironment(i)
                        )
                        for i in toolEnvironment
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if dependencyEnvironment is not None and not isinstance(
                    dependencyEnvironment, aas.SubmodelElement
                ):
                    dependencyEnvironment = self.DependencyEnvironment(
                        dependencyEnvironment
                    )

                # Build a submodel element if a raw value was passed in the argument

                if visualizationInformation is not None and not isinstance(
                    visualizationInformation, aas.SubmodelElement
                ):
                    visualizationInformation = self.VisualizationInformation(
                        visualizationInformation
                    )

                # A str would be split into its characters
                if isinstance(simulationTool, str):
                    raise TypeError("simulationTool takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    operatingSystem,
                    toolEnvironment,
                    dependencyEnvironment,
                    visualizationInformation,
                    simulationTool,
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

        class RefSimDocumentation(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"RefSimDocumentation",
                content_type: Optional[str] = r"application/pdf",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/RefSimDocumentation/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Ref Sim Documentation"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Documentation of example simulations of the model can be supplied. This includes a solver setup and sample circuit and sample results. e.g. zip file, PDF, html, ..."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"refSimDocumentation",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Documentation of example simulations of the model can be supplied. This includes a solver setup and sample circuit and sample results. e.g. zip file, PDF, html, ...",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value="refSimDocumentation'{0:00}'",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
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

        class ModelFile(aas.SubmodelElementCollection):

            class ModelFileType(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ModelFileType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/ModelFileType/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Model File Type"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'"Designation of the exchange format of the model. E.G.: FMI 1.0, Co-Simulation, Platform / Source - Code. FMI 2.0.2, Model Exchange, Source - Code, S-function, Version 2, 64bit, mex - Format / or C-Code, Modelica 3, encoded, VHDL'
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"modelFileType",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r'"Designation of the exchange format of the model. E.G.: FMI 1.0, Co-Simulation, Platform / Source - Code. FMI 2.0.2, Model Exchange, Source - Code. S-function, Version 2, 64bit, mex - Format / or C-Code. Modelica 3, encoded. VHDL',
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"modelFileType",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
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

            class ModelFileVersion(aas.SubmodelElementCollection):

                class ModelVersionId(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ModelVersionId",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/ModelVersionId/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Model Version Id"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Version number of the model from the vendor."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"modelVersionId",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Version number of the model from the vendor.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"modelVersionId",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class ModelPreviewImage(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ModelPreviewImage",
                        content_type: Optional[str] = r"image/png",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/ModelPreviewImage/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Model Preview Image"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Image file to represent the model in user interfaces, e.g. in a search."
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"modelPreviewImage",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Image file to represent the model in user interfaces, e.g. in a search.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"modelPreviewImage",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class DigitalFile(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"DigitalFile",
                        content_type: Optional[str] = r"application/octet-stream",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/DigitalFile/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Digital File"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Deployment of the model file."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"digitalFile",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Deployment of the model file.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"digitalFile",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class ModelFileReleaseNotesTxt(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"ModelFileReleaseNotesTxt",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesTxt/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Model File Release Notes Txt"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"contains information about this release"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"modelFileReleaseNotesTxt",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"contains information about this release",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"modelFileReleaseNotesTxt",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class ModelFileReleaseNotesFile(aas.File):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ModelFileReleaseNotesFile",
                        content_type: Optional[str] = r"text/plain",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/ModelFileReleaseNotesFile/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Model File Release Notes File"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"release notes link or file"}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"modelFileReleaseNotesFile",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"release notes link or file",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"modelFileReleaseNotesFile",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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
                    modelVersionId: Union[str, ModelVersionId],
                    digitalFile: DigitalFile,
                    modelPreviewImage: Optional[ModelPreviewImage] = None,
                    modelFileReleaseNotesTxt: Optional[
                        Union[aas.LangStringSet, ModelFileReleaseNotesTxt]
                    ] = None,
                    modelFileReleaseNotesFile: Optional[
                        ModelFileReleaseNotesFile
                    ] = None,
                    id_short: Optional[str] = r"ModelFileVersion",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/ModelFileVersion/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Model File Version"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Provision of a version of the simulation model with information to distinguish the versions. The versions are primarily intended for bug fixes without content changes."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"modelFileVersion",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Provision of a version of the simulation model with information to distinguish the versions. The versions are primarily intended for bug fixes without content changes.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="modelFileVersion'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if modelVersionId is not None and not isinstance(
                        modelVersionId, aas.SubmodelElement
                    ):
                        modelVersionId = self.ModelVersionId(modelVersionId)

                    # Build a submodel element if a raw value was passed in the argument

                    if modelFileReleaseNotesTxt is not None and not isinstance(
                        modelFileReleaseNotesTxt, aas.SubmodelElement
                    ):
                        modelFileReleaseNotesTxt = self.ModelFileReleaseNotesTxt(
                            modelFileReleaseNotesTxt
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        modelVersionId,
                        modelPreviewImage,
                        digitalFile,
                        modelFileReleaseNotesTxt,
                        modelFileReleaseNotesFile,
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
                modelFileVersion: Iterable[ModelFileVersion],
                modelFileType: Optional[Union[str, ModelFileType]] = None,
                id_short: Optional[str] = r"ModelFile",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/ModelFile/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Model File"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Providing versions of the simulation model and with characteristics to distinguish them."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"modelFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Providing versions of the simulation model and with characteristics to distinguish them.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"modelFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if modelFileType is not None and not isinstance(
                    modelFileType, aas.SubmodelElement
                ):
                    modelFileType = self.ModelFileType(modelFileType)

                # A str would be split into its characters
                if isinstance(modelFileVersion, str):
                    raise TypeError(
                        "modelFileVersion takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [modelFileType, modelFileVersion]:
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

        class ParamMethod(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ParamMethod",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/ParamMethod/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Param Method"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates whether the model must be parameterized and if so, which method is required."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"paramMethod",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Indicates whether the model must be parameterized and if so, which method is required.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"paramMethod",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r'by using "technical data" of asset; by using "technical data" and user; by user interface; by setting file; not necessary; by documentation file; pre-parametrized',
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

        class ParamFile(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ParamFile",
                content_type: Optional[str] = r"text/plain",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/ParamFile/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Param File"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"File for parameterization of the model. As parameter file or parameter documentation (e.g. pdf)."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"paramFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"File for parameterization of the model. As parameter file or parameter documentation (e.g. pdf). ",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"paramFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
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

        class InitStateMethod(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InitStateMethod",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/InitStateMethod/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Init State Method"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r'" Describes the state variables of the simulation model that must be initialized to start the simulation. For initial value problems, these quantities describe the system state at the start of the simulation. In this case, the system is in a state of equilibrium. Alternatively, a simulation model may include a method to determine consistent initial values at this step, e.g., at an operating point.'
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"initStateMethod",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r'" Describes the state variables of the simulation model that must be initialized to start the simulation. For initial value problems, these quantities describe the system state at the start of the simulation. In this case, the system is in a state of equilibrium. Alternatively, a simulation model may include a method to determine consistent initial values at this step, e.g., at an operating point. ',
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"initStateMethod",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormChoices",
                            value_type=str,
                            value=r"not necessary, by user interface; by setting file; set states within simulation environment; integrated in model; by documentation file",
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

        class InitStateFile(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"InitStateFile",
                content_type: Optional[str] = r"text/plain",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/InitStateFile/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Init State File"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"File for parameterizing the initial states of the model. As parameter file or parameter documentation (e.g. pdf)."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"initStateFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"File for parameterizing the initial states of the model. As parameter file or parameter documentation (e.g. pdf). ",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"initStateFile",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
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

        class DefaultSimTime(aas.Property):

            def __init__(
                self,
                value: xsd.Float,
                id_short: Optional[str] = r"DefaultSimTime",
                value_type: aas.DataTypeDefXsd = xsd.Float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/DefaultSimTime/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Default Sim Time"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Predefined simulation period in seconds"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"defaultSimTime",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Predefined simulation period in seconds ",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"defaultSimTime",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
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

        class SimModManufacturerInformation(aas.SubmodelElementCollection):

            class Company(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Company",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAW001#001",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Company"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"name of the company"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"company",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"name of the company",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"company",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class Language(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Language",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO895#003",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Language"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"available language"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"language",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"available language",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="language'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"OneToMany",
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

            class Email(aas.SubmodelElementCollection):

                class TypeOfEmailAddress(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfEmailAddress",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO199#003",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Type Of Email Address"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"characterization of an e-mail address according to its location or usage"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"typeOfEmailAddress",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"characterization of an e-mail address according to its location or usage",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"typeOfEmailAddress",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class EmailAddress(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"EmailAddress",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO198#002",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Email Address"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"electronic mail address of a business partner"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"emailAddress",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"electronic mail address of a business partner",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"emailAddress",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class TypeOfPublicKey(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfPublicKey",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO201#002",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Type Of Public Key"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"characterization of a public key according to its encryption process"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"typeOfPublicKey",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"characterization of a public key according to its encryption process",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"typeOfPublicKey",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class PublicKey(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"PublicKey",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO200#002",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Public Key"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"public part of an unsymmetrical key pair to sign or encrypt text or messages"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"publicKey",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"public part of an unsymmetrical key pair to sign or encrypt text or messages",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"publicKey",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                def __init__(
                    self,
                    emailAddress: Union[str, EmailAddress],
                    typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                    typeOfPublicKey: Optional[Union[str, TypeOfPublicKey]] = None,
                    publicKey: Optional[Union[str, PublicKey]] = None,
                    id_short: Optional[str] = r"Email",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAQ836#005",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Email"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"E-mail address and encryption method"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"email",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"E-mail address and encryption method",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"email",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfEmailAddress is not None and not isinstance(
                        typeOfEmailAddress, aas.SubmodelElement
                    ):
                        typeOfEmailAddress = self.TypeOfEmailAddress(typeOfEmailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if emailAddress is not None and not isinstance(
                        emailAddress, aas.SubmodelElement
                    ):
                        emailAddress = self.EmailAddress(emailAddress)

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfPublicKey is not None and not isinstance(
                        typeOfPublicKey, aas.SubmodelElement
                    ):
                        typeOfPublicKey = self.TypeOfPublicKey(typeOfPublicKey)

                    # Build a submodel element if a raw value was passed in the argument

                    if publicKey is not None and not isinstance(
                        publicKey, aas.SubmodelElement
                    ):
                        publicKey = self.PublicKey(publicKey)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [
                        typeOfEmailAddress,
                        emailAddress,
                        typeOfPublicKey,
                        publicKey,
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

            class Phone(aas.SubmodelElementCollection):

                class TypeOfTelephone(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TypeOfTelephone",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO137#003",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Type Of Telephone"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"characterization of a telephone according to its location or usage"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"typeOfTelephone",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"characterization of a telephone according to its location or usage",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"typeOfTelephone",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class TelephoneNumber(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"TelephoneNumber",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAO136#002",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Telephone Number"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"complete telephone number to be called to reach a business partner"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"telephoneNumber",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"complete telephone number to be called to reach a business partner",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"telephoneNumber",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class AvailableTime(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"AvailableTime",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Available Time"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Specification of the available time window"
                                }
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"availableTime",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Specification of the available time window",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"availableTime",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                def __init__(
                    self,
                    telephoneNumber: Union[str, TelephoneNumber],
                    typeOfTelephone: Optional[Union[str, TypeOfTelephone]] = None,
                    availableTime: Optional[Union[str, AvailableTime]] = None,
                    id_short: Optional[str] = r"Phone",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Phone"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Phone number including type"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"phone",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Phone number including type",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"phone",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if typeOfTelephone is not None and not isinstance(
                        typeOfTelephone, aas.SubmodelElement
                    ):
                        typeOfTelephone = self.TypeOfTelephone(typeOfTelephone)

                    # Build a submodel element if a raw value was passed in the argument

                    if telephoneNumber is not None and not isinstance(
                        telephoneNumber, aas.SubmodelElement
                    ):
                        telephoneNumber = self.TelephoneNumber(telephoneNumber)

                    # Build a submodel element if a raw value was passed in the argument

                    if availableTime is not None and not isinstance(
                        availableTime, aas.SubmodelElement
                    ):
                        availableTime = self.AvailableTime(availableTime)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [typeOfTelephone, telephoneNumber, availableTime]:
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
                company: Union[str, Company],
                language: Iterable[Union[str, Language]],
                email: Optional[Email] = None,
                phone: Optional[Phone] = None,
                id_short: Optional[str] = r"SimModManufacturerInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/SimModManufacturerInformation/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"Sim Mod Manufacturer Information"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provide access to  simulation support service provided by the distributor via mail or phone"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"simModManufacturerInformation",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Provide access to  simulation support service provided by the distributor via mail or phone",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value="simModManufacturerInformation'{0:00}'",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if company is not None and not isinstance(company, aas.SubmodelElement):
                    company = self.Company(company)

                # A str would be split into its characters
                if isinstance(language, str):
                    raise TypeError("language takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if language:
                    language = [
                        i if isinstance(i, aas.SubmodelElement) else self.Language(i)
                        for i in language
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [company, language, email, phone]:
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

        class Ports(aas.SubmodelElementCollection):

            class PortsConnector(aas.SubmodelElementCollection):

                class PortConnectorName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"PortConnectorName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/PortsConnectorName/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Port Connector Name"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Name of the Connector Port."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"portConnectorName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Name of the Connector Port.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"portConnectorName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class PortConDescription(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"PortConDescription",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/portConDescription/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Port Con Description"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Specifies Port Con Description."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"portConDescription",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Description of the Connector Port.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"portConDescription",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                class Variable(aas.SubmodelElementCollection):

                    class VariableName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"VariableName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/VariableName/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Variable Name"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Name of the variable."}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"variableName",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Name of the variable.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"variableName",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
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

                    class Range(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Range",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/Range/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Range"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Range of values for the variable (e.g. [min, max], [min, max[, ]min, max], ]min, max[, {val1, val2, ...})."
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"range",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Range of values for the variable (e.g. [min, max], [min, max[, ]min, max], ]min, max[, {val1, val2, ...}).",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"range",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToOne",
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

                    class VariableType(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"VariableType",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/VariableType/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Variable Type"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Type of the variable (e.g. Real, Integer, Boolean, String or Enum)."
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"variableType",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Type of the variable (e.g. Real, Integer, Boolean, String or Enum).",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"variableType",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"Real; Integer; Boolean; String; ENUM",
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

                    class VariableDescription(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"VariableDescription",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/VariableDescription/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Variable Description"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Description of the variable."}
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"variableDescription",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Description of the variable.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"variableDescription",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToOne",
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

                    class UnitList(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"UnitList",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/UnitList/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Unit List"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r'The most common units can be selected here. .. If "others" is selected, a free text can be entered.'
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"unitList",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r'The most common units can be selected here. .. If "others" is selected, a free text can be entered.',
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"unitList",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"s; m; kg; N; m/s; m/s^2; V; A; K; none",
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

                    class UnitDescription(aas.MultiLanguageProperty):

                        def __init__(
                            self,
                            value: aas.LangStringSet,
                            id_short: Optional[str] = r"UnitDescription",
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/UnitDescription/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Unit Description"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Text field for missing units of the list"
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"unitDescription",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"Text field for missing units of the list.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"unitDescription",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToOne",
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

                    class VariableCausality(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"VariableCausality",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/VariableCausality/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Variable Causality"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"The causality of the variable: input to inputs, output to ouputs, acausal connections (e.g. mechanical connection) do not have causality."
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"variableCausality",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value=r"The causality of the variable: input to inputs, output to ouputs, acausal connections (e.g. mechanical connection) do not have causality.",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"variableCausality",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"input; output; acausal",
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

                    class VariablePrefix(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"VariablePrefix",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/SimulationModels/VariablePrefix/1/0",
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

                            if display_name is None:
                                display_name = aas.MultiLanguageNameType(
                                    dict_={r"en": r"Variable Prefix"}
                                )

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": 'Prefix for acausal variable. Potential variables are set equal when connecting (no prefix). Stream variables are connected according to Kirchhoff\'s law, i.e. the sum of the variables equals zero. The bi-directional flow of matter is described with "stream" (e.g. for enthalpy).'
                                    }
                                )

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"FormTitle",
                                        value_type=str,
                                        value=r"variablePrefix",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormInfo",
                                        value_type=str,
                                        value='Prefix for acausal variable. Potential variables are set equal when connecting (no prefix). Stream variables are connected according to Kirchhoff\'s law, i.e. the sum of the variables equals zero. The bi-directional flow of matter is described with "stream" (e.g. for enthalpy).',
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"PresetIdShort",
                                        value_type=str,
                                        value=r"variablePrefix",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"Multiplicity",
                                        value_type=str,
                                        value=r"ZeroToOne",
                                        value_id=None,
                                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                        semantic_id=None,
                                        supplemental_semantic_id=(),
                                    ),
                                    aas.Qualifier(
                                        type_=r"FormChoices",
                                        value_type=str,
                                        value=r"Flow; Stream",
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

                    def __init__(
                        self,
                        variableName: Union[str, VariableName],
                        variableType: Union[str, VariableType],
                        unitList: Union[str, UnitList],
                        variableCausality: Union[str, VariableCausality],
                        range: Optional[Union[str, Range]] = None,
                        variableDescription: Optional[
                            Union[aas.LangStringSet, VariableDescription]
                        ] = None,
                        unitDescription: Optional[
                            Union[aas.LangStringSet, UnitDescription]
                        ] = None,
                        variablePrefix: Optional[Union[str, VariablePrefix]] = None,
                        id_short: Optional[str] = r"Variable",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/Variable/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Variable"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"List of variables of the port."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"variable",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"List of variables of the port.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"variable{0:00}",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if variableName is not None and not isinstance(
                            variableName, aas.SubmodelElement
                        ):
                            variableName = self.VariableName(variableName)

                        # Build a submodel element if a raw value was passed in the argument

                        if range is not None and not isinstance(
                            range, aas.SubmodelElement
                        ):
                            range = self.Range(range)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableType is not None and not isinstance(
                            variableType, aas.SubmodelElement
                        ):
                            variableType = self.VariableType(variableType)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableDescription is not None and not isinstance(
                            variableDescription, aas.SubmodelElement
                        ):
                            variableDescription = self.VariableDescription(
                                variableDescription
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if unitList is not None and not isinstance(
                            unitList, aas.SubmodelElement
                        ):
                            unitList = self.UnitList(unitList)

                        # Build a submodel element if a raw value was passed in the argument

                        if unitDescription is not None and not isinstance(
                            unitDescription, aas.SubmodelElement
                        ):
                            unitDescription = self.UnitDescription(unitDescription)

                        # Build a submodel element if a raw value was passed in the argument

                        if variableCausality is not None and not isinstance(
                            variableCausality, aas.SubmodelElement
                        ):
                            variableCausality = self.VariableCausality(
                                variableCausality
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if variablePrefix is not None and not isinstance(
                            variablePrefix, aas.SubmodelElement
                        ):
                            variablePrefix = self.VariablePrefix(variablePrefix)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            variableName,
                            range,
                            variableType,
                            variableDescription,
                            unitList,
                            unitDescription,
                            variableCausality,
                            variablePrefix,
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
                    portConnectorName: Union[str, PortConnectorName],
                    portConDescription: Optional[
                        Union[aas.LangStringSet, PortConDescription]
                    ] = None,
                    variable: Optional[Iterable[Variable]] = None,
                    id_short: Optional[str] = r"PortsConnector",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/PortsConnector/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Ports Connector"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"List of ports of the model. These include a name, a description, a list of variables, and a list of ports."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"portsConnector",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"List of ports of the model. These include a name, a description, a list of variables, and a list of ports.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="portsConnector'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if portConnectorName is not None and not isinstance(
                        portConnectorName, aas.SubmodelElement
                    ):
                        portConnectorName = self.PortConnectorName(portConnectorName)

                    # Build a submodel element if a raw value was passed in the argument

                    if portConDescription is not None and not isinstance(
                        portConDescription, aas.SubmodelElement
                    ):
                        portConDescription = self.PortConDescription(portConDescription)

                    # A str would be split into its characters
                    if isinstance(variable, str):
                        raise TypeError("variable takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [portConnectorName, portConDescription, variable]:
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

            class BinaryConnector(aas.SubmodelElementCollection):

                class BinaryConName(aas.Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"BinaryConName",
                        value_type: aas.DataTypeDefXsd = str,
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/BinaryConnectorName/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Binary Con Name"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Binary interface name."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"binaryConName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Binary interface name.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"binConName",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"One",
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

                class BinaryConDescription(aas.MultiLanguageProperty):

                    def __init__(
                        self,
                        value: aas.LangStringSet,
                        id_short: Optional[str] = r"BinaryConDescription",
                        value_id: Optional[aas.Reference] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/idta/SimulationModels/BinaryConDescription/1/0",
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

                        if display_name is None:
                            display_name = aas.MultiLanguageNameType(
                                dict_={r"en": r"Binary Con Description"}
                            )

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Binary interface description."}
                            )

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"FormTitle",
                                    value_type=str,
                                    value=r"binaryConDescription",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"FormInfo",
                                    value_type=str,
                                    value=r"Binary interface description.",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"PresetIdShort",
                                    value_type=str,
                                    value=r"binaryConDescription",
                                    value_id=None,
                                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                                aas.Qualifier(
                                    type_=r"Multiplicity",
                                    value_type=str,
                                    value=r"ZeroToOne",
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

                def __init__(
                    self,
                    binaryConName: Union[str, BinaryConName],
                    binaryConDescription: Optional[
                        Union[aas.LangStringSet, BinaryConDescription]
                    ] = None,
                    id_short: Optional[str] = r"BinaryConnector",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/BinaryConnector/1/0",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Binary Connector"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r'Binary interfaces (binaryType) based on the FMI 3.0 standard (https://fmi-standard.org/docs/3.0-dev/#definition-of-types). At this point the name (e.g. "Binary interface visualization") and the description (e.g. "Interface for binary transfer of visualization information") are specified.'
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"binaryConnector",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r'Binary interfaces (binaryType) based on the FMI 3.0 standard (https://fmi-standard.org/docs/3.0-dev/#definition-of-types). At this point the name (e.g. "Binary interface visualization") and the description (e.g. "Interface for binary transfer of visualization information") are specified.',
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value="binaryConnector'{0:00}'",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument

                    if binaryConName is not None and not isinstance(
                        binaryConName, aas.SubmodelElement
                    ):
                        binaryConName = self.BinaryConName(binaryConName)

                    # Build a submodel element if a raw value was passed in the argument

                    if binaryConDescription is not None and not isinstance(
                        binaryConDescription, aas.SubmodelElement
                    ):
                        binaryConDescription = self.BinaryConDescription(
                            binaryConDescription
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [binaryConName, binaryConDescription]:
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
                portsConnector: Optional[Iterable[PortsConnector]] = None,
                binaryConnector: Optional[Iterable[BinaryConnector]] = None,
                id_short: Optional[str] = r"Ports",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/Ports/1/0",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Ports"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Interfaces of the model. This includes inputs, outputs as well as acausal connections (e.g. mechanical connections). In addition, it is specified here whether the model provides binary interfaces (e.g. for visualization)."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"ports",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value=r"Interfaces of the model. This includes inputs, outputs as well as acausal connections (e.g. mechanical connections). In addition, it is specified here whether the model provides binary interfaces (e.g. for visualization).",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"ports",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(portsConnector, str):
                    raise TypeError("portsConnector takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(binaryConnector, str):
                    raise TypeError("binaryConnector takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [portsConnector, binaryConnector]:
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

        class Quality(aas.SubmodelElementCollection):

            class Usability(aas.Property):

                def __init__(
                    self,
                    value: xsd.PositiveInteger,
                    id_short: Optional[str] = r"Usability",
                    value_type: aas.DataTypeDefXsd = xsd.PositiveInteger,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/Usability/1/1",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Usability"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": "The model's ease of use, adaptability, and user-friendliness, ensuring it is accessible and manageable for intended roles."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"usability",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value="The model's ease of use, adaptability, and user-friendliness, ensuring it is accessible and manageable for intended roles.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"usability",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class Architecture(aas.Property):

                def __init__(
                    self,
                    value: xsd.PositiveInteger,
                    id_short: Optional[str] = r"Architecture",
                    value_type: aas.DataTypeDefXsd = xsd.PositiveInteger,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/Architecture/1/1",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Architecture"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The structural design and organization of the model, defining how its components interact to support accurate and efficient simulation."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"architecture",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"The structural design and organization of the model, defining how its components interact to support accurate and efficient simulation.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"architecture",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class Validation(aas.Property):

                def __init__(
                    self,
                    value: xsd.PositiveInteger,
                    id_short: Optional[str] = r"Validation",
                    value_type: aas.DataTypeDefXsd = xsd.PositiveInteger,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/Validation/1/1",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Validation"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The process of confirming that the model accurately replicates real-world processes or behaviors, meeting specified requirements for its intended application."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"validation",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"The process of confirming that the model accurately replicates real-world processes or behaviors, meeting specified requirements for its intended application.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"validation",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class QualityMetricFile(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"QualityMetricFile",
                    content_type: Optional[str] = r"text/plain",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/QualityMetricFile/1/1",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Quality Metric File"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"AML File containing the complete quality evaluation of the simulation model with all factors, criteria and attributes."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"qualityMetricFile",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"AML File containing the complete quality evaluation of the simulation model with all factors, criteria and attributes.",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"qualityMetricFile",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            class EvaluationPerspective(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"EvaluationPerspective",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/SimulationModels/EvaluationPerspective/1/1",
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

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(
                            dict_={r"en": r"Evaluation Perspective"}
                        )

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Role description indicating from which point of view the simulation model’s quality was evaluated (e.g., Model Provider, Model User, Model Consumer, Model Developer, etc.)."
                            }
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"FormTitle",
                                value_type=str,
                                value=r"evaluationPerspective",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"FormInfo",
                                value_type=str,
                                value=r"Role description indicating from which point of view the simulation model’s quality was evaluated (e.g., Model Provider, Model User, Model Consumer, Model Developer, etc.).",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"PresetIdShort",
                                value_type=str,
                                value=r"evaluationPerspective",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            aas.Qualifier(
                                type_=r"Multiplicity",
                                value_type=str,
                                value=r"One",
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

            def __init__(
                self,
                usability: Union[xsd.PositiveInteger, Usability],
                architecture: Union[xsd.PositiveInteger, Architecture],
                validation: Union[xsd.PositiveInteger, Validation],
                qualityMetricFile: QualityMetricFile,
                evaluationPerspective: Union[aas.LangStringSet, EvaluationPerspective],
                id_short: Optional[str] = r"Quality",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/SimulationModels/Quality/1/1",
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

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"Quality"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "The overall measure of a simulation model's ability to meet predefined standards and functional expectations, ensuring it accurately represents the intended system."
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"FormTitle",
                            value_type=str,
                            value=r"quality",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"FormInfo",
                            value_type=str,
                            value="The overall measure of a simulation model's ability to meet predefined standards and functional expectations, ensuring it accurately represents the intended system.",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"PresetIdShort",
                            value_type=str,
                            value=r"quality",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"Multiplicity",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if usability is not None and not isinstance(
                    usability, aas.SubmodelElement
                ):
                    usability = self.Usability(usability)

                # Build a submodel element if a raw value was passed in the argument

                if architecture is not None and not isinstance(
                    architecture, aas.SubmodelElement
                ):
                    architecture = self.Architecture(architecture)

                # Build a submodel element if a raw value was passed in the argument

                if validation is not None and not isinstance(
                    validation, aas.SubmodelElement
                ):
                    validation = self.Validation(validation)

                # Build a submodel element if a raw value was passed in the argument

                if evaluationPerspective is not None and not isinstance(
                    evaluationPerspective, aas.SubmodelElement
                ):
                    evaluationPerspective = self.EvaluationPerspective(
                        evaluationPerspective
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    usability,
                    architecture,
                    validation,
                    qualityMetricFile,
                    evaluationPerspective,
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
            simPurpose: SimPurpose,
            scopeOfModel: Iterable[Union[str, ScopeOfModel]],
            modelFile: ModelFile,
            paramMethod: Union[str, ParamMethod],
            initStateMethod: Union[str, InitStateMethod],
            summary: Optional[Union[aas.LangStringSet, Summary]] = None,
            typeOfModel: Optional[Iterable[Union[str, TypeOfModel]]] = None,
            licenseModel: Optional[Union[str, LicenseModel]] = None,
            engineeringDomain: Optional[Iterable[Union[str, EngineeringDomain]]] = None,
            environment: Optional[Iterable[Environment]] = None,
            refSimDocumentation: Optional[Iterable[RefSimDocumentation]] = None,
            paramFile: Optional[ParamFile] = None,
            initStateFile: Optional[InitStateFile] = None,
            defaultSimTime: Optional[Union[xsd.Float, DefaultSimTime]] = None,
            simModManufacturerInformation: Optional[
                Iterable[SimModManufacturerInformation]
            ] = None,
            ports: Optional[Ports] = None,
            quality: Optional[Iterable[Quality]] = None,
            id_short: Optional[str] = r"SimulationModel",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/SimulationModels/SimulationModel/1/1",
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

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"Simulation Model"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Specifies Simulation Model."}
                )

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"FormTitle",
                        value_type=str,
                        value=r"SimulationModel",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"FormInfo",
                        value_type=str,
                        value=r"Merkmalssammlung zur Bereitstellung oder Anfrage von Simulationsmodellen. Die Modelle können von der Zielstellung und inhaltlich beschrieben werden.",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"PresetIdShort",
                        value_type=str,
                        value="To be filleSimulationModel'{0:00}'",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                    aas.Qualifier(
                        type_=r"Multiplicity",
                        value_type=str,
                        value=r"ZeroToMany",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if summary is not None and not isinstance(summary, aas.SubmodelElement):
                summary = self.Summary(summary)

            # A str would be split into its characters
            if isinstance(typeOfModel, str):
                raise TypeError("typeOfModel takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if typeOfModel:
                typeOfModel = [
                    i if isinstance(i, aas.SubmodelElement) else self.TypeOfModel(i)
                    for i in typeOfModel
                ]

            # A str would be split into its characters
            if isinstance(scopeOfModel, str):
                raise TypeError("scopeOfModel takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if scopeOfModel:
                scopeOfModel = [
                    i if isinstance(i, aas.SubmodelElement) else self.ScopeOfModel(i)
                    for i in scopeOfModel
                ]

            # Build a submodel element if a raw value was passed in the argument

            if licenseModel is not None and not isinstance(
                licenseModel, aas.SubmodelElement
            ):
                licenseModel = self.LicenseModel(licenseModel)

            # A str would be split into its characters
            if isinstance(engineeringDomain, str):
                raise TypeError("engineeringDomain takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if engineeringDomain:
                engineeringDomain = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.EngineeringDomain(i)
                    )
                    for i in engineeringDomain
                ]

            # A str would be split into its characters
            if isinstance(environment, str):
                raise TypeError("environment takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(refSimDocumentation, str):
                raise TypeError("refSimDocumentation takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if paramMethod is not None and not isinstance(
                paramMethod, aas.SubmodelElement
            ):
                paramMethod = self.ParamMethod(paramMethod)

            # Build a submodel element if a raw value was passed in the argument

            if initStateMethod is not None and not isinstance(
                initStateMethod, aas.SubmodelElement
            ):
                initStateMethod = self.InitStateMethod(initStateMethod)

            # Build a submodel element if a raw value was passed in the argument

            if defaultSimTime is not None and not isinstance(
                defaultSimTime, aas.SubmodelElement
            ):
                defaultSimTime = self.DefaultSimTime(defaultSimTime)

            # A str would be split into its characters
            if isinstance(simModManufacturerInformation, str):
                raise TypeError(
                    "simModManufacturerInformation takes several elements, got a str"
                )

            # A str would be split into its characters
            if isinstance(quality, str):
                raise TypeError("quality takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                summary,
                simPurpose,
                typeOfModel,
                scopeOfModel,
                licenseModel,
                engineeringDomain,
                environment,
                refSimDocumentation,
                modelFile,
                paramMethod,
                paramFile,
                initStateMethod,
                initStateFile,
                defaultSimTime,
                simModManufacturerInformation,
                ports,
                quality,
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
        id_: str,
        simulationModel: Optional[Iterable[SimulationModel]] = None,
        id_short: Optional[str] = r"SimulationModels",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/SimulationModels/1/1",
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

        if display_name is None:
            display_name = aas.MultiLanguageNameType(
                dict_={r"en": r"Simulation Models"}
            )

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={r"en": r"Specifies Simulation Models."}
            )

        if qualifier is None:
            qualifier = (
                aas.Qualifier(
                    type_=r"FormTitle",
                    value_type=str,
                    value=r"Simulation Submodel v008",
                    value_id=None,
                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
                aas.Qualifier(
                    type_=r"FormInfo",
                    value_type=str,
                    value=r"Das Submodel kann ein oder meherer Simulationsmodelle bereitstellen, einen Service zur Generierung eines spezifischen Modells oder einen Zugang zu einer offenen oder spezifischen Anfrage.",
                    value_id=None,
                    kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
            )

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # A str would be split into its characters
        if isinstance(simulationModel, str):
            raise TypeError("simulationModel takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [simulationModel]:
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
