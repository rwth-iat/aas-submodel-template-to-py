from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


def global_ref(value: str) -> aas.ExternalReference:
    """External reference to the global identifier `value`, e.g. a semantic ID"""
    return aas.ExternalReference((aas.Key(aas.KeyTypes.GLOBAL_REFERENCE, value),))


def collect_submodel_elements(*elements: Any, number_repeated: bool = True) -> list[aas.SubmodelElement]:
    """Collect the submodel elements passed to an init in one list: single elements, unless None,
    and the elements of iterables, whose idShorts get an index if `number_repeated` (e.g. Keyword00)"""
    collected = []
    for element in elements:
        if element is None:
            continue
        elif isinstance(element, aas.SubmodelElement):
            collected.append(element)
        elif isinstance(element, Iterable):
            for n, item in enumerate(element):
                if number_repeated:
                    # Number with two digits at least, as the placeholders {00} and __00__ of templates
                    item.id_short = f"{item.id_short}{n:02d}"
                collected.append(item)
        else:
            raise TypeError(f"Expected a submodel element or an iterable of them, got {element.__class__}")
    return collected


class GeneratedSubmodelElementList(aas.SubmodelElementList):
    """SubmodelElementList, whose items may be instances of subclasses of type_value_list_element,
    such as the generated classes of its items"""

    def _check_constraints(self, new, existing) -> None:
        # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
        # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
        saved_id_short = new.id_short
        new.id_short = None

        # We relax constraint AASd-108 here: It is allowed to add subclasses of the specified in type_value_list_element
        if not isinstance(new, self.type_value_list_element):
            raise aas.AASConstraintViolation(
                108,
                "All first level elements must be of the type specified in "
                f"type_value_list_element={self.type_value_list_element.__name__}, "
                f"got {new!r}",
            )

        if (
            self.semantic_id_list_element is not None
            and new.semantic_id is not None
            and new.semantic_id != self.semantic_id_list_element
        ):
            # Constraint AASd-115 specifies that if the semantic_id of an item is not specified
            # but semantic_id_list_element is, the semantic_id of the new is assumed to be identical.
            # Not really a constraint...
            # TODO: maybe set the semantic_id of new to semantic_id_list_element if it is None
            raise aas.AASConstraintViolation(
                107,
                f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                "is specified all first level children must have the same "
                f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}",
            )

        # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
        # is either Property or Range. Thus, `new` must have the value_type property.
        # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
        if (
            self.type_value_list_element in (aas.Property, aas.Range)
            and new.value_type is not self.value_type_list_element
        ):  # type: ignore
            raise aas.AASConstraintViolation(
                109,
                "All first level elements must have the value_type "  # type: ignore
                "specified by value_type_list_element="
                f"{self.value_type_list_element.__name__}, got "  # type: ignore
                f"{new!r} with value_type={new.value_type.__name__}",
            )  # type: ignore

        # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
        # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
        if new.semantic_id is not None and self.semantic_id_list_element is None:
            for item in existing:
                if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                    raise aas.AASConstraintViolation(
                        114,
                        f"Element to be added {new!r} has semantic_id "
                        f"{new.semantic_id!r}, while already contained element "
                        f"{item!r} has semantic_id {item.semantic_id!r}, which "
                        "aren't equal.",
                    )

        # Re-assign id_short
        new.id_short = saved_id_short


