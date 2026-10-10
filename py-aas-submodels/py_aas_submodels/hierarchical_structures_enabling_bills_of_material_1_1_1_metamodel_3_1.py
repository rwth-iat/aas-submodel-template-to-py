from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class HierarchicalStructures(aas.Submodel):

    class EntryNode(aas.Entity):

        class Node(aas.Entity):

            class Node(aas.Entity):

                def __init__(
                    self,
                    id_short: Optional[str] = r"Node",
                    entity_type: Optional[
                        aas.EntityType
                    ] = aas.EntityType.SELF_MANAGED_ENTITY,
                    global_asset_id: Optional[
                        str
                    ] = r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                    specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0",
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
                                r"en": r"Can be a Co-managed or Self-managed entity. A Node reflects an element in the hierarchical model is set into relation with one or more defined relations. The name of a node can be picked freely but it must be unique in its hierarchical (sub-)level."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

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
                        statement=embedded_submodel_elements,
                        id_short=id_short,
                        entity_type=entity_type,
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

            class SameAs(aas.RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"SameAs",
                    first: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    second: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0",
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
                                r"en": r"Reference between two Entities in the same Submodel or across Submodels."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        id_short=id_short,
                        first=first,
                        second=second,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class IsPartOf(aas.RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"IsPartOf",
                    first: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    second: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0",
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
                                r"en": r'Modeling of logical connections between components and sub-components. Either this or "HasPart" must be used, not both.'
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        id_short=id_short,
                        first=first,
                        second=second,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class HasPart(aas.RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasPart",
                    first: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    second: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0",
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
                                r"en": r'Modeling of logical connections between components and sub-components. Either this or "IsPartOf" must be used, not both.'
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        id_short=id_short,
                        first=first,
                        second=second,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

            class BulkCount(aas.Property):

                def __init__(
                    self,
                    value: xsd.UnsignedLong,
                    id_short: Optional[str] = r"BulkCount",
                    value_type: aas.DataTypeDefXsd = xsd.UnsignedLong,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://admin-shell.io/idta/HierarchicalStructures/BulkCount/1/0",
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
                                r"en": r"To be used if bulk components are referenced, e.g., a 10x M4x30 screw."
                            }
                        )

                    if qualifier is None:
                        qualifier = ()

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
                node: Optional[Iterable[Node]] = None,
                sameAs: Optional[Iterable[SameAs]] = None,
                isPartOf: Optional[Iterable[IsPartOf]] = None,
                hasPart: Optional[Iterable[HasPart]] = None,
                bulkCount: Optional[Union[xsd.UnsignedLong, BulkCount]] = None,
                id_short: Optional[str] = r"Node",
                entity_type: Optional[
                    aas.EntityType
                ] = aas.EntityType.SELF_MANAGED_ENTITY,
                global_asset_id: Optional[
                    str
                ] = r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
                specific_asset_id: Iterable[aas.SpecificAssetId] = (),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/HierarchicalStructures/Node/1/0",
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
                            r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the Asset Administration Shell this Submodel is part of. The idShort of the EntryNode can be picked freely and may reflect a name of the asset."
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(node, str):
                    raise TypeError("node takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(sameAs, str):
                    raise TypeError("sameAs takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(isPartOf, str):
                    raise TypeError("isPartOf takes several elements, got a str")

                # A str would be split into its characters
                if isinstance(hasPart, str):
                    raise TypeError("hasPart takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if bulkCount is not None and not isinstance(
                    bulkCount, aas.SubmodelElement
                ):
                    bulkCount = self.BulkCount(bulkCount)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [node, sameAs, isPartOf, hasPart, bulkCount]:
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
                    statement=embedded_submodel_elements,
                    id_short=id_short,
                    entity_type=entity_type,
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

        class SameAs(aas.RelationshipElement):

            def __init__(
                self,
                id_short: Optional[str] = r"SameAs",
                first: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                second: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/HierarchicalStructures/SameAs/1/0",
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
                            r"en": r"Reference between two Entities in the same Submodel or across Submodels."
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    first=first,
                    second=second,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class IsPartOf(aas.RelationshipElement):

            def __init__(
                self,
                id_short: Optional[str] = r"IsPartOf",
                first: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                second: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/HierarchicalStructures/IsPartOf/1/0",
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
                            r"en": r'Modeling of logical connections between asset and sub-asset. Either this or "HasPart" must be used, not both.'
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    first=first,
                    second=second,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

        class HasPart(aas.RelationshipElement):

            def __init__(
                self,
                id_short: Optional[str] = r"HasPart",
                first: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                second: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/SMT/General/IntentionallyEmpty",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/HierarchicalStructures/HasPart/1/0",
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
                            r"en": r'Modeling of logical connections between components and sub-components. Either this or "IsPartOf" must be used, not both.'
                        }
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                super().__init__(
                    id_short=id_short,
                    first=first,
                    second=second,
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
            node: Iterable[Node],
            sameAs: Optional[Iterable[SameAs]] = None,
            isPartOf: Optional[Iterable[IsPartOf]] = None,
            hasPart: Optional[Iterable[HasPart]] = None,
            id_short: Optional[str] = r"EntryNode",
            entity_type: Optional[aas.EntityType] = aas.EntityType.SELF_MANAGED_ENTITY,
            global_asset_id: Optional[
                str
            ] = r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
            specific_asset_id: Iterable[aas.SpecificAssetId] = (),
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/HierarchicalStructures/EntryNode/1/0",
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
                        r"en": r"Base entry point for the Entity tree in this Submodel, this must be a Self-managed Entity reflecting the Assets administrated in the AAS this Submodel is part of."
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(node, str):
                raise TypeError("node takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(sameAs, str):
                raise TypeError("sameAs takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(isPartOf, str):
                raise TypeError("isPartOf takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(hasPart, str):
                raise TypeError("hasPart takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [node, sameAs, isPartOf, hasPart]:
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
                statement=embedded_submodel_elements,
                id_short=id_short,
                entity_type=entity_type,
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

    class ArcheType(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"ArcheType",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/HierarchicalStructures/ArcheType/1/0",
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
                        r"en": r"ArcheType of the Submodel, there are three allowed enumeration entries: 1. “Full”, 2. “OneDown” and 3. “OneUp”. "
                    }
                )

            if qualifier is None:
                qualifier = ()

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
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL,
                    value=r"https://admin-shell.io/idta/HierarchicalStructures/1/1/Submodel",
                ),
            ),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel HierarchicalStructures identified by its semanticId. The Submodel idShort can be picked freely."
                }
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if archeType is not None and not isinstance(archeType, aas.SubmodelElement):
            archeType = self.ArcheType(archeType)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [entryNode, archeType]:
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
