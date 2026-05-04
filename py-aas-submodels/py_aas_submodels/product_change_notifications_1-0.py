from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class ProductChangeNotifications(Submodel):

    class PcnEventsOutgoing(BasicEventElement):

        def __init__(
            self,
            id_short: Optional[str] = r"PcnEventsOutgoing",
            observed: ModelReference[
                Union[ForwardRef("AssetAdministrationShell"), Submodel, SubmodelElement]
            ] = ModelReference(
                key=(
                    Key(
                        type_=KeyTypes.SUBMODEL,
                        value=r"www.example.com/ids/sm/3212_3160_4022_4516",
                    ),
                ),
                type_=Submodel,
                referred_semantic_id=None,
            ),
            direction: Direction = Direction.INPUT,
            state: StateOfEvent = StateOfEvent.OFF,
            message_topic: Optional[str] = None,
            message_broker: Optional[
                ModelReference[
                    Union[
                        Submodel, SubmodelElementList, SubmodelElementCollection, Entity
                    ]
                ]
            ] = None,
            last_update: Optional[datetime] = None,
            min_interval: Optional[relativedelta] = None,
            max_interval: Optional[relativedelta] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Note: Industrial users will subscribe to this event by different implementation technologies."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"http://admin-shell.io/VDMA/Fluidics/ProductChangeNotification/EventsOutgoing/1/0",
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
                        value=r"ZeroToOne",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
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
                id_short=id_short,
                observed=observed,
                direction=direction,
                state=state,
                message_topic=message_topic,
                message_broker=message_broker,
                last_update=last_update,
                min_interval=min_interval,
                max_interval=max_interval,
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
        pcnEventsOutgoing: Optional[PcnEventsOutgoing] = None,
        id_short: Optional[str] = r"ProductChangeNotifications",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = None,
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta_02036",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ExternalReference(
            key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r"0173-1#01-AHE582#003"),),
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

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [pcnEventsOutgoing]:
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
