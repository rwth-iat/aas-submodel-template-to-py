from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class FactoryAutomationDataForPlant(Submodel):

    class AutomationMLData(File):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"AutomationMLData",
            content_type: str = r"text/plain",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"AutomationML Data"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Reference to the AutomationML project file that contains the engineering information of the asset."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/automationMLData/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"SMT/Cardinality",
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

    class AutomationMLVersion(Property):

        def __init__(
            self,
            value: PositiveInteger,
            id_short: Optional[str] = r"AutomationMLVersion",
            value_type: DataTypeDefXsd = PositiveInteger,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"AutomationML Version"}
            ),
            category: Optional[str] = r"PARAMETER",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"The AML version that the included AML file follows. This should be either 1 (i.e. CAEX 2.15) or 2 (i.e. CAEX 3.0)."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/automationMLVersion/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"SMT/Cardinality",
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

    class AutomationMLElementReference(ReferenceElement):

        def __init__(
            self,
            value: Reference,
            id_short: Optional[str] = r"AutomationMLElementReference",
            display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
                dict_={r"en": r"AutomationML Element Reference"}
            ),
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Reference to the AutomationML element hosting the engineering information of the asset."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/automationMLElementReference/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[Qualifier] = None,
            extension: Iterable[Extension] = (),
            supplemental_semantic_id: Iterable[Reference] = (),
            embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
        ):

            if qualifier is None:
                qualifier = (
                    Qualifier(
                        type_=r"SMT/Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"SMT/Cardinality",
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
        id_: str,
        automationMLData: AutomationMLData,
        automationMLVersion: Union[PositiveInteger, AutomationMLVersion],
        automationMLElementReference: Union[Reference, AutomationMLElementReference],
        id_short: Optional[str] = r"FactoryAutomationDataForPlant",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={r"en": r"Factory Automation Data For Plant"}
        ),
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = None,
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02075",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ModelReference(
            key=(
                Key(
                    type_=KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/cds/factoryAutomationDataForPlant/1",
                ),
            ),
            type_=Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
        extension: Iterable[Extension] = (),
        supplemental_semantic_id: Iterable[Reference] = (),
        embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument
        if automationMLVersion and not isinstance(automationMLVersion, SubmodelElement):
            automationMLVersion = self.AutomationMLVersion(automationMLVersion)

        # Build a submodel element if a raw value was passed in the argument
        if automationMLElementReference and not isinstance(
            automationMLElementReference, SubmodelElement
        ):
            automationMLElementReference = self.AutomationMLElementReference(
                automationMLElementReference
            )

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            automationMLData,
            automationMLVersion,
            automationMLElementReference,
        ]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {type(se_arg)}"
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
