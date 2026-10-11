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


class SafetyInstrumentedSystem(aas.Submodel):

    class SISName(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"SISName",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/cds/SISName/1"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"SIS name"})

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"gives relevant information about the SIS"})

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

    class SRSRequirements(aas.SubmodelElementCollection):

        class SurvivabilityRequirement(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SurvivabilityRequirement",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/cds/SurvivabilityRequirement/1"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"survivability requirement"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"})

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

        class RequirementForStartingUpAndRestartingSIS(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"RequirementForStartingUpAndRestartingSIS",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/cds/RequirementForStartingUpAndRestartingSIS/1"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"requirement for starting up and restarting SIS"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"})

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

        class InterfacingSystemSpecification(aas.SubmodelElementCollection):

            class InterfacingSystem(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"InterfacingSystem",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/cds/InterfacingSystem/1"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(dict_={r"en": r"Interfacing system"})

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"gives relevant information about the SIS"}
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

            class NetworkType(aas.Property):

                ALLOWED_VALUES = (r"control network", r"safety network")

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NetworkType",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/SafetyInstrumentedSystem/TypeOfNetwork/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(dict_={r"en": r"type of network"})

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"gives relevant information about the SIS"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"control network, safety network",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

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

            class TypeOfLinksHardwiredOrSoftware(aas.Property):

                ALLOWED_VALUES = (r"hardwired", r"software")

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"TypeOfLinksHardwiredOrSoftware",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/SafetyInstrumentedSystem/TypeOfLinks/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if display_name is None:
                        display_name = aas.MultiLanguageNameType(dict_={r"en": r"type of links"})

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"gives relevant information about the SIS"}
                        )

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"enumeration",
                                value_type=str,
                                value=r"hardwired, software",
                                value_id=None,
                                kind=aas.QualifierKind.VALUE_QUALIFIER,
                                semantic_id=None,
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    if value is not None and value not in self.ALLOWED_VALUES:
                        raise ValueError(
                            f"{value!r} is not an allowed value of {type(self).__name__}, allowed: {self.ALLOWED_VALUES}"
                        )

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
                interfacingSystem: Union[str, InterfacingSystem],
                networkType: Union[str, NetworkType],
                typeOfLinksHardwiredOrSoftware: Union[str, TypeOfLinksHardwiredOrSoftware],
                id_short: Optional[str] = r"InterfacingSystemSpecification",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/cds/InterfacingSystemSpecification/1"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"interfacing system specification"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"gives relevant information about the SIS"})

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if interfacingSystem is not None and not isinstance(interfacingSystem, aas.SubmodelElement):
                    interfacingSystem = self.InterfacingSystem(interfacingSystem)

                # Build a submodel element if a raw value was passed in the argument

                if networkType is not None and not isinstance(networkType, aas.SubmodelElement):
                    networkType = self.NetworkType(networkType)

                # Build a submodel element if a raw value was passed in the argument

                if typeOfLinksHardwiredOrSoftware is not None and not isinstance(
                    typeOfLinksHardwiredOrSoftware, aas.SubmodelElement
                ):
                    typeOfLinksHardwiredOrSoftware = self.TypeOfLinksHardwiredOrSoftware(typeOfLinksHardwiredOrSoftware)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    interfacingSystem, networkType, typeOfLinksHardwiredOrSoftware
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

        class PerformanceStandard(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PerformanceStandard",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/cds/PerformanceStandard/1"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"performance standard"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"gives relevant information about the SIS"})

                if qualifier is None:
                    qualifier = ()

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

        class ApplicationProgramSafetyRequirements(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ApplicationProgramSafetyRequirements",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/cds/ApplicationProgramSafetyRequirements/1"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"application program safety requirements"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"})

                if qualifier is None:
                    qualifier = ()

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

        class DALSpec(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"DALSpec",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/cds/DALSpec/1"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"DAL spec"})

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"})

                if qualifier is None:
                    qualifier = ()

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

        class Document(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Document",
                content_type: Optional[str] = r"application/octet-stream",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/cds/Document/1"),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"URL of document"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about relevant document(s)"}
                    )

                if qualifier is None:
                    qualifier = ()

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

        def __init__(
            self,
            survivabilityRequirement: Optional[Iterable[Union[str, SurvivabilityRequirement]]] = None,
            requirementForStartingUpAndRestartingSIS: Optional[
                Iterable[Union[str, RequirementForStartingUpAndRestartingSIS]]
            ] = None,
            interfacingSystemSpecification: Optional[Iterable[InterfacingSystemSpecification]] = None,
            performanceStandard: Optional[Iterable[PerformanceStandard]] = None,
            applicationProgramSafetyRequirements: Optional[ApplicationProgramSafetyRequirements] = None,
            dALSpec: Optional[DALSpec] = None,
            document: Optional[Iterable[Document]] = None,
            id_short: Optional[str] = r"SRSRequirements",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/cds/SRSRequirements/1"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(dict_={r"en": r"SRS requirements"})

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"SRS requirement(s) according to IEC 61511"})

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(survivabilityRequirement, str):
                raise TypeError("survivabilityRequirement takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if survivabilityRequirement:
                survivabilityRequirement = [
                    i if isinstance(i, aas.SubmodelElement) else self.SurvivabilityRequirement(i)
                    for i in survivabilityRequirement
                ]

            # A str would be split into its characters
            if isinstance(requirementForStartingUpAndRestartingSIS, str):
                raise TypeError("requirementForStartingUpAndRestartingSIS takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if requirementForStartingUpAndRestartingSIS:
                requirementForStartingUpAndRestartingSIS = [
                    i if isinstance(i, aas.SubmodelElement) else self.RequirementForStartingUpAndRestartingSIS(i)
                    for i in requirementForStartingUpAndRestartingSIS
                ]

            # A str would be split into its characters
            if isinstance(interfacingSystemSpecification, str):
                raise TypeError("interfacingSystemSpecification takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(performanceStandard, str):
                raise TypeError("performanceStandard takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(document, str):
                raise TypeError("document takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                survivabilityRequirement,
                requirementForStartingUpAndRestartingSIS,
                interfacingSystemSpecification,
                performanceStandard,
                applicationProgramSafetyRequirements,
                dALSpec,
                document,
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
        sISName: Union[str, SISName],
        sRSRequirements: SRSRequirements,
        id_short: Optional[str] = r"SafetyInstrumentedSystem",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = global_ref(
            r"https://admin-shell.io/idta/SubmodelTemplate/SafetyInstrumentedSystem/1/0"
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
                    r"en": r"The submodel Safety Instrumented System is a collection of properties about the functional safety requirements and information for the lifecycle of a device of a safety instrumented system realising one or more safety instrumented functions."
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02097-1-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if sISName is not None and not isinstance(sISName, aas.SubmodelElement):
            sISName = self.SISName(sISName)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(sISName, sRSRequirements)

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
