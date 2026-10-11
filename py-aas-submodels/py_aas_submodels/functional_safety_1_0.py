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


class FunctionalSafety(aas.Submodel):

    class NumberOfFunctionalSafetySetsOfCharacteristics(aas.Property):

        def __init__(
            self,
            value: xsd.Int,
            id_short: Optional[str] = r"NumberOfFunctionalSafetySetsOfCharacteristics",
            value_type: aas.DataTypeDefXsd = xsd.Int,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE005#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"number of functional safety sets of characteristics",
                        r"fr": "nombre d'ensembles de caractéristiques de sécurité fonctionnelle",
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

    class OperatingConditionsOfFunctionalSafetyCharacteristics(aas.SubmodelElementCollection):

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
            typeOfVoltage: Optional[Union[str, TypeOfVoltage]] = None,
            ratedVoltage: Optional[Union[float, RatedVoltage]] = None,
            minimumRatedVoltage: Optional[Union[float, MinimumRatedVoltage]] = None,
            maximumRatedVoltage: Optional[Union[float, MaximumRatedVoltage]] = None,
            ratedOperationalCurrent: Optional[Union[float, RatedOperationalCurrent]] = None,
            typeOfInterlockingDevice: Optional[Union[str, TypeOfInterlockingDevice]] = None,
            otherOperatingConditions: Optional[Union[str, OtherOperatingConditions]] = None,
            usefulLifeInNumberOfOperations: Optional[Union[float, UsefulLifeInNumberOfOperations]] = None,
            usefulLifeInTimeInterval: Optional[Union[float, UsefulLifeInTimeInterval]] = None,
            id_short: Optional[str] = r"OperatingConditionsOfFunctionalSafetyCharacteristics",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG057#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"operating conditions of functional safety characteristics",
                        r"fr": r"conditions de fonctionnement des caractéristiques de sécurité fonctionnelle",
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if typeOfVoltage is not None and not isinstance(typeOfVoltage, aas.SubmodelElement):
                typeOfVoltage = self.TypeOfVoltage(typeOfVoltage)

            # Build a submodel element if a raw value was passed in the argument

            if ratedVoltage is not None and not isinstance(ratedVoltage, aas.SubmodelElement):
                ratedVoltage = self.RatedVoltage(ratedVoltage)

            # Build a submodel element if a raw value was passed in the argument

            if minimumRatedVoltage is not None and not isinstance(minimumRatedVoltage, aas.SubmodelElement):
                minimumRatedVoltage = self.MinimumRatedVoltage(minimumRatedVoltage)

            # Build a submodel element if a raw value was passed in the argument

            if maximumRatedVoltage is not None and not isinstance(maximumRatedVoltage, aas.SubmodelElement):
                maximumRatedVoltage = self.MaximumRatedVoltage(maximumRatedVoltage)

            # Build a submodel element if a raw value was passed in the argument

            if ratedOperationalCurrent is not None and not isinstance(ratedOperationalCurrent, aas.SubmodelElement):
                ratedOperationalCurrent = self.RatedOperationalCurrent(ratedOperationalCurrent)

            # Build a submodel element if a raw value was passed in the argument

            if typeOfInterlockingDevice is not None and not isinstance(typeOfInterlockingDevice, aas.SubmodelElement):
                typeOfInterlockingDevice = self.TypeOfInterlockingDevice(typeOfInterlockingDevice)

            # Build a submodel element if a raw value was passed in the argument

            if otherOperatingConditions is not None and not isinstance(otherOperatingConditions, aas.SubmodelElement):
                otherOperatingConditions = self.OtherOperatingConditions(otherOperatingConditions)

            # Build a submodel element if a raw value was passed in the argument

            if usefulLifeInNumberOfOperations is not None and not isinstance(
                usefulLifeInNumberOfOperations, aas.SubmodelElement
            ):
                usefulLifeInNumberOfOperations = self.UsefulLifeInNumberOfOperations(usefulLifeInNumberOfOperations)

            # Build a submodel element if a raw value was passed in the argument

            if usefulLifeInTimeInterval is not None and not isinstance(usefulLifeInTimeInterval, aas.SubmodelElement):
                usefulLifeInTimeInterval = self.UsefulLifeInTimeInterval(usefulLifeInTimeInterval)

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

    class SafetyDeviceTypes(aas.SubmodelElementCollection):

        class FunctionalSafetyDeviceType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FunctionalSafetyDeviceType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH687"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH688"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH689"),
                        aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH690"),
                    ),
                    referred_semantic_id=None,
                ),
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE071#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"functional safety device type",
                            r"fr": r"type de dispositif de sécurité fonctionnelle",
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

        class SafetySubsystem(aas.SubmodelElementCollection):

            class SIL(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SIL",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH670#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH671#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH672#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE051#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"safety integrity level", r"fr": "niveau d'intégrité de sécurité"}
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

            class PFH(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"PFH",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE052#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"probability of dangerous failure within one hour",
                                r"fr": r"fréquence de défaillance dangereuse par heure",
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

            class ProofTestInterval(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ProofTestInterval",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE058#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"proof test interval", r"fr": r"intervalle entre essai périodique"}
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

            class PL(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PL",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH677#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH678#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH679#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH680#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH681#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE060#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"performance level", r"fr": r"niveau de performance"}
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

            class Category(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Category",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH682#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH683#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH684#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH685#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH686#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE063#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"category", r"fr": r"catégory"})

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
                sIL: Union[str, SIL],
                pFH: Optional[Union[float, PFH]] = None,
                proofTestInterval: Optional[Union[float, ProofTestInterval]] = None,
                pL: Optional[Union[str, PL]] = None,
                category_: Optional[Union[str, Category]] = None,
                id_short: Optional[str] = r"SafetySubsystem",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG065#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Safety subsystem", r"fr": r"Sous-système de sécurité"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if sIL is not None and not isinstance(sIL, aas.SubmodelElement):
                    sIL = self.SIL(sIL)

                # Build a submodel element if a raw value was passed in the argument

                if pFH is not None and not isinstance(pFH, aas.SubmodelElement):
                    pFH = self.PFH(pFH)

                # Build a submodel element if a raw value was passed in the argument

                if proofTestInterval is not None and not isinstance(proofTestInterval, aas.SubmodelElement):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Build a submodel element if a raw value was passed in the argument

                if pL is not None and not isinstance(pL, aas.SubmodelElement):
                    pL = self.PL(pL)

                # Build a submodel element if a raw value was passed in the argument

                if category_ is not None and not isinstance(category_, aas.SubmodelElement):
                    category_ = self.Category(category_)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(sIL, pFH, proofTestInterval, pL, category_)

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

        class ElectronicElement(aas.SubmodelElementCollection):

            class MTTFD(aas.Property):

                def __init__(
                    self,
                    value: xsd.Int,
                    id_short: Optional[str] = r"MTTFD",
                    value_type: aas.DataTypeDefXsd = xsd.Int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE057#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"mean time to dangerous failure",
                                r"fr": r"durée moyenne de fonctionnement avant défaillance dangereuse",
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

            class RDF(aas.Property):

                def __init__(
                    self,
                    value: xsd.Int,
                    id_short: Optional[str] = r"RDF",
                    value_type: aas.DataTypeDefXsd = xsd.Int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/FunctionalSafety/RDF/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"ratio of dangerous failure"})

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

            class ProofTestInterval(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ProofTestInterval",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE058#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"proof test interval", r"fr": r"intervalle entre essai périodique"}
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
                mTTFD: Optional[Union[xsd.Int, MTTFD]] = None,
                rDF: Optional[Union[xsd.Int, RDF]] = None,
                proofTestInterval: Optional[Union[float, ProofTestInterval]] = None,
                id_short: Optional[str] = r"ElectronicElement",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG066#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Electronic element", r"fr": r"Elément électronique"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if mTTFD is not None and not isinstance(mTTFD, aas.SubmodelElement):
                    mTTFD = self.MTTFD(mTTFD)

                # Build a submodel element if a raw value was passed in the argument

                if rDF is not None and not isinstance(rDF, aas.SubmodelElement):
                    rDF = self.RDF(rDF)

                # Build a submodel element if a raw value was passed in the argument

                if proofTestInterval is not None and not isinstance(proofTestInterval, aas.SubmodelElement):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(mTTFD, rDF, proofTestInterval)

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

        class ElectromechanicalElement(aas.SubmodelElementCollection):

            class B10D(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"B10D",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE056#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"number of operations until ten percent dangerous failure",
                                r"fr": "nombre de cycles jusqu'à dix pour cent de défaillances dangereuses",
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

            class ProofTestInterval(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ProofTestInterval",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE058#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"proof test interval", r"fr": r"intervalle entre essai périodique"}
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
                b10D: Optional[Union[float, B10D]] = None,
                proofTestInterval: Optional[Union[float, ProofTestInterval]] = None,
                id_short: Optional[str] = r"ElectromechanicalElement",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG067#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Electromechanical element", r"fr": r"Elément électromécanique de sous-système"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if b10D is not None and not isinstance(b10D, aas.SubmodelElement):
                    b10D = self.B10D(b10D)

                # Build a submodel element if a raw value was passed in the argument

                if proofTestInterval is not None and not isinstance(proofTestInterval, aas.SubmodelElement):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(b10D, proofTestInterval)

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

        class InherentlySafeSubsystem(aas.SubmodelElementCollection):

            class SIL(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"SIL",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH670#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH671#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH672#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE051#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"safety integrity level", r"fr": "niveau d'intégrité de sécurité"}
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

            class ProofTestInterval(aas.Property):

                def __init__(
                    self,
                    value: float,
                    id_short: Optional[str] = r"ProofTestInterval",
                    value_type: aas.DataTypeDefXsd = float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE058#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"proof test interval", r"fr": r"intervalle entre essai périodique"}
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

            class PL(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"PL",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH677#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH678#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH679#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH680#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH681#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE060#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"performance level", r"fr": r"niveau de performance"}
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

            class Category(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Category",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH682#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH683#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH684#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH685#001"),
                            aas.Key(type_=aas.KeyTypes.GLOBAL_REFERENCE, value=r"0112/2///62683#ACH686#001"),
                        ),
                        referred_semantic_id=None,
                    ),
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACE063#001"),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"category", r"fr": r"catégory"})

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
                sIL: Union[str, SIL],
                proofTestInterval: Optional[Union[float, ProofTestInterval]] = None,
                pL: Optional[Union[str, PL]] = None,
                category_: Optional[Union[str, Category]] = None,
                id_short: Optional[str] = r"InherentlySafeSubsystem",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG069#001"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Inherently safe subsystem", r"fr": r"Sous-système intrinsèquement sûr"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if sIL is not None and not isinstance(sIL, aas.SubmodelElement):
                    sIL = self.SIL(sIL)

                # Build a submodel element if a raw value was passed in the argument

                if proofTestInterval is not None and not isinstance(proofTestInterval, aas.SubmodelElement):
                    proofTestInterval = self.ProofTestInterval(proofTestInterval)

                # Build a submodel element if a raw value was passed in the argument

                if pL is not None and not isinstance(pL, aas.SubmodelElement):
                    pL = self.PL(pL)

                # Build a submodel element if a raw value was passed in the argument

                if category_ is not None and not isinstance(category_, aas.SubmodelElement):
                    category_ = self.Category(category_)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(sIL, proofTestInterval, pL, category_)

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
            functionalSafetyDeviceType: Union[str, FunctionalSafetyDeviceType],
            safetySubsystem: Optional[SafetySubsystem] = None,
            electronicElement: Optional[ElectronicElement] = None,
            electromechanicalElement: Optional[ElectromechanicalElement] = None,
            inherentlySafeSubsystem: Optional[InherentlySafeSubsystem] = None,
            id_short: Optional[str] = r"SafetyDeviceTypes",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///62683#ACG070#001"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"safety device", r"fr": r"dispositif de sécurité"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if functionalSafetyDeviceType is not None and not isinstance(
                functionalSafetyDeviceType, aas.SubmodelElement
            ):
                functionalSafetyDeviceType = self.FunctionalSafetyDeviceType(functionalSafetyDeviceType)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                functionalSafetyDeviceType,
                safetySubsystem,
                electronicElement,
                electromechanicalElement,
                inherentlySafeSubsystem,
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
        numberOfFunctionalSafetySetsOfCharacteristics: Union[xsd.Int, NumberOfFunctionalSafetySetsOfCharacteristics],
        operatingConditionsOfFunctionalSafetyCharacteristics: Optional[
            Iterable[OperatingConditionsOfFunctionalSafetyCharacteristics]
        ] = None,
        safetyDeviceTypes: Optional[Iterable[SafetyDeviceTypes]] = None,
        id_short: Optional[str] = r"FunctionalSafety",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ModelReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.SUBMODEL, value=r"https://admin-shell.io/idta/iec62683/1/0/FunctionalSafety"
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

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if numberOfFunctionalSafetySetsOfCharacteristics is not None and not isinstance(
            numberOfFunctionalSafetySetsOfCharacteristics, aas.SubmodelElement
        ):
            numberOfFunctionalSafetySetsOfCharacteristics = self.NumberOfFunctionalSafetySetsOfCharacteristics(
                numberOfFunctionalSafetySetsOfCharacteristics
            )

        # A str would be split into its characters
        if isinstance(operatingConditionsOfFunctionalSafetyCharacteristics, str):
            raise TypeError("operatingConditionsOfFunctionalSafetyCharacteristics takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(safetyDeviceTypes, str):
            raise TypeError("safetyDeviceTypes takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            numberOfFunctionalSafetySetsOfCharacteristics,
            operatingConditionsOfFunctionalSafetyCharacteristics,
            safetyDeviceTypes,
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
