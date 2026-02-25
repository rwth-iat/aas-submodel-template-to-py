from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class CarbonFootprint(Submodel):

    def __init__(
        self,
        id_: str,
        id_short: Optional[str] = r"CarbonFootprint",
        display_name: Optional[MultiLanguageNameType] = MultiLanguageNameType(
            dict_={r"de": r"C02 Footprint", r"en": r"carbon footprint"}
        ),
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"The Submodel provides the means to access the Carbon Footprint of the asset."
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02023-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/1/0",
                ),
            ),
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
        extension: Iterable[Extension] = (),
        supplemental_semantic_id: Iterable[Reference] = (
            ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#CarbonFootprintBattery",
                    ),
                ),
                referred_semantic_id=None,
            ),
        ),
        embedded_data_specifications: Iterable[EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in []:
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
