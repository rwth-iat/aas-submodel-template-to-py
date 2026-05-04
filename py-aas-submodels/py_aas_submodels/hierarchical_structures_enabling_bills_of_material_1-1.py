from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class HierarchicalStructures(Submodel):

    class EntryNode(Entity):

        def __init__(
            self,
            id_short: Optional[str] = r"EntryNode",
            entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
            statement: Iterable[SubmodelElement] = (
                Entity(
                    id_short=r"Node",
                    entity_type=EntityType.SELF_MANAGED_ENTITY,
                    statement=(
                        Entity(
                            id_short=r"Node",
                            entity_type=EntityType.SELF_MANAGED_ENTITY,
                            statement=(),
                            global_asset_id=r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                            specific_asset_id=(),
                            display_name=None,
                            category=None,
                            description=MultiLanguageTextType(
                                dict_={
                                    r"en": r"Can be a Co-managed or Self-managed entity. A Node reflects an element in the hierarchical model is set into relation with one or more defined relations. The name of a node can be picked freely but it must be unique in its hierarchical (sub-)level."
                                }
                            ),
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToMany",
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
                                Qualifier(
                                    type_=r"EditIdShort",
                                    value_type=str,
                                    value=r"True",
                                    value_id=None,
                                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                        Property(
                            id_short=r"BulkCount",
                            value_type=UnsignedLong,
                            value=None,
                            value_id=None,
                            display_name=None,
                            category=None,
                            description=MultiLanguageTextType(
                                dict_={
                                    r"en": r"To be used if bulk components are referenced, e.g., a 10x M4x30 screw."
                                }
                            ),
                            semantic_id=ExternalReference(
                                key=(
                                    Key(
                                        type_=KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier=(
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
                            ),
                            extension=(),
                            supplemental_semantic_id=(),
                            embedded_data_specifications=[],
                        ),
                    ),
                    global_asset_id=r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                    specific_asset_id=(),
                    display_name=None,
                    category=None,
                    description=MultiLanguageTextType(
                        dict_={
                            r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
                        }
                    ),
                    semantic_id=ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier=(
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
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
                        Qualifier(
                            type_=r"EditIdShort",
                            value_type=str,
                            value=r"True",
                            value_id=None,
                            kind=QualifierKind.TEMPLATE_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    ),
                    extension=(),
                    supplemental_semantic_id=(),
                    embedded_data_specifications=[],
                ),
            ),
            global_asset_id: Optional[
                str
            ] = r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
            specific_asset_id: Iterable[SpecificAssetId] = (),
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
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
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"EditIdShort",
                        value_type=str,
                        value=r"True",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                id_short=id_short,
                entity_type=entity_type,
                statement=statement,
                global_asset_id=global_asset_id,
                specific_asset_id=specific_asset_id,
                display_name=display_name,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                extension=extension,
                supplemental_semantic_id=supplemental_semantic_id,
                embedded_data_specifications=embedded_data_specifications,
            )

    class ArcheType(Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"ArcheType",
            value_type: DataTypeDefXsd = str,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"ArcheType of the Submodel, there are three allowed enumeration entries: 1. “Full”, 2. “OneDown” and 3. “OneUp”. "
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0",
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
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                    Qualifier(
                        type_=r"FormChoices",
                        value_type=str,
                        value=r"Full;OneDown;OneUp",
                        value_id=None,
                        kind=QualifierKind.TEMPLATE_QUALIFIER,
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
        id_: str,
        entryNode: EntryNode,
        archeType: Union[str, ArcheType],
        id_short: Optional[str] = r"HierarchicalStructures",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
            }
        ),
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel",
                ),
            ),
            referred_semantic_id=None,
        ),
        qualifier: Iterable[Qualifier] = None,
        kind: ModellingKind = ModellingKind.TEMPLATE,
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
                Qualifier(
                    type_=r"EditIdShort",
                    value_type=str,
                    value=r"True",
                    value_id=None,
                    kind=QualifierKind.TEMPLATE_QUALIFIER,
                    semantic_id=None,
                    supplemental_semantic_id=(),
                ),
            )

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument
        if archeType and not isinstance(archeType, SubmodelElement):
            archeType = self.ArcheType(archeType)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [entryNode, archeType]:
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
