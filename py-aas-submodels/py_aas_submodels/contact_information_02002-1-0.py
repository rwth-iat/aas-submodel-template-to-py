from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class ContactInformations(Submodel):
    class ContactInformation(SubmodelElementCollectionUnordered):
        class RoleOfContactPerson(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "RoleOfContactPerson",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO204#003",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "enumeration: 0173-1#07-AAS927#001 (administrativ contact), 0173-1#07-AAS928#001 (commercial contact), 0173-1#07-AAS929#001 (other contact), 0173-1#07-AAS930#001 (hazardous goods contact), 0173-1#07-AAS931#001 (technical contact). Note: the above mentioned ECLASS enumeration should be declared as “open” for further addition. ECLASS enumeration IRDI is preferable. If no IRDI available, custom input as String may also be accepted."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
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

        class NationalCode(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "NationalCode",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO134#002",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": " Note: country codes defined accord. to ISO 3166-1. Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Language(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "Language",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Language",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Note: language codes defined accord. to ISO 639-1. Note: as per ECLASS definition, Expression and representation of thoughts, information, feelings, ideas through characters."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
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

        class TimeZone(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "TimeZone",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/TimeZone",
                            id_type=KeyType.IRI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Note: notation accord. to ISO 8601 Note: for time in UTC the zone designator “Z” is to be used"
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
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

        class CityTown(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "CityTown",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO132#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Company(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Company",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAW001#001",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Department(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Department",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO127#003",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Phone(SubmodelElementCollectionUnordered):
            class TelephoneNumber(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "TelephoneNumber",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO136#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
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

            class TypeOfTelephone(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "TypeOfTelephone",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO137#003",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": " enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS755#001 (office mobile), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS757#001 (substitute), 0173-1#07-AAS758#001 (home), 0173-1#07-AAS759#001 (private mobile)"
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
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

            class AvailableTime(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "AvailableTime",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
                                id_type=KeyType.IRI,
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
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            )
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

            def __init__(
                self,
                telephoneNumber: Union[LangStringSet, TelephoneNumber],
                typeOfTelephone: Optional[Union[str, TypeOfTelephone]] = None,
                availableTime: Optional[Union[LangStringSet, AvailableTime]] = None,
                id_short: str = "Phone",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone",
                            id_type=KeyType.IRI,
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if telephoneNumber and not isinstance(telephoneNumber, SubmodelElement):
                    telephoneNumber = self.TelephoneNumber(telephoneNumber)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfTelephone and not isinstance(typeOfTelephone, SubmodelElement):
                    typeOfTelephone = self.TypeOfTelephone(typeOfTelephone)

                # Build a submodel element if a raw value was passed in the argument
                if availableTime and not isinstance(availableTime, SubmodelElement):
                    availableTime = self.AvailableTime(availableTime)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [telephoneNumber, typeOfTelephone, availableTime]:
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

        class Fax(SubmodelElementCollectionUnordered):
            class FaxNumber(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "FaxNumber",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO195#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
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

            class TypeOfFaxNumber(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "TypeOfFaxNumber",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO196#003",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS758#001 (home)"
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
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
                faxNumber: Union[LangStringSet, FaxNumber],
                typeOfFaxNumber: Optional[Union[str, TypeOfFaxNumber]] = None,
                id_short: str = "Fax",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAQ834#005",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if faxNumber and not isinstance(faxNumber, SubmodelElement):
                    faxNumber = self.FaxNumber(faxNumber)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfFaxNumber and not isinstance(typeOfFaxNumber, SubmodelElement):
                    typeOfFaxNumber = self.TypeOfFaxNumber(typeOfFaxNumber)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [faxNumber, typeOfFaxNumber]:
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

        class Email(SubmodelElementCollectionUnordered):
            class EmailAddress(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "EmailAddress",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO198#002",
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
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
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

            class PublicKey(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "PublicKey",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO200#002",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            )
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

            class TypeOfEmailAddress(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "TypeOfEmailAddress",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO199#003",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "enumeration: 0173-1#07-AAS754#001 (office), 0173-1#07-AAS756#001 (secretary), 0173-1#07-AAS757#001 (substitute), 0173-1#07-AAS758#001 (home)"
                        }

                    if qualifier is None:
                        qualifier = {
                            Qualifier(
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
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

            class TypeOfPublicKey(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "TypeOfPublicKey",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO201#002",
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
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            )
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

            def __init__(
                self,
                emailAddress: Union[str, EmailAddress],
                publicKey: Optional[Union[LangStringSet, PublicKey]] = None,
                typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                typeOfPublicKey: Optional[Union[LangStringSet, TypeOfPublicKey]] = None,
                id_short: str = "Email",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAQ836#005",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if emailAddress and not isinstance(emailAddress, SubmodelElement):
                    emailAddress = self.EmailAddress(emailAddress)

                # Build a submodel element if a raw value was passed in the argument
                if publicKey and not isinstance(publicKey, SubmodelElement):
                    publicKey = self.PublicKey(publicKey)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfEmailAddress and not isinstance(
                    typeOfEmailAddress, SubmodelElement
                ):
                    typeOfEmailAddress = self.TypeOfEmailAddress(typeOfEmailAddress)

                # Build a submodel element if a raw value was passed in the argument
                if typeOfPublicKey and not isinstance(typeOfPublicKey, SubmodelElement):
                    typeOfPublicKey = self.TypeOfPublicKey(typeOfPublicKey)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    emailAddress,
                    publicKey,
                    typeOfEmailAddress,
                    typeOfPublicKey,
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

        class IPCommunication(SubmodelElementCollectionUnordered):
            class AddressOfAdditionalLink(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "AddressOfAdditionalLink",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAQ326#002",
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
                                type_="Multiplicity",
                                value_type=str,
                                value="One",
                                value_id=None,
                                semantic_id=None,
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

            class TypeOfCommunication(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "TypeOfCommunication",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/1/0/ ContactInformations/ContactInformation/IPCommunication/TypeOfCommunication",
                                id_type=KeyType.IRI,
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
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
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

            class AvailableTime(MultiLanguageProperty):
                def __init__(
                    self,
                    value: LangStringSet,
                    id_short: str = "AvailableTime",
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/",
                                id_type=KeyType.IRI,
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
                                type_="Multiplicity",
                                value_type=str,
                                value="ZeroToOne",
                                value_id=None,
                                semantic_id=None,
                            )
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

            def __init__(
                self,
                addressOfAdditionalLink: Union[str, AddressOfAdditionalLink],
                typeOfCommunication: Optional[Union[str, TypeOfCommunication]] = None,
                availableTime: Optional[Union[LangStringSet, AvailableTime]] = None,
                id_short: str = "IPCommunication",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/",
                            id_type=KeyType.IRI,
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToMany",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if addressOfAdditionalLink and not isinstance(
                    addressOfAdditionalLink, SubmodelElement
                ):
                    addressOfAdditionalLink = self.AddressOfAdditionalLink(
                        addressOfAdditionalLink
                    )

                # Build a submodel element if a raw value was passed in the argument
                if typeOfCommunication and not isinstance(
                    typeOfCommunication, SubmodelElement
                ):
                    typeOfCommunication = self.TypeOfCommunication(typeOfCommunication)

                # Build a submodel element if a raw value was passed in the argument
                if availableTime and not isinstance(availableTime, SubmodelElement):
                    availableTime = self.AvailableTime(availableTime)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    addressOfAdditionalLink,
                    typeOfCommunication,
                    availableTime,
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

        class Street(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Street",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO128#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Zipcode(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Zipcode",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO129#002",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class POBox(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "POBox",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO130#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class ZipCodeOfPOBox(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "ZipCodeOfPOBox",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO131#002",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
                    }

                if qualifier is None:
                    qualifier = {
                        Qualifier(
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class StateCounty(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "StateCounty",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO133#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class NameOfContact(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "NameOfContact",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO205#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class FirstName(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "FirstName",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO206#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class MiddleNames(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "MiddleNames",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO207#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class Title(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "Title",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO208#003",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class AcademicTitle(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "AcademicTitle",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO209#003",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class FurtherDetailsOfContact(MultiLanguageProperty):
            def __init__(
                self,
                value: LangStringSet,
                id_short: str = "FurtherDetailsOfContact",
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAO210#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
                        )
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

        class AddressOfAdditionalLink(Property):
            def __init__(
                self,
                value: str,
                id_short: str = "AddressOfAdditionalLink",
                value_type: DataTypeDef = str,
                value_id: Optional[Reference] = None,
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#02-AAQ326#002",
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
                            type_="Multiplicity",
                            value_type=str,
                            value="ZeroToOne",
                            value_id=None,
                            semantic_id=None,
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
            roleOfContactPerson: Optional[Union[str, RoleOfContactPerson]] = None,
            nationalCode: Optional[Union[LangStringSet, NationalCode]] = None,
            language: Optional[Iterable[Union[str, Language]]] = None,
            timeZone: Optional[Union[str, TimeZone]] = None,
            cityTown: Optional[Union[LangStringSet, CityTown]] = None,
            company: Optional[Union[LangStringSet, Company]] = None,
            department: Optional[Union[LangStringSet, Department]] = None,
            phone: Optional[Phone] = None,
            fax: Optional[Fax] = None,
            email: Optional[Email] = None,
            iPCommunication: Optional[Iterable[IPCommunication]] = None,
            street: Optional[Union[LangStringSet, Street]] = None,
            zipcode: Optional[Union[LangStringSet, Zipcode]] = None,
            pOBox: Optional[Union[LangStringSet, POBox]] = None,
            zipCodeOfPOBox: Optional[Union[LangStringSet, ZipCodeOfPOBox]] = None,
            stateCounty: Optional[Union[LangStringSet, StateCounty]] = None,
            nameOfContact: Optional[Union[LangStringSet, NameOfContact]] = None,
            firstName: Optional[Union[LangStringSet, FirstName]] = None,
            middleNames: Optional[Union[LangStringSet, MiddleNames]] = None,
            title: Optional[Union[LangStringSet, Title]] = None,
            academicTitle: Optional[Union[LangStringSet, AcademicTitle]] = None,
            furtherDetailsOfContact: Optional[
                Union[LangStringSet, FurtherDetailsOfContact]
            ] = None,
            addressOfAdditionalLink: Optional[
                Union[str, AddressOfAdditionalLink]
            ] = None,
            id_short: str = "ContactInformation",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation",
                        id_type=KeyType.IRI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required"
                }

            if qualifier is None:
                qualifier = {
                    Qualifier(
                        type_="Multiplicity",
                        value_type=str,
                        value="OneToMany",
                        value_id=None,
                        semantic_id=None,
                    )
                }

            # Build a submodel element if a raw value was passed in the argument
            if roleOfContactPerson and not isinstance(
                roleOfContactPerson, SubmodelElement
            ):
                roleOfContactPerson = self.RoleOfContactPerson(roleOfContactPerson)

            # Build a submodel element if a raw value was passed in the argument
            if nationalCode and not isinstance(nationalCode, SubmodelElement):
                nationalCode = self.NationalCode(nationalCode)

            # Build a list of submodel elements if a raw values were passed in the argument
            if language and all([isinstance(i, str) for i in language]):
                language = [self.Language(i) for i in language]

            # Build a submodel element if a raw value was passed in the argument
            if timeZone and not isinstance(timeZone, SubmodelElement):
                timeZone = self.TimeZone(timeZone)

            # Build a submodel element if a raw value was passed in the argument
            if cityTown and not isinstance(cityTown, SubmodelElement):
                cityTown = self.CityTown(cityTown)

            # Build a submodel element if a raw value was passed in the argument
            if company and not isinstance(company, SubmodelElement):
                company = self.Company(company)

            # Build a submodel element if a raw value was passed in the argument
            if department and not isinstance(department, SubmodelElement):
                department = self.Department(department)

            # Build a submodel element if a raw value was passed in the argument
            if street and not isinstance(street, SubmodelElement):
                street = self.Street(street)

            # Build a submodel element if a raw value was passed in the argument
            if zipcode and not isinstance(zipcode, SubmodelElement):
                zipcode = self.Zipcode(zipcode)

            # Build a submodel element if a raw value was passed in the argument
            if pOBox and not isinstance(pOBox, SubmodelElement):
                pOBox = self.POBox(pOBox)

            # Build a submodel element if a raw value was passed in the argument
            if zipCodeOfPOBox and not isinstance(zipCodeOfPOBox, SubmodelElement):
                zipCodeOfPOBox = self.ZipCodeOfPOBox(zipCodeOfPOBox)

            # Build a submodel element if a raw value was passed in the argument
            if stateCounty and not isinstance(stateCounty, SubmodelElement):
                stateCounty = self.StateCounty(stateCounty)

            # Build a submodel element if a raw value was passed in the argument
            if nameOfContact and not isinstance(nameOfContact, SubmodelElement):
                nameOfContact = self.NameOfContact(nameOfContact)

            # Build a submodel element if a raw value was passed in the argument
            if firstName and not isinstance(firstName, SubmodelElement):
                firstName = self.FirstName(firstName)

            # Build a submodel element if a raw value was passed in the argument
            if middleNames and not isinstance(middleNames, SubmodelElement):
                middleNames = self.MiddleNames(middleNames)

            # Build a submodel element if a raw value was passed in the argument
            if title and not isinstance(title, SubmodelElement):
                title = self.Title(title)

            # Build a submodel element if a raw value was passed in the argument
            if academicTitle and not isinstance(academicTitle, SubmodelElement):
                academicTitle = self.AcademicTitle(academicTitle)

            # Build a submodel element if a raw value was passed in the argument
            if furtherDetailsOfContact and not isinstance(
                furtherDetailsOfContact, SubmodelElement
            ):
                furtherDetailsOfContact = self.FurtherDetailsOfContact(
                    furtherDetailsOfContact
                )

            # Build a submodel element if a raw value was passed in the argument
            if addressOfAdditionalLink and not isinstance(
                addressOfAdditionalLink, SubmodelElement
            ):
                addressOfAdditionalLink = self.AddressOfAdditionalLink(
                    addressOfAdditionalLink
                )

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                roleOfContactPerson,
                nationalCode,
                language,
                timeZone,
                cityTown,
                company,
                department,
                phone,
                fax,
                email,
                iPCommunication,
                street,
                zipcode,
                pOBox,
                zipCodeOfPOBox,
                stateCounty,
                nameOfContact,
                firstName,
                middleNames,
                title,
                academicTitle,
                furtherDetailsOfContact,
                addressOfAdditionalLink,
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

    def __init__(
        self,
        identification: Identifier,
        contactInformation: Iterable[ContactInformation],
        id_short: str = "ContactInformations",
        category: Optional[str] = None,
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.CONCEPT_DESCRIPTION,
                    local=True,
                    value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations",
                    id_type=KeyType.IRI,
                ),
            )
        ),
        qualifier: Optional[Set[Constraint]] = None,
        kind: ModelingKind = ModelingKind.INSTANCE,
    ):
        if description is None:
            description = set()

        if qualifier is None:
            qualifier = set()

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [contactInformation]:
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
