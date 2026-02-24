from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *


class Nameplate(Submodel):
    class URIOfTheProduct(Property):
        def __init__(
            self,
            value: str,
            id_short: str = "URIOfTheProduct",
            value_type: DataTypeDef = str,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAY811#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABN590#001 URI of product instance "
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
                value_type=value_type,
                value_id=value_id,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class ManufacturerName(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ManufacturerName",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAO677#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA565#007 manufacturer Note: mandatory property according to EU Machine Directive 2006/42/EC. "
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

    class ManufacturerProductDesignation(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ManufacturerProductDesignation",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAW338#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA567#007 name of product Note: Short designation of the product is meant. Note: mandatory property according to EU Machine Directive 2006/42/EC. "
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
                        "en": "Note: see also [IRDI] 0112/2///61360_4#ADA005#001 country code. country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes. Mandatory property according to EU Machine Directive 2006/42/EC. Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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
                    description = {
                        "en": "Note: see also [IRDI] 0112/2///61987#ABA129#001 city/town. Mandatory property according to EU Machine Directive 2006/42/EC."
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
                    description = {
                        "en": "Note: see also [IRDI] 0112/2///61987#ABA286#001 street. Mandatory property according to EU Machine Directive 2006/42/EC"
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
                        "en": "Note: see also [IRDI] 0112/2///61987#ABA281#001 ZIP/Postal code. Mandatory property according to EU Machine Directive 2006/42/EC. Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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
            nationalCode: Union[LangStringSet, NationalCode],
            cityTown: Union[LangStringSet, CityTown],
            street: Union[LangStringSet, Street],
            zipcode: Union[LangStringSet, Zipcode],
            roleOfContactPerson: Optional[Union[str, RoleOfContactPerson]] = None,
            language: Optional[Iterable[Union[str, Language]]] = None,
            timeZone: Optional[Union[str, TimeZone]] = None,
            company: Optional[Union[LangStringSet, Company]] = None,
            department: Optional[Union[LangStringSet, Department]] = None,
            phone: Optional[Phone] = None,
            fax: Optional[Fax] = None,
            email: Optional[Email] = None,
            iPCommunication: Optional[Iterable[IPCommunication]] = None,
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
                    "en": "The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required. Note: physical address is a mandatory property according to EU Machine Directive 2006/42/EC"
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

    class ManufacturerProductRoot(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ManufacturerProductRoot",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAU732#001",
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

    class ManufacturerProductFamily(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ManufacturerProductFamily",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAU731#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: conditionally mandatory property according to EU Machine Directive 2006/42/EC. One of the two properties must be provided: ManufacturerProductFamily (0173-1#02-AAU731#001) or ManufacturerProductType (0173-1#02-AAO057#002). "
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

    class ManufacturerProductType(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ManufacturerProductType",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAO057#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA300#006 code of product Note: conditionally mandatory property according to EU Machine Directive 2006/42/EC. One of the two properties must be provided: ManufacturerProductFamily (0173-1#02-AAU731#001) or ManufacturerProductType (0173-1#02-AAO057#002). "
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

    class OrderCodeOfManufacturer(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "OrderCodeOfManufacturer",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAO227#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA950#006 order code of product Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

    class ProductArticleNumberOfManufacturer(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "ProductArticleNumberOfManufacturer",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAO676#003",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA581#006 article number Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

    class SerialNumber(Property):
        def __init__(
            self,
            value: str,
            id_short: str = "SerialNumber",
            value_type: DataTypeDef = str,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAM556#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA951#007 serial number "
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

    class YearOfConstruction(Property):
        def __init__(
            self,
            value: str,
            id_short: str = "YearOfConstruction",
            value_type: DataTypeDef = str,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAP906#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: mandatory property according to EU Machine Directive 2006/42/EC. "
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
                value_type=value_type,
                value_id=value_id,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class DateOfManufacture(Property):
        def __init__(
            self,
            value: Date,
            id_short: str = "DateOfManufacture",
            value_type: DataTypeDef = Date,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAR972#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABB757#007 date of manufacture Note: format by lexical representation: CCYY-MM-DD "
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

    class HardwareVersion(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "HardwareVersion",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAN270#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA926#006 hardware version Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

    class FirmwareVersion(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "FirmwareVersion",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAM985#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA302#004 firmware version Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

    class SoftwareVersion(MultiLanguageProperty):
        def __init__(
            self,
            value: LangStringSet,
            id_short: str = "SoftwareVersion",
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAM737#002",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61987#ABA601#006 software version Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

    class CountryOfOrigin(Property):
        def __init__(
            self,
            value: str,
            id_short: str = "CountryOfOrigin",
            value_type: DataTypeDef = str,
            value_id: Optional[Reference] = None,
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#02-AAO259#004",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: see also [IRDI] 0112/2///61360_4#ADA034#001 country of origin Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes "
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

    class CompanyLogo(File):
        def __init__(
            self,
            value: str,
            mime_type: str,
            id_short: str = "CompanyLogo",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/CompanyLogo ",
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
                mime_type=mime_type,
                id_short=id_short,
                category=category,
                description=description,
                semantic_id=semantic_id,
                qualifier=qualifier,
                kind=kind,
            )

    class Markings(SubmodelElementCollectionUnordered):
        class Marking(SubmodelElementCollectionUnordered):
            class MarkingName(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "MarkingName",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingName",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: see also [IRDI] 0173-1#02-BAB392#015 certificate/approval valueId with ECLASS enumeration IRDI is preferable, e.g. [IRDI] 0173-1#07-DAA603#004 for CE. If no IRDI available, string value can also be accepted. Note: CE marking is declared as mandatory according to Blue Guide of the EU-Commission "
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
                        value_type=value_type,
                        value_id=value_id,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class DesignationOfCertificateOrApproval(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "DesignationOfCertificateOrApproval",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0112/2///61987#ABH783#001",
                                id_type=KeyType.IRDI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: Approval identifier, reference to the certificate number, to be entered without spaces "
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

            class IssueDate(Property):
                def __init__(
                    self,
                    value: Date,
                    id_short: str = "IssueDate",
                    value_type: DataTypeDef = Date,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/IssueDate",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
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

            class ExpiryDate(Property):
                def __init__(
                    self,
                    value: Date,
                    id_short: str = "ExpiryDate",
                    value_type: DataTypeDef = Date,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExpiryDate",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: see also ([IRDI] 0173-1#02-AAO997#001 Validity date Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
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

            class MarkingFile(File):
                def __init__(
                    self,
                    value: str,
                    mime_type: str,
                    id_short: str = "MarkingFile",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingFile",
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
                                value="One",
                                value_id=None,
                                semantic_id=None,
                            )
                        }

                    super().__init__(
                        value=value,
                        mime_type=mime_type,
                        id_short=id_short,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        kind=kind,
                    )

            class MarkingAdditionalText(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "MarkingAdditionalText",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/MarkingAdditionalText",
                                id_type=KeyType.IRI,
                            ),
                        )
                    ),
                    qualifier: Optional[Set[Constraint]] = None,
                    kind: ModelingKind = ModelingKind.INSTANCE,
                ):
                    if description is None:
                        description = {
                            "en": "Note: see also [IRDI] 0173-1#02-AAM954#002 details of other certificate "
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

            class ExplosionSafeties(SubmodelElementCollectionUnordered):
                class ExplosionSafety(SubmodelElementCollectionUnordered):
                    class DesignationOfCertificateOrApproval(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "DesignationOfCertificateOrApproval",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0112/2///61987#ABH783#001",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: Approval identifier, reference to the certificate number, to be entered without spaces "
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

                    class TypeOfApproval(MultiLanguageProperty):
                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: str = "TypeOfApproval",
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0173-1#02-AAM812#003",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: see also [IRDI] 0112/2///61987#ABA231#008 type of hazardous area approval Note: name of the approval system, e.g. ATEX, IECEX, NEC, EAC, CCC, CEC Note: only values from the enumeration should be used as stated. For additional systems further values can be used. Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

                    class ApprovalAgencyTestingAgency(MultiLanguageProperty):
                        def __init__(
                            self,
                            value: LangStringSet,
                            id_short: str = "ApprovalAgencyTestingAgency",
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0173-1#02-AAM632#001",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: see also [IRDI] 0112/2///61987#ABA634#004 approval agency/testing agency Note: name of the agency, which has issued the certificate, e.g. PTB, KEMA, CSA, SIRA Note: only values from the enumeration should be used as stated. For additional systems further values can be used. Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

                    class TypeOfProtection(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "TypeOfProtection",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0173-1#02-AAQ325#003",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: see also [IRDI] 0112/2///61987#ABA589#002 type of protection (Ex) Note:  ·       Type of protection for the device as listed in the certificate ·       Symbol(s) for the Type of protection. Several types of protection are separated by a semicolon “;” ·       If several TypeOfProtection are listed in the same certificate, for each TypeOfProtection a separate SMC “Explosion Safety” shall be provided "
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

                    class RatedInsulationVoltage(Property):
                        def __init__(
                            self,
                            value: Decimal,
                            id_short: str = "RatedInsulationVoltage",
                            value_type: DataTypeDef = Decimal,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0173-1#02-AAN532#003",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: Um(eff) Note: Insulation voltage, if specified in the certificate "
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

                    class InstructionsControlDrawing(ReferenceElement):
                        def __init__(
                            self,
                            value: Reference,
                            id_short: str = "InstructionsControlDrawing",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="0112/2///61987#ABO102#001",
                                        id_type=KeyType.IRDI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: Reference to the instruction manual or control drawing "
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
                                category=category,
                                description=description,
                                semantic_id=semantic_id,
                                qualifier=qualifier,
                                kind=kind,
                            )

                    class SpecificConditionsForUse(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "SpecificConditionsForUse",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/SpecificConditionsForUse",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: X if any, otherwise no entry"
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

                    class IncompleteDevice(Property):
                        def __init__(
                            self,
                            value: str,
                            id_short: str = "IncompleteDevice",
                            value_type: DataTypeDef = str,
                            value_id: Optional[Reference] = None,
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/IncompleteDevice",
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

                    class AmbientConditions(SubmodelElementCollectionUnordered):
                        class DeviceCategory(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "DeviceCategory",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAK297#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA467#002 equipment/device category Note: editorial definiton: Category of device in accordance with directive 2014/34/EU Note: Equipment category according to the ATEX system. According to the current nameplate, also the combination “GD” is permitted Note: The combination “GD” is no longer accepted and was changed in the standards. Currently the marking for “G” and “D” must be provided in a separate marking string. Older devices may still exist with the marking “GD”. "
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

                        class EquipmentProtectionLevel(MultiLanguageProperty):
                            def __init__(
                                self,
                                value: LangStringSet,
                                id_short: str = "EquipmentProtectionLevel",
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAM668#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA464#005 equipment protection level Note: editorial definition: Level of protection assigned to equipment based on its likelihood of becoming a source of ignition Note: Equipment protection level according to the IEC standards. According to the current nameplate, also the combination “GD” is permitted Note: The combination “GD” is no longer accepted and was changed in the standards. Currently the marking for “G” and “D” must be provided in a separate marking string. Older devices may still exist with the marking “GD”. Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

                        class RegionalSpecificMarking(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "RegionalSpecificMarking",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/RegionalSpecificMarking",
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

                        class TypeOfProtection(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TypeOfProtection",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAQ325#003",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA589#002 type of protection (Ex) Note: Symbol(s) for the Type of protection. Several types of protection are separated by a semicolon “;” "
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

                        class ExplosionGroup(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "ExplosionGroup",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAT372#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA961#007 permitted gas group/explosion group Note: Equipment grouping according to IEC 60079-0 is meant by this property Note: Symbol(s) for the gas group (IIA…IIC) or dust group (IIIA…IIIC) "
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

                        class MinimumAmbientTemperature(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "MinimumAmbientTemperature",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAZ952#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA621#007 minimum ambient temperature Note: editorial defnition: lower limit of the temperature range of the environment in which the component, the pipework or the system can be operated Note: Rated minimum ambient temperature Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class MaxAmbientTemperature(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "MaxAmbientTemperature",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-BAA039#010",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA623#007 maximum ambient temperature Note: editorial definition: upper limit of the temperature range of the environment in which the component, the pipework or the system can be operated Note: Rated maximum ambient temperature Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class MaxSurfaceTemperatureForDustProof(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "MaxSurfaceTemperatureForDustProof",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAM666#005",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABB159#004 maximum surface temperature for dust-proof Note: Maximum surface temperature of the device (dust layer ≤ 5 mm) for specified maximum ambient and maximum process temperature, relevant for Group III only Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class TemperatureClass(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TemperatureClass",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAO371#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA593#002 temperature class Note: editorial definition: classification system of electrical apparatus, based on its maximum surface temperature, intended for use in an explosive atmospheres with flammable gas, vapour or mist. Note: Temperature class for specified maximum ambient and maximum process temperature, relevant for Group II only (Further combinations may be provided in the instruction manual). "
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
                            deviceCategory: Optional[Union[str, DeviceCategory]] = None,
                            equipmentProtectionLevel: Optional[
                                Union[LangStringSet, EquipmentProtectionLevel]
                            ] = None,
                            regionalSpecificMarking: Optional[
                                Union[str, RegionalSpecificMarking]
                            ] = None,
                            typeOfProtection: Optional[
                                Union[str, TypeOfProtection]
                            ] = None,
                            explosionGroup: Optional[Union[str, ExplosionGroup]] = None,
                            minimumAmbientTemperature: Optional[
                                Union[Decimal, MinimumAmbientTemperature]
                            ] = None,
                            maxAmbientTemperature: Optional[
                                Union[Decimal, MaxAmbientTemperature]
                            ] = None,
                            maxSurfaceTemperatureForDustProof: Optional[
                                Union[Decimal, MaxSurfaceTemperatureForDustProof]
                            ] = None,
                            temperatureClass: Optional[
                                Union[str, TemperatureClass]
                            ] = None,
                            id_short: str = "AmbientConditions",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/AmbientConditions",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: If the device is mounted in the process boundary, ambient and process conditions are provided separately. "
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

                            # Build a submodel element if a raw value was passed in the argument
                            if deviceCategory and not isinstance(
                                deviceCategory, SubmodelElement
                            ):
                                deviceCategory = self.DeviceCategory(deviceCategory)

                            # Build a submodel element if a raw value was passed in the argument
                            if equipmentProtectionLevel and not isinstance(
                                equipmentProtectionLevel, SubmodelElement
                            ):
                                equipmentProtectionLevel = (
                                    self.EquipmentProtectionLevel(
                                        equipmentProtectionLevel
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if regionalSpecificMarking and not isinstance(
                                regionalSpecificMarking, SubmodelElement
                            ):
                                regionalSpecificMarking = self.RegionalSpecificMarking(
                                    regionalSpecificMarking
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if typeOfProtection and not isinstance(
                                typeOfProtection, SubmodelElement
                            ):
                                typeOfProtection = self.TypeOfProtection(
                                    typeOfProtection
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if explosionGroup and not isinstance(
                                explosionGroup, SubmodelElement
                            ):
                                explosionGroup = self.ExplosionGroup(explosionGroup)

                            # Build a submodel element if a raw value was passed in the argument
                            if minimumAmbientTemperature and not isinstance(
                                minimumAmbientTemperature, SubmodelElement
                            ):
                                minimumAmbientTemperature = (
                                    self.MinimumAmbientTemperature(
                                        minimumAmbientTemperature
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if maxAmbientTemperature and not isinstance(
                                maxAmbientTemperature, SubmodelElement
                            ):
                                maxAmbientTemperature = self.MaxAmbientTemperature(
                                    maxAmbientTemperature
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if maxSurfaceTemperatureForDustProof and not isinstance(
                                maxSurfaceTemperatureForDustProof, SubmodelElement
                            ):
                                maxSurfaceTemperatureForDustProof = (
                                    self.MaxSurfaceTemperatureForDustProof(
                                        maxSurfaceTemperatureForDustProof
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if temperatureClass and not isinstance(
                                temperatureClass, SubmodelElement
                            ):
                                temperatureClass = self.TemperatureClass(
                                    temperatureClass
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                deviceCategory,
                                equipmentProtectionLevel,
                                regionalSpecificMarking,
                                typeOfProtection,
                                explosionGroup,
                                minimumAmbientTemperature,
                                maxAmbientTemperature,
                                maxSurfaceTemperatureForDustProof,
                                temperatureClass,
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

                    class ProcessConditions(SubmodelElementCollectionUnordered):
                        class DeviceCategory(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "DeviceCategory",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAK297#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA467#002 equipment/device category Note: editorial defnition: Category of device in accordance with directive 2014/34/EU Note: Equipment category according to the ATEX system. "
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

                        class EquipmentProtectionLevel(MultiLanguageProperty):
                            def __init__(
                                self,
                                value: LangStringSet,
                                id_short: str = "EquipmentProtectionLevel",
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAM668#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA464#005 equipment protection level Note: editorial defnition: Level of protection assigned to equipment based on its likelihood of becoming a source of ignition Note: Equipment protection level according to the IEC or other standards, e.g. Ga (IEC), Class I/Division 1 (US), Zone (EAC) Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

                        class RegionalSpecificMarking(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "RegionalSpecificMarking",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/RegionalSpecificMarking",
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

                        class TypeOfProtection(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TypeOfProtection",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAQ325#003",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA589#002 type of protection (Ex) Note: Symbol(s) for the Type of protection. Several types of protection are separated by a semicolon “;” "
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

                        class ExplosionGroup(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "ExplosionGroup",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAT372#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA961#007 permitted gas group/explosion group Note: editorial definition: classification of dangerous gaseous substances based on their ability to be ignited Note: Equipment grouping according to IEC 60079-0 is meant by this property Note: Symbol(s) for the gas group (IIA…IIC) or dust group (IIIA…IIIC) "
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

                        class LowerLimitingValueOfProcessTemperature(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "LowerLimitingValueOfProcessTemperature",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAN309#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: Rated minimum process temperature Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class UpperLimitingValueOfProcessTemperature(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "UpperLimitingValueOfProcessTemperature",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAN307#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: Rated maximum process temperature Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class MaxSurfaceTemperatureForDustProof(Property):
                            def __init__(
                                self,
                                value: Decimal,
                                id_short: str = "MaxSurfaceTemperatureForDustProof",
                                value_type: DataTypeDef = Decimal,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAM666#005",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABB159#004 maximum surface temperature for dust-proof Note: Maximum surface temperature (dust layer ≤ 5 mm) for specified maximum ambient and maximum process temperature, relevant for Group III only Note: Positive temperatures are listed without “+” sign. If several temperatures ranges are marked, only the most general range shall be indicated in the template, which is consistent with the specified temperature class or maximum surface temperature. Other temperature ranges and temperature classes/maximum surface temperatures may be listed in the instructions."
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

                        class TemperatureClass(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TemperatureClass",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAO371#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA593#002 temperature class Note: editorial definition: classification system of electrical apparatus, based on its maximum surface temperature, intended for use in an explosive atmospheres with flammable gas, vapour or mist. Note: Temperature class for specified maximum ambient and maximum process temperature, relevant for Group II only (Further combinations may be provided in the instruction manual). "
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
                            deviceCategory: Optional[Union[str, DeviceCategory]] = None,
                            equipmentProtectionLevel: Optional[
                                Union[LangStringSet, EquipmentProtectionLevel]
                            ] = None,
                            regionalSpecificMarking: Optional[
                                Union[str, RegionalSpecificMarking]
                            ] = None,
                            typeOfProtection: Optional[
                                Union[str, TypeOfProtection]
                            ] = None,
                            explosionGroup: Optional[Union[str, ExplosionGroup]] = None,
                            lowerLimitingValueOfProcessTemperature: Optional[
                                Union[Decimal, LowerLimitingValueOfProcessTemperature]
                            ] = None,
                            upperLimitingValueOfProcessTemperature: Optional[
                                Union[Decimal, UpperLimitingValueOfProcessTemperature]
                            ] = None,
                            maxSurfaceTemperatureForDustProof: Optional[
                                Union[Decimal, MaxSurfaceTemperatureForDustProof]
                            ] = None,
                            temperatureClass: Optional[
                                Union[str, TemperatureClass]
                            ] = None,
                            id_short: str = "ProcessConditions",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ProcessConditions",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: If the device is mounted in the process boundary, ambient and process conditions are provided separately. "
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

                            # Build a submodel element if a raw value was passed in the argument
                            if deviceCategory and not isinstance(
                                deviceCategory, SubmodelElement
                            ):
                                deviceCategory = self.DeviceCategory(deviceCategory)

                            # Build a submodel element if a raw value was passed in the argument
                            if equipmentProtectionLevel and not isinstance(
                                equipmentProtectionLevel, SubmodelElement
                            ):
                                equipmentProtectionLevel = (
                                    self.EquipmentProtectionLevel(
                                        equipmentProtectionLevel
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if regionalSpecificMarking and not isinstance(
                                regionalSpecificMarking, SubmodelElement
                            ):
                                regionalSpecificMarking = self.RegionalSpecificMarking(
                                    regionalSpecificMarking
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if typeOfProtection and not isinstance(
                                typeOfProtection, SubmodelElement
                            ):
                                typeOfProtection = self.TypeOfProtection(
                                    typeOfProtection
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if explosionGroup and not isinstance(
                                explosionGroup, SubmodelElement
                            ):
                                explosionGroup = self.ExplosionGroup(explosionGroup)

                            # Build a submodel element if a raw value was passed in the argument
                            if (
                                lowerLimitingValueOfProcessTemperature
                                and not isinstance(
                                    lowerLimitingValueOfProcessTemperature,
                                    SubmodelElement,
                                )
                            ):
                                lowerLimitingValueOfProcessTemperature = (
                                    self.LowerLimitingValueOfProcessTemperature(
                                        lowerLimitingValueOfProcessTemperature
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if (
                                upperLimitingValueOfProcessTemperature
                                and not isinstance(
                                    upperLimitingValueOfProcessTemperature,
                                    SubmodelElement,
                                )
                            ):
                                upperLimitingValueOfProcessTemperature = (
                                    self.UpperLimitingValueOfProcessTemperature(
                                        upperLimitingValueOfProcessTemperature
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if maxSurfaceTemperatureForDustProof and not isinstance(
                                maxSurfaceTemperatureForDustProof, SubmodelElement
                            ):
                                maxSurfaceTemperatureForDustProof = (
                                    self.MaxSurfaceTemperatureForDustProof(
                                        maxSurfaceTemperatureForDustProof
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if temperatureClass and not isinstance(
                                temperatureClass, SubmodelElement
                            ):
                                temperatureClass = self.TemperatureClass(
                                    temperatureClass
                                )

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                deviceCategory,
                                equipmentProtectionLevel,
                                regionalSpecificMarking,
                                typeOfProtection,
                                explosionGroup,
                                lowerLimitingValueOfProcessTemperature,
                                upperLimitingValueOfProcessTemperature,
                                maxSurfaceTemperatureForDustProof,
                                temperatureClass,
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

                    class ExternalElectricalCircuit(SubmodelElementCollectionUnordered):
                        class DesignationOfElectricalTerminal(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "DesignationOfElectricalTerminal",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0112/2///61987#ABB147#004",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: For each circuit the designation of the terminals shall be specified. If several circuits are provided with the same parameters, their terminal pairs are listed and separated by a semicolon. If several circuits belong to one channel this shall be described in the instructions. "
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

                        class TypeOfProtection(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TypeOfProtection",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAQ325#003",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA589#002 type of protection (Ex)) Note:  ·       Type of protection for the device as listed in the certificate ·       Symbol(s) for the Type of protection. Several types of protection are separated by a semicolon “;” ·       If several TypeOfProtection are listed in the same certificate, for each TypeOfProtection a separate SMC “Explosion Safety” shall be provided "
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

                        class EquipmentProtectionLevel(MultiLanguageProperty):
                            def __init__(
                                self,
                                value: LangStringSet,
                                id_short: str = "EquipmentProtectionLevel",
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAM668#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA464#005 equipment protection level Note: editorial definition: Level of protection assigned to equipment based on its likelihood of becoming a source of ignition Note: EPL according to IEC standards Note: value should be chosen from an enumeration list with values “Ga, Gb, Gc, Da, Db, Dc, Ma, Mb”  Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice."
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

                        class ExplosionGroup(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "ExplosionGroup",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAT372#001",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABA961#007 permitted gas group/explosion group Note: editorial definition: classification of dangerous gaseous substances based on their ability to be ignited Note: Equipment grouping according to IEC 60079-0 is meant by this property Note: Symbol(s) for the gas group (IIA…IIC) or dust group (IIIA…IIIC) "
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

                        class Characteristics(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "Characteristics",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ExternalElectricalCircuit/Characteristics",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {"en": "Note: linear/ non-linear "}

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

                        class Fisco(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "Fisco",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ExternalElectricalCircuit/Fisco",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {"en": "Note: Enter “x” if relevant "}

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

                        class TwoWISE(Property):
                            def __init__(
                                self,
                                value: str,
                                id_short: str = "TwoWISE",
                                value_type: DataTypeDef = str,
                                value_id: Optional[Reference] = None,
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ExternalElectricalCircuit/TwoWISE",
                                            id_type=KeyType.IRI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {"en": "Note: Enter “x” if relevant "}

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

                        class SafetyRelatedPropertiesForPassiveBehaviour(
                            SubmodelElementCollectionUnordered
                        ):
                            class MaxInputPower(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxInputPower",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAQ372#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA981#001 maximum input power (Pi) Note: Limit value for input power "
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

                            class MaxInputVoltage(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxInputVoltage",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM638#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA982#001 maximum input voltage (Ui) Note: Limit value for input voltage "
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

                            class MaxInputCurrent(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxInputCurrent",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM642#004",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA983#001 maximum input current (Ii) Note: Limit value for input current "
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

                            class MaxInternalCapacitance(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxInternalCapacitance",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM640#004",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA984#001 maximum internal capacitance (Ci) Note: Maximum internal capacitance of the circuit "
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

                            class MaxInternalInductance(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxInternalInductance",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM639#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA985#001 maximum internal inductance (Li) Note: Maximum internal inductance of the circuit "
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
                                maxInputPower: Optional[
                                    Union[Decimal, MaxInputPower]
                                ] = None,
                                maxInputVoltage: Optional[
                                    Union[Decimal, MaxInputVoltage]
                                ] = None,
                                maxInputCurrent: Optional[
                                    Union[Decimal, MaxInputCurrent]
                                ] = None,
                                maxInternalCapacitance: Optional[
                                    Union[Decimal, MaxInternalCapacitance]
                                ] = None,
                                maxInternalInductance: Optional[
                                    Union[Decimal, MaxInternalInductance]
                                ] = None,
                                id_short: str = "SafetyRelatedPropertiesForPassiveBehaviour",
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAQ380#006",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABC586#001 Safety related properties for passive behaviour Note: IS-parameters for passive circuits, if relevant (e.g. 2 wire field devices, valves) "
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

                                # Build a submodel element if a raw value was passed in the argument
                                if maxInputPower and not isinstance(
                                    maxInputPower, SubmodelElement
                                ):
                                    maxInputPower = self.MaxInputPower(maxInputPower)

                                # Build a submodel element if a raw value was passed in the argument
                                if maxInputVoltage and not isinstance(
                                    maxInputVoltage, SubmodelElement
                                ):
                                    maxInputVoltage = self.MaxInputVoltage(
                                        maxInputVoltage
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxInputCurrent and not isinstance(
                                    maxInputCurrent, SubmodelElement
                                ):
                                    maxInputCurrent = self.MaxInputCurrent(
                                        maxInputCurrent
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxInternalCapacitance and not isinstance(
                                    maxInternalCapacitance, SubmodelElement
                                ):
                                    maxInternalCapacitance = (
                                        self.MaxInternalCapacitance(
                                            maxInternalCapacitance
                                        )
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxInternalInductance and not isinstance(
                                    maxInternalInductance, SubmodelElement
                                ):
                                    maxInternalInductance = self.MaxInternalInductance(
                                        maxInternalInductance
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    maxInputPower,
                                    maxInputVoltage,
                                    maxInputCurrent,
                                    maxInternalCapacitance,
                                    maxInternalInductance,
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

                        class SafetyRelatedPropertiesForActiveBehaviour(
                            SubmodelElementCollectionUnordered
                        ):
                            class MaxOutputPower(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxOutputPower",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAQ371#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA987#001 maximum output power (Po) Note: Limit value for output power "
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

                            class MaxOutputVoltage(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxOutputVoltage",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM635#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA989#001 maximum output voltage (Uo) Note: Limit value for open circuits output voltage "
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

                            class MaxOutputCurrent(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxOutputCurrent",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM641#004",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA988#001maximum output current (Io) Note: Limit value for closed circuit output current "
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

                            class MaxExternalCapacitance(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxExternalCapacitance",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM637#004",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA990#001 maximum external capacitance (Co) Note: Maximum external capacitance to be connected to the circuit "
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

                            class MaxExternalInductance(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxExternalInductance",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM636#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABA991#001 maximum external inductance (Lo) Note: Maximum external inductance to be connected to the circuit "
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

                            class MaxExternalInductanceResistanceRatio(Property):
                                def __init__(
                                    self,
                                    value: Decimal,
                                    id_short: str = "MaxExternalInductanceResistanceRatio",
                                    value_type: DataTypeDef = Decimal,
                                    value_id: Optional[Reference] = None,
                                    category: Optional[str] = None,
                                    description: Optional[LangStringSet] = None,
                                    semantic_id: Optional[Reference] = Reference(
                                        key=(
                                            Key(
                                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                                local=True,
                                                value="0173-1#02-AAM634#003",
                                                id_type=KeyType.IRDI,
                                            ),
                                        )
                                    ),
                                    qualifier: Optional[Set[Constraint]] = None,
                                    kind: ModelingKind = ModelingKind.INSTANCE,
                                ):
                                    if description is None:
                                        description = {
                                            "en": "Note: see also [IRDI] 0112/2///61987#ABB145#001 maximum external inductance/resistance ratio (Lo/Ro) Note: External Inductance to Resistance ratio "
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
                                maxOutputPower: Optional[
                                    Union[Decimal, MaxOutputPower]
                                ] = None,
                                maxOutputVoltage: Optional[
                                    Union[Decimal, MaxOutputVoltage]
                                ] = None,
                                maxOutputCurrent: Optional[
                                    Union[Decimal, MaxOutputCurrent]
                                ] = None,
                                maxExternalCapacitance: Optional[
                                    Union[Decimal, MaxExternalCapacitance]
                                ] = None,
                                maxExternalInductance: Optional[
                                    Union[Decimal, MaxExternalInductance]
                                ] = None,
                                maxExternalInductanceResistanceRatio: Optional[
                                    Union[Decimal, MaxExternalInductanceResistanceRatio]
                                ] = None,
                                id_short: str = "SafetyRelatedPropertiesForActiveBehaviour",
                                category: Optional[str] = None,
                                description: Optional[LangStringSet] = None,
                                semantic_id: Optional[Reference] = Reference(
                                    key=(
                                        Key(
                                            type_=KeyElements.CONCEPT_DESCRIPTION,
                                            local=True,
                                            value="0173-1#02-AAQ381#006",
                                            id_type=KeyType.IRDI,
                                        ),
                                    )
                                ),
                                qualifier: Optional[Set[Constraint]] = None,
                                kind: ModelingKind = ModelingKind.INSTANCE,
                            ):
                                if description is None:
                                    description = {
                                        "en": "Note: see also [IRDI] 0112/2///61987#ABC585#001 Safety related properties for active behaviour Note: IS-parameters for active circuits, if relevant (e.g. power supply, IS-barriers) "
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

                                # Build a submodel element if a raw value was passed in the argument
                                if maxOutputPower and not isinstance(
                                    maxOutputPower, SubmodelElement
                                ):
                                    maxOutputPower = self.MaxOutputPower(maxOutputPower)

                                # Build a submodel element if a raw value was passed in the argument
                                if maxOutputVoltage and not isinstance(
                                    maxOutputVoltage, SubmodelElement
                                ):
                                    maxOutputVoltage = self.MaxOutputVoltage(
                                        maxOutputVoltage
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxOutputCurrent and not isinstance(
                                    maxOutputCurrent, SubmodelElement
                                ):
                                    maxOutputCurrent = self.MaxOutputCurrent(
                                        maxOutputCurrent
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxExternalCapacitance and not isinstance(
                                    maxExternalCapacitance, SubmodelElement
                                ):
                                    maxExternalCapacitance = (
                                        self.MaxExternalCapacitance(
                                            maxExternalCapacitance
                                        )
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if maxExternalInductance and not isinstance(
                                    maxExternalInductance, SubmodelElement
                                ):
                                    maxExternalInductance = self.MaxExternalInductance(
                                        maxExternalInductance
                                    )

                                # Build a submodel element if a raw value was passed in the argument
                                if (
                                    maxExternalInductanceResistanceRatio
                                    and not isinstance(
                                        maxExternalInductanceResistanceRatio,
                                        SubmodelElement,
                                    )
                                ):
                                    maxExternalInductanceResistanceRatio = (
                                        self.MaxExternalInductanceResistanceRatio(
                                            maxExternalInductanceResistanceRatio
                                        )
                                    )

                                # Add all passed/initialized submodel elements to a single list
                                embedded_submodel_elements = []
                                for se_arg in [
                                    maxOutputPower,
                                    maxOutputVoltage,
                                    maxOutputCurrent,
                                    maxExternalCapacitance,
                                    maxExternalInductance,
                                    maxExternalInductanceResistanceRatio,
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
                            designationOfElectricalTerminal: Optional[
                                Union[str, DesignationOfElectricalTerminal]
                            ] = None,
                            typeOfProtection: Optional[
                                Union[str, TypeOfProtection]
                            ] = None,
                            equipmentProtectionLevel: Optional[
                                Union[LangStringSet, EquipmentProtectionLevel]
                            ] = None,
                            explosionGroup: Optional[Union[str, ExplosionGroup]] = None,
                            characteristics: Optional[
                                Union[str, Characteristics]
                            ] = None,
                            fisco: Optional[Union[str, Fisco]] = None,
                            twoWISE: Optional[Union[str, TwoWISE]] = None,
                            safetyRelatedPropertiesForPassiveBehaviour: Optional[
                                SafetyRelatedPropertiesForPassiveBehaviour
                            ] = None,
                            safetyRelatedPropertiesForActiveBehaviour: Optional[
                                SafetyRelatedPropertiesForActiveBehaviour
                            ] = None,
                            id_short: str = "ExternalElectricalCircuit",
                            category: Optional[str] = None,
                            description: Optional[LangStringSet] = None,
                            semantic_id: Optional[Reference] = Reference(
                                key=(
                                    Key(
                                        type_=KeyElements.CONCEPT_DESCRIPTION,
                                        local=True,
                                        value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ExternalElectricalCircuit",
                                        id_type=KeyType.IRI,
                                    ),
                                )
                            ),
                            qualifier: Optional[Set[Constraint]] = None,
                            kind: ModelingKind = ModelingKind.INSTANCE,
                        ):
                            if description is None:
                                description = {
                                    "en": "Note: If several external circuits can be connected to the device, this block shall provide a cardinality with the number of circuits Note: If for one external IS circuit several sets of safety parameters are provided (e.g. for several material groups), each set is specified in a separate block as a separate circuit. "
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

                            # Build a submodel element if a raw value was passed in the argument
                            if designationOfElectricalTerminal and not isinstance(
                                designationOfElectricalTerminal, SubmodelElement
                            ):
                                designationOfElectricalTerminal = (
                                    self.DesignationOfElectricalTerminal(
                                        designationOfElectricalTerminal
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if typeOfProtection and not isinstance(
                                typeOfProtection, SubmodelElement
                            ):
                                typeOfProtection = self.TypeOfProtection(
                                    typeOfProtection
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if equipmentProtectionLevel and not isinstance(
                                equipmentProtectionLevel, SubmodelElement
                            ):
                                equipmentProtectionLevel = (
                                    self.EquipmentProtectionLevel(
                                        equipmentProtectionLevel
                                    )
                                )

                            # Build a submodel element if a raw value was passed in the argument
                            if explosionGroup and not isinstance(
                                explosionGroup, SubmodelElement
                            ):
                                explosionGroup = self.ExplosionGroup(explosionGroup)

                            # Build a submodel element if a raw value was passed in the argument
                            if characteristics and not isinstance(
                                characteristics, SubmodelElement
                            ):
                                characteristics = self.Characteristics(characteristics)

                            # Build a submodel element if a raw value was passed in the argument
                            if fisco and not isinstance(fisco, SubmodelElement):
                                fisco = self.Fisco(fisco)

                            # Build a submodel element if a raw value was passed in the argument
                            if twoWISE and not isinstance(twoWISE, SubmodelElement):
                                twoWISE = self.TwoWISE(twoWISE)

                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [
                                designationOfElectricalTerminal,
                                typeOfProtection,
                                equipmentProtectionLevel,
                                explosionGroup,
                                characteristics,
                                fisco,
                                twoWISE,
                                safetyRelatedPropertiesForPassiveBehaviour,
                                safetyRelatedPropertiesForActiveBehaviour,
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
                        designationOfCertificateOrApproval: Optional[
                            Union[str, DesignationOfCertificateOrApproval]
                        ] = None,
                        typeOfApproval: Optional[
                            Union[LangStringSet, TypeOfApproval]
                        ] = None,
                        approvalAgencyTestingAgency: Optional[
                            Union[LangStringSet, ApprovalAgencyTestingAgency]
                        ] = None,
                        typeOfProtection: Optional[Union[str, TypeOfProtection]] = None,
                        ratedInsulationVoltage: Optional[
                            Union[Decimal, RatedInsulationVoltage]
                        ] = None,
                        instructionsControlDrawing: Optional[
                            Union[Reference, InstructionsControlDrawing]
                        ] = None,
                        specificConditionsForUse: Optional[
                            Union[str, SpecificConditionsForUse]
                        ] = None,
                        incompleteDevice: Optional[Union[str, IncompleteDevice]] = None,
                        ambientConditions: Optional[AmbientConditions] = None,
                        processConditions: Optional[ProcessConditions] = None,
                        externalElectricalCircuit: Optional[
                            Iterable[ExternalElectricalCircuit]
                        ] = None,
                        id_short: str = "ExplosionSafety",
                        category: Optional[str] = None,
                        description: Optional[LangStringSet] = None,
                        semantic_id: Optional[Reference] = Reference(
                            key=(
                                Key(
                                    type_=KeyElements.CONCEPT_DESCRIPTION,
                                    local=True,
                                    value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety",
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
                                    value="OneToMany",
                                    value_id=None,
                                    semantic_id=None,
                                )
                            }

                        # Build a submodel element if a raw value was passed in the argument
                        if designationOfCertificateOrApproval and not isinstance(
                            designationOfCertificateOrApproval, SubmodelElement
                        ):
                            designationOfCertificateOrApproval = (
                                self.DesignationOfCertificateOrApproval(
                                    designationOfCertificateOrApproval
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if typeOfApproval and not isinstance(
                            typeOfApproval, SubmodelElement
                        ):
                            typeOfApproval = self.TypeOfApproval(typeOfApproval)

                        # Build a submodel element if a raw value was passed in the argument
                        if approvalAgencyTestingAgency and not isinstance(
                            approvalAgencyTestingAgency, SubmodelElement
                        ):
                            approvalAgencyTestingAgency = (
                                self.ApprovalAgencyTestingAgency(
                                    approvalAgencyTestingAgency
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if typeOfProtection and not isinstance(
                            typeOfProtection, SubmodelElement
                        ):
                            typeOfProtection = self.TypeOfProtection(typeOfProtection)

                        # Build a submodel element if a raw value was passed in the argument
                        if ratedInsulationVoltage and not isinstance(
                            ratedInsulationVoltage, SubmodelElement
                        ):
                            ratedInsulationVoltage = self.RatedInsulationVoltage(
                                ratedInsulationVoltage
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if instructionsControlDrawing and not isinstance(
                            instructionsControlDrawing, SubmodelElement
                        ):
                            instructionsControlDrawing = (
                                self.InstructionsControlDrawing(
                                    instructionsControlDrawing
                                )
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if specificConditionsForUse and not isinstance(
                            specificConditionsForUse, SubmodelElement
                        ):
                            specificConditionsForUse = self.SpecificConditionsForUse(
                                specificConditionsForUse
                            )

                        # Build a submodel element if a raw value was passed in the argument
                        if incompleteDevice and not isinstance(
                            incompleteDevice, SubmodelElement
                        ):
                            incompleteDevice = self.IncompleteDevice(incompleteDevice)

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [
                            designationOfCertificateOrApproval,
                            typeOfApproval,
                            approvalAgencyTestingAgency,
                            typeOfProtection,
                            ratedInsulationVoltage,
                            instructionsControlDrawing,
                            specificConditionsForUse,
                            incompleteDevice,
                            ambientConditions,
                            processConditions,
                            externalElectricalCircuit,
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
                    explosionSafety: Iterable[ExplosionSafety],
                    id_short: str = "ExplosionSafeties",
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties",
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

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [explosionSafety]:
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
                markingName: Union[str, MarkingName],
                markingFile: MarkingFile,
                designationOfCertificateOrApproval: Optional[
                    Union[str, DesignationOfCertificateOrApproval]
                ] = None,
                issueDate: Optional[Union[Date, IssueDate]] = None,
                expiryDate: Optional[Union[Date, ExpiryDate]] = None,
                markingAdditionalText: Optional[
                    Iterable[Union[str, MarkingAdditionalText]]
                ] = None,
                explosionSafeties: Optional[ExplosionSafeties] = None,
                id_short: str = "Marking",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#01-AHD206#001",
                            id_type=KeyType.IRDI,
                        ),
                    )
                ),
                qualifier: Optional[Set[Constraint]] = None,
                kind: ModelingKind = ModelingKind.INSTANCE,
            ):
                if description is None:
                    description = {
                        "en": "Note: see also [IRDI] 0112/2///61987#ABH515#003 Certificate or approval Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission "
                    }

                if qualifier is None:
                    qualifier = set()

                # Build a submodel element if a raw value was passed in the argument
                if markingName and not isinstance(markingName, SubmodelElement):
                    markingName = self.MarkingName(markingName)

                # Build a submodel element if a raw value was passed in the argument
                if designationOfCertificateOrApproval and not isinstance(
                    designationOfCertificateOrApproval, SubmodelElement
                ):
                    designationOfCertificateOrApproval = (
                        self.DesignationOfCertificateOrApproval(
                            designationOfCertificateOrApproval
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument
                if issueDate and not isinstance(issueDate, SubmodelElement):
                    issueDate = self.IssueDate(issueDate)

                # Build a submodel element if a raw value was passed in the argument
                if expiryDate and not isinstance(expiryDate, SubmodelElement):
                    expiryDate = self.ExpiryDate(expiryDate)

                # Build a list of submodel elements if a raw values were passed in the argument
                if markingAdditionalText and all(
                    [isinstance(i, str) for i in markingAdditionalText]
                ):
                    markingAdditionalText = [
                        self.MarkingAdditionalText(i) for i in markingAdditionalText
                    ]

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    markingName,
                    designationOfCertificateOrApproval,
                    issueDate,
                    expiryDate,
                    markingFile,
                    markingAdditionalText,
                    explosionSafeties,
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
            marking: Marking,
            id_short: str = "Markings",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#01-AGZ673#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: CE marking is declared as mandatory according to EU Machine Directive 2006/42/EC."
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [marking]:
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

    class AssetSpecificProperties(SubmodelElementCollectionUnordered):
        class GuidelineSpecificProperties(SubmodelElementCollectionUnordered):
            class GuidelineForConformityDeclaration(Property):
                def __init__(
                    self,
                    value: str,
                    id_short: str = "GuidelineForConformityDeclaration",
                    value_type: DataTypeDef = str,
                    value_id: Optional[Reference] = None,
                    category: Optional[str] = None,
                    description: Optional[LangStringSet] = None,
                    semantic_id: Optional[Reference] = Reference(
                        key=(
                            Key(
                                type_=KeyElements.CONCEPT_DESCRIPTION,
                                local=True,
                                value="0173-1#02-AAO856#002",
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

            def __init__(
                self,
                guidelineForConformityDeclaration: Union[
                    str, GuidelineForConformityDeclaration
                ],
                id_short: str = "GuidelineSpecificProperties",
                category: Optional[str] = None,
                description: Optional[LangStringSet] = None,
                semantic_id: Optional[Reference] = Reference(
                    key=(
                        Key(
                            type_=KeyElements.CONCEPT_DESCRIPTION,
                            local=True,
                            value="0173-1#01-AHD205#001",
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
                            value="OneToMany",
                            value_id=None,
                            semantic_id=None,
                        )
                    }

                # Build a submodel element if a raw value was passed in the argument
                if guidelineForConformityDeclaration and not isinstance(
                    guidelineForConformityDeclaration, SubmodelElement
                ):
                    guidelineForConformityDeclaration = (
                        self.GuidelineForConformityDeclaration(
                            guidelineForConformityDeclaration
                        )
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [guidelineForConformityDeclaration]:
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
            guidelineSpecificProperties: Iterable[GuidelineSpecificProperties],
            id_short: str = "AssetSpecificProperties",
            category: Optional[str] = None,
            description: Optional[LangStringSet] = None,
            semantic_id: Optional[Reference] = Reference(
                key=(
                    Key(
                        type_=KeyElements.CONCEPT_DESCRIPTION,
                        local=True,
                        value="0173-1#01-AGZ672#001",
                        id_type=KeyType.IRDI,
                    ),
                )
            ),
            qualifier: Optional[Set[Constraint]] = None,
            kind: ModelingKind = ModelingKind.INSTANCE,
        ):
            if description is None:
                description = {
                    "en": "Note: defined as “Asset specific nameplate information” per ECLASS "
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

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [guidelineSpecificProperties]:
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
        uRIOfTheProduct: Union[str, URIOfTheProduct],
        manufacturerName: Union[LangStringSet, ManufacturerName],
        manufacturerProductDesignation: Union[
            LangStringSet, ManufacturerProductDesignation
        ],
        contactInformation: ContactInformation,
        yearOfConstruction: Union[str, YearOfConstruction],
        manufacturerProductRoot: Optional[
            Union[LangStringSet, ManufacturerProductRoot]
        ] = None,
        manufacturerProductFamily: Optional[
            Union[LangStringSet, ManufacturerProductFamily]
        ] = None,
        manufacturerProductType: Optional[
            Union[LangStringSet, ManufacturerProductType]
        ] = None,
        orderCodeOfManufacturer: Optional[
            Union[LangStringSet, OrderCodeOfManufacturer]
        ] = None,
        productArticleNumberOfManufacturer: Optional[
            Union[LangStringSet, ProductArticleNumberOfManufacturer]
        ] = None,
        serialNumber: Optional[Union[str, SerialNumber]] = None,
        dateOfManufacture: Optional[Union[Date, DateOfManufacture]] = None,
        hardwareVersion: Optional[Union[LangStringSet, HardwareVersion]] = None,
        firmwareVersion: Optional[Union[LangStringSet, FirmwareVersion]] = None,
        softwareVersion: Optional[Union[LangStringSet, SoftwareVersion]] = None,
        countryOfOrigin: Optional[Union[str, CountryOfOrigin]] = None,
        companyLogo: Optional[CompanyLogo] = None,
        markings: Optional[Markings] = None,
        assetSpecificProperties: Optional[AssetSpecificProperties] = None,
        id_short: str = "Nameplate",
        category: Optional[str] = None,
        description: Optional[LangStringSet] = None,
        administration: Optional[AdministrativeInformation] = None,
        semantic_id: Optional[Reference] = Reference(
            key=(
                Key(
                    type_=KeyElements.CONCEPT_DESCRIPTION,
                    local=True,
                    value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate",
                    id_type=KeyType.IRI,
                ),
            )
        ),
        qualifier: Optional[Set[Constraint]] = None,
        kind: ModelingKind = ModelingKind.INSTANCE,
    ):
        if description is None:
            description = {
                "en": "Contains the nameplate information attached to the product"
            }

        if qualifier is None:
            qualifier = set()

        # Build a submodel element if a raw value was passed in the argument
        if uRIOfTheProduct and not isinstance(uRIOfTheProduct, SubmodelElement):
            uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

        # Build a submodel element if a raw value was passed in the argument
        if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
            manufacturerName = self.ManufacturerName(manufacturerName)

        # Build a submodel element if a raw value was passed in the argument
        if manufacturerProductDesignation and not isinstance(
            manufacturerProductDesignation, SubmodelElement
        ):
            manufacturerProductDesignation = self.ManufacturerProductDesignation(
                manufacturerProductDesignation
            )

        # Build a submodel element if a raw value was passed in the argument
        if manufacturerProductRoot and not isinstance(
            manufacturerProductRoot, SubmodelElement
        ):
            manufacturerProductRoot = self.ManufacturerProductRoot(
                manufacturerProductRoot
            )

        # Build a submodel element if a raw value was passed in the argument
        if manufacturerProductFamily and not isinstance(
            manufacturerProductFamily, SubmodelElement
        ):
            manufacturerProductFamily = self.ManufacturerProductFamily(
                manufacturerProductFamily
            )

        # Build a submodel element if a raw value was passed in the argument
        if manufacturerProductType and not isinstance(
            manufacturerProductType, SubmodelElement
        ):
            manufacturerProductType = self.ManufacturerProductType(
                manufacturerProductType
            )

        # Build a submodel element if a raw value was passed in the argument
        if orderCodeOfManufacturer and not isinstance(
            orderCodeOfManufacturer, SubmodelElement
        ):
            orderCodeOfManufacturer = self.OrderCodeOfManufacturer(
                orderCodeOfManufacturer
            )

        # Build a submodel element if a raw value was passed in the argument
        if productArticleNumberOfManufacturer and not isinstance(
            productArticleNumberOfManufacturer, SubmodelElement
        ):
            productArticleNumberOfManufacturer = (
                self.ProductArticleNumberOfManufacturer(
                    productArticleNumberOfManufacturer
                )
            )

        # Build a submodel element if a raw value was passed in the argument
        if serialNumber and not isinstance(serialNumber, SubmodelElement):
            serialNumber = self.SerialNumber(serialNumber)

        # Build a submodel element if a raw value was passed in the argument
        if yearOfConstruction and not isinstance(yearOfConstruction, SubmodelElement):
            yearOfConstruction = self.YearOfConstruction(yearOfConstruction)

        # Build a submodel element if a raw value was passed in the argument
        if dateOfManufacture and not isinstance(dateOfManufacture, SubmodelElement):
            dateOfManufacture = self.DateOfManufacture(dateOfManufacture)

        # Build a submodel element if a raw value was passed in the argument
        if hardwareVersion and not isinstance(hardwareVersion, SubmodelElement):
            hardwareVersion = self.HardwareVersion(hardwareVersion)

        # Build a submodel element if a raw value was passed in the argument
        if firmwareVersion and not isinstance(firmwareVersion, SubmodelElement):
            firmwareVersion = self.FirmwareVersion(firmwareVersion)

        # Build a submodel element if a raw value was passed in the argument
        if softwareVersion and not isinstance(softwareVersion, SubmodelElement):
            softwareVersion = self.SoftwareVersion(softwareVersion)

        # Build a submodel element if a raw value was passed in the argument
        if countryOfOrigin and not isinstance(countryOfOrigin, SubmodelElement):
            countryOfOrigin = self.CountryOfOrigin(countryOfOrigin)

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            uRIOfTheProduct,
            manufacturerName,
            manufacturerProductDesignation,
            contactInformation,
            manufacturerProductRoot,
            manufacturerProductFamily,
            manufacturerProductType,
            orderCodeOfManufacturer,
            productArticleNumberOfManufacturer,
            serialNumber,
            yearOfConstruction,
            dateOfManufacture,
            hardwareVersion,
            firmwareVersion,
            softwareVersion,
            countryOfOrigin,
            companyLogo,
            markings,
            assetSpecificProperties,
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
            identification=identification,
            id_short=id_short,
            category=category,
            description=description,
            administration=administration,
            semantic_id=semantic_id,
            qualifier=qualifier,
            kind=kind,
        )
