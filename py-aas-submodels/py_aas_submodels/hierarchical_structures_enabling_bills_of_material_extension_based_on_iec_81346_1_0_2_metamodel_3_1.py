from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class IEC81346Structure(aas.Submodel):

    def __init__(
        self,
        id_: str,
        id_short: Optional[str] = r"IEC81346Structure",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/HierarchicalStructures/ExtensionIEC81346/1/0",
                ),
            ),
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
                    r"en": r"Definition of the Submodel Extension IEC 81346 of HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
                }
            )

        if qualifier is None:
            qualifier = (
                aas.Qualifier(
                    type_=r"EditIdShort",
                    value_type=str,
                    value=r"True",
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
        for se_arg in []:
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
