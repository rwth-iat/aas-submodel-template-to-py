from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class HandoverDocumentation(Submodel):
    class NumberOfDocuments(Property):
        def __init__(
            self,
            value: int,
            id_short: str = "numberOfDocuments",
            value_type: DataTypeDef = int,
            value_id: Optional[Reference] = None,
            category: Optional[str] = "PARAMETER",
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-ABH990#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = set()

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Cardinality",
                        value_type=str,
                        value="ZeroToOne",
                        value_id=None,
                        semantic_id=Reference(
                            key=(
                                Key(
                                    type_=KeyElements.GLOBAL_REFERENCE,
                                    local=False,
                                    value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    id_type=KeyType.IRI,
                                ),
                            )
                        ),
                    )
                }

            super().__init__(
                value=value,
                id_short=id_short,
                value_type=value_type,
                value_id=value_id,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class Document(SubmodelElementCollectionUnordered):
        class DocumentId(SubmodelElementCollectionUnordered):
            class DocumentDomainId(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "DocumentDomainId",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH994#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organisation."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="1213455566",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class ValueId(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "ValueId",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO099#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Identification number of the Document within a given domain, e.g. the providing organisation."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="XF90-884",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class IsPrimary(Property):
                def __init__(
                    self,
                    value: bool,
                    id_short: str = "IsPrimary",
                    value_type: DataTypeDef = bool,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH995#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Flag indicating that a DocumentId within a collection of at least two DocumentId`s is the ‘primary’ identifier for the document. This is the preferred ID of the document (commonly from the point of view of the owner of the asset). Note: can be omitted, if the ID is not primary. Note: can be omitted, if only one ID is for a Document. Contraint: only one DocumentId in a collection may be marked as primary."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=bool,
                                value=True,
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            def __init__(
                self,
                documentDomainId: Union[str, DocumentDomainId],
                valueId: Union[str, ValueId],
                isPrimary: Optional[Union[bool, IsPrimary]] = None,
                id_short: str = "DocumentId",
                category: Optional[str] = "PARAMETER",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-ABI501#001/0173-1#01-AHF580#001*01",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Set of document identifiers for the Document. One ID in this collection should be used as a preferred ID"
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Cardinality",
                            value_type=str,
                            value="OneToMany",
                            value_id=None,
                            semantic_id=Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.GLOBAL_REFERENCE,
                                        local=False,
                                        value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if documentDomainId and not isinstance(
                    documentDomainId, SubmodelElement
                ):
                    documentDomainId = self.DocumentDomainId(documentDomainId)

                # Build a submodel element if a raw value was passed in the argument
                if valueId and not isinstance(valueId, SubmodelElement):
                    valueId = self.ValueId(valueId)

                # Build a submodel element if a raw value was passed in the argument
                if isPrimary and not isinstance(isPrimary, SubmodelElement):
                    isPrimary = self.IsPrimary(isPrimary)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [documentDomainId, valueId, isPrimary]:
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
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class DocumentClassification(SubmodelElementCollectionUnordered):
            class ClassId(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "ClassId",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH996#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Unique ID of the document class within a ClassficationSystem. Constraint: If ClassificationSystem is set to “VDI2770:2018”, the given IDs of VDI2770:2018 shall be used"
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="03-02",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class ClassName(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "ClassName",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO102#003",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "List of language-dependent names of the selected ClassID. Constraint: If ClassificationSystem is set to “VDI2770:2018” then the given names of VDI2770:2018 need be used. Constraint: languages shall match at least the language specifications of the included DocumentVersions (below)."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Operation@en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class ClassificationSystem(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "ClassificationSystem",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH997#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": 'Identification of the classification system. For classifications according VDI 2270 always set to "VDI2770:2018". Further classification systems are commonly used, such as "IEC61355-1:2008".'
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="VDI2770:2018",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            def __init__(
                self,
                classId: Union[str, ClassId],
                className: Union[LangStringSet, ClassName],
                classificationSystem: Union[str, ClassificationSystem],
                id_short: str = "DocumentClassification",
                category: Optional[str] = "PARAMETER",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-ABI502#001/0173-1#01-AHF581#001*01",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Set of information for describing the classification of the Document according to ClassificationSystems. Constraint: at least one classification according to VDI 2770 shall be provided."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Cardinality",
                            value_type=str,
                            value="OneToMany",
                            value_id=None,
                            semantic_id=Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.GLOBAL_REFERENCE,
                                        local=False,
                                        value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if classId and not isinstance(classId, SubmodelElement):
                    classId = self.ClassId(classId)

                # Build a submodel element if a raw value was passed in the argument
                if className and not isinstance(className, SubmodelElement):
                    className = self.ClassName(className)

                # Build a submodel element if a raw value was passed in the argument
                if classificationSystem and not isinstance(
                    classificationSystem, SubmodelElement
                ):
                    classificationSystem = self.ClassificationSystem(
                        classificationSystem
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [classId, className, classificationSystem]:
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
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class DocumentVersion(SubmodelElementCollectionUnordered):
            class Language(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "Language",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAN468#006",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "This property contains a list of languages used within the DocumentVersion. Each property codes one language identification according to ISO 639-1 or ISO 639-2 used in the Document."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="Language[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class DocumentVersionId(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "DocumentVersionId",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO100#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Unambigous identification number of a DocumentVersion."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="V1.2",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Title(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "Title",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO105#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "List of language-dependent titles of the Document. Constraint: For each language-depended Title a Summary and at least one KeyWord shall exist for the given language."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Examplary title@en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class SubTitle(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "SubTitle",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH998#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "List of language-dependent subtitles of the Document."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Examplary subtitle@en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class Summary(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "Summary",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO106#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "List of language-dependent summaries of the Document. Constraint: For each language-depended Summary a Title and at least one KeyWord shall exist for the given language."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Abstract@en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class KeyWords(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "KeyWords",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABH999#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "List of language-dependent keywords of the Document. Note: Mutiple keywords are given as comma separated list for each language. Constraint: For each language-depended KeyWord a Title and Summary shall exist for the given language. Note: This can be intentionally a blank."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Examplary keywords@en",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class StatusSetDate(Property):
                def __init__(
                    self,
                    value: Date,
                    id_short: str = "StatusSetDate",
                    value_type: DataTypeDef = Date,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI000#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Date when the document status was set. Format is YYYY-MM-dd."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=Date,
                                value=Date(),
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class StatusValue(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "StatusValue",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI001#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Each document version represents a point in time in the document life cycle. This status value refers to the milestones in the document life cycle. The following two values should be used for the application of this guideline: InReview (under review), Released (released)"
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Released",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class OrganizationName(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "OrganizationName",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI002#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Organiziation short name of the author of the Document."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Example company",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class OrganizationOfficialName(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "OrganizationOfficialName",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI004#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Official name of the organization of author of the Document."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="Example company Ltd.",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class RefersTo(ReferenceElement):
                def __init__(
                    self,
                    value: Reference,
                    id_short: str = "RefersTo",
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI006#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": 'Forms a generic RefersTo-relationship to another Document or DocumentVersion. They have a loose relationship. Constraint: reference targets a SMC "Document" or a “DocumentVersion”.'
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="RefersTo[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class BasedOn(ReferenceElement):
                def __init__(
                    self,
                    value: Reference,
                    id_short: str = "BasedOn",
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI007#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": 'Forms a BasedOn-relationship to another Document or DocumentVersion. Typically states, that the content of the document bases on another document (e.g. specification requirements). Both have a strong relationship. Constraint: reference targets a SMC "Document" or a “DocumentVersion”.'
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="BasedOn[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class TranslationOf(ReferenceElement):
                def __init__(
                    self,
                    value: Reference,
                    id_short: str = "TranslationOf",
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI008#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": 'Forms a TranslationOf-relationship to another Document or DocumentVersion. Both have a strong relationship. Constaint: The (language independent) content must be identical in both documents or document versions. Constraint: reference targets a SMC "Document" or a “DocumentVersion”.'
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="TranslationOf[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    super().__init__(
                        value=value,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class DigitalFile(SubmodelElementCollectionUnordered):
                class MimeType(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "MimeType",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "PARAMETER",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO214#002 ",
                                    id_type=KeyType.IRDI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "The MIME-Type classifies the data of massage."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="Cardinality",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.GLOBAL_REFERENCE,
                                                local=False,
                                                value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                id_type=KeyType.IRI,
                                            ),
                                        )
                                    ),
                                )
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class DocumentPath(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "DocumentPath",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "PARAMETER",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-ABI005#001 ",
                                    id_type=KeyType.IRDI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "The document path leads to the document."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="Cardinality",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.GLOBAL_REFERENCE,
                                                local=False,
                                                value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                id_type=KeyType.IRI,
                                            ),
                                        )
                                    ),
                                )
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    mimeType: Union[str, MimeType],
                    documentPath: Union[str, DocumentPath],
                    id_short: str = "DigitalFile",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI504#001/0173-1#01-AHF583#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: each DigitalFile represents the same content or Document version, but can be provided in different technical formats (PDF, PDFA, html..) or by a link."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="docu_cecc_fullmanual_DE.PDF",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="DigitalFile[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="OneToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if mimeType and not isinstance(mimeType, SubmodelElement):
                        mimeType = self.MimeType(mimeType)

                    # Build a submodel element if a raw value was passed in the argument
                    if documentPath and not isinstance(documentPath, SubmodelElement):
                        documentPath = self.DocumentPath(documentPath)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [mimeType, documentPath]:
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
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class PreviewFile(SubmodelElementCollectionUnordered):
                class MimeType(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "MimeType",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "PARAMETER",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-AAO214#002 ",
                                    id_type=KeyType.IRDI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "The MIME-Type classifies the data of massage."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="Cardinality",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.GLOBAL_REFERENCE,
                                                local=False,
                                                value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                id_type=KeyType.IRI,
                                            ),
                                        )
                                    ),
                                )
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                class DocumentPath(Property):
                    def __init__(
                        self,
                        value: str,
                        id_short: str = "DocumentPath",
                        value_type: DataTypeDef = str,
                        value_id: Optional[Reference] = None,
                        category: Optional[str] = "PARAMETER",
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="0173-1#02-ABI005#001 ",
                                    id_type=KeyType.IRDI,
                                ),
                            )
                        ),
                        qualifier: Optional[Set[Constraint]] = None,
                        kind: ModelingKind = ModelingKind.INSTANCE,
                    ):
                        if description is None:
                            description = {
                                "en": "The document path leads to the document."
                            }

                        if qualifier is None:
                            qualifier = {
                                Qualifier(
                                    type_="Cardinality",
                                    value_type=str,
                                    value="One",
                                    value_id=None,
                                    semantic_id=Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.GLOBAL_REFERENCE,
                                                local=False,
                                                value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                id_type=KeyType.IRI,
                                            ),
                                        )
                                    ),
                                )
                            }

                        super().__init__(
                            value=value,
                            id_short=id_short,
                            value_type=value_type,
                            value_id=value_id,
                            category=category,
                            description=description,
                            semantic_id=semantic_id,
                            qualifier=qualifier,
                            kind=kind,
                        )

                def __init__(
                    self,
                    mimeType: Union[str, MimeType],
                    documentPath: Union[str, DocumentPath],
                    id_short: str = "PreviewFile",
                    category: Optional[str] = "PARAMETER",
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-ABI505#001 /0173-1#01-AHF584#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Provides a preview image of the DocumentVersion, e.g. first page, in a commonly used image format and low resolution. Note: low resolution e.g. < 512 x 512 pixels. Constraint: the MIME type needs to match the file type. Allowed file types are JPG, PNG, BMP."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Cardinality",
                                value_type=str,
                                value="ZeroToMany",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="ExampleValue",
                                value_type=str,
                                value="docu_cecc_fullmanual_DE.jpg",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                            Qualifier(
                                type_="AllowedIdShort",
                                value_type=str,
                                value="PreviewFile[\d{2,3}]",
                                value_id=None,
                                semantic_id=Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.GLOBAL_REFERENCE,
                                            local=False,
                                            value="https://admin-shell.io/SubmodelTemplates/AllowedIdShort/1/0",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                            ),
                        }

                    # Build a submodel element if a raw value was passed in the argument
                    if mimeType and not isinstance(mimeType, SubmodelElement):
                        mimeType = self.MimeType(mimeType)

                    # Build a submodel element if a raw value was passed in the argument
                    if documentPath and not isinstance(documentPath, SubmodelElement):
                        documentPath = self.DocumentPath(documentPath)

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [mimeType, documentPath]:
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
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            def __init__(
                self,
                language: Iterable[Union[str, Language]],
                documentVersionId: Union[str, DocumentVersionId],
                title: Union[LangStringSet, Title],
                summary: Union[LangStringSet, Summary],
                keyWords: Union[LangStringSet, KeyWords],
                statusSetDate: Union[Date, StatusSetDate],
                statusValue: Union[str, StatusValue],
                organizationName: Union[str, OrganizationName],
                organizationOfficialName: Union[str, OrganizationOfficialName],
                digitalFile: Iterable[DigitalFile],
                subTitle: Optional[Union[LangStringSet, SubTitle]] = None,
                refersTo: Optional[Iterable[Union[Reference, RefersTo]]] = None,
                basedOn: Optional[Iterable[Union[Reference, BasedOn]]] = None,
                translationOf: Optional[
                    Iterable[Union[Reference, TranslationOf]]
                ] = None,
                previewFile: Optional[Iterable[PreviewFile]] = None,
                id_short: str = "DocumentVersion",
                category: Optional[str] = "PARAMETER",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-ABI503#001/0173-1#01-AHF582#001*01",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Information elements of individual VDI 2770 DocumentVersion entities. Note: at the time of handover, this collection shall include at least one DocumentVersion."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Cardinality",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.GLOBAL_REFERENCE,
                                        local=False,
                                        value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                        )
                    }

                # Build a list of submodel elements if a raw values were passed in the argument
                if language and all([isinstance(i, str) for i in language]):
                    language = [self.Language(i) for i in language]

                # Build a submodel element if a raw value was passed in the argument
                if documentVersionId and not isinstance(
                    documentVersionId, SubmodelElement
                ):
                    documentVersionId = self.DocumentVersionId(documentVersionId)

                # Build a submodel element if a raw value was passed in the argument
                if title and not isinstance(title, SubmodelElement):
                    title = self.Title(title)

                # Build a submodel element if a raw value was passed in the argument
                if subTitle and not isinstance(subTitle, SubmodelElement):
                    subTitle = self.SubTitle(subTitle)

                # Build a submodel element if a raw value was passed in the argument
                if summary and not isinstance(summary, SubmodelElement):
                    summary = self.Summary(summary)

                # Build a submodel element if a raw value was passed in the argument
                if keyWords and not isinstance(keyWords, SubmodelElement):
                    keyWords = self.KeyWords(keyWords)

                # Build a submodel element if a raw value was passed in the argument
                if statusSetDate and not isinstance(statusSetDate, SubmodelElement):
                    statusSetDate = self.StatusSetDate(statusSetDate)

                # Build a submodel element if a raw value was passed in the argument
                if statusValue and not isinstance(statusValue, SubmodelElement):
                    statusValue = self.StatusValue(statusValue)

                # Build a submodel element if a raw value was passed in the argument
                if organizationName and not isinstance(
                    organizationName, SubmodelElement
                ):
                    organizationName = self.OrganizationName(organizationName)

                # Build a submodel element if a raw value was passed in the argument
                if organizationOfficialName and not isinstance(
                    organizationOfficialName, SubmodelElement
                ):
                    organizationOfficialName = self.OrganizationOfficialName(
                        organizationOfficialName
                    )

                # Build a list of submodel elements if a raw values were passed in the argument
                if refersTo and all([isinstance(i, Reference) for i in refersTo]):
                    refersTo = [self.RefersTo(i) for i in refersTo]

                # Build a list of submodel elements if a raw values were passed in the argument
                if basedOn and all([isinstance(i, Reference) for i in basedOn]):
                    basedOn = [self.BasedOn(i) for i in basedOn]

                # Build a list of submodel elements if a raw values were passed in the argument
                if translationOf and all(
                    [isinstance(i, Reference) for i in translationOf]
                ):
                    translationOf = [self.TranslationOf(i) for i in translationOf]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    language,
                    documentVersionId,
                    title,
                    subTitle,
                    summary,
                    keyWords,
                    statusSetDate,
                    statusValue,
                    organizationName,
                    organizationOfficialName,
                    refersTo,
                    basedOn,
                    translationOf,
                    digitalFile,
                    previewFile,
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
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        class DocumentedEntity(ReferenceElement):
            def __init__(
                self,
                value: Reference,
                id_short: str = "DocumentedEntity",
                category: Optional[str] = "PARAMETER",
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.GLOBAL_REFERENCE,
                            local=False,
                            value="https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Identifies entities, which are subject to the Document. Note: can be omitted, if the subject of the Document is the overall Asset of the Asset Administration Shell. Note: if no Entity according clause 2.2 is referenced, this ReferenceElement is not required at all. Note: This mechanism substitutes the ObjectId-provision of the VDI2770 (see section 2.2 and appendix B)."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Cardinality",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.GLOBAL_REFERENCE,
                                        local=False,
                                        value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                        )
                    }

                super().__init__(
                    value=value,
                    id_short=id_short,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    kind=kind,
                )

        def __init__(
            self,
            documentId: Iterable[DocumentId],
            documentClassification: Iterable[DocumentClassification],
            documentVersion: Optional[Iterable[DocumentVersion]] = None,
            documentedEntity: Optional[
                Iterable[Union[Reference, DocumentedEntity]]
            ] = None,
            id_short: str = "Document",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-ABI500#001/0173-1#01-AHF579#001*01",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Each SMC describes a Document (see IEC 82045-1 and IEC 8245-2), which is associated to the particular Asset Administration Shell."
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Cardinality",
                        value_type=str,
                        value="ZeroToMany",
                        value_id=None,
                        semantic_id=Reference(
                            key=(
                                Key(
                                    type_=KeyElements.GLOBAL_REFERENCE,
                                    local=False,
                                    value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    id_type=KeyType.IRI,
                                ),
                            )
                        ),
                    )
                }

            # Build a list of submodel elements if a raw values were passed in the argument
            if documentedEntity and all(
                [isinstance(i, Reference) for i in documentedEntity]
            ):
                documentedEntity = [self.DocumentedEntity(i) for i in documentedEntity]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                documentId,
                documentClassification,
                documentVersion,
                documentedEntity,
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
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class Entity(Entity):
        def __init__(
            self,
            id_short: str = "Entity",
            entity_type: EntityType = EntityType.CO_MANAGED_ENTITY,
            statement: Iterable[SubmodelElement] = (),
            asset: Optional[AASReference[ForwardRef("Asset")]] = None,
            category: Optional[str] = "PARAMETER",
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.GLOBAL_REFERENCE,
                        local=False,
                        value="https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation",
                        id_type=KeyType.IRI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "States, that the described Entity is an important entity for documentation of the superordinate Asset of the Asset Administration Shell. Note: typically, such Entities are well-identified sub-parts of the Asset, such as supplier parts delivered to the manufacturer of the Asset."
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Cardinality",
                        value_type=str,
                        value="ZeroToMany",
                        value_id=None,
                        semantic_id=Reference(
                            key=(
                                Key(
                                    type_=KeyElements.GLOBAL_REFERENCE,
                                    local=False,
                                    value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    id_type=KeyType.IRI,
                                ),
                            )
                        ),
                    )
                }

            super().__init__(
                id_short=id_short,
                entity_type=entity_type,
                statement=statement,
                asset=asset,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    def __init__(
        self,
        identification: Identifier,
        numberOfDocuments: Optional[Union[int, NumberOfDocuments]] = None,
        document: Optional[Iterable[Document]] = None,
        entity: Optional[Iterable[Entity]] = None,
        id_short: str = "HandoverDocumentation",
        category: Optional[str] = "PARAMETER",
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = AdministrativeInformation(
            version="1", revision="2"
        ),
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.SUBMODEL,
                    local=True,
                    value="0173-1#01-AHF578#001",
                    id_type=KeyType.IRDI,
                ),
            )
        ),
        qualifier: Optional[Set[Constraint]] = None,
        kind: ModelingKind = ModelingKind.INSTANCE,
    ):
        if description is None:
            description = {
                "en": "The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment."
            }

        if qualifier is None:
            qualifier = set()

        # Build a submodel element if a raw value was passed in the argument
        if numberOfDocuments and not isinstance(numberOfDocuments, SubmodelElement):
            numberOfDocuments = self.NumberOfDocuments(numberOfDocuments)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [numberOfDocuments, document, entity]:
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
            identification=identification,
            id_short=id_short,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
        )
