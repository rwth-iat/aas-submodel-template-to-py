from typing import Any, ForwardRef, Iterable, Optional, Tuple, TypedDict, Union, Unpack
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


class MultiLanguagePropertyMetadata(TypedDict, total=False):
    """Metadata of aas.MultiLanguageProperty, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class PropertyMetadata(TypedDict, total=False):
    """Metadata of aas.Property, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    value_id: Optional[aas.Reference]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelElementCollectionMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementCollection, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelElementListMetadata(TypedDict, total=False):
    """Metadata of aas.SubmodelElementList, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    type_value_list_element: type[aas.SubmodelElement]
    semantic_id_list_element: Optional[aas.Reference]
    value_type_list_element: Optional[aas.DataTypeDefXsd]
    order_relevant: bool
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class SubmodelMetadata(TypedDict, total=False):
    """Metadata of aas.Submodel, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    administration: Optional[aas.AdministrativeInformation]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    kind: aas.ModellingKind
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class WorkstationWorkerMatchingData(aas.Submodel):

    class GeneralWorkstationData(aas.SubmodelElementCollection):

        class WorkstationInformation(aas.SubmodelElementCollection):

            class WorkstationName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WorkstationName",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Workstation name", r"de": r"Name der Arbeitsstation"}
                        ),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Workstation name"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/workstationname/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class WorkstationId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WorkstationId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Workstation ID", r"de": r"Arbeitsstation ID"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/workstationid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OrgName(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"OrgName",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Organizational name", r"de": r"Organisationsname"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/orgname/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class TypeOfWorkstation(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"TypeOfWorkstation",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Workstation type", r"de": r"Arbeitsstationsart"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/typeofworkstation/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class WorkerAssistanceInformation(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"WorkerAssistanceInformation",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Worker assistance information", r"de": r"Informationen zur Werkerassistenz"}
                        ),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Worker assistance information"}),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/workerassistanceeinformation/1/0"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class RequiredPersonalSafetyEquipment(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"RequiredPersonalSafetyEquipment",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={
                                r"en": r"Required personal safety equipment",
                                r"de": r"Erforderliche persönliche Schutzausrüstung",
                            }
                        ),
                        "description": aas.MultiLanguageTextType(dict_={r"en": r"Required personal safety equipment"}),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/requiredpersonalsafetyequipment/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class NecessaryPersonalTools(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"NecessaryPersonalTools",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Necessary personal tools", r"de": r"Notwendige persönliche Werkzeuge"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/necessarypersonaltools/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PersonalDataProcessing(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"PersonalDataProcessing",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Personal data processing ", r"de": r"Verarbeitung persönlicher Daten"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/personaldataprocessing/1/0"),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class LocationDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"LocationDescription",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Location description", r"de": r"Ortsbeschreibung"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/locationdescription/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Directions(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"Directions",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Directions", r"de": r"Wegbeschreibung"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/directions/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"WorkstationInformation",
                    "display_name": aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"General workstation information",
                            r"de": r"Allgemeine Arbeitsstationsinformationen",
                        }
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"General information about the workstation in respect of worker deployment",
                            r"de": r"Allgemeine Informationen zur Arbeitsstation mit Relevanz für die Mitarbeitereinsatzplanung",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/workstationinformation/1/0"),
                }

            def __init__(
                self,
                workstationId: Union[str, WorkstationId],
                workstationName: Optional[Union[str, WorkstationName]] = None,
                orgName: Optional[Union[aas.LangStringSet, OrgName]] = None,
                typeOfWorkstation: Optional[Union[aas.LangStringSet, TypeOfWorkstation]] = None,
                workerAssistanceInformation: Optional[Union[aas.LangStringSet, WorkerAssistanceInformation]] = None,
                requiredPersonalSafetyEquipment: Optional[
                    Union[aas.LangStringSet, RequiredPersonalSafetyEquipment]
                ] = None,
                necessaryPersonalTools: Optional[Union[aas.LangStringSet, NecessaryPersonalTools]] = None,
                personalDataProcessing: Optional[Union[aas.LangStringSet, PersonalDataProcessing]] = None,
                locationDescription: Optional[Union[aas.LangStringSet, LocationDescription]] = None,
                directions: Optional[Union[aas.LangStringSet, Directions]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if workstationName is not None and not isinstance(workstationName, aas.SubmodelElement):
                    workstationName = self.WorkstationName(workstationName)

                # Build a submodel element if a raw value was passed in the argument

                if workstationId is not None and not isinstance(workstationId, aas.SubmodelElement):
                    workstationId = self.WorkstationId(workstationId)

                # Build a submodel element if a raw value was passed in the argument

                if orgName is not None and not isinstance(orgName, aas.SubmodelElement):
                    orgName = self.OrgName(orgName)

                # Build a submodel element if a raw value was passed in the argument

                if typeOfWorkstation is not None and not isinstance(typeOfWorkstation, aas.SubmodelElement):
                    typeOfWorkstation = self.TypeOfWorkstation(typeOfWorkstation)

                # Build a submodel element if a raw value was passed in the argument

                if workerAssistanceInformation is not None and not isinstance(
                    workerAssistanceInformation, aas.SubmodelElement
                ):
                    workerAssistanceInformation = self.WorkerAssistanceInformation(workerAssistanceInformation)

                # Build a submodel element if a raw value was passed in the argument

                if requiredPersonalSafetyEquipment is not None and not isinstance(
                    requiredPersonalSafetyEquipment, aas.SubmodelElement
                ):
                    requiredPersonalSafetyEquipment = self.RequiredPersonalSafetyEquipment(
                        requiredPersonalSafetyEquipment
                    )

                # Build a submodel element if a raw value was passed in the argument

                if necessaryPersonalTools is not None and not isinstance(necessaryPersonalTools, aas.SubmodelElement):
                    necessaryPersonalTools = self.NecessaryPersonalTools(necessaryPersonalTools)

                # Build a submodel element if a raw value was passed in the argument

                if personalDataProcessing is not None and not isinstance(personalDataProcessing, aas.SubmodelElement):
                    personalDataProcessing = self.PersonalDataProcessing(personalDataProcessing)

                # Build a submodel element if a raw value was passed in the argument

                if locationDescription is not None and not isinstance(locationDescription, aas.SubmodelElement):
                    locationDescription = self.LocationDescription(locationDescription)

                # Build a submodel element if a raw value was passed in the argument

                if directions is not None and not isinstance(directions, aas.SubmodelElement):
                    directions = self.Directions(directions)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    workstationName,
                    workstationId,
                    orgName,
                    typeOfWorkstation,
                    workerAssistanceInformation,
                    requiredPersonalSafetyEquipment,
                    necessaryPersonalTools,
                    personalDataProcessing,
                    locationDescription,
                    directions,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class GeneralQualificationDemand(GeneratedSubmodelElementList):

            class Generalqualificationdemand_item(aas.SubmodelElementCollection):

                class QualificationClassificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QualificationClassificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Qualification classification (ID)",
                                    r"de": r"Qualifikationsklassifizierung (ID)",
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/qualificationclassificationid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QualificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QualificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Qualification (ID)", r"de": r"Qualifikation (ID)"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/qualificationid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ExceptionRules(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ExceptionRules",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Exception rules", r"de": r"Ausnahmeregelungen"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/mlp/exceptionrules/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Worker qualification that is required to work at the workstation"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Worker qualification that is required to work at the workstation"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/smc/generalqualificationdemandrecord/1/0"
                        ),
                    }

                def __init__(
                    self,
                    qualificationClassificationId: Union[str, QualificationClassificationId],
                    qualificationId: Union[str, QualificationId],
                    exceptionRules: Optional[Union[aas.LangStringSet, ExceptionRules]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if qualificationClassificationId is not None and not isinstance(
                        qualificationClassificationId, aas.SubmodelElement
                    ):
                        qualificationClassificationId = self.QualificationClassificationId(
                            qualificationClassificationId
                        )

                    # Build a submodel element if a raw value was passed in the argument

                    if qualificationId is not None and not isinstance(qualificationId, aas.SubmodelElement):
                        qualificationId = self.QualificationId(qualificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if exceptionRules is not None and not isinstance(exceptionRules, aas.SubmodelElement):
                        exceptionRules = self.ExceptionRules(exceptionRules)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        qualificationClassificationId, qualificationId, exceptionRules
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"GeneralQualificationDemand",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"General qualification demand", r"de": r"Allgemeine Qualifikationsanforderungen"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker qualifications that are required in order to work at the workstation",
                            r"de": r"Mitarbeiterqualifikationen die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/generalqualificationdemand/1/0"),
                }

            def __init__(
                self,
                generalqualificationdemand_items: Optional[Iterable[Generalqualificationdemand_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(generalqualificationdemand_items, str):
                    raise TypeError("generalqualificationdemand_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    generalqualificationdemand_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class GeneralSkillDemand(GeneratedSubmodelElementList):

            class Generalskilldemand_item(aas.SubmodelElementCollection):

                class SkillClassificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SkillClassificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Skill classification (ID)", r"de": r"Fähigkeitenklassifizierung (ID)"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/skillclassificationid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SkillLevelClassificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SkillLevelClassificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Skill level classification (ID)",
                                    r"de": r"Fähigkeitenklassifizierung (ID)",
                                }
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/skilllevelclassificationid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SkillLevelId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SkillLevelId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Skill level (ID)", r"de": r"Fähigkeitenstufe (ID)"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/skilllevelid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class SkillId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"SkillId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Skill (ID)", r"de": r"Fähigkeit (ID)"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/skillid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ExceptionRules(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ExceptionRules",
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Exception rules", r"de": r"Ausnahmeregelungen"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/exceptionrules/1/0"),
                        }

                    def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Worker skill that is required in order to work at the workstation"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/generalskilldemandrecord/1/0"),
                    }

                def __init__(
                    self,
                    skillClassificationId: Union[str, SkillClassificationId],
                    skillId: Union[str, SkillId],
                    skillLevelClassificationId: Optional[Union[str, SkillLevelClassificationId]] = None,
                    skillLevelId: Optional[Union[str, SkillLevelId]] = None,
                    exceptionRules: Optional[Union[aas.LangStringSet, ExceptionRules]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if skillClassificationId is not None and not isinstance(skillClassificationId, aas.SubmodelElement):
                        skillClassificationId = self.SkillClassificationId(skillClassificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if skillLevelClassificationId is not None and not isinstance(
                        skillLevelClassificationId, aas.SubmodelElement
                    ):
                        skillLevelClassificationId = self.SkillLevelClassificationId(skillLevelClassificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if skillLevelId is not None and not isinstance(skillLevelId, aas.SubmodelElement):
                        skillLevelId = self.SkillLevelId(skillLevelId)

                    # Build a submodel element if a raw value was passed in the argument

                    if skillId is not None and not isinstance(skillId, aas.SubmodelElement):
                        skillId = self.SkillId(skillId)

                    # Build a submodel element if a raw value was passed in the argument

                    if exceptionRules is not None and not isinstance(exceptionRules, aas.SubmodelElement):
                        exceptionRules = self.ExceptionRules(exceptionRules)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        skillClassificationId, skillLevelClassificationId, skillLevelId, skillId, exceptionRules
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"GeneralSkillDemand",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"General skill demand", r"de": r"Allgemeine Fähigkeitsanforderungen"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Worker skills that are required in order to work at the workstation",
                            r"de": r"Mitarbeiterfähigkeiten die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/generalskilldemand/1/0"),
                }

            def __init__(
                self,
                generalskilldemand_items: Optional[Iterable[Generalskilldemand_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(generalskilldemand_items, str):
                    raise TypeError("generalskilldemand_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(generalskilldemand_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"GeneralWorkstationData",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"General workstation data, which are relevant for worker deployment control and deployment planning",
                        r"de": r"Allgemeine Arbeitsstationsdaten, die für die Mitarbeitereinsatzsteuerung und -planung relevant sind",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/generalworkstationdata/1/0"),
            }

        def __init__(
            self,
            workstationInformation: WorkstationInformation,
            generalQualificationDemand: Optional[
                Union[Iterable[GeneralQualificationDemand.Generalqualificationdemand_item], GeneralQualificationDemand]
            ] = None,
            generalSkillDemand: Optional[
                Union[Iterable[GeneralSkillDemand.Generalskilldemand_item], GeneralSkillDemand]
            ] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(generalQualificationDemand, str):
                raise TypeError("generalQualificationDemand takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if generalQualificationDemand is not None and not isinstance(
                generalQualificationDemand, aas.SubmodelElement
            ):
                generalQualificationDemand = self.GeneralQualificationDemand(generalQualificationDemand)

            # A str would be split into its characters
            if isinstance(generalSkillDemand, str):
                raise TypeError("generalSkillDemand takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if generalSkillDemand is not None and not isinstance(generalSkillDemand, aas.SubmodelElement):
                generalSkillDemand = self.GeneralSkillDemand(generalSkillDemand)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                workstationInformation, generalQualificationDemand, generalSkillDemand
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ErgonomicWorkstationProfile(aas.SubmodelElementCollection):

        class MaxLiftingWeight(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MaxLiftingWeight",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Max. lifting weight", r"de": r"Max. Hebegewicht"}
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/maxliftingweight/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MinWorkerHeight(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"MinWorkerHeight",
                    "value_type": int,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Minimum worker height ", r"de": r"Minimale Mitarbeitergröße "}
                    ),
                    "semantic_id": aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"https://admin-shell.io/idta/prop/minworkerheight/1/0",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class AllowedPersonalLimitations(GeneratedSubmodelElementList):

            class Allowedpersonallimitations_item(aas.SubmodelElementCollection):

                class LimitationClassificationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LimitationClassificationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={
                                    r"en": r"Limitation classification (ID)",
                                    r"de": r"Einschränkungsklassifizierung (ID)",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/prop/limitationclassificationid/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PersonalLimitationId(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PersonalLimitationId",
                            "value_type": str,
                            "display_name": aas.MultiLanguageNameType(
                                dict_={r"en": r"Personal limitation (ID)", r"de": r"Persönliche Einschränkung (ID)"}
                            ),
                            "semantic_id": aas.ModelReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                        value=r"https://admin-shell.io/idta/prop/personallimitationid/1/0",
                                    ),
                                ),
                                type_=aas.ConceptDescription,
                                referred_semantic_id=None,
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Personal limitation that is accepted for working at the workstation, e.g., special measures have been implemented"
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/smc/allowedpersonallimitationsrecord/1/0"
                        ),
                    }

                def __init__(
                    self,
                    limitationClassificationId: Union[str, LimitationClassificationId],
                    personalLimitationId: Union[str, PersonalLimitationId],
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if limitationClassificationId is not None and not isinstance(
                        limitationClassificationId, aas.SubmodelElement
                    ):
                        limitationClassificationId = self.LimitationClassificationId(limitationClassificationId)

                    # Build a submodel element if a raw value was passed in the argument

                    if personalLimitationId is not None and not isinstance(personalLimitationId, aas.SubmodelElement):
                        personalLimitationId = self.PersonalLimitationId(personalLimitationId)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        limitationClassificationId, personalLimitationId
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"AllowedPersonalLimitations",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "display_name": aas.MultiLanguageNameType(
                        dict_={r"en": r"Allowed personal limitations", r"de": r"Akzeptierte Mitarbeitereinschränkungen"}
                    ),
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of all personal limitations that are accepted for working at the workstation, e.g., special measures have been implemented",
                            r"de": r"Liste von persönlichen Einschränkungen, die an der Arbeitsstation zugelassen sind. Zum Beispiel weil bestimmte Arbeitsgestaltungsmaßnahmen getroffen wurden.",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/allowedpersonallimitations/1/0"),
                }

            def __init__(
                self,
                allowedpersonallimitations_items: Iterable[Allowedpersonallimitations_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(allowedpersonallimitations_items, str):
                    raise TypeError("allowedpersonallimitations_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    allowedpersonallimitations_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ErgonomicWorkstationProfile",
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Ergonomic workstation profile", r"de": r"Ergonomisches Arbeitsplatzprofil"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Ergonomic characteristics of the workstation which might influence the worker deployment",
                        r"de": r"Ergonomische Arbeitsplatzeigenschaften, die einen Einfluss auf den Mitarbeitereinsatz haben",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/ergonomicworkstationprofile/1/0"),
            }

        def __init__(
            self,
            maxLiftingWeight: Optional[Union[int, MaxLiftingWeight]] = None,
            minWorkerHeight: Optional[Union[int, MinWorkerHeight]] = None,
            allowedPersonalLimitations: Optional[
                Union[Iterable[AllowedPersonalLimitations.Allowedpersonallimitations_item], AllowedPersonalLimitations]
            ] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if maxLiftingWeight is not None and not isinstance(maxLiftingWeight, aas.SubmodelElement):
                maxLiftingWeight = self.MaxLiftingWeight(maxLiftingWeight)

            # Build a submodel element if a raw value was passed in the argument

            if minWorkerHeight is not None and not isinstance(minWorkerHeight, aas.SubmodelElement):
                minWorkerHeight = self.MinWorkerHeight(minWorkerHeight)

            # A str would be split into its characters
            if isinstance(allowedPersonalLimitations, str):
                raise TypeError("allowedPersonalLimitations takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if allowedPersonalLimitations is not None and not isinstance(
                allowedPersonalLimitations, aas.SubmodelElement
            ):
                allowedPersonalLimitations = self.AllowedPersonalLimitations(allowedPersonalLimitations)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                maxLiftingWeight, minWorkerHeight, allowedPersonalLimitations
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class WorkstationConfigurationRecords(GeneratedSubmodelElementList):

        class Workstationconfigurationrecords_item(aas.SubmodelElementCollection):

            class WorkerId(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WorkerId",
                        "value_type": str,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Worker (ID)", r"de": r"Werker (ID)"}),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/workerid/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AccessStart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AccessStart",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Access start ", r"de": r"Zugriffsstart"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/accessstart/1/0"),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class AccessEnd(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AccessEnd",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(dict_={r"en": r"Access end", r"de": r"Zugriffsende"}),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/accessend/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PreferredHeight(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PreferredHeight",
                        "value_type": int,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Preferred height", r"de": r"Bevorzugte Höhe"}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/preferredheight/1/0"),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProprietaryConfigurations(GeneratedSubmodelElementList):

                class Proprietaryconfigurations_item(aas.SubmodelElementCollection):

                    class ConfigurationName(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ConfigurationName",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Configuation name", r"de": r"Konfigurationsname"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/configurationname/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ConfigurationValue(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ConfigurationValue",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Configuration value", r"de": r"Konfigurationswert"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/configurationvalue/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Proprietary worker-depending configuration"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/smc/proprietaryconfigurationsrecord/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        configurationName: Union[str, ConfigurationName],
                        configurationValue: Union[str, ConfigurationValue],
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if configurationName is not None and not isinstance(configurationName, aas.SubmodelElement):
                            configurationName = self.ConfigurationName(configurationName)

                        # Build a submodel element if a raw value was passed in the argument

                        if configurationValue is not None and not isinstance(configurationValue, aas.SubmodelElement):
                            configurationValue = self.ConfigurationValue(configurationValue)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(configurationName, configurationValue)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"ProprietaryConfigurations",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Proprietary configurations", r"de": r"Proprietäre Konfigurationen"}
                        ),
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Proprietary worker-depending configurations ",
                                r"de": r"Proprietäre werkerindividuelle Konfigurationsmerkmale",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/proprietaryconfigurations/1/0"),
                    }

                def __init__(
                    self,
                    proprietaryconfigurations_items: Iterable[Proprietaryconfigurations_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(proprietaryconfigurations_items, str):
                        raise TypeError("proprietaryconfigurations_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        proprietaryconfigurations_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Worker specific configuration options of a workstation"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/workstationconfigurationrecord/1/0"),
                }

            def __init__(
                self,
                workerId: Union[str, WorkerId],
                accessStart: Optional[Union[xsd.DateTime, AccessStart]] = None,
                accessEnd: Optional[Union[xsd.DateTime, AccessEnd]] = None,
                preferredHeight: Optional[Union[int, PreferredHeight]] = None,
                proprietaryConfigurations: Optional[
                    Union[Iterable[ProprietaryConfigurations.Proprietaryconfigurations_item], ProprietaryConfigurations]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if workerId is not None and not isinstance(workerId, aas.SubmodelElement):
                    workerId = self.WorkerId(workerId)

                # Build a submodel element if a raw value was passed in the argument

                if accessStart is not None and not isinstance(accessStart, aas.SubmodelElement):
                    accessStart = self.AccessStart(accessStart)

                # Build a submodel element if a raw value was passed in the argument

                if accessEnd is not None and not isinstance(accessEnd, aas.SubmodelElement):
                    accessEnd = self.AccessEnd(accessEnd)

                # Build a submodel element if a raw value was passed in the argument

                if preferredHeight is not None and not isinstance(preferredHeight, aas.SubmodelElement):
                    preferredHeight = self.PreferredHeight(preferredHeight)

                # A str would be split into its characters
                if isinstance(proprietaryConfigurations, str):
                    raise TypeError("proprietaryConfigurations takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if proprietaryConfigurations is not None and not isinstance(
                    proprietaryConfigurations, aas.SubmodelElement
                ):
                    proprietaryConfigurations = self.ProprietaryConfigurations(proprietaryConfigurations)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    workerId, accessStart, accessEnd, preferredHeight, proprietaryConfigurations
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"WorkstationConfigurationRecords",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(
                    dict_={
                        r"en": r"Workstation configuration records ",
                        r"de": r"Arbeitsstationskonfigurationseinträge",
                    }
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Worker specific configuration options of a workstation",
                        r"de": r"Arbeitsstationskonfigurationsoptionen für einen Mitarbeiter",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/workstationconfigurationrecords/1/0"),
            }

        def __init__(
            self,
            workstationconfigurationrecords_items: Iterable[Workstationconfigurationrecords_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(workstationconfigurationrecords_items, str):
                raise TypeError("workstationconfigurationrecords_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                workstationconfigurationrecords_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class PlannedQualificationDemand(GeneratedSubmodelElementList):

        class Plannedqualificationdemand_item(aas.SubmodelElementCollection):

            class IntervalDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"IntervalDescription",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval description", r"de": r"Intervallbeschreibung"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/intervaldescription/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IntervalStart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IntervalStart",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval start", r"de": r"Intervallstart"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/intervalstart/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IntervalEnd(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IntervalEnd",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval end", r"de": r"Intervallende"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/intervalend/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class QualificationDemandRecords(GeneratedSubmodelElementList):

                class Qualificationdemandrecords_item(aas.SubmodelElementCollection):

                    class QualificationClassificationId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"QualificationClassificationId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Qualification classification (ID)",
                                        r"de": r"Qualifikationsklassifizierung (ID)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/prop/qualificationclassificationid/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class QualificationId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"QualificationId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Qualification (ID)", r"de": r"Qualifikation (ID)"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/qualificationid/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ExceptionRules(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ExceptionRules",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Exception rules", r"de": r"Ausnahmeregelungen"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/exceptionrules/1/0"),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DemandKind(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DemandKind",
                                "value_type": str,
                                "value_id": aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/adhocdemand",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/generaldemand",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/orderdependingdemand",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Demand kind", r"de": r"Bedarfsquelle"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/demandkind/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StartTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StartTime",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Start time", r"de": r"Startzeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/starttime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class EndTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"EndTime",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"End time", r"de": r"Endzeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/endtime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ProcessTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ProcessTime",
                                "value_type": int,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Process time", r"de": r"Prozesszeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/processtime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Worker qualification that is required to work at the workstation"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/qualificationdemandrecord/1/0"),
                        }

                    def __init__(
                        self,
                        qualificationClassificationId: Union[str, QualificationClassificationId],
                        qualificationId: Union[str, QualificationId],
                        startTime: Union[xsd.DateTime, StartTime],
                        endTime: Union[xsd.DateTime, EndTime],
                        processTime: Union[int, ProcessTime],
                        exceptionRules: Optional[Union[aas.LangStringSet, ExceptionRules]] = None,
                        demandKind: Optional[Union[str, DemandKind]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if qualificationClassificationId is not None and not isinstance(
                            qualificationClassificationId, aas.SubmodelElement
                        ):
                            qualificationClassificationId = self.QualificationClassificationId(
                                qualificationClassificationId
                            )

                        # Build a submodel element if a raw value was passed in the argument

                        if qualificationId is not None and not isinstance(qualificationId, aas.SubmodelElement):
                            qualificationId = self.QualificationId(qualificationId)

                        # Build a submodel element if a raw value was passed in the argument

                        if exceptionRules is not None and not isinstance(exceptionRules, aas.SubmodelElement):
                            exceptionRules = self.ExceptionRules(exceptionRules)

                        # Build a submodel element if a raw value was passed in the argument

                        if demandKind is not None and not isinstance(demandKind, aas.SubmodelElement):
                            demandKind = self.DemandKind(demandKind)

                        # Build a submodel element if a raw value was passed in the argument

                        if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                            startTime = self.StartTime(startTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                            endTime = self.EndTime(endTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if processTime is not None and not isinstance(processTime, aas.SubmodelElement):
                            processTime = self.ProcessTime(processTime)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            qualificationClassificationId,
                            qualificationId,
                            exceptionRules,
                            demandKind,
                            startTime,
                            endTime,
                            processTime,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"QualificationDemandRecords",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Worker qualifications that are required in order to work at the workstation",
                                r"de": r"Mitarbeiterqualifikationen die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/qualificationdemandrecords/1/0"),
                    }

                def __init__(
                    self,
                    qualificationdemandrecords_items: Iterable[Qualificationdemandrecords_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(qualificationdemandrecords_items, str):
                        raise TypeError("qualificationdemandrecords_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        qualificationdemandrecords_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Production plan depending planned qualification demand at a workstation"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/plannedqualificationdemandrecord/1/0"),
                }

            def __init__(
                self,
                intervalDescription: Optional[Union[aas.LangStringSet, IntervalDescription]] = None,
                intervalStart: Optional[Union[xsd.DateTime, IntervalStart]] = None,
                intervalEnd: Optional[Union[xsd.DateTime, IntervalEnd]] = None,
                qualificationDemandRecords: Optional[
                    Union[
                        Iterable[QualificationDemandRecords.Qualificationdemandrecords_item], QualificationDemandRecords
                    ]
                ] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if intervalDescription is not None and not isinstance(intervalDescription, aas.SubmodelElement):
                    intervalDescription = self.IntervalDescription(intervalDescription)

                # Build a submodel element if a raw value was passed in the argument

                if intervalStart is not None and not isinstance(intervalStart, aas.SubmodelElement):
                    intervalStart = self.IntervalStart(intervalStart)

                # Build a submodel element if a raw value was passed in the argument

                if intervalEnd is not None and not isinstance(intervalEnd, aas.SubmodelElement):
                    intervalEnd = self.IntervalEnd(intervalEnd)

                # A str would be split into its characters
                if isinstance(qualificationDemandRecords, str):
                    raise TypeError("qualificationDemandRecords takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if qualificationDemandRecords is not None and not isinstance(
                    qualificationDemandRecords, aas.SubmodelElement
                ):
                    qualificationDemandRecords = self.QualificationDemandRecords(qualificationDemandRecords)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    intervalDescription, intervalStart, intervalEnd, qualificationDemandRecords
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"PlannedQualificationDemand",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Planned qualification demand", r"de": r"Geplanter Qualifikationsbedarf"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Production plan depending planned qualification demand at a workstation",
                        r"de": r"Vom Produktionsplan abhängiger und geplanter Qualifikationsbedarf an einer Arbeitsstation",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/plannedqualificationdemand/1/0"),
            }

        def __init__(
            self,
            plannedqualificationdemand_items: Optional[Iterable[Plannedqualificationdemand_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(plannedqualificationdemand_items, str):
                raise TypeError("plannedqualificationdemand_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                plannedqualificationdemand_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class PlannedSkillDemand(GeneratedSubmodelElementList):

        class Plannedskilldemand_item(aas.SubmodelElementCollection):

            class IntervalDescription(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": r"IntervalDescription",
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval description", r"de": r"Intervallbeschreibung"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/mlp/intervaldescription/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IntervalStart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IntervalStart",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval start", r"de": r"Intervallstart"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/intervalstart/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IntervalEnd(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IntervalEnd",
                        "value_type": xsd.DateTime,
                        "display_name": aas.MultiLanguageNameType(
                            dict_={r"en": r"Interval end", r"de": r"Intervallende"}
                        ),
                        "semantic_id": aas.ModelReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                    value=r"https://admin-shell.io/idta/prop/intervalend/1/0",
                                ),
                            ),
                            type_=aas.ConceptDescription,
                            referred_semantic_id=None,
                        ),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SkillDemandRecords(GeneratedSubmodelElementList):

                class Skilldemandrecords_item(aas.SubmodelElementCollection):

                    class SkillClassificationId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SkillClassificationId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Skill classification (ID)",
                                        r"de": r"Fähigkeitenklassifizierung (ID)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/prop/skillclassificationid/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SkillLevelClassificationId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SkillLevelClassificationId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={
                                        r"en": r"Skill level classification (ID)",
                                        r"de": r"Fähigkeitenklassifizierung (ID)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/prop/skilllevelclassificationid/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SkillLevelId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SkillLevelId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Skill level (ID)", r"de": r"Fähigkeitenstufe (ID)"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/skilllevelid/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SkillId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SkillId",
                                "value_type": str,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Skill (ID)", r"de": r"Fähigkeit (ID)"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/skillid/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ExceptionRules(aas.MultiLanguageProperty):

                        @staticmethod
                        def template_defaults() -> MultiLanguagePropertyMetadata:
                            return {
                                "id_short": r"ExceptionRules",
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Exception rules", r"de": r"Ausnahmeregelungen"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/mlp/exceptionrules/1/0"),
                            }

                        def __init__(self, value: aas.LangStringSet, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class DemandKind(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"DemandKind",
                                "value_type": str,
                                "value_id": aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/adhocdemand",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/generaldemand",
                                        ),
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/idta/enum/orderdependingdemand",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Demand kind", r"de": r"Bedarfsquelle"}
                                ),
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/prop/demandkind/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class StartTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"StartTime",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Start time", r"de": r"Startzeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/starttime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class EndTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"EndTime",
                                "value_type": xsd.DateTime,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"End time", r"de": r"Endzeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/endtime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ProcessTime(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ProcessTime",
                                "value_type": int,
                                "display_name": aas.MultiLanguageNameType(
                                    dict_={r"en": r"Process time", r"de": r"Prozesszeit"}
                                ),
                                "semantic_id": aas.ModelReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                            value=r"https://admin-shell.io/idta/prop/processtime/1/0",
                                        ),
                                    ),
                                    type_=aas.ConceptDescription,
                                    referred_semantic_id=None,
                                ),
                            }

                        def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Worker skill that is required in order to work at the workstation"}
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/skilldemandrecord/1/0"),
                        }

                    def __init__(
                        self,
                        skillClassificationId: Union[str, SkillClassificationId],
                        skillId: Union[str, SkillId],
                        startTime: Union[xsd.DateTime, StartTime],
                        endTime: Union[xsd.DateTime, EndTime],
                        processTime: Union[int, ProcessTime],
                        skillLevelClassificationId: Optional[Union[str, SkillLevelClassificationId]] = None,
                        skillLevelId: Optional[Union[str, SkillLevelId]] = None,
                        exceptionRules: Optional[Union[aas.LangStringSet, ExceptionRules]] = None,
                        demandKind: Optional[Union[str, DemandKind]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if skillClassificationId is not None and not isinstance(
                            skillClassificationId, aas.SubmodelElement
                        ):
                            skillClassificationId = self.SkillClassificationId(skillClassificationId)

                        # Build a submodel element if a raw value was passed in the argument

                        if skillLevelClassificationId is not None and not isinstance(
                            skillLevelClassificationId, aas.SubmodelElement
                        ):
                            skillLevelClassificationId = self.SkillLevelClassificationId(skillLevelClassificationId)

                        # Build a submodel element if a raw value was passed in the argument

                        if skillLevelId is not None and not isinstance(skillLevelId, aas.SubmodelElement):
                            skillLevelId = self.SkillLevelId(skillLevelId)

                        # Build a submodel element if a raw value was passed in the argument

                        if skillId is not None and not isinstance(skillId, aas.SubmodelElement):
                            skillId = self.SkillId(skillId)

                        # Build a submodel element if a raw value was passed in the argument

                        if exceptionRules is not None and not isinstance(exceptionRules, aas.SubmodelElement):
                            exceptionRules = self.ExceptionRules(exceptionRules)

                        # Build a submodel element if a raw value was passed in the argument

                        if demandKind is not None and not isinstance(demandKind, aas.SubmodelElement):
                            demandKind = self.DemandKind(demandKind)

                        # Build a submodel element if a raw value was passed in the argument

                        if startTime is not None and not isinstance(startTime, aas.SubmodelElement):
                            startTime = self.StartTime(startTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if endTime is not None and not isinstance(endTime, aas.SubmodelElement):
                            endTime = self.EndTime(endTime)

                        # Build a submodel element if a raw value was passed in the argument

                        if processTime is not None and not isinstance(processTime, aas.SubmodelElement):
                            processTime = self.ProcessTime(processTime)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            skillClassificationId,
                            skillLevelClassificationId,
                            skillLevelId,
                            skillId,
                            exceptionRules,
                            demandKind,
                            startTime,
                            endTime,
                            processTime,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"SkillDemandRecords",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Worker skills that are required in order to work at the workstation",
                                r"de": r"Mitarbeiterfähigkeiten die vorhanden sein müssen, um an der Arbeitsstation eingesetzt werden zu können",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/skilldemandrecords/1/0"),
                    }

                def __init__(
                    self,
                    skilldemandrecords_items: Iterable[Skilldemandrecords_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(skilldemandrecords_items, str):
                        raise TypeError("skilldemandrecords_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        skilldemandrecords_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Production plan depending planned skill demand at a workstation"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/smc/plannedskilldemandrecord/1/0"),
                }

            def __init__(
                self,
                skillDemandRecords: Union[Iterable[SkillDemandRecords.Skilldemandrecords_item], SkillDemandRecords],
                intervalDescription: Optional[Union[aas.LangStringSet, IntervalDescription]] = None,
                intervalStart: Optional[Union[xsd.DateTime, IntervalStart]] = None,
                intervalEnd: Optional[Union[xsd.DateTime, IntervalEnd]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if intervalDescription is not None and not isinstance(intervalDescription, aas.SubmodelElement):
                    intervalDescription = self.IntervalDescription(intervalDescription)

                # Build a submodel element if a raw value was passed in the argument

                if intervalStart is not None and not isinstance(intervalStart, aas.SubmodelElement):
                    intervalStart = self.IntervalStart(intervalStart)

                # Build a submodel element if a raw value was passed in the argument

                if intervalEnd is not None and not isinstance(intervalEnd, aas.SubmodelElement):
                    intervalEnd = self.IntervalEnd(intervalEnd)

                # A str would be split into its characters
                if isinstance(skillDemandRecords, str):
                    raise TypeError("skillDemandRecords takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if skillDemandRecords is not None and not isinstance(skillDemandRecords, aas.SubmodelElement):
                    skillDemandRecords = self.SkillDemandRecords(skillDemandRecords)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    intervalDescription, intervalStart, intervalEnd, skillDemandRecords
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"PlannedSkillDemand",
                "type_value_list_element": aas.SubmodelElementCollection,
                "display_name": aas.MultiLanguageNameType(
                    dict_={r"en": r"Planned skill demand", r"de": r"Geplanter Fähigkeitenbedarf"}
                ),
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Production plan depending planned skill demand at a workstation",
                        r"de": r"Vom Produktionsplan abhängiger und geplanter Qualifikationsbedarf an einer Arbeitsstation",
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/sml/plannedskilldemand/1/0"),
            }

        def __init__(
            self,
            plannedskilldemand_items: Optional[Iterable[Plannedskilldemand_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(plannedskilldemand_items, str):
                raise TypeError("plannedskilldemand_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(plannedskilldemand_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"WorkstationWorkerMatchingData",
            "display_name": aas.MultiLanguageNameType(
                dict_={r"en": r"Workstation Worker Matching Data", r"de": r"Daten für die Mitarbeitereinsatzplanung"}
            ),
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"Submodel containing workstation data in order to match and deploy workers to workstations",
                    r"de": r"Teilmodell mit Arbeitsstationsdaten für die Mitarbeitereinsatzplanung",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/sm/workstationworkermatchingdata",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        generalWorkstationData: GeneralWorkstationData,
        workstationConfigurationRecords: Union[
            Iterable[WorkstationConfigurationRecords.Workstationconfigurationrecords_item],
            WorkstationConfigurationRecords,
        ],
        ergonomicWorkstationProfile: Optional[ErgonomicWorkstationProfile] = None,
        plannedQualificationDemand: Optional[
            Union[Iterable[PlannedQualificationDemand.Plannedqualificationdemand_item], PlannedQualificationDemand]
        ] = None,
        plannedSkillDemand: Optional[
            Union[Iterable[PlannedSkillDemand.Plannedskilldemand_item], PlannedSkillDemand]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(workstationConfigurationRecords, str):
            raise TypeError("workstationConfigurationRecords takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if workstationConfigurationRecords is not None and not isinstance(
            workstationConfigurationRecords, aas.SubmodelElement
        ):
            workstationConfigurationRecords = self.WorkstationConfigurationRecords(workstationConfigurationRecords)

        # A str would be split into its characters
        if isinstance(plannedQualificationDemand, str):
            raise TypeError("plannedQualificationDemand takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if plannedQualificationDemand is not None and not isinstance(plannedQualificationDemand, aas.SubmodelElement):
            plannedQualificationDemand = self.PlannedQualificationDemand(plannedQualificationDemand)

        # A str would be split into its characters
        if isinstance(plannedSkillDemand, str):
            raise TypeError("plannedSkillDemand takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if plannedSkillDemand is not None and not isinstance(plannedSkillDemand, aas.SubmodelElement):
            plannedSkillDemand = self.PlannedSkillDemand(plannedSkillDemand)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            generalWorkstationData,
            ergonomicWorkstationProfile,
            workstationConfigurationRecords,
            plannedQualificationDemand,
            plannedSkillDemand,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
