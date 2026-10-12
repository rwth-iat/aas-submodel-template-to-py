from typing import Any, Iterable, Optional, Tuple, TypedDict, Union, Unpack, cast
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


class RangeMetadata(TypedDict, total=False):
    """Metadata of aas.Range, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    value_type: aas.DataTypeDefXsd
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class ReferenceElementMetadata(TypedDict, total=False):
    """Metadata of aas.ReferenceElement, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
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


class QualityControlForMachining(aas.Submodel):

    class QualityFeatures(aas.SubmodelElementCollection):

        class LinearFeaturesList(GeneratedSubmodelElementList):

            class Linearfeatureslist_item(aas.SubmodelElementCollection):

                class LinearFeatureName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LinearFeatureName",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeatureName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DimensionDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DimensionDescription",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/DimensionDescription/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MeasurementProcedure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MeasurementProcedure",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InspectionRelevant(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"InspectionRelevant",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ToleranceNorm(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ToleranceNorm",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO933#003"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class NominalValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"NominalValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Value for physical quantities that may be expressed as the nominal value of the quantity together with deviations from that nominal value as percentages or absolute values",
                                    r"de": r"Wert für physikalische Größen, der als Nominalwert der Größe zusammen mit Abweichungen von diesem Nominalwert als Prozentsätze oder absolute Werte ausgedrückt werden kann",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/NominalValue/1/0"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0112/2///61360_4#AAA235#001"),),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UpperTolerance(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UpperTolerance",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Upper tolerance limit of the feature as an absolute value.If there is a one-sided tolerance, only one tolerance limit is specified.",
                                    r"de": r"Obere Toranzgrenze des Merkmals als absoluter Wert. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/UpperTolerance/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LowerTolerance(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LowerTolerance",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Lower tolerance limit of the feature as an absolute value. If there is a one-sided tolerance, only one tolerance limit is specified.",
                                    r"de": r"Untere Toranzgrenze des Merkmals als absoluter Wert. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/LowerTolerance/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class OneSided(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"OneSided",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Is the measure tolerated one-sidedly? True means yes, false means no. If there is a one-sided tolerance, only one tolerance limit is specified",
                                    r"de": r"Ist das Maß einseitig toleriert? True bedeutet ja, false nein. Wenn eine einseitige Tolerierung vorliegt, wird entsprechend nur eine Toleranzgrenze angegeben",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/OneSided/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EngineeringUnit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EngineeringUnit",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Physical unit of feature", r"de": r"Physikalische Einheit des Merkmals"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GeometryReferenceList(GeneratedSubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": None,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Reference to a Geometry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometrie, beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"GeometryReferenceList",
                            "type_value_list_element": aas.ReferenceElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError("geometryreferencelist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Geometryreferencelist_item(i)
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            geometryreferencelist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class IDList3DModel(GeneratedSubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"IDList3DModel",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        idlist3dmodel_items: Optional[Iterable[Union[str, Idlist3dmodel_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError("idlist3dmodel_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Idlist3dmodel_item(i)
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            idlist3dmodel_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Reference2DList(GeneratedSubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Page",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Coordinate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Coordinate",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0"
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if page is not None and not isinstance(page, aas.SubmodelElement):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(coordinate, aas.SubmodelElement):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(page, coordinate)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Reference2DList",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        reference2dlist_items: Optional[Iterable[Reference2dlist_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(reference2dlist_items, str):
                            raise TypeError("reference2dlist_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reference2dlist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Description of the definition of a linear quality characteristic such as length, weight, angle, according to DIN EN ISO 14405-1: Dimensional tolerancing - Part 1: Linear size dimensions",
                                r"de": r"Beschreibung der Definition eines linearen Qualitätsmerkmals wie z.B. Länge, Gewicht, Winkel, gemäß DIN EN ISO 14405-1: Dimensionelle Tolerierung – Teil 1: Lineare Größenmaße",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeature/1/0"
                        ),
                    }

                def __init__(
                    self,
                    linearFeatureName: Union[str, LinearFeatureName],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    nominalValue: Union[float, NominalValue],
                    engineeringUnit: Union[str, EngineeringUnit],
                    dimensionDescription: Optional[Union[str, DimensionDescription]] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    upperTolerance: Optional[Union[float, UpperTolerance]] = None,
                    lowerTolerance: Optional[Union[float, LowerTolerance]] = None,
                    oneSided: Optional[Union[bool, OneSided]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[Union[aas.Reference, GeometryReferenceList.Geometryreferencelist_item]],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]], IDList3DModel]
                    ] = None,
                    reference2DList: Optional[
                        Union[Iterable[Reference2DList.Reference2dlist_item], Reference2DList]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if linearFeatureName is not None and not isinstance(linearFeatureName, aas.SubmodelElement):
                        linearFeatureName = self.LinearFeatureName(linearFeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if dimensionDescription is not None and not isinstance(dimensionDescription, aas.SubmodelElement):
                        dimensionDescription = self.DimensionDescription(dimensionDescription)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(measurementProcedure, aas.SubmodelElement):
                        measurementProcedure = self.MeasurementProcedure(measurementProcedure)

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(inspectionRelevant, aas.SubmodelElement):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError("toleranceNorm takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            i if isinstance(i, aas.SubmodelElement) else self.ToleranceNorm(i) for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if nominalValue is not None and not isinstance(nominalValue, aas.SubmodelElement):
                        nominalValue = self.NominalValue(nominalValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if upperTolerance is not None and not isinstance(upperTolerance, aas.SubmodelElement):
                        upperTolerance = self.UpperTolerance(upperTolerance)

                    # Build a submodel element if a raw value was passed in the argument

                    if lowerTolerance is not None and not isinstance(lowerTolerance, aas.SubmodelElement):
                        lowerTolerance = self.LowerTolerance(lowerTolerance)

                    # Build a submodel element if a raw value was passed in the argument

                    if oneSided is not None and not isinstance(oneSided, aas.SubmodelElement):
                        oneSided = self.OneSided(oneSided)

                    # Build a submodel element if a raw value was passed in the argument

                    if engineeringUnit is not None and not isinstance(engineeringUnit, aas.SubmodelElement):
                        engineeringUnit = self.EngineeringUnit(engineeringUnit)

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError("geometryReferenceList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(geometryReferenceList, aas.SubmodelElement):
                        geometryReferenceList = self.GeometryReferenceList(geometryReferenceList)

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError("iDList3DModel takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(iDList3DModel, aas.SubmodelElement):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError("reference2DList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(reference2DList, aas.SubmodelElement):
                        reference2DList = self.Reference2DList(reference2DList)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        linearFeatureName,
                        dimensionDescription,
                        measurementProcedure,
                        inspectionRelevant,
                        toleranceNorm,
                        nominalValue,
                        upperTolerance,
                        lowerTolerance,
                        oneSided,
                        engineeringUnit,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"LinearFeaturesList",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of linear quality characteristics, such as dimensions, weight, angles",
                            r"de": r"Liste linearer Qualitätsmerkmale, wie Dimensionen, Gewicht, Winkel",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/LinearFeaturesList/1/0"
                    ),
                }

            def __init__(
                self,
                linearfeatureslist_items: Optional[Iterable[Linearfeatureslist_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(linearfeatureslist_items, str):
                    raise TypeError("linearfeatureslist_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(linearfeatureslist_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class AttributiveFeaturesList(GeneratedSubmodelElementList):

            class Attributivefeatureslist_item(aas.SubmodelElementCollection):

                class AttributiveFeatureName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AttributiveFeatureName",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeatureName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AttibutiveFeatureDescription(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AttibutiveFeatureDescription",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/AttibutiveFeatureDescription/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MeasurementProcedure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MeasurementProcedure",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ToleranceNorm(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ToleranceNorm",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO933#003"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InspectionRelevant(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"InspectionRelevant",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GeometryReferenceList(GeneratedSubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": None,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"GeometryReferenceList",
                            "type_value_list_element": aas.ReferenceElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError("geometryreferencelist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Geometryreferencelist_item(i)
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            geometryreferencelist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class IDList3DModel(GeneratedSubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"IDList3DModel",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        idlist3dmodel_items: Optional[Iterable[Union[str, Idlist3dmodel_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError("idlist3dmodel_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Idlist3dmodel_item(i)
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            idlist3dmodel_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Reference2DList(GeneratedSubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Page",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Coordinate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Coordinate",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0"
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if page is not None and not isinstance(page, aas.SubmodelElement):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(coordinate, aas.SubmodelElement):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(page, coordinate)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Reference2DList",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        reference2dlist_items: Optional[Iterable[Reference2dlist_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(reference2dlist_items, str):
                            raise TypeError("reference2dlist_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reference2dlist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class OKAttributesList(GeneratedSubmodelElementList):

                    class Okattributeslist_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of an attribute that is accepted or tolerable in terms of quality assurance (OK attribute)",
                                        r"de": r"Bezeichnung eines Attributs, das akzeptiert bzw. im Sinne der Qualitätssicherung tolerabel ist (i.O.-Attribut)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/OKAttributName/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"OKAttributesList",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of attributes that are accepted or tolerable in terms of quality assurance (OK attributes)",
                                    r"de": r"Liste der Attribute, die akzeptiert bzw. im Sinne der Qualitätssicherung tolerabel sind (i.O.-Attribute)",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/OKAttributesList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        okattributeslist_items: Optional[Iterable[Union[str, Okattributeslist_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(okattributeslist_items, str):
                            raise TypeError("okattributeslist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if okattributeslist_items:
                            okattributeslist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Okattributeslist_item(i)
                                for i in okattributeslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            okattributeslist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class NOKAttributesList(GeneratedSubmodelElementList):

                    class Nokattributeslist_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of an attribute that is not accepted or intolerable in terms of quality assurance (not OK attribute)",
                                        r"de": r"Bezeichnung eines Attributs, das nicht akzeptiert bzw. im Sinne der Qualitätssicherung intolerabel ist (n.i.O.-Attribut)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/NOKAttributName/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"NOKAttributesList",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of attributes that are not accepted or intolerable in terms of quality assurance (not OK attributes)",
                                    r"de": r"Liste der Attribute, die nicht akzeptiert bzw. im Sinne der Qualitätssicherung intolerabel sind (n.i.O.-Attribute)",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/NOKAttributesList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        nokattributeslist_items: Optional[Iterable[Union[str, Nokattributeslist_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(nokattributeslist_items, str):
                            raise TypeError("nokattributeslist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if nokattributeslist_items:
                            nokattributeslist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Nokattributeslist_item(i)
                                for i in nokattributeslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            nokattributeslist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Information about an attributive quality feature",
                                r"de": r"Informationen zu einem attributiven Qualitätsmerkmal",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeature/1/0"
                        ),
                    }

                def __init__(
                    self,
                    attributiveFeatureName: Union[str, AttributiveFeatureName],
                    attibutiveFeatureDescription: Union[str, AttibutiveFeatureDescription],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    oKAttributesList: Union[
                        Iterable[Union[str, OKAttributesList.Okattributeslist_item]], OKAttributesList
                    ],
                    nOKAttributesList: Union[
                        Iterable[Union[str, NOKAttributesList.Nokattributeslist_item]], NOKAttributesList
                    ],
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[Union[aas.Reference, GeometryReferenceList.Geometryreferencelist_item]],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]], IDList3DModel]
                    ] = None,
                    reference2DList: Optional[
                        Union[Iterable[Reference2DList.Reference2dlist_item], Reference2DList]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if attributiveFeatureName is not None and not isinstance(
                        attributiveFeatureName, aas.SubmodelElement
                    ):
                        attributiveFeatureName = self.AttributiveFeatureName(attributiveFeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if attibutiveFeatureDescription is not None and not isinstance(
                        attibutiveFeatureDescription, aas.SubmodelElement
                    ):
                        attibutiveFeatureDescription = self.AttibutiveFeatureDescription(attibutiveFeatureDescription)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(measurementProcedure, aas.SubmodelElement):
                        measurementProcedure = self.MeasurementProcedure(measurementProcedure)

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError("toleranceNorm takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            i if isinstance(i, aas.SubmodelElement) else self.ToleranceNorm(i) for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(inspectionRelevant, aas.SubmodelElement):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError("geometryReferenceList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(geometryReferenceList, aas.SubmodelElement):
                        geometryReferenceList = self.GeometryReferenceList(geometryReferenceList)

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError("iDList3DModel takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(iDList3DModel, aas.SubmodelElement):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError("reference2DList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(reference2DList, aas.SubmodelElement):
                        reference2DList = self.Reference2DList(reference2DList)

                    # A str would be split into its characters
                    if isinstance(oKAttributesList, str):
                        raise TypeError("oKAttributesList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if oKAttributesList is not None and not isinstance(oKAttributesList, aas.SubmodelElement):
                        oKAttributesList = self.OKAttributesList(oKAttributesList)

                    # A str would be split into its characters
                    if isinstance(nOKAttributesList, str):
                        raise TypeError("nOKAttributesList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if nOKAttributesList is not None and not isinstance(nOKAttributesList, aas.SubmodelElement):
                        nOKAttributesList = self.NOKAttributesList(nOKAttributesList)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        attributiveFeatureName,
                        attibutiveFeatureDescription,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        oKAttributesList,
                        nOKAttributesList,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"AttributiveFeaturesList",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of attributive quality characteristics",
                            r"de": r"Liste attributiver Qualtätsmerkmale",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/AttributiveFeaturesList/1/0"
                    ),
                }

            def __init__(
                self,
                attributivefeatureslist_items: Optional[Iterable[Attributivefeatureslist_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(attributivefeatureslist_items, str):
                    raise TypeError("attributivefeatureslist_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    attributivefeatureslist_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class GeometricFeaturesList(GeneratedSubmodelElementList):

            class Geometricfeatureslist_item(aas.SubmodelElementCollection):

                class GPS_FeatureName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GPS_FeatureName",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GPS_FeatureName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GPS_Description(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GPS_Description",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Description/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MeasurementProcedure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MeasurementProcedure",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ToleranceNorm(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ToleranceNorm",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO933#003"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InspectionRelevant(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"InspectionRelevant",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GPS_Type(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GPS_Type",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"ValueList (straightness, flatness, roundness, cylindricity, line shape, surface shape, parallelism, perpendicularity, inclination, line profile direction, surface profile direction, position, coaxiality, concentricity, symmetry, line profile location, surface profile location, concentricity, axial runout, total concentricity, overall plan run)",
                                    r"de": r"ValueList (Geradheit, Ebenheit, Rundheit, Zylindrizität, Linienform, Flächenform, Parallelität, Rechtwinkligkeit, Neigung, Linienprofil-Richtung, Flächenprofil-Richtung, Position, Koaxialität, Konzentrizität, Symmetrie, Linienprofil-Ort, Flächenprofil-Ort, Rundlauf, Planlauf, Gesamtrundlauf, Gesamtplanlauf)",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Type/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GPS_ReferenceRequired(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GPS_ReferenceRequired",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Does a geometric reference have to be specified to make the feature unique? true corresponds to yes, false no",
                                    r"de": r"Muss zur Eindeutigkeit des Merkmals ein geometrischer Bezug angegeben werden? true entspricht ja, false nein",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GPS_ReferenceRequired/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GPS_ToleranceZone(aas.SubmodelElementCollection):

                    class Shape(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Shape",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Shape of the tolerance zone according to DIN EN ISO 1101",
                                        r"de": r"Gestalt der Toreanzzone gemäß DIN EN ISO 1101",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Shape/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ToleranceZoneDescription(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ToleranceZoneDescription",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Information on the partition based on the deviation from the ideal value within a certain area",
                                        r"de": r"Angaben zur Toleranzzone anhand der Abweichung vom Sollwert innerhalb eines bestimmten Bereichs",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceZoneDescription/1/0"
                                ),
                                "supplemental_semantic_id": (global_ref(r"0173-1#02-AAH964#005"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SpecificationModificator(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SpecificationModificator",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specification modifier according to DIN EN ISO 14405-1: LP, LS, GG, GX, GN, GC, CC, CA, CV, SX, SN, SA, SM, SD, SR, SQ)",
                                        r"de": r"Spezifikationsmodifikator gemäß DIN EN ISO 14405-1: LP, LS, GG, GX, GN, GC, CC, CA, CV, SX, SN, SA, SM, SD, SR, SQ)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SpecificationModificator/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class WidthExtendValue(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"WidthExtendValue",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Value for the width or extent of the tolerance zone according to DIN EN ISO 1101",
                                        r"de": r"Wert für Weite bzw.  Ausdehnung der Toleranzzone gemäß DIN EN ISO 1101",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendValue/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class WidthExtendTolerance1(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"WidthExtendTolerance1",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Tolerated deviation", r"de": r"TolerierteAbweichung"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendTolerance1/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class WidthExtendSign1(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"WidthExtendSign1",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Sign of tolerance (p, m, pm)",
                                        r"de": r"Vorzeichen der Tolerienung (p, m, pm)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendSign1/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class WidthExtendTolerance2(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"WidthExtendTolerance2",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Tolerated deviation", r"de": r"TolerierteAbweichung"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendTolerance2/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class WidthExtendSign2(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"WidthExtendSign2",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Sign of tolerance (p, m, pm)",
                                        r"de": r"Vorzeichen der Tolerienung (p, m, pm)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/WidthExtendSign2/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class EngineeringUnit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"EngineeringUnit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Physical unit of feature",
                                        r"de": r"Physikalische Einheit des Merkmals",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"GPS_ToleranceZone",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Tolerance zone according to DIN EN ISO 1101. The tolerance zone must be arranged symmetrically around the reference geometry element, unless otherwise stated.",
                                    r"de": r"Toleranzzone gemäß DIN EN ISO 1101. Die Toleranzzone muss symmetrisch um das Referenzgeometrieelement herum angeordnet werden, soweit nichts anderes angegeben ist.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GPS_ToleranceZone/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        shape: Union[str, Shape],
                        widthExtendTolerance1: Union[float, WidthExtendTolerance1],
                        widthExtendSign1: Union[str, WidthExtendSign1],
                        engineeringUnit: Union[str, EngineeringUnit],
                        toleranceZoneDescription: Optional[Union[str, ToleranceZoneDescription]] = None,
                        specificationModificator: Optional[Iterable[Union[str, SpecificationModificator]]] = None,
                        widthExtendValue: Optional[Iterable[Union[float, WidthExtendValue]]] = None,
                        widthExtendTolerance2: Optional[Union[float, WidthExtendTolerance2]] = None,
                        widthExtendSign2: Optional[Union[str, WidthExtendSign2]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if shape is not None and not isinstance(shape, aas.SubmodelElement):
                            shape = self.Shape(shape)

                        # Build a submodel element if a raw value was passed in the argument

                        if toleranceZoneDescription is not None and not isinstance(
                            toleranceZoneDescription, aas.SubmodelElement
                        ):
                            toleranceZoneDescription = self.ToleranceZoneDescription(toleranceZoneDescription)

                        # A str would be split into its characters
                        if isinstance(specificationModificator, str):
                            raise TypeError("specificationModificator takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if specificationModificator:
                            specificationModificator = [
                                i if isinstance(i, aas.SubmodelElement) else self.SpecificationModificator(i)
                                for i in specificationModificator
                            ]

                        # A str would be split into its characters
                        if isinstance(widthExtendValue, str):
                            raise TypeError("widthExtendValue takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if widthExtendValue:
                            widthExtendValue = [
                                i if isinstance(i, aas.SubmodelElement) else self.WidthExtendValue(i)
                                for i in widthExtendValue
                            ]

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendTolerance1 is not None and not isinstance(
                            widthExtendTolerance1, aas.SubmodelElement
                        ):
                            widthExtendTolerance1 = self.WidthExtendTolerance1(widthExtendTolerance1)

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendSign1 is not None and not isinstance(widthExtendSign1, aas.SubmodelElement):
                            widthExtendSign1 = self.WidthExtendSign1(widthExtendSign1)

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendTolerance2 is not None and not isinstance(
                            widthExtendTolerance2, aas.SubmodelElement
                        ):
                            widthExtendTolerance2 = self.WidthExtendTolerance2(widthExtendTolerance2)

                        # Build a submodel element if a raw value was passed in the argument

                        if widthExtendSign2 is not None and not isinstance(widthExtendSign2, aas.SubmodelElement):
                            widthExtendSign2 = self.WidthExtendSign2(widthExtendSign2)

                        # Build a submodel element if a raw value was passed in the argument

                        if engineeringUnit is not None and not isinstance(engineeringUnit, aas.SubmodelElement):
                            engineeringUnit = self.EngineeringUnit(engineeringUnit)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            shape,
                            toleranceZoneDescription,
                            specificationModificator,
                            widthExtendValue,
                            widthExtendTolerance1,
                            widthExtendSign1,
                            widthExtendTolerance2,
                            widthExtendSign2,
                            engineeringUnit,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class GeometryReferenceList(GeneratedSubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": None,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"GeometryReferenceList",
                            "type_value_list_element": aas.ReferenceElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError("geometryreferencelist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Geometryreferencelist_item(i)
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            geometryreferencelist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class IDList3DModel(GeneratedSubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"IDList3DModel",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        idlist3dmodel_items: Optional[Iterable[Union[str, Idlist3dmodel_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError("idlist3dmodel_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Idlist3dmodel_item(i)
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            idlist3dmodel_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Reference2DList(GeneratedSubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Page",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Coordinate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Coordinate",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0"
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if page is not None and not isinstance(page, aas.SubmodelElement):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(coordinate, aas.SubmodelElement):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(page, coordinate)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Reference2DList",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        reference2dlist_items: Optional[Iterable[Reference2dlist_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(reference2dlist_items, str):
                            raise TypeError("reference2dlist_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reference2dlist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class DatumField1(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DatumField1",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/DatumField1/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DatumField2(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DatumField2",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/DatumField2/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DatumField3(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DatumField3",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Information about a geometric reference that is required to define the feature",
                                    r"de": r"Angaben zu einem geometrischen Bezug der für die Definition des Merkmals benötigt wird",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/DatumField3/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AdditionalInformationList(GeneratedSubmodelElementList):

                    class Additionalinformationlist_item(aas.SubmodelElementCollection):

                        class GPS_Identifier(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"GPS_Identifier",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Identifier of additional GPS field information according to DIN EN 1101",
                                            r"de": r"Bezeichner einer zusätzlichen GPS Feldinformationen gemäß DIN EN 1101",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Identifier/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class GPS_Value(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"GPS_Value",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Value of additional GPS field information according to DIN EN 1101",
                                            r"de": r"Wert einer zusätzlichen GPS Feldinformation gemäß DIN EN 1101",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/GPS_Value/1/0"
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
                                        r"en": r"Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                        r"de": r"Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/AdditionalInformation/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            gPS_Identifier: Optional[Iterable[Union[str, GPS_Identifier]]] = None,
                            gPS_Value: Optional[Iterable[Union[str, GPS_Value]]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # A str would be split into its characters
                            if isinstance(gPS_Identifier, str):
                                raise TypeError("gPS_Identifier takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if gPS_Identifier:
                                gPS_Identifier = [
                                    i if isinstance(i, aas.SubmodelElement) else self.GPS_Identifier(i)
                                    for i in gPS_Identifier
                                ]

                            # A str would be split into its characters
                            if isinstance(gPS_Value, str):
                                raise TypeError("gPS_Value takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if gPS_Value:
                                gPS_Value = [
                                    i if isinstance(i, aas.SubmodelElement) else self.GPS_Value(i) for i in gPS_Value
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(gPS_Identifier, gPS_Value)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"AdditionalInformationList",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List with information on other GPS fields in accordance with DIN EN 1101",
                                    r"de": r"Liste mit Informationen zu weiteren GPS-Feldern gemäß DIN EN 1101",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/AdditionalInformationList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        additionalinformationlist_items: Optional[Iterable[Additionalinformationlist_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(additionalinformationlist_items, str):
                            raise TypeError("additionalinformationlist_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            additionalinformationlist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Information on a geometric quality feature according to DIN EN ISO 1101",
                                r"de": r"Angaben zu einem geometrischen Qualitätsmerkmal nach DIN EN ISO 1101",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/GeometricFeature/1/0"
                        ),
                    }

                def __init__(
                    self,
                    gPS_FeatureName: Union[str, GPS_FeatureName],
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    gPS_Type: Union[str, GPS_Type],
                    gPS_ReferenceRequired: Union[bool, GPS_ReferenceRequired],
                    gPS_Description: Optional[Union[str, GPS_Description]] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    gPS_ToleranceZone: Optional[Iterable[GPS_ToleranceZone]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[Union[aas.Reference, GeometryReferenceList.Geometryreferencelist_item]],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]], IDList3DModel]
                    ] = None,
                    reference2DList: Optional[
                        Union[Iterable[Reference2DList.Reference2dlist_item], Reference2DList]
                    ] = None,
                    datumField1: Optional[Union[str, DatumField1]] = None,
                    datumField2: Optional[Union[str, DatumField2]] = None,
                    datumField3: Optional[Union[str, DatumField3]] = None,
                    additionalInformationList: Optional[
                        Union[
                            Iterable[AdditionalInformationList.Additionalinformationlist_item],
                            AdditionalInformationList,
                        ]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_FeatureName is not None and not isinstance(gPS_FeatureName, aas.SubmodelElement):
                        gPS_FeatureName = self.GPS_FeatureName(gPS_FeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_Description is not None and not isinstance(gPS_Description, aas.SubmodelElement):
                        gPS_Description = self.GPS_Description(gPS_Description)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(measurementProcedure, aas.SubmodelElement):
                        measurementProcedure = self.MeasurementProcedure(measurementProcedure)

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError("toleranceNorm takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            i if isinstance(i, aas.SubmodelElement) else self.ToleranceNorm(i) for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(inspectionRelevant, aas.SubmodelElement):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_Type is not None and not isinstance(gPS_Type, aas.SubmodelElement):
                        gPS_Type = self.GPS_Type(gPS_Type)

                    # Build a submodel element if a raw value was passed in the argument

                    if gPS_ReferenceRequired is not None and not isinstance(gPS_ReferenceRequired, aas.SubmodelElement):
                        gPS_ReferenceRequired = self.GPS_ReferenceRequired(gPS_ReferenceRequired)

                    # A str would be split into its characters
                    if isinstance(gPS_ToleranceZone, str):
                        raise TypeError("gPS_ToleranceZone takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError("geometryReferenceList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(geometryReferenceList, aas.SubmodelElement):
                        geometryReferenceList = self.GeometryReferenceList(geometryReferenceList)

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError("iDList3DModel takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(iDList3DModel, aas.SubmodelElement):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError("reference2DList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(reference2DList, aas.SubmodelElement):
                        reference2DList = self.Reference2DList(reference2DList)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField1 is not None and not isinstance(datumField1, aas.SubmodelElement):
                        datumField1 = self.DatumField1(datumField1)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField2 is not None and not isinstance(datumField2, aas.SubmodelElement):
                        datumField2 = self.DatumField2(datumField2)

                    # Build a submodel element if a raw value was passed in the argument

                    if datumField3 is not None and not isinstance(datumField3, aas.SubmodelElement):
                        datumField3 = self.DatumField3(datumField3)

                    # A str would be split into its characters
                    if isinstance(additionalInformationList, str):
                        raise TypeError("additionalInformationList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if additionalInformationList is not None and not isinstance(
                        additionalInformationList, aas.SubmodelElement
                    ):
                        additionalInformationList = self.AdditionalInformationList(additionalInformationList)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        gPS_FeatureName,
                        gPS_Description,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        gPS_Type,
                        gPS_ReferenceRequired,
                        gPS_ToleranceZone,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        datumField1,
                        datumField2,
                        datumField3,
                        additionalInformationList,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"GeometricFeaturesList",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of geometric quality characteristics according to DIN EN ISO 1101",
                            r"de": r"Liste geometrischer Qualitätsmerkmale gemäß DIN EN ISO 1101",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/GeometricFeaturesList/1/0"
                    ),
                }

            def __init__(
                self,
                geometricfeatureslist_items: Optional[Iterable[Geometricfeatureslist_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(geometricfeatureslist_items, str):
                    raise TypeError("geometricfeatureslist_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    geometricfeatureslist_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class ArealSurfaceFeaturesList(GeneratedSubmodelElementList):

            class Arealsurfacefeatureslist_item(aas.SubmodelElementCollection):

                class ASF_FeatureName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ASF_FeatureName",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ASF_FeatureName/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ASF_Description(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ASF_Description",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ASF_Description/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MeasurementProcedure(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MeasurementProcedure",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the measurement procedure, e.g. series measurements have to be averaged",
                                    r"de": r"Beschreibung der Messmethode, z. B. Werte der Messserie müssen gemittelt werden.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MeasurementProcedure/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ToleranceNorm(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ToleranceNorm",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to one or more norms and guidelines in which the code for the used tolerance is defined",
                                    r"de": r"Verweis auf eine oder mehrere Normen und Richtlinien, in denen der Code für die verwendete Toleranz festgelegt ist",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ToleranceNorm/1/0"
                            ),
                            "supplemental_semantic_id": (global_ref(r"0173-1#02-AAO933#003"),),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class InspectionRelevant(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"InspectionRelevant",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Is the measurement relevant as a test measure for quality assurance? True means yes, false means no",
                                    r"de": r"Ist das Maß als Prüfmaß für die Qualiätssicherung relevant? True bedeutet ja, false nein",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/InspectionRelevant/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ArealSurfaceFeatureType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ArealSurfaceFeatureType",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r'Type of surface feature according to DIN EN ISO 25178-1(Value List "S-L" or "S-F")',
                                    r"de": r'Typ der Oberflächenbeschaffenheit gemäß DIN EN ISO 25178-1 (Value-List "S-L" oder "S-F")',
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeatureType/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GeometryReferenceList(GeneratedSubmodelElementList):

                    class Geometryreferencelist_item(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": None,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Reference to a Geomatry element described by a SMC Geometry in the Submodel Provision of 3D Models",
                                        r"de": r"Referenz zu einer Geometry beschrieben durch eine SMC Geometry innerhalb des Teilmodells Provision of 3D Models",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ReferenceGeometry3DModel/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"GeometryReferenceList",
                            "type_value_list_element": aas.ReferenceElement,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Geomtery Reference List in Submodel Provision of 3D Models",
                                    r"de": r"Geometriereferenzliste im Teilmodell Provision of 3D Models",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/GeometryReferenceList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        geometryreferencelist_items: Optional[
                            Iterable[Union[aas.Reference, Geometryreferencelist_item]]
                        ] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(geometryreferencelist_items, str):
                            raise TypeError("geometryreferencelist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if geometryreferencelist_items:
                            geometryreferencelist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Geometryreferencelist_item(i)
                                for i in geometryreferencelist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            geometryreferencelist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class IDList3DModel(GeneratedSubmodelElementList):

                    class Idlist3dmodel_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"One element ID which relates to the quality feature",
                                        r"de": r"Eine Element ID, auf das sich das Qualitätsmerkmal bezieht",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/ElementID/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"IDList3DModel",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of IDs in 3D Model which relate to the quality feature",
                                    r"de": r"Liste von IDs im 3D Modell, die sich auf das Qualitätsmerkmal beziehen",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/IDList3DModel/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        idlist3dmodel_items: Optional[Iterable[Union[str, Idlist3dmodel_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(idlist3dmodel_items, str):
                            raise TypeError("idlist3dmodel_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if idlist3dmodel_items:
                            idlist3dmodel_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Idlist3dmodel_item(i)
                                for i in idlist3dmodel_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            idlist3dmodel_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Reference2DList(GeneratedSubmodelElementList):

                    class Reference2dlist_item(aas.SubmodelElementCollection):

                        class Page(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Page",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Page in the 2D document where the quality feature is illustrated",
                                            r"de": r"Seite im 2D Dokument, auf der das Qualitätsmerkmal dargestellt ist",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Page/1/0"
                                    ),
                                }

                            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                                super().__init__(value=value, **(self.template_defaults() | kwargs))

                        class Coordinate(aas.Property):

                            @staticmethod
                            def template_defaults() -> PropertyMetadata:
                                return {
                                    "id_short": r"Coordinate",
                                    "value_type": str,
                                    "description": aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Coordinate of the quality feature in a 2D document, e.g., 1B",
                                            r"de": r"Koordinate des Qualitätsmerkmals in 2D Dokument, z.B. 1B",
                                        }
                                    ),
                                    "semantic_id": global_ref(
                                        r"https://admin-shell.io/idta/QualityControlForMachining/Coordinate/1/0"
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
                                        r"en": r"Reference to an element in a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                        r"de": r"Referenz zu einem Element in einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Reference2D/1/0"
                                ),
                            }

                        def __init__(
                            self,
                            page: Optional[Union[str, Page]] = None,
                            coordinate: Optional[Union[str, Coordinate]] = None,
                            **kwargs: Unpack[SubmodelElementCollectionMetadata],
                        ):

                            # Build a submodel element if a raw value was passed in the argument

                            if page is not None and not isinstance(page, aas.SubmodelElement):
                                page = self.Page(page)

                            # Build a submodel element if a raw value was passed in the argument

                            if coordinate is not None and not isinstance(coordinate, aas.SubmodelElement):
                                coordinate = self.Coordinate(coordinate)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(page, coordinate)

                            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"Reference2DList",
                            "type_value_list_element": aas.SubmodelElementCollection,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"List of references to a 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed",
                                    r"de": r"Liste mit Referenzen zu einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Reference2DList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        reference2dlist_items: Optional[Iterable[Reference2dlist_item]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(reference2dlist_items, str):
                            raise TypeError("reference2dlist_items takes several elements, got a str")

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            reference2dlist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class SL_Parameters(aas.SubmodelElementCollection):

                    class SL_ASP_Limit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_Limit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Either U (upper) or L (lower) specification limit according to ISO 25178-1",
                                        r"de": r"Entweder U (obere) oder L (untere) Spezifikationsgrenze gemäß ISO 25178-1",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Limit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_S_FilterType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_S_FilterType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Filter type of S-filter", r"de": r"Filtertyp des S-Filters"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_S_FilterType/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_S_FilterNestingIndex(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_S_FilterNestingIndex",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Nesting index of the S-filter",
                                        r"de": r"Nesting-Index des S-Filters",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_S_FilterNestingIndex/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_L_FilterType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_L_FilterType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Filter type of L-filter", r"de": r"Filtertyp des L-Filters"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_L_FilterType/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_L_FilterNestingIndex(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_L_FilterNestingIndex",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Nesting index of the L-filter",
                                        r"de": r"Nesting-Index des L-Filters",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_L_FilterNestingIndex/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_F_Operator(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_F_Operator",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Type of association operator and nesting index",
                                        r"de": r"Typ des Assoziationsoperators und des Nesting-Indexes",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_F_Operator/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_Indicator(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_Indicator",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of the areal parameter. See also ISO 25178-2:2012, 3.2",
                                        r"de": r"Bezeichnung der flächenhaften Kenngröße. Siehe auch ISO 25178-2:2012, 3.2",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Indicator/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_Value(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_Value",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Value/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_Unit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Unit of the parameter value, if it is not the default unit",
                                        r"de": r"Einheit des Kenngrößenwertes, sofern es nicht die defaultmäßige Einheit ist.",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Unit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SL_ASP_Or(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SL_ASP_Or",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Symbol for the option to choose other requirements according to DIN EN ISO ISO 25178-2. Additional requirements are specified here.",
                                        r"de": r"Symbol für die Wahlmöglichkeit sonstige Anforderungen gemäß DIN EN ISO 25178-2. An dieser Stelle werden zusätzliche Anforderungen angegeben.",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SL_ASP_Or/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"SL_Parameters",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Specification of an S-L surface finish according to DIN EN ISO 25178-1",
                                    r"de": r"Spezifikation einer S-L-Oberflächenbeschaffenheit gemäß DIN EN ISO 25178-1",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/SL_Parameters/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        sL_ASP_Limit: Union[str, SL_ASP_Limit],
                        sL_ASP_S_FilterType: Union[str, SL_ASP_S_FilterType],
                        sL_ASP_S_FilterNestingIndex: Union[str, SL_ASP_S_FilterNestingIndex],
                        sL_ASP_L_FilterType: Union[str, SL_ASP_L_FilterType],
                        sL_ASP_L_FilterNestingIndex: Union[str, SL_ASP_L_FilterNestingIndex],
                        sL_ASP_F_Operator: Union[str, SL_ASP_F_Operator],
                        sL_ASP_Indicator: Union[str, SL_ASP_Indicator],
                        sL_ASP_Value: Union[float, SL_ASP_Value],
                        sL_ASP_Unit: Union[str, SL_ASP_Unit],
                        sL_ASP_Or: Optional[Union[str, SL_ASP_Or]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Limit is not None and not isinstance(sL_ASP_Limit, aas.SubmodelElement):
                            sL_ASP_Limit = self.SL_ASP_Limit(sL_ASP_Limit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_S_FilterType is not None and not isinstance(sL_ASP_S_FilterType, aas.SubmodelElement):
                            sL_ASP_S_FilterType = self.SL_ASP_S_FilterType(sL_ASP_S_FilterType)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_S_FilterNestingIndex is not None and not isinstance(
                            sL_ASP_S_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sL_ASP_S_FilterNestingIndex = self.SL_ASP_S_FilterNestingIndex(sL_ASP_S_FilterNestingIndex)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_L_FilterType is not None and not isinstance(sL_ASP_L_FilterType, aas.SubmodelElement):
                            sL_ASP_L_FilterType = self.SL_ASP_L_FilterType(sL_ASP_L_FilterType)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_L_FilterNestingIndex is not None and not isinstance(
                            sL_ASP_L_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sL_ASP_L_FilterNestingIndex = self.SL_ASP_L_FilterNestingIndex(sL_ASP_L_FilterNestingIndex)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_F_Operator is not None and not isinstance(sL_ASP_F_Operator, aas.SubmodelElement):
                            sL_ASP_F_Operator = self.SL_ASP_F_Operator(sL_ASP_F_Operator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Indicator is not None and not isinstance(sL_ASP_Indicator, aas.SubmodelElement):
                            sL_ASP_Indicator = self.SL_ASP_Indicator(sL_ASP_Indicator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Value is not None and not isinstance(sL_ASP_Value, aas.SubmodelElement):
                            sL_ASP_Value = self.SL_ASP_Value(sL_ASP_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Unit is not None and not isinstance(sL_ASP_Unit, aas.SubmodelElement):
                            sL_ASP_Unit = self.SL_ASP_Unit(sL_ASP_Unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sL_ASP_Or is not None and not isinstance(sL_ASP_Or, aas.SubmodelElement):
                            sL_ASP_Or = self.SL_ASP_Or(sL_ASP_Or)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            sL_ASP_Limit,
                            sL_ASP_S_FilterType,
                            sL_ASP_S_FilterNestingIndex,
                            sL_ASP_L_FilterType,
                            sL_ASP_L_FilterNestingIndex,
                            sL_ASP_F_Operator,
                            sL_ASP_Indicator,
                            sL_ASP_Value,
                            sL_ASP_Unit,
                            sL_ASP_Or,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class SF_Parameters(aas.SubmodelElementCollection):

                    class SF_ASP_Limit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_Limit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Either U (upper) or L (lower) specification limit according to ISO 25178-1",
                                        r"de": r"Entweder U (obere) oder L (untere) Spezifikationsgrenze gemäß ISO 25178-1",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Limit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_S_FilterType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_S_FilterType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Filter type of S-filter", r"de": r"Filtertyp des S-Filters"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_S_FilterType/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_S_FilterNestingIndex(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_S_FilterNestingIndex",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Nesting index of the S-filter",
                                        r"de": r"Nesting-Index des S-Filters",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_S_FilterNestingIndex/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_F_Operator(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_F_Operator",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Type of association operator and nesting index",
                                        r"de": r"Typ des Assoziationsoperators und des Nesting-Indexes",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_F_Operator/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_Indicator(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_Indicator",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Name of the areal parameter. See also ISO 25178-2:2012, 3.2",
                                        r"de": r"Bezeichnung der flächenhaften Kenngröße. Siehe auch ISO 25178-2:2012, 3.2",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Indicator/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_Value(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_Value",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Value/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_Unit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Unit of the parameter value, if it is not the default unit (the default unit µm does not need to be specified)",
                                        r"de": r"Einheit des Kenngrößenwertes, sofern es nicht die defaultmäßige Einheit ist (die defaultmäßige Einheit µm braucht nicht angegeben zu werden)",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Unit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_ES(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_ES",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Choice of electromagnetic surface, according to DIN EN 25178-2",
                                        r"de": r"Wahlmöglichkeit elektromagnetische Oberfläche gemäß DIN EN ISO 25178-2",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_ES/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SF_ASP_Or(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SF_ASP_Or",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Symbol for the option to choose other requirements according to DIN EN ISO 25178-2. Additional requirements are specified here.",
                                        r"de": r"Symbol für die Wahlmöglichkeit sonstige Anforderungen gemäß DIN EN ISO 25178-2. An dieser Stelle werden zusätzliche Anforderungen angegeben.",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/SF_ASP_Or/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"SF_Parameters",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Specification of an S-F surface finish, see ISO 25178-2:2012, 3.1.6",
                                    r"de": r"Spezifikation einer S-F-Oberflächenbeschaffenheit, siehe ISO 25178-2:2012, 3.1.6",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/SF_Parameters/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        sF_ASP_Limit: Union[str, SF_ASP_Limit],
                        sF_ASP_S_FilterType: Union[str, SF_ASP_S_FilterType],
                        sF_ASP_S_FilterNestingIndex: Union[str, SF_ASP_S_FilterNestingIndex],
                        sF_ASP_F_Operator: Union[str, SF_ASP_F_Operator],
                        sF_ASP_Indicator: Union[str, SF_ASP_Indicator],
                        sF_ASP_Value: Union[float, SF_ASP_Value],
                        sF_ASP_Unit: Optional[Union[str, SF_ASP_Unit]] = None,
                        sF_ASP_ES: Optional[Union[str, SF_ASP_ES]] = None,
                        sF_ASP_Or: Optional[Union[str, SF_ASP_Or]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Limit is not None and not isinstance(sF_ASP_Limit, aas.SubmodelElement):
                            sF_ASP_Limit = self.SF_ASP_Limit(sF_ASP_Limit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_S_FilterType is not None and not isinstance(sF_ASP_S_FilterType, aas.SubmodelElement):
                            sF_ASP_S_FilterType = self.SF_ASP_S_FilterType(sF_ASP_S_FilterType)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_S_FilterNestingIndex is not None and not isinstance(
                            sF_ASP_S_FilterNestingIndex, aas.SubmodelElement
                        ):
                            sF_ASP_S_FilterNestingIndex = self.SF_ASP_S_FilterNestingIndex(sF_ASP_S_FilterNestingIndex)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_F_Operator is not None and not isinstance(sF_ASP_F_Operator, aas.SubmodelElement):
                            sF_ASP_F_Operator = self.SF_ASP_F_Operator(sF_ASP_F_Operator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Indicator is not None and not isinstance(sF_ASP_Indicator, aas.SubmodelElement):
                            sF_ASP_Indicator = self.SF_ASP_Indicator(sF_ASP_Indicator)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Value is not None and not isinstance(sF_ASP_Value, aas.SubmodelElement):
                            sF_ASP_Value = self.SF_ASP_Value(sF_ASP_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Unit is not None and not isinstance(sF_ASP_Unit, aas.SubmodelElement):
                            sF_ASP_Unit = self.SF_ASP_Unit(sF_ASP_Unit)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_ES is not None and not isinstance(sF_ASP_ES, aas.SubmodelElement):
                            sF_ASP_ES = self.SF_ASP_ES(sF_ASP_ES)

                        # Build a submodel element if a raw value was passed in the argument

                        if sF_ASP_Or is not None and not isinstance(sF_ASP_Or, aas.SubmodelElement):
                            sF_ASP_Or = self.SF_ASP_Or(sF_ASP_Or)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            sF_ASP_Limit,
                            sF_ASP_S_FilterType,
                            sF_ASP_S_FilterNestingIndex,
                            sF_ASP_F_Operator,
                            sF_ASP_Indicator,
                            sF_ASP_Value,
                            sF_ASP_Unit,
                            sF_ASP_ES,
                            sF_ASP_Or,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class Smr_Parameters(aas.SubmodelElementCollection):

                    class Smr_RefCValue(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Smr_RefCValue",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specification of the reference level as a percentage of the material proportion curve, see ISO 25178-2:2012, 4.4.3. The default reference is the highest point 0% of the material proportion curve and does not need to be specified.",
                                        r"de": "Spezifikation des Bezugsniveaus als prozentualer Anteil der Materialanteilskurve, siehe\nISO 25178-2:2012, 4.4.3. Der Default-Bezug ist der höchste Punkt 0 % der Materialanteilskurve und braucht nicht angegeben zu werden.",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Smr_RefCValue/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Smr_CValue(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Smr_CValue",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Set height distance in relation to the reference c value in µm, see ISO 25178-2:2012, 4.4.2. The c-value is negative if it is below the reference c-value and is positive if it is is above the reference c value",
                                        r"de": "Festgelegter Höhenabstand im Verhältnis zum Bezugs-c-Wert in µm, siehe\nISO 25178-2:2012, 4.4.2.\nDer c-Wert ist negativ, wenn er unter dem Bezugs-c-Wert liegt, und ist positiv, wenn er\nüber dem Bezugs-c-Wert liegt",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Smr_CValue/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Smr_Value(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Smr_Value",
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specified limit value of the parameter",
                                        r"de": r"Festgelegter Grenzwert der Kenngröße",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Value/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class Smr_Unit(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"Smr_Unit",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Unit, default: %, must always be specified",
                                        r"de": r"Einhheit, default: %, muss immer angegeben werden",
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Unit/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"Smr_Parameters",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Control elements for specifying the parameter value Smr for the material ratio in technical drawings, applies to both S-L and S-F surface finishes, see also ISO 25178-2:2012, 3.1.6",
                                    r"de": r"Steuerelemente für die Angabe des Kenngrößenwertes Smr für das Materialverhältnis in technischen Zeichnungen, gilt sowohl für S-L als auch für S-F Oberflächenbeschaffenheiten, siehe auch ISO 25178-2:2012, 3.1.6",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Smr_Parameters/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        smr_CValue: Union[str, Smr_CValue],
                        smr_Value: Union[float, Smr_Value],
                        smr_Unit: Union[str, Smr_Unit],
                        smr_RefCValue: Optional[Union[str, Smr_RefCValue]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_RefCValue is not None and not isinstance(smr_RefCValue, aas.SubmodelElement):
                            smr_RefCValue = self.Smr_RefCValue(smr_RefCValue)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_CValue is not None and not isinstance(smr_CValue, aas.SubmodelElement):
                            smr_CValue = self.Smr_CValue(smr_CValue)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_Value is not None and not isinstance(smr_Value, aas.SubmodelElement):
                            smr_Value = self.Smr_Value(smr_Value)

                        # Build a submodel element if a raw value was passed in the argument

                        if smr_Unit is not None and not isinstance(smr_Unit, aas.SubmodelElement):
                            smr_Unit = self.Smr_Unit(smr_Unit)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            smr_RefCValue, smr_CValue, smr_Value, smr_Unit
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Definition of an areal surface parameter according to DIN EN ISO 25178-1",
                                r"de": r"Definition einer flächenhaften Oberflächenkenngröße gemäß DIN EN ISO 25178-1",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeature/1/0"
                        ),
                    }

                def __init__(
                    self,
                    measurementProcedure: Union[str, MeasurementProcedure],
                    inspectionRelevant: Union[bool, InspectionRelevant],
                    arealSurfaceFeatureType: Union[str, ArealSurfaceFeatureType],
                    aSF_FeatureName: Optional[Union[str, ASF_FeatureName]] = None,
                    aSF_Description: Optional[Union[str, ASF_Description]] = None,
                    toleranceNorm: Optional[Iterable[Union[str, ToleranceNorm]]] = None,
                    geometryReferenceList: Optional[
                        Union[
                            Iterable[Union[aas.Reference, GeometryReferenceList.Geometryreferencelist_item]],
                            GeometryReferenceList,
                        ]
                    ] = None,
                    iDList3DModel: Optional[
                        Union[Iterable[Union[str, IDList3DModel.Idlist3dmodel_item]], IDList3DModel]
                    ] = None,
                    reference2DList: Optional[
                        Union[Iterable[Reference2DList.Reference2dlist_item], Reference2DList]
                    ] = None,
                    sL_Parameters: Optional[Iterable[SL_Parameters]] = None,
                    sF_Parameters: Optional[Iterable[SF_Parameters]] = None,
                    smr_Parameters: Optional[Smr_Parameters] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if aSF_FeatureName is not None and not isinstance(aSF_FeatureName, aas.SubmodelElement):
                        aSF_FeatureName = self.ASF_FeatureName(aSF_FeatureName)

                    # Build a submodel element if a raw value was passed in the argument

                    if aSF_Description is not None and not isinstance(aSF_Description, aas.SubmodelElement):
                        aSF_Description = self.ASF_Description(aSF_Description)

                    # Build a submodel element if a raw value was passed in the argument

                    if measurementProcedure is not None and not isinstance(measurementProcedure, aas.SubmodelElement):
                        measurementProcedure = self.MeasurementProcedure(measurementProcedure)

                    # A str would be split into its characters
                    if isinstance(toleranceNorm, str):
                        raise TypeError("toleranceNorm takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if toleranceNorm:
                        toleranceNorm = [
                            i if isinstance(i, aas.SubmodelElement) else self.ToleranceNorm(i) for i in toleranceNorm
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if inspectionRelevant is not None and not isinstance(inspectionRelevant, aas.SubmodelElement):
                        inspectionRelevant = self.InspectionRelevant(inspectionRelevant)

                    # Build a submodel element if a raw value was passed in the argument

                    if arealSurfaceFeatureType is not None and not isinstance(
                        arealSurfaceFeatureType, aas.SubmodelElement
                    ):
                        arealSurfaceFeatureType = self.ArealSurfaceFeatureType(arealSurfaceFeatureType)

                    # A str would be split into its characters
                    if isinstance(geometryReferenceList, str):
                        raise TypeError("geometryReferenceList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if geometryReferenceList is not None and not isinstance(geometryReferenceList, aas.SubmodelElement):
                        geometryReferenceList = self.GeometryReferenceList(geometryReferenceList)

                    # A str would be split into its characters
                    if isinstance(iDList3DModel, str):
                        raise TypeError("iDList3DModel takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if iDList3DModel is not None and not isinstance(iDList3DModel, aas.SubmodelElement):
                        iDList3DModel = self.IDList3DModel(iDList3DModel)

                    # A str would be split into its characters
                    if isinstance(reference2DList, str):
                        raise TypeError("reference2DList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if reference2DList is not None and not isinstance(reference2DList, aas.SubmodelElement):
                        reference2DList = self.Reference2DList(reference2DList)

                    # A str would be split into its characters
                    if isinstance(sL_Parameters, str):
                        raise TypeError("sL_Parameters takes several elements, got a str")

                    # A str would be split into its characters
                    if isinstance(sF_Parameters, str):
                        raise TypeError("sF_Parameters takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        aSF_FeatureName,
                        aSF_Description,
                        measurementProcedure,
                        toleranceNorm,
                        inspectionRelevant,
                        arealSurfaceFeatureType,
                        geometryReferenceList,
                        iDList3DModel,
                        reference2DList,
                        sL_Parameters,
                        sF_Parameters,
                        smr_Parameters,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"ArealSurfaceFeaturesList",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of areal surface parameters according to EN ISO 25178-1",
                            r"de": r"Liste flächenhafter Oberflächenkenngrößen gemäß EN ISO 25178-1",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/ArealSurfaceFeaturesList/1/0"
                    ),
                }

            def __init__(
                self,
                arealsurfacefeatureslist_items: Optional[Iterable[Arealsurfacefeatureslist_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(arealsurfacefeatureslist_items, str):
                    raise TypeError("arealsurfacefeatureslist_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    arealsurfacefeatureslist_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"QualityFeatures",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Quality criteria of the item and their properties",
                        r"de": r"Qualitätskriterien des Artikels und deren Eigenschaften",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/QualityFeatures/1/0"
                ),
            }

        def __init__(
            self,
            linearFeaturesList: Optional[
                Union[Iterable[LinearFeaturesList.Linearfeatureslist_item], LinearFeaturesList]
            ] = None,
            attributiveFeaturesList: Optional[
                Union[Iterable[AttributiveFeaturesList.Attributivefeatureslist_item], AttributiveFeaturesList]
            ] = None,
            geometricFeaturesList: Optional[
                Union[Iterable[GeometricFeaturesList.Geometricfeatureslist_item], GeometricFeaturesList]
            ] = None,
            arealSurfaceFeaturesList: Optional[
                Union[Iterable[ArealSurfaceFeaturesList.Arealsurfacefeatureslist_item], ArealSurfaceFeaturesList]
            ] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(linearFeaturesList, str):
                raise TypeError("linearFeaturesList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if linearFeaturesList is not None and not isinstance(linearFeaturesList, aas.SubmodelElement):
                linearFeaturesList = self.LinearFeaturesList(linearFeaturesList)

            # A str would be split into its characters
            if isinstance(attributiveFeaturesList, str):
                raise TypeError("attributiveFeaturesList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if attributiveFeaturesList is not None and not isinstance(attributiveFeaturesList, aas.SubmodelElement):
                attributiveFeaturesList = self.AttributiveFeaturesList(attributiveFeaturesList)

            # A str would be split into its characters
            if isinstance(geometricFeaturesList, str):
                raise TypeError("geometricFeaturesList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if geometricFeaturesList is not None and not isinstance(geometricFeaturesList, aas.SubmodelElement):
                geometricFeaturesList = self.GeometricFeaturesList(geometricFeaturesList)

            # A str would be split into its characters
            if isinstance(arealSurfaceFeaturesList, str):
                raise TypeError("arealSurfaceFeaturesList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if arealSurfaceFeaturesList is not None and not isinstance(arealSurfaceFeaturesList, aas.SubmodelElement):
                arealSurfaceFeaturesList = self.ArealSurfaceFeaturesList(arealSurfaceFeaturesList)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                linearFeaturesList, attributiveFeaturesList, geometricFeaturesList, arealSurfaceFeaturesList
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class ProductionCriteria(aas.SubmodelElementCollection):

        class TechnicalData(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"TechnicalData",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Reference to the AAS Submodel Technical Data for Industrial\nEquipment in Manufacturing",
                            r"de": 'Referenz auf das AAS Submodel Technical Data for Industrial\nEquipment in Manufacturing"',
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/TechnicalData/1/0"
                    ),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductionJobOrderParameters(aas.SubmodelElementCollection):

            class ProductionStart(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProductionStart",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Date and time when production started for the production order",
                                r"de": r"Datum und Uhrzeit des Starts der Produktion für den Produktionsauftrag",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/ProductionStart/1/0"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0112/2///61360_4#ADA031#001"),),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ProductionEnd(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ProductionEnd",
                        "value_type": xsd.DateTime,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Date and time when production ended for the production order",
                                r"de": r"Datum und Uhrzeit des Endes der Produktion für den Produktionsauftrag",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/ProductionEnd/1/0"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0112/2///61360_4#ADA031#001"),),
                    }

                def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class JobName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"JobName",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Human readable name of the job. Array shall always contain the same text, potentially in different languages.",
                                r"de": r"Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class JobOrderNumber(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"JobOrderNumber",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.",
                                r"de": r"Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PlannedPartsPerRun(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PlannedPartsPerRun",
                        "value_type": int,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The number of parts produced by one run",
                                r"de": r"Die Anzahl der Teile, die in einem Lauf produziert werden",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0"
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class PlannedOrderQuantity(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"PlannedOrderQuantity",
                        "value_type": int,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The planned order quantity shall be the planned quantity of products for a production order (lot size, production order quantity). [Source: ISO 22400]",
                                r"de": r"Die geplante Auftragsmenge ist die geplante Produktmenge für einen Produktionsauftrag (Losgröße, Produktionsauftragsmenge). [Quelle: ISO 22400]",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/PlannedOrderQuantity/1/0"
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ActualPartsInRun(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"ActualPartsInRun",
                        "value_type": int,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"The number of parts actually measuerd by one run",
                                r"de": r"Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0"
                        ),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class JobFinished(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"JobFinished",
                        "value_type": bool,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Status order completed. True: yes, false: no",
                                r"de": r"Status Auftrag beendet. True: ja, false: nein",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"ProductionJobOrderParameters",
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Production order information", r"de": r"Informationen zum Produktionsauftrag"}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/ProductionJobOrderParameters/1/0"
                    ),
                }

            def __init__(
                self,
                productionStart: Union[xsd.DateTime, ProductionStart],
                jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
                plannedOrderQuantity: Union[int, PlannedOrderQuantity],
                productionEnd: Optional[Union[xsd.DateTime, ProductionEnd]] = None,
                jobName: Optional[Union[str, JobName]] = None,
                plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
                actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
                jobFinished: Optional[Union[bool, JobFinished]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if productionStart is not None and not isinstance(productionStart, aas.SubmodelElement):
                    productionStart = self.ProductionStart(productionStart)

                # Build a submodel element if a raw value was passed in the argument

                if productionEnd is not None and not isinstance(productionEnd, aas.SubmodelElement):
                    productionEnd = self.ProductionEnd(productionEnd)

                # Build a submodel element if a raw value was passed in the argument

                if jobName is not None and not isinstance(jobName, aas.SubmodelElement):
                    jobName = self.JobName(jobName)

                # A str would be split into its characters
                if isinstance(jobOrderNumber, str):
                    raise TypeError("jobOrderNumber takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if jobOrderNumber:
                    jobOrderNumber = [
                        i if isinstance(i, aas.SubmodelElement) else self.JobOrderNumber(i) for i in jobOrderNumber
                    ]

                # Build a submodel element if a raw value was passed in the argument

                if plannedPartsPerRun is not None and not isinstance(plannedPartsPerRun, aas.SubmodelElement):
                    plannedPartsPerRun = self.PlannedPartsPerRun(plannedPartsPerRun)

                # Build a submodel element if a raw value was passed in the argument

                if plannedOrderQuantity is not None and not isinstance(plannedOrderQuantity, aas.SubmodelElement):
                    plannedOrderQuantity = self.PlannedOrderQuantity(plannedOrderQuantity)

                # Build a submodel element if a raw value was passed in the argument

                if actualPartsInRun is not None and not isinstance(actualPartsInRun, aas.SubmodelElement):
                    actualPartsInRun = self.ActualPartsInRun(actualPartsInRun)

                # Build a submodel element if a raw value was passed in the argument

                if jobFinished is not None and not isinstance(jobFinished, aas.SubmodelElement):
                    jobFinished = self.JobFinished(jobFinished)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    productionStart,
                    productionEnd,
                    jobName,
                    jobOrderNumber,
                    plannedPartsPerRun,
                    plannedOrderQuantity,
                    actualPartsInRun,
                    jobFinished,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"ProductionCriteria",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Information on production-relevant criteria in connection with the production of a specific component",
                        r"de": r"Informationen zu produktionsrevelvanten Kriterien im Zusammenhang mit der Fertigung eines konkreten Bauteils",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/ProductionCriteria/1/0"
                ),
            }

        def __init__(
            self,
            productionJobOrderParameters: ProductionJobOrderParameters,
            technicalData: Optional[Union[aas.Reference, TechnicalData]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if technicalData is not None and not isinstance(technicalData, aas.SubmodelElement):
                technicalData = self.TechnicalData(technicalData)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(technicalData, productionJobOrderParameters)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class PartInformation(aas.SubmodelElementCollection):

        class DigitalNameplate(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"DigitalNameplate",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to the component’s Digital Nameplate submodel, including details such as serial number, product family, product type, and manufacturer.",
                            r"de": r"Referenz zum Submodel Digital Nameplate des Bauteils, mit Informationen zur Seriennummer, Produktfamilie, Produkttyp und Hersteller",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/DigitalNameplate/1/0"
                    ),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PartIdentifier(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PartIdentifier",
                    "value_type": xsd.AnyURI,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to the AAS of the component: IRDI of the management shell of the component, which is carried in the machine to assign the manufacturing data for the component",
                            r"de": r"Referenz auf die AAS des Bauteils: IRDI der Verwaltungschale des Bauteils, die in der Maschine zur Zuordnung der Fertigungsdaten für das Bauteil mitgeführt wird",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/PartIdentifier/1/0"
                    ),
                }

            def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PartNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PartNumber",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Consecutive number of the manufactured component in the batch from the CNC",
                            r"de": r"Fortlaufende Nummer des gefertigten Bauteil im Los aus der CNC",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/PartNumber/1/0"),
                    "supplemental_semantic_id": (global_ref(r"0112/2///61360_4#ADA029#001"),),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OrderNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"OrderNumber",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifier to identify the order. Shall be provided if defined in OutputInfo.",
                            r"de": r"Bezeichner zur Identifizierung der Bestellung. Wird bereitgestellt, wenn in Output Info definiert.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/OrderNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class LotNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"LotNumber",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Identifier to identify the production lot. Shall be provided if defined in OutputInfo.",
                            r"de": r"Bezeichner zur Identifizierung des Fertigungsloses. Wird bereitgestellt, wenn in Output Info definiert.",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/LotNumber/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SubmodelReference3D(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"SubmodelReference3D",
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to IDTA Submodel Provision of 3D Models",
                            r"de": r"Reference auf IDTA Submodel Provision of 3D Models",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/3DSubmodelReference/1/0"
                    ),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DrawingReference2D(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DrawingReference2D",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to a pdf-file containing the 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed. All drawings referenced in the submodel have to be included in a single PDF document.",
                            r"de": r"Referenz zum pdf-Dokument einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann. Es wird vorausgesetzt, dass alle im Submodel referenzierten Zeichnungen in einem pdf Dokument enthalten sind.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/DrawingReference2D/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CADFileReference3D(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CADFileReference3D",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Reference to a file which contains a §D CAD  model, elg. STL-file",
                            r"de": r"Referenz auf eine Datei die ein §D CAD Modell enthält, z.B. STL-file",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/CADFileReference3D/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"PartInformation",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Production information about the component",
                        r"de": r"Produktionsinformationen zu dem Bauteil",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/PartInformation/1/0"
                ),
            }

        def __init__(
            self,
            partIdentifier: Union[xsd.AnyURI, PartIdentifier],
            digitalNameplate: Optional[Union[aas.Reference, DigitalNameplate]] = None,
            partNumber: Optional[Union[int, PartNumber]] = None,
            orderNumber: Optional[Union[str, OrderNumber]] = None,
            lotNumber: Optional[Union[str, LotNumber]] = None,
            submodelReference3D: Optional[Union[aas.Reference, SubmodelReference3D]] = None,
            drawingReference2D: Optional[Union[str, DrawingReference2D]] = None,
            cADFileReference3D: Optional[Union[str, CADFileReference3D]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if digitalNameplate is not None and not isinstance(digitalNameplate, aas.SubmodelElement):
                digitalNameplate = self.DigitalNameplate(digitalNameplate)

            # Build a submodel element if a raw value was passed in the argument

            if partIdentifier is not None and not isinstance(partIdentifier, aas.SubmodelElement):
                partIdentifier = self.PartIdentifier(partIdentifier)

            # Build a submodel element if a raw value was passed in the argument

            if partNumber is not None and not isinstance(partNumber, aas.SubmodelElement):
                partNumber = self.PartNumber(partNumber)

            # Build a submodel element if a raw value was passed in the argument

            if orderNumber is not None and not isinstance(orderNumber, aas.SubmodelElement):
                orderNumber = self.OrderNumber(orderNumber)

            # Build a submodel element if a raw value was passed in the argument

            if lotNumber is not None and not isinstance(lotNumber, aas.SubmodelElement):
                lotNumber = self.LotNumber(lotNumber)

            # Build a submodel element if a raw value was passed in the argument

            if submodelReference3D is not None and not isinstance(submodelReference3D, aas.SubmodelElement):
                submodelReference3D = self.SubmodelReference3D(submodelReference3D)

            # Build a submodel element if a raw value was passed in the argument

            if drawingReference2D is not None and not isinstance(drawingReference2D, aas.SubmodelElement):
                drawingReference2D = self.DrawingReference2D(drawingReference2D)

            # Build a submodel element if a raw value was passed in the argument

            if cADFileReference3D is not None and not isinstance(cADFileReference3D, aas.SubmodelElement):
                cADFileReference3D = self.CADFileReference3D(cADFileReference3D)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                digitalNameplate,
                partIdentifier,
                partNumber,
                orderNumber,
                lotNumber,
                submodelReference3D,
                drawingReference2D,
                cADFileReference3D,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class QualityResponsibilityList(GeneratedSubmodelElementList):

        class Qualityresponsibilitylist_item(aas.SubmodelElementCollection):

            class DepartmentName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DepartmentName",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Name of the institution/testing body",
                                r"de": r"Bezeichnung der Institution/Prüfstelle",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/DepartmentName/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Role(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Role",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Role of the QS testing body (e.g. external quality testing laboratory)",
                                r"de": r"Rolle der QS-Prüfstelle (z.B. externes Qualitätsprüflabor)",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/Role/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ContactInformation(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"ContactInformation",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to the AAS submodel “Contact Information”",
                                r"de": r'Referenz auf das AAS Submodel "Contact Information"',
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/ContactInformation/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Information about an organizational unit responsible for quality assurance",
                            r"de": r"Informationen zu einer für Qualitätssicherung verantwortlichen Organisationseinheiten",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/QualityResponsibility/1/0"
                    ),
                }

            def __init__(
                self,
                departmentName: Union[str, DepartmentName],
                role: Union[str, Role],
                contactInformation: Optional[Union[aas.Reference, ContactInformation]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if departmentName is not None and not isinstance(departmentName, aas.SubmodelElement):
                    departmentName = self.DepartmentName(departmentName)

                # Build a submodel element if a raw value was passed in the argument

                if role is not None and not isinstance(role, aas.SubmodelElement):
                    role = self.Role(role)

                # Build a submodel element if a raw value was passed in the argument

                if contactInformation is not None and not isinstance(contactInformation, aas.SubmodelElement):
                    contactInformation = self.ContactInformation(contactInformation)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(departmentName, role, contactInformation)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"QualityResponsibilityList",
                "type_value_list_element": aas.SubmodelElementCollection,
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List of organizational units responsible for quality assurance",
                        r"de": r"Liste der für die Qualitätssicherung verantwortlichen Organisationseinheiten",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/QualityResponsibilityList/1/0"
                ),
            }

        def __init__(
            self,
            qualityresponsibilitylist_items: Optional[Iterable[Qualityresponsibilitylist_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(qualityresponsibilitylist_items, str):
                raise TypeError("qualityresponsibilitylist_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                qualityresponsibilitylist_items, number_repeated=False
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class TestingDevicesList(GeneratedSubmodelElementList):

        class Testingdeviceslist_item(aas.SubmodelElementCollection):

            class Responsibility(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"Responsibility",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to SMC QualityResponsibility",
                                r"de": r"Referenz auf SMC QualityResponsibility",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/Responsibility/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DigitalNameplateTestingDevice(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"DigitalNameplateTestingDevice",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to the testing device’s Digital Nameplate submodel, including details such as serial number, product family, product type, and manufacturer.",
                                r"de": r"Referenz zum Submodel Digital Nameplate des Prüfgeräts, mit Informationen zur Seriennummer, Produktfamilie, Produkttyp und Hersteller",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/DigitalNameplateTestingDevice/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class DeviceName(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"DeviceName",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Name of the test device", r"de": r"Bezeichnung des Prüfgeräts"}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/DeviceName/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuringType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MeasuringType",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Type of measurement method, e.g. according to DIN EN ISO 25178-6, DIN EN ISO 25178-601, DIN EN ISO 25178-602",
                                r"de": r"Art der Messmethode, z.B. nach DIN EN ISO 25178-6, DIN EN ISO 25178-601, DIN EN ISO 25178-602",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringType/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuringUnit(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"MeasuringUnit",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Unit in which the information on the measuring range and resolution is given",
                                r"de": r"Einheit, in der die Angaben zum Messbereich und Auflösung erfolgen",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringUnit/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class MeasuringRange(aas.Range):

                @staticmethod
                def template_defaults() -> RangeMetadata:
                    return {
                        "id_short": r"MeasuringRange",
                        "value_type": float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"range defined by two values of the measurand, or quantity to be supplied, within which the limits of uncertainty of the measuring instrument are specified",
                                r"de": r"Bereich in dem die Messabweichungen oder Messgeräteabweichungen innerhalb festgelegter Grenzen bleiben",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/MeasuringRange/1/0"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-AAN807#002"),),
                    }

                def __init__(self, min: float, max: float, **kwargs: Unpack[RangeMetadata]):

                    super().__init__(min=min, max=max, **(self.template_defaults() | kwargs))

            class Resolution(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Resolution",
                        "value_type": float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Physical resolution of the measuring instrument",
                                r"de": r"Physikalische Auflösung des Messinstruments",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/Resolution/1/0"
                        ),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Accuracy(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Accuracy",
                        "value_type": float,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Accuracy expressed as a percentage. Containing the parameters referring to percentage measuring accuracy",
                                r"de": r"Genauigkeit ausgedrückt in Prozent. Enthält die Parameter, die sich auf die prozentuale Messgenauigkeit beziehen",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/Accuracy/1/0"
                        ),
                        "supplemental_semantic_id": (global_ref(r"0173-1#02-AAQ616#009"),),
                    }

                def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Norm(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Norm",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to the relevant standard in which the measuring method is described, e.g. DIN EN ISO 25178-601",
                                r"de": r"Verweis auf entsprechende Norm in der die Messmethode beschrieben ist, z.B. DIN EN ISO 25178-601",
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/Norm/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CalibrationCertificate(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"CalibrationCertificate",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Reference to AAS Submodel Digital Quality Document",
                                r"de": r"Referenz auf AAS Submodel Digital Quality Document",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/CalibrationCertificate/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"QS relevant information about the test device",
                            r"de": r"QS relelvante Informationen über das Prüfgerät",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/TestingDeviceProperties/1/0"
                    ),
                }

            def __init__(
                self,
                deviceName: Union[str, DeviceName],
                measuringType: Union[str, MeasuringType],
                measuringUnit: Union[str, MeasuringUnit],
                measuringRange: Union[Tuple[float, float], MeasuringRange],
                responsibility: Optional[Union[aas.Reference, Responsibility]] = None,
                digitalNameplateTestingDevice: Optional[Union[aas.Reference, DigitalNameplateTestingDevice]] = None,
                resolution: Optional[Union[float, Resolution]] = None,
                accuracy: Optional[Union[float, Accuracy]] = None,
                norm: Optional[Union[str, Norm]] = None,
                calibrationCertificate: Optional[Iterable[Union[aas.Reference, CalibrationCertificate]]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if responsibility is not None and not isinstance(responsibility, aas.SubmodelElement):
                    responsibility = self.Responsibility(responsibility)

                # Build a submodel element if a raw value was passed in the argument

                if digitalNameplateTestingDevice is not None and not isinstance(
                    digitalNameplateTestingDevice, aas.SubmodelElement
                ):
                    digitalNameplateTestingDevice = self.DigitalNameplateTestingDevice(digitalNameplateTestingDevice)

                # Build a submodel element if a raw value was passed in the argument

                if deviceName is not None and not isinstance(deviceName, aas.SubmodelElement):
                    deviceName = self.DeviceName(deviceName)

                # Build a submodel element if a raw value was passed in the argument

                if measuringType is not None and not isinstance(measuringType, aas.SubmodelElement):
                    measuringType = self.MeasuringType(measuringType)

                # Build a submodel element if a raw value was passed in the argument

                if measuringUnit is not None and not isinstance(measuringUnit, aas.SubmodelElement):
                    measuringUnit = self.MeasuringUnit(measuringUnit)

                # Build a submodel element if a raw value was passed in the argument

                if measuringRange is not None and not isinstance(measuringRange, aas.SubmodelElement):
                    measuringRange = self.MeasuringRange(min=measuringRange[0], max=measuringRange[1])

                # Build a submodel element if a raw value was passed in the argument

                if resolution is not None and not isinstance(resolution, aas.SubmodelElement):
                    resolution = self.Resolution(resolution)

                # Build a submodel element if a raw value was passed in the argument

                if accuracy is not None and not isinstance(accuracy, aas.SubmodelElement):
                    accuracy = self.Accuracy(accuracy)

                # Build a submodel element if a raw value was passed in the argument

                if norm is not None and not isinstance(norm, aas.SubmodelElement):
                    norm = self.Norm(norm)

                # A str would be split into its characters
                if isinstance(calibrationCertificate, str):
                    raise TypeError("calibrationCertificate takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if calibrationCertificate:
                    calibrationCertificate = [
                        i if isinstance(i, aas.SubmodelElement) else self.CalibrationCertificate(i)
                        for i in calibrationCertificate
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    responsibility,
                    digitalNameplateTestingDevice,
                    deviceName,
                    measuringType,
                    measuringUnit,
                    measuringRange,
                    resolution,
                    accuracy,
                    norm,
                    calibrationCertificate,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"TestingDevicesList",
                "type_value_list_element": aas.SubmodelElementCollection,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"List of testing devices used", r"de": r"Liste der verwendeten Prüfgeräte"}
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/TestingDevicesList/1/0"
                ),
            }

        def __init__(
            self,
            testingdeviceslist_items: Iterable[Testingdeviceslist_item],
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(testingdeviceslist_items, str):
                raise TypeError("testingdeviceslist_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(testingdeviceslist_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class MetrologyJobResults(aas.SubmodelElementCollection):

        class JobStart(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"JobStart",
                    "value_type": xsd.DateTime,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Date time of job start", r"de": r"Datum und Zeit des Starts des Auftrags"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/JobStart/1/0"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class JobEnd(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"JobEnd",
                    "value_type": xsd.DateTime,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Date time of job end", r"de": r"Datum und Zeit des Endes des Auftrags"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/JobEnd/1/0"),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class JobName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"JobName",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Human readable name of the job. Array shall always contain the same text, potentially in different languages.",
                            r"de": r"Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.",
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class JobOrderNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"JobOrderNumber",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.",
                            r"de": r"Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0"
                    ),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class PlannedPartsPerRun(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"PlannedPartsPerRun",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The number of parts planned to be measured by one run",
                            r"de": r"Die Anzahl der Teile, die in einem Lauf gemessen werden sollen",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0"
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ActualPartsInRun(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ActualPartsInRun",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"The number of parts actually measuerd by one run",
                            r"de": r"Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0"
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class JobFinished(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"JobFinished",
                    "value_type": bool,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Status order completed. True: yes, false: no",
                            r"de": r"Status Auftrag beendet. True: ja, false: nein",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0"
                    ),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MetrologyResultsList(GeneratedSubmodelElementList):

            class Metrologyresultslist_item(aas.SubmodelElementCollection):

                class QualityFeatureReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"QualityFeatureReference",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to QualityFeature in SMC QualityFeaturesList",
                                    r"de": r"Referenz auf QualityFeature in SMC QualityFeaturesList",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/QualityFeatureReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class TestingDeviceReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"TestingDeviceReference",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to the test device used in SMC TestingDeviceList",
                                    r"de": r"Referenz auf das verwendete Prüfgerät in SMC TestingDeviceList",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/TestingDeviceReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PartReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"PartReference",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Reference to the AAS of the component if the SMC MetrologyData is not within this AAS",
                                    r"de": r"Referenz auf die AAS des Bauteils, falls sich die SMC MetrologyData nicht innerhalb dieser AAS befindet",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/PartReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ID(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ID",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Name or ID of the quality feature",
                                    r"de": r"Name oder ID des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/QualityControlForMachining/ID/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Description(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Description",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Description of the quality feature",
                                    r"de": r"Beschreibung des Qualitätsmerkmals",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Description/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EngineeringUnit(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EngineeringUnit",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Physical unit of feature", r"de": r"Physikalische Einheit des Merkmals"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/EngineeringUnit/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QualityActualValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QualityActualValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Value or values (with several repeated measurements) for the specific quality feature of the component",
                                    r"de": r"Wert oder Werte (bei mehreren Wiederholungsmessungen) für das bestimmte Qualitätsmerkmal des Bauteils",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/QualityActualValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QualityActualAttribute(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QualityActualAttribute",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"For attributive characteristics: attribute or attributes in the case of several repeat determinations) for the specific quality characteristic of the component",
                                    r"de": r"Bei attributiven Qualitätsmerkmalen: Attribut oder Attibute bei mehreren Wiederholungsbestimmungen für das bestimmte Qualitätsmerkmal des Bauteils",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/QualityActualAttribute/1/0"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class QualityInSpec(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"QualityInSpec",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Indication whether the feature is within the tolerance, i.e. OK.",
                                    r"de": r"Angabe, ob das Merkmal innerhalb der Toleranz liegt, also i.O. ist.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/QualityInSpec/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Deviation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Deviation",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Deviation from nominal value", r"de": r"Abweichung vom Sollwert"}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Deviation/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AverageValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AverageValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Average value, if several values ​​are measured when determining the characteristic",
                                    r"de": r"Arithmetischer Mittelwert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/AverageValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MinValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MinValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Minimum value if several values ​​are measured when determining the characteristic",
                                    r"de": r"Minimaler Wert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MinValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MaxValue(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"MaxValue",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Maximum value if several values ​​are measured when determining the characteristic",
                                    r"de": r"Maximaler Wert, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MaxValue/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class Standarddeviation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"Standarddeviation",
                            "value_type": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Standarddeviation of measuring results if several values ​​are measured when determining the characteristic",
                                    r"de": r"Standardabweichung der Messergebnisse, wenn bei Bestimmung des Merkmals mehrere Werte gemessen werden",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/Standarddeviation/1/0"
                            ),
                        }

                    def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DataAggregatedFromSeries(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DataAggregatedFromSeries",
                            "value_type": bool,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Boolean variable which indicates that the measured quality data is provided as aggregated value for a series of parts (e.g. as an average value for a lot or batch). Has to be set on false, if the measuring data is provided part specific.",
                                    r"de": r"Boolesche Variable, die angibt, dass die gemessenen Qualitätsdaten als aggregierter Wert, z.B. als Mittelwert für eine Reihe von Teilen (z. B. Los oder Charge) bereitgestellt werden. Muss auf false gesetzt werden, wenn die Messdaten teilespezifisch bereitgestellt werden.",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/DataAggregatedFromSeries/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class MeasuredValuesList(GeneratedSubmodelElementList):

                    class Measuredvalueslist_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": float,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Measured value", r"de": r"Gemessener Wert"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/MeasuredValue/1/0"
                                ),
                            }

                        def __init__(self, value: float, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"MeasuredValuesList",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": float,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Optional list of measured values",
                                    r"de": r"Optionale Liste gemessener Werte",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MeasuredValuesList/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        measuredvalueslist_items: Optional[Iterable[Union[float, Measuredvalueslist_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(measuredvalueslist_items, str):
                            raise TypeError("measuredvalueslist_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if measuredvalueslist_items:
                            measuredvalueslist_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Measuredvalueslist_item(i)
                                for i in measuredvalueslist_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            measuredvalueslist_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                class MetrologyDataFile(aas.SubmodelElementCollection):

                    class FileLink(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"FileLink",
                                "value_type": xsd.AnyURI,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Link to the file", r"de": r"Link zu der Datei"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/File/1/0"
                                ),
                                "supplemental_semantic_id": (global_ref(r"0173-1#02-ABK126#001"),),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class MimeType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"MimeType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"MIME type of the file", r"de": r"MIME-typ der Datei"}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/QualityControlForMachining/MimeType/1/0"
                                ),
                                "supplemental_semantic_id": (global_ref(r"0112/2///61360_4#ACB113#001"),),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"MetrologyDataFile",
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Optional measurement data file with the original measurement protocol",
                                    r"de": r"Optionale Messdatendatei mit dem original Messprotokoll",
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyDataFile/1/0"
                            ),
                        }

                    def __init__(
                        self,
                        fileLink: Optional[Union[xsd.AnyURI, FileLink]] = None,
                        mimeType: Optional[Union[str, MimeType]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if fileLink is not None and not isinstance(fileLink, aas.SubmodelElement):
                            fileLink = self.FileLink(fileLink)

                        # Build a submodel element if a raw value was passed in the argument

                        if mimeType is not None and not isinstance(mimeType, aas.SubmodelElement):
                            mimeType = self.MimeType(mimeType)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(fileLink, mimeType)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Measurement results a quality feature",
                                r"de": r"Messergebnisse einem Qualitätsmerkmal",
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyData/1/0"
                        ),
                    }

                def __init__(
                    self,
                    qualityFeatureReference: Union[aas.Reference, QualityFeatureReference],
                    testingDeviceReference: Union[aas.Reference, TestingDeviceReference],
                    partReference: Union[aas.Reference, PartReference],
                    qualityInSpec: Union[bool, QualityInSpec],
                    dataAggregatedFromSeries: Union[bool, DataAggregatedFromSeries],
                    iD: Optional[Union[str, ID]] = None,
                    description_: Optional[Union[str, Description]] = None,
                    engineeringUnit: Optional[Union[str, EngineeringUnit]] = None,
                    qualityActualValue: Optional[Iterable[Union[float, QualityActualValue]]] = None,
                    qualityActualAttribute: Optional[Iterable[Union[str, QualityActualAttribute]]] = None,
                    deviation: Optional[Union[float, Deviation]] = None,
                    averageValue: Optional[Union[float, AverageValue]] = None,
                    minValue: Optional[Union[float, MinValue]] = None,
                    maxValue: Optional[Union[float, MaxValue]] = None,
                    standarddeviation: Optional[Union[float, Standarddeviation]] = None,
                    measuredValuesList: Optional[
                        Union[Iterable[Union[float, MeasuredValuesList.Measuredvalueslist_item]], MeasuredValuesList]
                    ] = None,
                    metrologyDataFile: Optional[MetrologyDataFile] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if qualityFeatureReference is not None and not isinstance(
                        qualityFeatureReference, aas.SubmodelElement
                    ):
                        qualityFeatureReference = self.QualityFeatureReference(qualityFeatureReference)

                    # Build a submodel element if a raw value was passed in the argument

                    if testingDeviceReference is not None and not isinstance(
                        testingDeviceReference, aas.SubmodelElement
                    ):
                        testingDeviceReference = self.TestingDeviceReference(testingDeviceReference)

                    # Build a submodel element if a raw value was passed in the argument

                    if partReference is not None and not isinstance(partReference, aas.SubmodelElement):
                        partReference = self.PartReference(partReference)

                    # Build a submodel element if a raw value was passed in the argument

                    if iD is not None and not isinstance(iD, aas.SubmodelElement):
                        iD = self.ID(iD)

                    # Build a submodel element if a raw value was passed in the argument

                    if description_ is not None and not isinstance(description_, aas.SubmodelElement):
                        description_ = self.Description(description_)

                    # Build a submodel element if a raw value was passed in the argument

                    if engineeringUnit is not None and not isinstance(engineeringUnit, aas.SubmodelElement):
                        engineeringUnit = self.EngineeringUnit(engineeringUnit)

                    # A str would be split into its characters
                    if isinstance(qualityActualValue, str):
                        raise TypeError("qualityActualValue takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if qualityActualValue:
                        qualityActualValue = [
                            i if isinstance(i, aas.SubmodelElement) else self.QualityActualValue(i)
                            for i in qualityActualValue
                        ]

                    # A str would be split into its characters
                    if isinstance(qualityActualAttribute, str):
                        raise TypeError("qualityActualAttribute takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if qualityActualAttribute:
                        qualityActualAttribute = [
                            i if isinstance(i, aas.SubmodelElement) else self.QualityActualAttribute(i)
                            for i in qualityActualAttribute
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if qualityInSpec is not None and not isinstance(qualityInSpec, aas.SubmodelElement):
                        qualityInSpec = self.QualityInSpec(qualityInSpec)

                    # Build a submodel element if a raw value was passed in the argument

                    if deviation is not None and not isinstance(deviation, aas.SubmodelElement):
                        deviation = self.Deviation(deviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if averageValue is not None and not isinstance(averageValue, aas.SubmodelElement):
                        averageValue = self.AverageValue(averageValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if minValue is not None and not isinstance(minValue, aas.SubmodelElement):
                        minValue = self.MinValue(minValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if maxValue is not None and not isinstance(maxValue, aas.SubmodelElement):
                        maxValue = self.MaxValue(maxValue)

                    # Build a submodel element if a raw value was passed in the argument

                    if standarddeviation is not None and not isinstance(standarddeviation, aas.SubmodelElement):
                        standarddeviation = self.Standarddeviation(standarddeviation)

                    # Build a submodel element if a raw value was passed in the argument

                    if dataAggregatedFromSeries is not None and not isinstance(
                        dataAggregatedFromSeries, aas.SubmodelElement
                    ):
                        dataAggregatedFromSeries = self.DataAggregatedFromSeries(dataAggregatedFromSeries)

                    # A str would be split into its characters
                    if isinstance(measuredValuesList, str):
                        raise TypeError("measuredValuesList takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if measuredValuesList is not None and not isinstance(measuredValuesList, aas.SubmodelElement):
                        measuredValuesList = self.MeasuredValuesList(measuredValuesList)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        qualityFeatureReference,
                        testingDeviceReference,
                        partReference,
                        iD,
                        description_,
                        engineeringUnit,
                        qualityActualValue,
                        qualityActualAttribute,
                        qualityInSpec,
                        deviation,
                        averageValue,
                        minValue,
                        maxValue,
                        standarddeviation,
                        dataAggregatedFromSeries,
                        measuredValuesList,
                        metrologyDataFile,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"MetrologyResultsList",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"List of measurement results for the quality characteristics",
                            r"de": r"Liste der Messergebnisse zu den Qualitätsmerkmalen",
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyResultsList/1/0"
                    ),
                }

            def __init__(
                self,
                metrologyresultslist_items: Iterable[Metrologyresultslist_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(metrologyresultslist_items, str):
                    raise TypeError("metrologyresultslist_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    metrologyresultslist_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"MetrologyJobResults",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Information and measurements on the results of a quality assessment order",
                        r"de": r"Informationen und Messwerte zu Ergebnissen eines Qualitätsbewertungsauftrag",
                    }
                ),
                "semantic_id": global_ref(
                    r"https://admin-shell.io/idta/QualityControlForMachining/MetrologyJobResults/1/0"
                ),
            }

        def __init__(
            self,
            jobStart: Union[xsd.DateTime, JobStart],
            jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
            metrologyResultsList: Union[Iterable[MetrologyResultsList.Metrologyresultslist_item], MetrologyResultsList],
            jobEnd: Optional[Union[xsd.DateTime, JobEnd]] = None,
            jobName: Optional[Union[str, JobName]] = None,
            plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
            actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
            jobFinished: Optional[Union[bool, JobFinished]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if jobStart is not None and not isinstance(jobStart, aas.SubmodelElement):
                jobStart = self.JobStart(jobStart)

            # Build a submodel element if a raw value was passed in the argument

            if jobEnd is not None and not isinstance(jobEnd, aas.SubmodelElement):
                jobEnd = self.JobEnd(jobEnd)

            # Build a submodel element if a raw value was passed in the argument

            if jobName is not None and not isinstance(jobName, aas.SubmodelElement):
                jobName = self.JobName(jobName)

            # A str would be split into its characters
            if isinstance(jobOrderNumber, str):
                raise TypeError("jobOrderNumber takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if jobOrderNumber:
                jobOrderNumber = [
                    i if isinstance(i, aas.SubmodelElement) else self.JobOrderNumber(i) for i in jobOrderNumber
                ]

            # Build a submodel element if a raw value was passed in the argument

            if plannedPartsPerRun is not None and not isinstance(plannedPartsPerRun, aas.SubmodelElement):
                plannedPartsPerRun = self.PlannedPartsPerRun(plannedPartsPerRun)

            # Build a submodel element if a raw value was passed in the argument

            if actualPartsInRun is not None and not isinstance(actualPartsInRun, aas.SubmodelElement):
                actualPartsInRun = self.ActualPartsInRun(actualPartsInRun)

            # Build a submodel element if a raw value was passed in the argument

            if jobFinished is not None and not isinstance(jobFinished, aas.SubmodelElement):
                jobFinished = self.JobFinished(jobFinished)

            # A str would be split into its characters
            if isinstance(metrologyResultsList, str):
                raise TypeError("metrologyResultsList takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if metrologyResultsList is not None and not isinstance(metrologyResultsList, aas.SubmodelElement):
                metrologyResultsList = self.MetrologyResultsList(metrologyResultsList)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                jobStart,
                jobEnd,
                jobName,
                jobOrderNumber,
                plannedPartsPerRun,
                actualPartsInRun,
                jobFinished,
                metrologyResultsList,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"QualityControlForMachining",
            "description": aas.MultiLanguageTextType(
                dict_={
                    r"en": r"The Submodel Quality Control for Machining allows the collection of quality relevant information about parts produced in cyclical manufacturing processes. The focus is on looking at the production result and on machining manufacturing processes of milling, turning and drilling. However, the Submodel can also be used for other manufacturing processes.",
                    r"de": r"Das Teilmodell Quality Control for Machining erlaubt die Erfassung von qualitätsrelevanten Informationen über in zyklischen Fertigungsprozessen produzierte Bauteile. Der Fokus liegt auf der Betrachtung des Produktionsresultats und auf den zerspanenden Fertigungsverfahren Fräsen, Drehen, Bohren. Das Teilmodell kann jedoch auch für andere Fertigungsverfahren verwendet werden.",
                }
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02049",
                embedded_data_specifications=[],
            ),
        }

    def __init__(
        self,
        id_: str,
        qualityFeatures: QualityFeatures,
        partInformation: PartInformation,
        testingDevicesList: Union[Iterable[TestingDevicesList.Testingdeviceslist_item], TestingDevicesList],
        metrologyJobResults: Iterable[MetrologyJobResults],
        productionCriteria: Optional[ProductionCriteria] = None,
        qualityResponsibilityList: Optional[
            Union[Iterable[QualityResponsibilityList.Qualityresponsibilitylist_item], QualityResponsibilityList]
        ] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(qualityResponsibilityList, str):
            raise TypeError("qualityResponsibilityList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if qualityResponsibilityList is not None and not isinstance(qualityResponsibilityList, aas.SubmodelElement):
            qualityResponsibilityList = self.QualityResponsibilityList(qualityResponsibilityList)

        # A str would be split into its characters
        if isinstance(testingDevicesList, str):
            raise TypeError("testingDevicesList takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if testingDevicesList is not None and not isinstance(testingDevicesList, aas.SubmodelElement):
            testingDevicesList = self.TestingDevicesList(testingDevicesList)

        # A str would be split into its characters
        if isinstance(metrologyJobResults, str):
            raise TypeError("metrologyJobResults takes several elements, got a str")

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            qualityFeatures,
            productionCriteria,
            partInformation,
            qualityResponsibilityList,
            testingDevicesList,
            metrologyJobResults,
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