class Reliability(aas.Submodel):

    class NumberOfReliabilitySets(aas.Property):

        def __init__(
            self,
            value: xsd.Int,
            id_short: Optional[str] = r"NumberOfReliabilitySets",
            value_type: aas.DataTypeDefXsd = xsd.Int,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE006#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"number of reliability sets of characteristics",
                        r"fr": "nombre d'ensembles de caractéristiques de fiabilité",
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

    class OperatingConditionsOfReliabilityCharacteristics(aas.SubmodelElementCollection):

        class TypeOfVoltage(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TypeOfVoltage",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///61987#ABL837#001"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///61987#ABL838#001"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///61987#ABI407#004"),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABA969#007"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"type of voltage", r"fr": r"type de tension", r"de": r"Spannungsart"}
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

        class RatedVoltage(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"RatedVoltage",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABA588#004"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"rated voltage", r"fr": r"tension assignée", r"de": r"Bemessungsspannung"}
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

        class MinimumRatedVoltage(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"MinimumRatedVoltage",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABD461#004"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"minimum rated voltage",
                            r"fr": r"tension assignée minimale",
                            r"de": r"minimale Bemessungsspannung",
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

        class MaximumRatedVoltage(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"MaximumRatedVoltage",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABD462#004"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"maximum rated voltage",
                            r"fr": r"tension assignée maximale",
                            r"de": r"maximale Bemessungsspannung",
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

        class RatedOperationalCurrent(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"RatedOperationalCurrent",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/FunctionalSafety/RatedOperationalCurrent/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"rated operational current"})

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

        class TypeOfInterlockingDevice(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TypeOfInterlockingDevice",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH673#001"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH674#001"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH675#001"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH676#001"),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE053#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"type of interlocking device", r"fr": r"type de dispositif de verrouillage"}
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

        class OtherOperatingConditions(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"OtherOperatingConditions",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE070#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"other operating conditions", r"fr": r"autres conditions de fonctionnement"}
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

        class UsefulLifeInNumberOfOperations(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"UsefulLifeInNumberOfOperations",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE055#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"useful life in number of operations",
                            r"fr": r"durée de vie utile en cycle de fonctionnement",
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

        class UsefulLifeInTimeInterval(aas.Property):

            def __init__(
                self,
                value: float,
                id_short: Optional[str] = r"UsefulLifeInTimeInterval",
                value_type: aas.DataTypeDefXsd = float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE054#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"useful life in time interval",
                            r"fr": r"durée de vie utile en intervalle de temps",
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
            typeOfVoltage: Optional[Iterable[Union[str, TypeOfVoltage]]] = None,
            ratedVoltage: Optional[Iterable[Union[float, RatedVoltage]]] = None,
            minimumRatedVoltage: Optional[Iterable[Union[float, MinimumRatedVoltage]]] = None,
            maximumRatedVoltage: Optional[Iterable[Union[float, MaximumRatedVoltage]]] = None,
            ratedOperationalCurrent: Optional[Iterable[Union[float, RatedOperationalCurrent]]] = None,
            typeOfInterlockingDevice: Optional[Iterable[Union[str, TypeOfInterlockingDevice]]] = None,
            otherOperatingConditions: Optional[Iterable[Union[str, OtherOperatingConditions]]] = None,
            usefulLifeInNumberOfOperations: Optional[Iterable[Union[float, UsefulLifeInNumberOfOperations]]] = None,
            usefulLifeInTimeInterval: Optional[Iterable[Union[float, UsefulLifeInTimeInterval]]] = None,
            id_short: Optional[str] = r"OperatingConditionsOfReliabilityCharacteristics",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG071#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"operating conditions of reliability characteristics",
                        r"fr": r"conditions de fonctionnement des caractéristiques de fiabilité et de sécurité fonctionnelle",
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(typeOfVoltage, str):
                raise TypeError("typeOfVoltage takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if typeOfVoltage:
                typeOfVoltage = [
                    i if isinstance(i, aas.SubmodelElement) else self.TypeOfVoltage(i) for i in typeOfVoltage
                ]

            # A str would be split into its characters
            if isinstance(ratedVoltage, str):
                raise TypeError("ratedVoltage takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if ratedVoltage:
                ratedVoltage = [i if isinstance(i, aas.SubmodelElement) else self.RatedVoltage(i) for i in ratedVoltage]

            # A str would be split into its characters
            if isinstance(minimumRatedVoltage, str):
                raise TypeError("minimumRatedVoltage takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if minimumRatedVoltage:
                minimumRatedVoltage = [
                    i if isinstance(i, aas.SubmodelElement) else self.MinimumRatedVoltage(i)
                    for i in minimumRatedVoltage
                ]

            # A str would be split into its characters
            if isinstance(maximumRatedVoltage, str):
                raise TypeError("maximumRatedVoltage takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if maximumRatedVoltage:
                maximumRatedVoltage = [
                    i if isinstance(i, aas.SubmodelElement) else self.MaximumRatedVoltage(i)
                    for i in maximumRatedVoltage
                ]

            # A str would be split into its characters
            if isinstance(ratedOperationalCurrent, str):
                raise TypeError("ratedOperationalCurrent takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if ratedOperationalCurrent:
                ratedOperationalCurrent = [
                    i if isinstance(i, aas.SubmodelElement) else self.RatedOperationalCurrent(i)
                    for i in ratedOperationalCurrent
                ]

            # A str would be split into its characters
            if isinstance(typeOfInterlockingDevice, str):
                raise TypeError("typeOfInterlockingDevice takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if typeOfInterlockingDevice:
                typeOfInterlockingDevice = [
                    i if isinstance(i, aas.SubmodelElement) else self.TypeOfInterlockingDevice(i)
                    for i in typeOfInterlockingDevice
                ]

            # A str would be split into its characters
            if isinstance(otherOperatingConditions, str):
                raise TypeError("otherOperatingConditions takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if otherOperatingConditions:
                otherOperatingConditions = [
                    i if isinstance(i, aas.SubmodelElement) else self.OtherOperatingConditions(i)
                    for i in otherOperatingConditions
                ]

            # A str would be split into its characters
            if isinstance(usefulLifeInNumberOfOperations, str):
                raise TypeError("usefulLifeInNumberOfOperations takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if usefulLifeInNumberOfOperations:
                usefulLifeInNumberOfOperations = [
                    i if isinstance(i, aas.SubmodelElement) else self.UsefulLifeInNumberOfOperations(i)
                    for i in usefulLifeInNumberOfOperations
                ]

            # A str would be split into its characters
            if isinstance(usefulLifeInTimeInterval, str):
                raise TypeError("usefulLifeInTimeInterval takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if usefulLifeInTimeInterval:
                usefulLifeInTimeInterval = [
                    i if isinstance(i, aas.SubmodelElement) else self.UsefulLifeInTimeInterval(i)
                    for i in usefulLifeInTimeInterval
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                typeOfVoltage,
                ratedVoltage,
                minimumRatedVoltage,
                maximumRatedVoltage,
                ratedOperationalCurrent,
                typeOfInterlockingDevice,
                otherOperatingConditions,
                usefulLifeInNumberOfOperations,
                usefulLifeInTimeInterval,
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

    class ReliabilityCharacteristics(aas.SubmodelElementCollection):

        class MTTF(aas.Property):

            def __init__(
                self,
                value: xsd.Int,
                id_short: Optional[str] = r"MTTF",
                value_type: aas.DataTypeDefXsd = xsd.Int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE061#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"mean operating time to failure",
                            r"fr": r"durée moyenne de fonctionnement avant défaillance",
                            r"de": r"mittlere Betriebszeit bis zum Ausfall",
                            r"jp": r"平均故障間動作時間",
                            r"cn": r"平均失效前工作时间",
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

        class MTBF(aas.Property):

            def __init__(
                self,
                value: xsd.Int,
                id_short: Optional[str] = r"MTBF",
                value_type: aas.DataTypeDefXsd = xsd.Int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE062#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"mean operating time between failure",
                            r"fr": r"moyenne des temps de bon fonctionnement",
                            r"de": r"mittlere Betriebszeit zwischen Ausfällen",
                            r"cn": r"平均失效间隔工作时间",
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

        class B(aas.Property):

            def __init__(
                self,
                value: xsd.Int,
                id_short: Optional[str] = r"B",
                value_type: aas.DataTypeDefXsd = xsd.Int,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/Reliability/B10/1/0"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"B10"})

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
            mTTF: Optional[Iterable[Union[xsd.Int, MTTF]]] = None,
            mTBF: Optional[Iterable[Union[xsd.Int, MTBF]]] = None,
            b: Optional[Iterable[Union[xsd.Int, B]]] = None,
            id_short: Optional[str] = r"ReliabilityCharacteristics",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG080#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Reliability characteristics", r"fr": r"Caractéristiques de fiabilité"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(mTTF, str):
                raise TypeError("mTTF takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if mTTF:
                mTTF = [i if isinstance(i, aas.SubmodelElement) else self.MTTF(i) for i in mTTF]

            # A str would be split into its characters
            if isinstance(mTBF, str):
                raise TypeError("mTBF takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if mTBF:
                mTBF = [i if isinstance(i, aas.SubmodelElement) else self.MTBF(i) for i in mTBF]

            # A str would be split into its characters
            if isinstance(b, str):
                raise TypeError("b takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if b:
                b = [i if isinstance(i, aas.SubmodelElement) else self.B(i) for i in b]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(mTTF, mTBF, b)

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
        numberOfReliabilitySets: Union[xsd.Int, NumberOfReliabilitySets],
        operatingConditionsOfReliabilityCharacteristics: Optional[
            Iterable[OperatingConditionsOfReliabilityCharacteristics]
        ] = None,
        reliabilityCharacteristics: Optional[Iterable[ReliabilityCharacteristics]] = None,
        id_short: Optional[str] = r"Reliability",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(aas.Key(type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/iec62683/1/0/Reliability"),),
            type_=aas.Submodel,
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if numberOfReliabilitySets is not None and not isinstance(numberOfReliabilitySets, aas.SubmodelElement):
            numberOfReliabilitySets = self.NumberOfReliabilitySets(numberOfReliabilitySets)

        # A str would be split into its characters
        if isinstance(operatingConditionsOfReliabilityCharacteristics, str):
            raise TypeError("operatingConditionsOfReliabilityCharacteristics takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(reliabilityCharacteristics, str):
            raise TypeError("reliabilityCharacteristics takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            numberOfReliabilitySets, operatingConditionsOfReliabilityCharacteristics, reliabilityCharacteristics
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
