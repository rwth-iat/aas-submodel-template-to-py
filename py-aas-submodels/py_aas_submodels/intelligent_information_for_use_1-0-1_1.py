from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class IntelligentInformationforUse(Submodel):

    class ResourceIRI(Property):

        def __init__(
            self,
            value: AnyURI,
            id_short: Optional[str] = r"ResourceIRI",
            value_type: DataTypeDefXsd = AnyURI,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"Identifies instances of the iirds:classes and subclasses"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"http://iirds.tekom.de/iirds#ResourceIRI",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

    class FormatRestriction(Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"FormatRestriction",
            value_type: DataTypeDefXsd = str,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"restriction of media formats allowed in an iiRDS package"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"http://iirds.tekom.de/iirds#formatRestriction",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

    class IirdsVersion(Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"IirdsVersion",
            value_type: DataTypeDefXsd = str,
            value_id: Optional[Reference] = None,
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"iiRDS version with which the iiRDS package complies"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"http://iirds.tekom.de/iirds#iiRDSVersion",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
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

    class InformationUnitCollection(SubmodelElementCollection):

        class Document(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Title(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Title",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"name of the information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#title",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfCreation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfCreation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"date of creation of the resource"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfCreation",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfLastModification(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfLastModification",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "date and time of an information unit's last change "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfLastModification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Language(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Language",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "identifier of the content's language"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#language",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Revision(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Revision",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"version of an information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#revision",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Rights(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Rights",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"declaration of specific rights regarding the usage of the information"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#rights",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasRendition(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasRendition",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"RenditionCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Rendition",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its rendition"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-rendition",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasContentLifecycleStatus(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasContentLifecycleStatus",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ContentLifecycleStatus",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its content lifecycle status"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-content-lifecycle-status",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class IsReplacementOf(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"IsReplacementOf",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing the information unit to be replaced"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-replacement-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"ExampleValue",
                                value_type=str,
                                value=r"ResourceIRI of the information unit which shall be replaced",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class IsVersionOf(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"IsVersionOf",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObjectCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObject",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its information object"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-version-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToEvent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToEvent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Event",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an event"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-event",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToSupply(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToSupply",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Supply",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a supply"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-supply",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToQualification(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToQualification",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"SkillLevel",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a qualification "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-qualification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasIdentity(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasIdentity",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Identity",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "iiRDS resource's property referencing an identifier"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-identity",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasDocumentType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasDocumentType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#InstallationInstructions",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "document's property referencing its document type"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-document-type",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToComponent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToComponent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Component",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a component"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-component",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasSubject(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasSubject",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its subject"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-subject",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToAction(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToAction",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Action",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an action"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-action",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductFeature(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductFeature",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductFeature",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product feature"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-feature",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductLifecyclePhase(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductLifecyclePhase",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductLifeCyclePhase",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductVariant(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductVariant",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductVariant",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product variant"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ProductVariant",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasPlanningTime(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasPlanningTime",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"WorkingTime",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-planning-time",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[
                    Union[str, DateOfLastModification]
                ] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[LangStringSet, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[
                    Iterable[HasContentLifecycleStatus]
                ] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                relatesToQualification: Optional[
                    Iterable[RelatesToQualification]
                ] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                hasDocumentType: Optional[Iterable[HasDocumentType]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[
                    Iterable[RelatesToProductFeature]
                ] = None,
                relatesToProductLifecyclePhase: Optional[
                    Iterable[RelatesToProductLifecyclePhase]
                ] = None,
                relatesToProductVariant: Optional[
                    Iterable[RelatesToProductVariant]
                ] = None,
                hasPlanningTime: Optional[Iterable[HasPlanningTime]] = None,
                id_short: Optional[str] = r"Document",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"information unit consisting of an ordered set of information intended by the sender to be regarded as an entity"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Document",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if title and not isinstance(title, SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfCreation and not isinstance(dateOfCreation, SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfLastModification and not isinstance(
                    dateOfLastModification, SubmodelElement
                ):
                    dateOfLastModification = self.DateOfLastModification(
                        dateOfLastModification
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if language and all([isinstance(i, str) for i in language]):
                    language = [self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument
                if revision and not isinstance(revision, SubmodelElement):
                    revision = self.Revision(revision)

                # Build a list of submodel elements if a raw values were passed in the argument
                if rights and all([isinstance(i, LangStringSet) for i in rights]):
                    rights = [self.Rights(i) for i in rights]

                # Build a submodel element if a raw value was passed in the argument
                if isReplacementOf and not isinstance(isReplacementOf, SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    isVersionOf,
                    relatesToEvent,
                    relatesToSupply,
                    relatesToQualification,
                    hasIdentity,
                    relatesToParty,
                    hasDocumentType,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
                    relatesToProductVariant,
                    hasPlanningTime,
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

        class Topic(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasTopicType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasTopicType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#GenericConcept",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its topic type"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-topic-type",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class IsVersionOf(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"IsVersionOf",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObjectCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObject",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its information object"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-version-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToQualification(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToQualification",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Role",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a qualification "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-qualification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductVariant(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductVariant",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductVariant",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product variant"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ProductVariant",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class Title(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Title",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"name of the information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#title",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfCreation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfCreation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"date of creation of the resource"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfCreation",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfLastModification(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfLastModification",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "date and time of an information unit's last change "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfLastModification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Language(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Language",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "identifier of the content's language"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#language",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Revision(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Revision",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"version of an information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#revision",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Rights(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Rights",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"declaration of specific rights regarding the usage of the information"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#rights",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasRendition(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasRendition",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"RenditionCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Rendition",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its rendition"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-rendition",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasContentLifecycleStatus(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasContentLifecycleStatus",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ContentLifecycleStatus",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its content lifecycle status"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-content-lifecycle-status",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class IsReplacementOf(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"IsReplacementOf",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing the information unit to be replaced"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-replacement-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"ExampleValue",
                                value_type=str,
                                value=r"ResourceIRI of the information unit which shall be replaced",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class RelatesToEvent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToEvent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Event",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an event"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-event",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToSupply(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToSupply",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Supply",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a supply"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-supply",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasIdentity(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasIdentity",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Identity",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "iiRDS resource's property referencing an identifier"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-identity",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToComponent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToComponent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Component",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a component"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-component",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasSubject(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasSubject",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its subject"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-subject",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToAction(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToAction",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Action",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an action"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-action",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductFeature(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductFeature",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductFeature",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product feature"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-feature",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductLifecyclePhase(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductLifecyclePhase",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductLifeCyclePhase",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class IsApplicableForDocumentType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"IsApplicableForDocumentType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#OperatingInstructions",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-applicable-for-document-type",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasPlanningTime(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasPlanningTime",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Topic",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"MaintenanceInterval",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-planning-time",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                hasTopicType: Optional[Iterable[HasTopicType]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToQualification: Optional[
                    Iterable[RelatesToQualification]
                ] = None,
                relatesToProductVariant: Optional[
                    Iterable[RelatesToProductVariant]
                ] = None,
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[
                    Union[str, DateOfLastModification]
                ] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[LangStringSet, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[
                    Iterable[HasContentLifecycleStatus]
                ] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[
                    Iterable[RelatesToProductFeature]
                ] = None,
                relatesToProductLifecyclePhase: Optional[
                    Iterable[RelatesToProductLifecyclePhase]
                ] = None,
                isApplicableForDocumentType: Optional[
                    Iterable[IsApplicableForDocumentType]
                ] = None,
                hasPlanningTime: Optional[Iterable[HasPlanningTime]] = None,
                id_short: Optional[str] = r"Topic",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"information unit covering a single subject"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Topic",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if title and not isinstance(title, SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfCreation and not isinstance(dateOfCreation, SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfLastModification and not isinstance(
                    dateOfLastModification, SubmodelElement
                ):
                    dateOfLastModification = self.DateOfLastModification(
                        dateOfLastModification
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if language and all([isinstance(i, str) for i in language]):
                    language = [self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument
                if revision and not isinstance(revision, SubmodelElement):
                    revision = self.Revision(revision)

                # Build a list of submodel elements if a raw values were passed in the argument
                if rights and all([isinstance(i, LangStringSet) for i in rights]):
                    rights = [self.Rights(i) for i in rights]

                # Build a submodel element if a raw value was passed in the argument
                if isReplacementOf and not isinstance(isReplacementOf, SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    hasTopicType,
                    isVersionOf,
                    relatesToQualification,
                    relatesToProductVariant,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    relatesToEvent,
                    relatesToSupply,
                    hasIdentity,
                    relatesToParty,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
                    isApplicableForDocumentType,
                    hasPlanningTime,
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

        class Fragment(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class RelatesToProductVariant(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductVariant",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductVariant",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product variant"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ProductVariant",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class Title(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Title",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"name of the information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#title",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfCreation(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfCreation",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"date of creation of the resource"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfCreation",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfLastModification(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfLastModification",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "date and time of an information unit's last change "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfLastModification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Language(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Language",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "identifier of the content's language"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#language",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Revision(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Revision",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"version of an information unit"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#revision",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Rights(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Rights",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"declaration of specific rights regarding the usage of the information"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#rights",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasRendition(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasRendition",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"RenditionCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Rendition",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its rendition"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-rendition",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasContentLifecycleStatus(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasContentLifecycleStatus",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ContentLifecycleStatus",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its content lifecycle status"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-content-lifecycle-status",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class IsReplacementOf(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"IsReplacementOf",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing the information unit to be replaced"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-replacement-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                            Qualifier(
                                type_=r"ExampleValue",
                                value_type=str,
                                value=r"ResourceIRI of the information unit which shall be replaced",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class IsVersionOf(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"IsVersionOf",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObjectCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationObject",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its information object"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#is-version-of",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToEvent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToEvent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Event",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an event"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-event",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToQualification(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToQualification",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"SkillLevel",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a qualification "
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-qualification",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToSupply(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToSupply",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Supply",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a supply"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-supply",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasIdentity(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasIdentity",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Identity",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "iiRDS resource's property referencing an identifier"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-identity",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToComponent(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToComponent",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Component",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a component"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-component",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasSubject(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasSubject",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#GenericTechnicalOverview",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing its subject"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-subject",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToAction(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToAction",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Action",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing an action"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-action",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductFeature(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductFeature",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductFeature",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "information unit's property referencing a product feature"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-feature",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToProductLifecyclePhase(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToProductLifecyclePhase",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Fragment",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductLifeCyclePhase",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-product-lifecycle-phase",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                relatesToProductVariant: Optional[
                    Iterable[RelatesToProductVariant]
                ] = None,
                title: Optional[Union[str, Title]] = None,
                dateOfCreation: Optional[Union[str, DateOfCreation]] = None,
                dateOfLastModification: Optional[
                    Union[str, DateOfLastModification]
                ] = None,
                language: Optional[Iterable[Union[str, Language]]] = None,
                revision: Optional[Union[str, Revision]] = None,
                rights: Optional[Iterable[Union[LangStringSet, Rights]]] = None,
                hasRendition: Optional[Iterable[HasRendition]] = None,
                hasContentLifecycleStatus: Optional[
                    Iterable[HasContentLifecycleStatus]
                ] = None,
                isReplacementOf: Optional[Union[str, IsReplacementOf]] = None,
                isVersionOf: Optional[IsVersionOf] = None,
                relatesToEvent: Optional[Iterable[RelatesToEvent]] = None,
                relatesToQualification: Optional[
                    Iterable[RelatesToQualification]
                ] = None,
                relatesToSupply: Optional[Iterable[RelatesToSupply]] = None,
                hasIdentity: Optional[Iterable[HasIdentity]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                relatesToComponent: Optional[Iterable[RelatesToComponent]] = None,
                hasSubject: Optional[Iterable[HasSubject]] = None,
                relatesToAction: Optional[Iterable[RelatesToAction]] = None,
                relatesToProductFeature: Optional[
                    Iterable[RelatesToProductFeature]
                ] = None,
                relatesToProductLifecyclePhase: Optional[
                    Iterable[RelatesToProductLifecyclePhase]
                ] = None,
                id_short: Optional[str] = r"Fragment",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"information unit that requires additional context"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Fragment",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if title and not isinstance(title, SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfCreation and not isinstance(dateOfCreation, SubmodelElement):
                    dateOfCreation = self.DateOfCreation(dateOfCreation)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfLastModification and not isinstance(
                    dateOfLastModification, SubmodelElement
                ):
                    dateOfLastModification = self.DateOfLastModification(
                        dateOfLastModification
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if language and all([isinstance(i, str) for i in language]):
                    language = [self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument
                if revision and not isinstance(revision, SubmodelElement):
                    revision = self.Revision(revision)

                # Build a list of submodel elements if a raw values were passed in the argument
                if rights and all([isinstance(i, LangStringSet) for i in rights]):
                    rights = [self.Rights(i) for i in rights]

                # Build a submodel element if a raw value was passed in the argument
                if isReplacementOf and not isinstance(isReplacementOf, SubmodelElement):
                    isReplacementOf = self.IsReplacementOf(isReplacementOf)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    relatesToProductVariant,
                    title,
                    dateOfCreation,
                    dateOfLastModification,
                    language,
                    revision,
                    rights,
                    hasRendition,
                    hasContentLifecycleStatus,
                    isReplacementOf,
                    isVersionOf,
                    relatesToEvent,
                    relatesToQualification,
                    relatesToSupply,
                    hasIdentity,
                    relatesToParty,
                    relatesToComponent,
                    hasSubject,
                    relatesToAction,
                    relatesToProductFeature,
                    relatesToProductLifecyclePhase,
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
            document: Optional[Iterable[Document]] = None,
            topic: Optional[Iterable[Topic]] = None,
            fragment: Optional[Iterable[Fragment]] = None,
            id_short: Optional[str] = r"InformationUnitCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"collection of instances of iirds:topic, iirds:document and iirds:fragment, which are subclasses of iirds:informationunit"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/InformationUnitCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [document, topic, fragment]:
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

    class InformationObjectCollection(SubmodelElementCollection):

        class InformationObject(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                id_short: Optional[str] = r"InformationObject",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"version- and language-independent abstraction of an information unit"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#InformationObject",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI]:
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
            informationObject: Optional[Iterable[InformationObject]] = None,
            id_short: Optional[str] = r"InformationObjectCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"collection of iirds:InformationObject instances"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/InformationObjectCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [informationObject]:
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

    class DirectoryNodeCollection(SubmodelElementCollection):

        class DirectoryNode(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r'http://iirds.tekom.de/iirds#ResourceIRI">',
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class RelatesToInformationUnit(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToInformationUnit",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"DirectoryNodeCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"DirectoryNode",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"InformationUnitCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Document",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "directory node's property referencing the corresponding information unit"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-information-unit",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasNextSibling(SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasNextSibling",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "directory node's property referencing the following directory node on the same hierarchy level in a directory structure Verweist auf den folgenden Verzeichniseintrag einer Verzeichnisstruktur auf gleicher Ebene."
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-next-sibling",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasFirstChild(SubmodelElementCollection):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasFirstChild",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "directory node's property referencing the first directory node on the next subordinate level in a directory structure"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-first-child",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasDirectoryStructureType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasDirectoryStructureType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"DirectoryNodeCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"DirectoryNode",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#TableOfContents",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "directory node's property referencing its node type"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-directory-structure-type",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human- readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                relatesToInformationUnit: Optional[RelatesToInformationUnit] = None,
                hasNextSibling: Optional[HasNextSibling] = None,
                hasFirstChild: Optional[HasFirstChild] = None,
                hasDirectoryStructureType: Optional[HasDirectoryStructureType] = None,
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"DirectoryNode",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"node in a tree-like, ordered collection"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#DirectoryNode",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    relatesToInformationUnit,
                    hasNextSibling,
                    hasFirstChild,
                    hasDirectoryStructureType,
                    label,
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
            directoryNode: Optional[Iterable[DirectoryNode]] = None,
            id_short: Optional[str] = r"DirectoryNodeCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"collection of iirds:DirectoryNode instances"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/DirectoryNodeCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [directoryNode]:
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

    class RenditionCollection(SubmodelElementCollection):

        class Rendition(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Format(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Format",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"media type of the rendition"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#format",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Source(File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Source",
                    content_type: str = r"text/plain",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"relative path of a file in the iiRDS package, containing the content of a rendition"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#source",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasSelector(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasSelector",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"RenditionCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Rendition",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"RenditionCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FragmentSelector",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "rendition's property referencing a selector"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-selector",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RangeSelector(SubmodelElementCollection):

                class ResourceIRI(Property):

                    def __init__(
                        self,
                        value: AnyURI,
                        id_short: Optional[str] = r"ResourceIRI",
                        value_type: DataTypeDefXsd = AnyURI,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Identifies instances of the iirds:classes and subclasses"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class HasStartSelector(RelationshipElement):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"HasStartSelector",
                        first: Reference = ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.SUBMODEL,
                                    value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RenditionCollection",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RangeSelector",
                                ),
                                Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=Property,
                            referred_semantic_id=None,
                        ),
                        second: Reference = ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.SUBMODEL,
                                    value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RenditionCollection",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FragmentSelector",
                                ),
                                Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=Property,
                            referred_semantic_id=None,
                        ),
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": "range selector's property referencing the start of its range"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://iirds.tekom.de/iirds#has-start-selector",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

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

                class HasEndSelector(RelationshipElement):

                    def __init__(
                        self,
                        id_short: Optional[str] = r"HasEndSelector",
                        first: Reference = ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.SUBMODEL,
                                    value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RenditionCollection",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RangeSelector",
                                ),
                                Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=Property,
                            referred_semantic_id=None,
                        ),
                        second: Reference = ModelReference(
                            key=(
                                Key(
                                    type_=KeyTypes.SUBMODEL,
                                    value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"RenditionCollection",
                                ),
                                Key(
                                    type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                    value=r"FragmentSelector",
                                ),
                                Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                            ),
                            type_=Property,
                            referred_semantic_id=None,
                        ),
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": "range selector's property referencing the end of its range"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://iirds.tekom.de/iirds#has-end-selector",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
                                    semantic_id=None,
                                    supplemental_semantic_id=(),
                                ),
                            )

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
                    hasStartSelector: HasStartSelector,
                    hasEndSelector: HasEndSelector,
                    resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                    id_short: Optional[str] = r"RangeSelector",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"selector defining the start point and the end point of a part of content"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#RangeSelector",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                        resourceIRI = self.ResourceIRI(resourceIRI)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [resourceIRI, hasStartSelector, hasEndSelector]:
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

            class FragmentSelector(SubmodelElementCollection):

                class ResourceIRI(Property):

                    def __init__(
                        self,
                        value: AnyURI,
                        id_short: Optional[str] = r"ResourceIRI",
                        value_type: DataTypeDefXsd = AnyURI,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[
                            MultiLanguageTextType
                        ] = MultiLanguageTextType(
                            dict_={
                                r"en": r"Identifies instances of the iirds:classes and subclasses"
                            }
                        ),
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"ZeroToOne",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class ConformsTo(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"ConformsTo",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"http://purl.org/dc/terms/conformsTo",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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

                class Value(Property):

                    def __init__(
                        self,
                        value: str,
                        id_short: Optional[str] = r"Value",
                        value_type: DataTypeDefXsd = str,
                        value_id: Optional[Reference] = None,
                        display_name: Optional[MultiLanguageNameType] = None,
                        category: Optional[str] = r"CONSTANT",
                        description: Optional[MultiLanguageTextType] = None,
                        semantic_id: Optional[Reference] = ExternalReference(
                            key=(
                                Key(
                                    type_=KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://www.w3.org/TR/rdf12-schema/#ch_value",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        qualifier: Iterable[Qualifier] = None,
                        extension: Iterable[Extension] = (),
                        supplemental_semantic_id: Iterable[Reference] = (),
                        embedded_data_specifications: Iterable[
                            EmbeddedDataSpecification
                        ] = None,
                    ):

                        if qualifier is None:
                            qualifier = (
                                Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"One",
                                    value_id=None,
                                    kind=QualifierKind.CONCEPT_QUALIFIER,
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
                    conformsTo: Union[str, ConformsTo],
                    value_: Union[str, Value],
                    resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                    id_short: Optional[str] = r"FragmentSelector",
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"selector defining a part of content by a single identifier"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#FragmentSelector",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # Build a submodel element if a raw value was passed in the argument
                    if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                        resourceIRI = self.ResourceIRI(resourceIRI)

                    # Build a submodel element if a raw value was passed in the argument
                    if conformsTo and not isinstance(conformsTo, SubmodelElement):
                        conformsTo = self.ConformsTo(conformsTo)

                    # Build a submodel element if a raw value was passed in the argument
                    if value_ and not isinstance(value_, SubmodelElement):
                        value_ = self.Value(value_)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [resourceIRI, conformsTo, value_]:
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
                format: Union[str, Format],
                source: Source,
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                hasSelector: Optional[HasSelector] = None,
                rangeSelector: Optional[Iterable[RangeSelector]] = None,
                fragmentSelector: Optional[Iterable[FragmentSelector]] = None,
                id_short: Optional[str] = r"Rendition",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"content of an information unit in a specific format"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Rendition",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if format and not isinstance(format, SubmodelElement):
                    format = self.Format(format)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    format,
                    source,
                    hasSelector,
                    rangeSelector,
                    fragmentSelector,
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
            rendition: Optional[Iterable[Rendition]] = None,
            id_short: Optional[str] = r"RenditionCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={r"en": r"collection of iirds:Rendition instances"}
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/RenditionCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [rendition]:
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

    class AdministrativeMetadataCollection(SubmodelElementCollection):

        class ContentLifecycleStatus(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfEffect(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfEffect",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"date and time on which the given content"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfEffect",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfExpiry(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfExpiry",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"date and time on which the given content lifecycle status becomes invalid"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfExpiry",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class DateOfStatus(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"DateOfStatus",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "date and time of a lifecycle status's last change"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#dateOfStatus",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class StatusComment(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"StatusComment",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"note on a content lifecycle status"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#statusComment",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Purpose(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Purpose",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "reason for an information unit's lifecycle status"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#purpose",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasContentLifecycleStatusValue(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasContentLifecycleStatusValue",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ContentLifecycleStatus",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#Approved",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "content lifecycle status's property referencing its value"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-content-lifecycle-status-value",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ContentLifecycleStatus",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                hasContentLifecycleStatusValue: HasContentLifecycleStatusValue,
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                dateOfEffect: Optional[Union[str, DateOfEffect]] = None,
                dateOfExpiry: Optional[Union[str, DateOfExpiry]] = None,
                dateOfStatus: Optional[Union[str, DateOfStatus]] = None,
                statusComment: Optional[Iterable[Union[str, StatusComment]]] = None,
                purpose: Optional[Union[str, Purpose]] = None,
                relatesToParty: Optional[RelatesToParty] = None,
                id_short: Optional[str] = r"ContentLifecycleStatus",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[MultiLanguageTextType] = None,
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#ContentLifeCycleStatus",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfEffect and not isinstance(dateOfEffect, SubmodelElement):
                    dateOfEffect = self.DateOfEffect(dateOfEffect)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfExpiry and not isinstance(dateOfExpiry, SubmodelElement):
                    dateOfExpiry = self.DateOfExpiry(dateOfExpiry)

                # Build a submodel element if a raw value was passed in the argument
                if dateOfStatus and not isinstance(dateOfStatus, SubmodelElement):
                    dateOfStatus = self.DateOfStatus(dateOfStatus)

                # Build a list of submodel elements if a raw values were passed in the argument
                if statusComment and all([isinstance(i, str) for i in statusComment]):
                    statusComment = [self.StatusComment(i) for i in statusComment]

                # Build a submodel element if a raw value was passed in the argument
                if purpose and not isinstance(purpose, SubmodelElement):
                    purpose = self.Purpose(purpose)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    resourceIRI,
                    dateOfEffect,
                    dateOfExpiry,
                    dateOfStatus,
                    statusComment,
                    purpose,
                    hasContentLifecycleStatusValue,
                    relatesToParty,
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

        class Identity(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Identifier(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Identifier",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"unique name of the resource within a given domain"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#identifier",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasIdentityDomain(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasIdentityDomain",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Identity",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"IdentityDomain",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "identifier's property referencing the domain in which it is unique"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-identity-domain",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                identifier: Union[str, Identifier],
                hasIdentityDomain: HasIdentityDomain,
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                id_short: Optional[str] = r"Identity",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"complex identifier of a resource in an external system"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Identity",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if identifier and not isinstance(identifier, SubmodelElement):
                    identifier = self.Identifier(identifier)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, identifier, hasIdentityDomain]:
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

        class Party(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasPartyRole(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasPartyRole",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"http://iirds.tekom.de/iirds#Manufacturer",
                            ),
                        ),
                        type_=ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "party's property referencing its role"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-party-role",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToVcard(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToVcard",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"VCard",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "party's property referencing an organization or person"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-vcard",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                hasPartyRole: Optional[HasPartyRole] = None,
                relatesToVcard: Optional[RelatesToVcard] = None,
                id_short: Optional[str] = r"Party",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"person, organization or system"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Party",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, hasPartyRole, relatesToVcard]:
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

        class IdentityDomain(SubmodelElementCollection):

            class HasIdentityType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasIdentityType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"IdentityDomain",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"IdentityType "),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"distinguished set of identifiers that are assigned to an iiRDS identity"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#IdentityType",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"IdentityDomain",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                hasIdentityType: Optional[HasIdentityType] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                id_short: Optional[str] = r"IdentityDomain",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"organizational origin of an identifier that is assigned to an iiRDS identity"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#IdentityDomain",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [hasIdentityType, relatesToParty]:
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

        class IdentityType(Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"IdentityType",
                value_type: DataTypeDefXsd = str,
                value_id: Optional[Reference] = None,
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"distinguished set of identifiers that are assigned to an iiRDS identity"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#IdentityType",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

        class VCard(SubmodelElementCollection):

            def __init__(
                self,
                id_short: Optional[str] = r"VCard",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"vCard is a file format standard for electronic business cards"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://www.w3.org/2006/vcard/ns#Kind",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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
            contentLifecycleStatus: Optional[Iterable[ContentLifecycleStatus]] = None,
            identity: Optional[Iterable[Identity]] = None,
            party: Optional[Iterable[Party]] = None,
            identityDomain: Optional[Iterable[IdentityDomain]] = None,
            identityType: Optional[Iterable[Union[str, IdentityType]]] = None,
            vCard: Optional[Iterable[VCard]] = None,
            id_short: Optional[str] = r"AdministrativeMetadataCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"collection of instances of the subclasses of iirds:AdministrativeMetadata"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/AdministrativeMetadataCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a list of submodel elements if a raw values were passed in the argument
            if identityType and all([isinstance(i, str) for i in identityType]):
                identityType = [self.IdentityType(i) for i in identityType]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                contentLifecycleStatus,
                identity,
                party,
                identityDomain,
                identityType,
                vCard,
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

    class FunctionalMetadataCollection(SubmodelElementCollection):

        class Supply(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"Supply",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"physical object used by an actor performing work tasks described in technical documentation"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Supply",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class Event(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class HasEventCode(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasEventCode",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Event",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"EventCode",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": r"property to identify an event"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-event-code",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class HasEventType(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"HasEventType",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Event",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"FunctionalMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"EventType",
                            ),
                        ),
                        type_=SubmodelElementCollection,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "event's property referencing its type"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#has-event-type",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                hasEventCode: HasEventCode,
                hasEventType: HasEventType,
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"Event",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"something noticeable that takes place at a given location and point in time"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Event",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, hasEventCode, hasEventType, label]:
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

        class EventCode(SubmodelElementCollection):

            def __init__(
                self,
                id_short: Optional[str] = r"EventCode",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"property to identify an event"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#EventCode",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

        class EventType(SubmodelElementCollection):

            def __init__(
                self,
                id_short: Optional[str] = r"EventType",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": "event's property referencing its type"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value="event's property referencing its type",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
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

        class Role(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"Role",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"set of connected behaviors, privileges and obligations associated with a party"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Role",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class SkillLevel(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"SkillLevel",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"degree of qualification of an individual"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#SkillLevel",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class Action(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"Action",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"atomic manipulation of an object by a participant"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Action",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class WorkingTime(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Duration(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Duration",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(dict_={r"en": r"span of time"}),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#duration",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"WorkingTime",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"period of time that is required for conducting a specific task"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#WorkingTime",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument
                if duration and not isinstance(duration, SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label, duration]:
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

        class MaintenanceInterval(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Frequency(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Frequency",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"intended interval between recurring maintanance tasks"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#frequency",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Duration(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Duration",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(dict_={r"en": r"span of time"}),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#duration",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                frequency: Union[str, Frequency],
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"MaintenanceInterval",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"period of time between scheduled maintenance operations"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#MaintenanceInterval",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument
                if frequency and not isinstance(frequency, SubmodelElement):
                    frequency = self.Frequency(frequency)

                # Build a submodel element if a raw value was passed in the argument
                if duration and not isinstance(duration, SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label, frequency, duration]:
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

        class DownTime(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Duration(Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Duration",
                    value_type: DataTypeDefXsd = str,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(dict_={r"en": r"span of time"}),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#duration",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                duration: Union[str, Duration],
                resourceIRI: Optional[Union[AnyURI, ResourceIRI]] = None,
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"DownTime",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"period of time during which an item is not in condition to perform its intended function"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#DownTime",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Build a submodel element if a raw value was passed in the argument
                if duration and not isinstance(duration, SubmodelElement):
                    duration = self.Duration(duration)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label, duration]:
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
            supply: Optional[Iterable[Supply]] = None,
            event: Optional[Iterable[Event]] = None,
            eventCode: Optional[Iterable[EventCode]] = None,
            eventType: Optional[Iterable[EventType]] = None,
            role: Optional[Iterable[Role]] = None,
            skillLevel: Optional[Iterable[SkillLevel]] = None,
            action: Optional[Iterable[Action]] = None,
            workingTime: Optional[Iterable[WorkingTime]] = None,
            maintenanceInterval: Optional[Iterable[MaintenanceInterval]] = None,
            downTime: Optional[Iterable[DownTime]] = None,
            id_short: Optional[str] = r"FunctionalMetadataCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"collection of instances of the subclasses of iirds:FunctionalMetadata"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/FunctionalMetadataCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                supply,
                event,
                eventCode,
                eventType,
                role,
                skillLevel,
                action,
                workingTime,
                maintenanceInterval,
                downTime,
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

    class ProductMetadataCollection(SubmodelElementCollection):

        class Component(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Asset(Entity):

                def __init__(
                    self,
                    id_short: Optional[str] = r"Asset",
                    entity_type: EntityType = EntityType.SELF_MANAGED_ENTITY,
                    statement: Iterable[SubmodelElement] = (),
                    global_asset_id: Optional[str] = r"externalAsset",
                    specific_asset_id: Iterable[SpecificAssetId] = (),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Entity in terms of the asset administration shell"
                        }
                    ),
                    semantic_id: Optional[Reference] = None,
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Component",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                asset: Optional[Iterable[Asset]] = None,
                label: Optional[Union[LangStringSet, Label]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                id_short: Optional[str] = r"Component",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"part used as a constituent in an assembled product, system or plant"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#Component",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, asset, label, relatesToParty]:
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

        class ProductFeature(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"ProductFeature",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={r"en": r"product characteristics"}
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#ProductFeature",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class ProductLifeCyclePhase(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[MultiLanguageTextType] = None,
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                id_short: Optional[str] = r"ProductLifeCyclePhase",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"Defined period in the evolution of a product from the conceptual idea to its ultimate disposal"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#ProductLifeCyclePhase",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label]:
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

        class ProductVariant(SubmodelElementCollection):

            class ResourceIRI(Property):

                def __init__(
                    self,
                    value: AnyURI,
                    id_short: Optional[str] = r"ResourceIRI",
                    value_type: DataTypeDefXsd = AnyURI,
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifies instances of the iirds:classes and subclasses"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#ResourceIRI",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class Label(MultiLanguageProperty):

                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: Optional[str] = r"Label",
                    value_id: Optional[Reference] = None,
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={
                            r"en": "used to provide a human-readable version of a resource's name"
                        }
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://www.w3.org/2000/01/rdf-schema#label",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
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

            class RelatesToParty(RelationshipElement):

                def __init__(
                    self,
                    id_short: Optional[str] = r"RelatesToParty",
                    first: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"ProductVariant",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    second: Reference = ModelReference(
                        key=(
                            Key(
                                type_=KeyTypes.SUBMODEL,
                                value=r"https://example.com/ids/sm/1154_0130_2032_3996",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"AdministrativeMetadataCollection",
                            ),
                            Key(
                                type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
                                value=r"Party",
                            ),
                            Key(type_=KeyTypes.PROPERTY, value=r"ResourceIRI"),
                        ),
                        type_=Property,
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[MultiLanguageNameType] = None,
                    category: Optional[str] = r"CONSTANT",
                    description: Optional[
                        MultiLanguageTextType
                    ] = MultiLanguageTextType(
                        dict_={r"en": "iiRDS resource's property referencing a party"}
                    ),
                    semantic_id: Optional[Reference] = ExternalReference(
                        key=(
                            Key(
                                type_=KeyTypes.GLOBAL_REFERENCE,
                                value=r"http://iirds.tekom.de/iirds#relates-to-party",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[Qualifier] = None,
                    extension: Iterable[Extension] = (),
                    supplemental_semantic_id: Iterable[Reference] = (),
                    embedded_data_specifications: Iterable[
                        EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"ZeroToMany",
                                value_id=None,
                                kind=QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

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
                resourceIRI: Union[AnyURI, ResourceIRI],
                label: Optional[Union[LangStringSet, Label]] = None,
                relatesToParty: Optional[Iterable[RelatesToParty]] = None,
                id_short: Optional[str] = r"ProductVariant",
                display_name: Optional[MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                    dict_={
                        r"en": r"item or service offered on the market and designed to meet the needs or wishes of customers"
                    }
                ),
                semantic_id: Optional[Reference] = ExternalReference(
                    key=(
                        Key(
                            type_=KeyTypes.GLOBAL_REFERENCE,
                            value=r"http://iirds.tekom.de/iirds#ProductVariant",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[Qualifier] = None,
                extension: Iterable[Extension] = (),
                supplemental_semantic_id: Iterable[Reference] = (),
                embedded_data_specifications: Iterable[
                    EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"ZeroToMany",
                            value_id=None,
                            kind=QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument
                if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
                    resourceIRI = self.ResourceIRI(resourceIRI)

                # Build a submodel element if a raw value was passed in the argument
                if label and not isinstance(label, SubmodelElement):
                    label = self.Label(label)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [resourceIRI, label, relatesToParty]:
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
            component: Optional[Iterable[Component]] = None,
            productFeature: Optional[Iterable[ProductFeature]] = None,
            productLifeCyclePhase: Optional[Iterable[ProductLifeCyclePhase]] = None,
            productVariant: Optional[Iterable[ProductVariant]] = None,
            id_short: Optional[str] = r"ProductMetadataCollection",
            display_name: Optional[MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
                dict_={
                    r"en": r"collection of instances of the subclasses of iirds:ProductMetadata"
                }
            ),
            semantic_id: Optional[Reference] = ExternalReference(
                key=(
                    Key(
                        type_=KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/IntelligentInformationForUse/ProductMetadataCollection/1/0",
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
                        kind=QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=None,
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                component,
                productFeature,
                productLifeCyclePhase,
                productVariant,
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
        resourceIRI: Union[AnyURI, ResourceIRI],
        iirdsVersion: Union[str, IirdsVersion],
        formatRestriction: Optional[Union[str, FormatRestriction]] = None,
        informationUnitCollection: Optional[InformationUnitCollection] = None,
        informationObjectCollection: Optional[InformationObjectCollection] = None,
        directoryNodeCollection: Optional[DirectoryNodeCollection] = None,
        renditionCollection: Optional[RenditionCollection] = None,
        administrativeMetadataCollection: Optional[
            AdministrativeMetadataCollection
        ] = None,
        functionalMetadataCollection: Optional[FunctionalMetadataCollection] = None,
        productMetadataCollection: Optional[ProductMetadataCollection] = None,
        id_short: Optional[str] = r"IntelligentInformationforUse",
        display_name: Optional[MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[MultiLanguageTextType] = MultiLanguageTextType(
            dict_={
                r"en": r"This Submodel template aims at interoperable provision of information describing the provisioning of “Intelligent Information for Use”, i.e. information of the Technical Documentation enriched by metadata based on the iiRDS"
            }
        ),
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"https://admin-shell.io/idta-02063-1-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[Reference] = ExternalReference(
            key=(
                Key(
                    type_=KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/IntelligentInformationForUse/1/0",
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
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument
        if resourceIRI and not isinstance(resourceIRI, SubmodelElement):
            resourceIRI = self.ResourceIRI(resourceIRI)

        # Build a submodel element if a raw value was passed in the argument
        if formatRestriction and not isinstance(formatRestriction, SubmodelElement):
            formatRestriction = self.FormatRestriction(formatRestriction)

        # Build a submodel element if a raw value was passed in the argument
        if iirdsVersion and not isinstance(iirdsVersion, SubmodelElement):
            iirdsVersion = self.IirdsVersion(iirdsVersion)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            resourceIRI,
            formatRestriction,
            iirdsVersion,
            informationUnitCollection,
            informationObjectCollection,
            directoryNodeCollection,
            renditionCollection,
            administrativeMetadataCollection,
            functionalMetadataCollection,
            productMetadataCollection,
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
