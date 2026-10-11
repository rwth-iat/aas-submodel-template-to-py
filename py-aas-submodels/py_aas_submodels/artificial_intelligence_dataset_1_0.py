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


class AIDataset(aas.Submodel):

    class URIOfTheProduct(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"URIOfTheProduct",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"PARAMETER",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0112/2///61987#ABN590#002 "),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"de": r"eindeutige globale Identifizierung der Produktinstanz unter Verwendung eines universellen Ressourcenbezeichners (URI)",
                        r"en": r"unique global identification of the product instance using an universal resource identifier (URI)",
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

    class Version(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"Version",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"PARAMETER",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"0173-1#02-AAS354#002"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"de": r"Version des Datensatzes", r"en": r"Version of the dataset"}
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

    class ContactInformation(aas.ReferenceElement):

        def __init__(
            self,
            value: aas.Reference,
            id_short: Optional[str] = r"ContactInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"PARAMETER",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AIDataset/ContactInformation/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Refernce to the Contact Information IDTA Submodel to describe the responsible person for the Submodel"
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            super().__init__(
                value=value,
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

    class Storage(aas.Property):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"Storage",
            value_type: aas.DataTypeDefXsd = str,
            value_id: Optional[aas.Reference] = None,
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"PARAMETER",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/AIDataset/Storage/1/0"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Path to the dataset (e.g. local path, serverpath,...)"}
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

    class Labeled(aas.SubmodelElementCollection):

        class Classification(aas.SubmodelElementCollection):

            class NumberLables(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"NumberLables",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/NumberLabels/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Number of the different labels in the dataset"}
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

            class Labels(aas.SubmodelElementCollection):

                class ExampleLabel(aas.SubmodelElementCollection):

                    class ClassName(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"ClassName",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/ClassName/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(dict_={r"en": r"Name of the class"})

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

                    class NumberOfSamples(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"NumberOfSamples",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/NumberOfSamples/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Number of occurrences of the label in the dataset"}
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
                        className: Union[str, ClassName],
                        numberOfSamples: Optional[Union[str, NumberOfSamples]] = None,
                        id_short: Optional[str] = r"ExampleLabel",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = r"PARAMETER",
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/Label/1/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Additional information about one label"}
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if className is not None and not isinstance(className, aas.SubmodelElement):
                            className = self.ClassName(className)

                        # Build a submodel element if a raw value was passed in the argument

                        if numberOfSamples is not None and not isinstance(numberOfSamples, aas.SubmodelElement):
                            numberOfSamples = self.NumberOfSamples(numberOfSamples)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(className, numberOfSamples)

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
                    exampleLabel: Iterable[ExampleLabel],
                    id_short: Optional[str] = r"Labels",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Labels/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Every label as a property and the number of samples"}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(exampleLabel, str):
                        raise TypeError("exampleLabel takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleLabel)

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

            class SingleFiles(aas.SubmodelElementCollection):

                class ExampleSingleFile(aas.SubmodelElementCollection):

                    class Name(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"Name",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Name/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(dict_={r"en": r"Name of the file"})

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

                    class Labels(aas.SubmodelElementCollection):

                        class NumberLabels(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"NumberLabels",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/NumberLabels/1/0"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={r"en": r"Number of labels in this dataset element"}
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

                        class Label(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"Label",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/Label/1/0"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"Example label, this property should be existing for every label with the labelname as value"
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
                            numberLabels: Union[str, NumberLabels],
                            label: Optional[Iterable[Union[str, Label]]] = None,
                            id_short: Optional[str] = r"Labels",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/Labels/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Collection containing all the labels within the dataset element"}
                                )

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if numberLabels is not None and not isinstance(numberLabels, aas.SubmodelElement):
                                numberLabels = self.NumberLabels(numberLabels)

                            # A str would be split into its characters
                            if isinstance(label, str):
                                raise TypeError("label takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if label:
                                label = [i if isinstance(i, aas.SubmodelElement) else self.Label(i) for i in label]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(numberLabels, label)

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

                    class SingleFilePath(aas.Property):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"SingleFilePath",
                            value_type: aas.DataTypeDefXsd = str,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFilePath/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(dict_={r"en": r"Path to the dataset element"})

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

                    class AnnotationFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"AnnotationFile",
                            content_type: Optional[str] = r"application/json",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/AnnotationFile/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Annotation file with labeling information about the dataset element"
                                    }
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

                    class SingleFileDetails(aas.SubmodelElementCollection):

                        class ExampleSingleFileDetail(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ExampleSingleFileDetail",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFileDetails/SingleFileDetail/1/0"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={r"en": r"additional information about the dataset element"}
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
                            exampleSingleFileDetail: Union[str, ExampleSingleFileDetail],
                            id_short: Optional[str] = r"SingleFileDetails",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/SingleFileDetails/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Collection to add addtional information about the dataset element (e.g. speaker information for audio data)"
                                    }
                                )

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # Build a submodel element if a raw value was passed in the argument

                            if exampleSingleFileDetail is not None and not isinstance(
                                exampleSingleFileDetail, aas.SubmodelElement
                            ):
                                exampleSingleFileDetail = self.ExampleSingleFileDetail(exampleSingleFileDetail)

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(exampleSingleFileDetail)

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
                        name: Union[str, Name],
                        labels: Labels,
                        singleFilePath: Union[str, SingleFilePath],
                        annotationFile: Optional[AnnotationFile] = None,
                        singleFileDetails: Optional[SingleFileDetails] = None,
                        id_short: Optional[str] = r"ExampleSingleFile",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/SingleFile/1/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Collection for features and the annotatin file for a single dataset element"
                                }
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if name is not None and not isinstance(name, aas.SubmodelElement):
                            name = self.Name(name)

                        # Build a submodel element if a raw value was passed in the argument

                        if singleFilePath is not None and not isinstance(singleFilePath, aas.SubmodelElement):
                            singleFilePath = self.SingleFilePath(singleFilePath)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            name, labels, singleFilePath, annotationFile, singleFileDetails
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
                    exampleSingleFile: Iterable[ExampleSingleFile],
                    id_short: Optional[str] = r"SingleFiles",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/SingleFiles/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection containing every dataset element individuallly"}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(exampleSingleFile, str):
                        raise TypeError("exampleSingleFile takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleSingleFile)

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

            class Balance(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"Balance",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/Balance/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"Balance between the classes"})

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

            class AnnotationFile(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AnnotationFile",
                    content_type: Optional[str] = r"application/json",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Classification/AnnotationFile/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Annotation file of the dataset (e.g. CSV,JSON,Path...)"}
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
                numberLables: Union[str, NumberLables],
                labels: Optional[Labels] = None,
                singleFiles: Optional[SingleFiles] = None,
                balance: Optional[Union[str, Balance]] = None,
                annotationFile: Optional[AnnotationFile] = None,
                id_short: Optional[str] = r"Classification",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/Labeled/Classification/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about labeled data for classification"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if numberLables is not None and not isinstance(numberLables, aas.SubmodelElement):
                    numberLables = self.NumberLables(numberLables)

                # Build a submodel element if a raw value was passed in the argument

                if balance is not None and not isinstance(balance, aas.SubmodelElement):
                    balance = self.Balance(balance)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    numberLables, labels, singleFiles, balance, annotationFile
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

        class Regression(aas.SubmodelElementCollection):

            class Labeledescription(aas.MultiLanguageProperty):

                def __init__(
                    self,
                    value: aas.LangStringSet,
                    id_short: Optional[str] = r"labeledescription",
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Regression/labeledescription/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"The meaning of the label"})

                    if qualifier is None:
                        qualifier = ()

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

            class AnnotationFile(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"AnnotationFile",
                    content_type: Optional[str] = r"text/plain",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Regression/AnnotationFile/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"Annotation file of the labeled data"})

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

            class SingleFiles(aas.SubmodelElementCollection):

                class ExampleAnnotation(aas.SubmodelElementCollection):

                    class AnnotationFile(aas.File):

                        def __init__(
                            self,
                            value: str,
                            id_short: Optional[str] = r"AnnotationFile",
                            content_type: Optional[str] = r"text/plain",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = r"PARAMETER",
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/AnnotationFile/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Annotation file with labeling information about the dataset element"
                                    }
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

                    class SingleFileDetails(aas.SubmodelElementCollection):

                        class ExampleDetails(aas.Property):

                            def __init__(
                                self,
                                value: str,
                                id_short: Optional[str] = r"ExampleDetails",
                                value_type: aas.DataTypeDefXsd = str,
                                value_id: Optional[aas.Reference] = None,
                                display_name: Optional[aas.MultiLanguageNameType] = None,
                                category: Optional[str] = r"PARAMETER",
                                description: Optional[aas.MultiLanguageTextType] = None,
                                semantic_id: Optional[aas.Reference] = global_ref(
                                    r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/SingleFileDetails/Detail/1/0"
                                ),
                                qualifier: Iterable[aas.Qualifier] = None,
                                extension: Iterable[aas.Extension] = (),
                                supplemental_semantic_id: Iterable[aas.Reference] = (),
                                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                            ):

                                if description is None:
                                    description = aas.MultiLanguageTextType(
                                        dict_={
                                            r"en": r"This is a property for a specific metainformation for single regressionfiles"
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
                            exampleDetails: Optional[Iterable[Union[str, ExampleDetails]]] = None,
                            id_short: Optional[str] = r"SingleFileDetails",
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[aas.Reference] = global_ref(
                                r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/SingleFileDetails/1/0"
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (),
                            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                        ):

                            if description is None:
                                description = aas.MultiLanguageTextType(
                                    dict_={r"en": r"Collection to add addtional information about the dataset element"}
                                )

                            if qualifier is None:
                                qualifier = ()

                            if embedded_data_specifications is None:
                                embedded_data_specifications = []

                            # A str would be split into its characters
                            if isinstance(exampleDetails, str):
                                raise TypeError("exampleDetails takes several elements, got a str")

                            # Build submodel elements from raw values passed in the argument
                            if exampleDetails:
                                exampleDetails = [
                                    i if isinstance(i, aas.SubmodelElement) else self.ExampleDetails(i)
                                    for i in exampleDetails
                                ]

                            # Add all passed/initialized submodel elements to a single list

                            embedded_submodel_elements = collect_submodel_elements(exampleDetails)

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
                        annotationFile: Optional[AnnotationFile] = None,
                        singleFileDetails: Optional[SingleFileDetails] = None,
                        id_short: Optional[str] = r"ExampleAnnotation",
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[aas.MultiLanguageTextType] = None,
                        semantic_id: Optional[aas.Reference] = global_ref(
                            r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/Annotation/1/0"
                        ),
                        qualifier: Iterable[aas.Qualifier] = None,
                        extension: Iterable[aas.Extension] = (),
                        supplemental_semantic_id: Iterable[aas.Reference] = (),
                        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                    ):

                        if description is None:
                            description = aas.MultiLanguageTextType(
                                dict_={r"en": r"Collection for a single annotation of a dataset element"}
                            )

                        if qualifier is None:
                            qualifier = ()

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(annotationFile, singleFileDetails)

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
                    exampleAnnotation: Iterable[ExampleAnnotation],
                    id_short: Optional[str] = r"SingleFiles",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/labeled/Regression/SingleFiles/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(
                            dict_={r"en": r"Collection containing every dataset element individually"}
                        )

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(exampleAnnotation, str):
                        raise TypeError("exampleAnnotation takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(exampleAnnotation)

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
                labeledescription: Union[aas.LangStringSet, Labeledescription],
                annotationFile: Optional[AnnotationFile] = None,
                singleFiles: Optional[SingleFiles] = None,
                id_short: Optional[str] = r"Regression",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/Labeled/Regression/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about labeled data for regression"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if labeledescription is not None and not isinstance(labeledescription, aas.SubmodelElement):
                    labeledescription = self.Labeledescription(labeledescription)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(labeledescription, annotationFile, singleFiles)

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
            classification: Optional[Iterable[Classification]] = None,
            regression: Optional[Iterable[Regression]] = None,
            id_short: Optional[str] = r"Labeled",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/AIDataset/labeled/1/0"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Additional Information typical for labeled datasets"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(classification, str):
                raise TypeError("classification takes several elements, got a str")

            # A str would be split into its characters
            if isinstance(regression, str):
                raise TypeError("regression takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(classification, regression)

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

    class SizeInformation(aas.SubmodelElementCollection):

        class CompleteSize(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CompleteSize",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset//SizeInformation/CompleteSize/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"Number of all samples in the dataset"})

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

        class TrainSize(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TrainSize",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/SizeInformation/TrainSize/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the training subset"}
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

        class ValSize(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ValSize",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/SizeInformationValSize/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the validation subset"}
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

        class TestSize(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TestSize",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"VARIABLE",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/SizeInformation/TestSize/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Number of all dataset elements in the test subset"}
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

        class SplitRatio(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"SplitRatio",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/SizeInformation/SplitRatio/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Splitratio between the sets, notate as value1:value2:value3 if all three exist, else value1:value2"
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
            completeSize: Union[str, CompleteSize],
            trainSize: Optional[Union[str, TrainSize]] = None,
            valSize: Optional[Union[str, ValSize]] = None,
            testSize: Optional[Union[str, TestSize]] = None,
            splitRatio: Optional[Union[str, SplitRatio]] = None,
            id_short: Optional[str] = r"SizeInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AIDataset/SizeInformation/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection about the number of dataset elements in the dataset and subsets"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if completeSize is not None and not isinstance(completeSize, aas.SubmodelElement):
                completeSize = self.CompleteSize(completeSize)

            # Build a submodel element if a raw value was passed in the argument

            if trainSize is not None and not isinstance(trainSize, aas.SubmodelElement):
                trainSize = self.TrainSize(trainSize)

            # Build a submodel element if a raw value was passed in the argument

            if valSize is not None and not isinstance(valSize, aas.SubmodelElement):
                valSize = self.ValSize(valSize)

            # Build a submodel element if a raw value was passed in the argument

            if testSize is not None and not isinstance(testSize, aas.SubmodelElement):
                testSize = self.TestSize(testSize)

            # Build a submodel element if a raw value was passed in the argument

            if splitRatio is not None and not isinstance(splitRatio, aas.SubmodelElement):
                splitRatio = self.SplitRatio(splitRatio)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                completeSize, trainSize, valSize, testSize, splitRatio
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

    class MetaData(aas.SubmodelElementCollection):

        class FileType(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"FileType",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"CONSTANT",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/MetaData/FileType/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Data type of the dataset elements (e.g. .WAV, .JPEG, ... )"}
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

        class AdditionalInformation(aas.SubmodelElementCollection):

            class ExampleInfo(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ExampleInfo",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/MetaData/AdditionalInformation/Info/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"Meta data information of the dataset"})

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
                exampleInfo: Iterable[Union[str, ExampleInfo]],
                id_short: Optional[str] = r"AdditionalInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/MetaData/AdditionalInformation/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection of additional meta information of the dataset"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(exampleInfo, str):
                    raise TypeError("exampleInfo takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if exampleInfo:
                    exampleInfo = [
                        i if isinstance(i, aas.SubmodelElement) else self.ExampleInfo(i) for i in exampleInfo
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(exampleInfo)

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
            fileType: Iterable[Union[str, FileType]],
            additionalInformation: Optional[AdditionalInformation] = None,
            id_short: Optional[str] = r"MetaData",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = r"CONSTANT",
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/AIDataset/MetaData/1/0"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Collection of meta data information about the dataset"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # A str would be split into its characters
            if isinstance(fileType, str):
                raise TypeError("fileType takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if fileType:
                fileType = [i if isinstance(i, aas.SubmodelElement) else self.FileType(i) for i in fileType]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(fileType, additionalInformation)

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

    class Metrics(aas.SubmodelElementCollection):

        class ExampleMetric(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ExampleMetric",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/MetaData/Metrics/Metric/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(dict_={r"en": r"metric of the dataset"})

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
            exampleMetric: Optional[Union[str, ExampleMetric]] = None,
            id_short: Optional[str] = r"Metrics",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(r"https://admin-shell.io/idta/AIDataset/Metrics/1/0"),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(dict_={r"en": r"Collection of different metrics"})

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if exampleMetric is not None and not isinstance(exampleMetric, aas.SubmodelElement):
                exampleMetric = self.ExampleMetric(exampleMetric)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(exampleMetric)

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

    class BoundaryConditions(aas.SubmodelElementCollection):

        class DataCollectors(aas.SubmodelElementCollection):

            class Collector(aas.ReferenceElement):

                def __init__(
                    self,
                    value: aas.Reference,
                    id_short: Optional[str] = r"Collector",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/DataCollectors/CollectorDescription/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"Reference to the data collector"})

                    if qualifier is None:
                        qualifier = ()

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    super().__init__(
                        value=value,
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
                collector: Optional[Iterable[Union[aas.Reference, Collector]]] = None,
                id_short: Optional[str] = r"DataCollectors",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/DataCollectors/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Information about the datacollector (e.g. a sensor)."}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(collector, str):
                    raise TypeError("collector takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if collector:
                    collector = [i if isinstance(i, aas.SubmodelElement) else self.Collector(i) for i in collector]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(collector)

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

        class EnviromentConditions(aas.SubmodelElementCollection):

            class ExampleCondition(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"ExampleCondition",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = global_ref(
                        r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/EnviromentConditions/Condition/1/0"
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (),
                    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
                ):

                    if description is None:
                        description = aas.MultiLanguageTextType(dict_={r"en": r"Condition about the enviroment"})

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
                exampleCondition: Optional[Union[str, ExampleCondition]] = None,
                id_short: Optional[str] = r"EnviromentConditions",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/EnviromentConditions/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Collection about environmental conditions the dataset was created with"}
                    )

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if exampleCondition is not None and not isinstance(exampleCondition, aas.SubmodelElement):
                    exampleCondition = self.ExampleCondition(exampleCondition)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(exampleCondition)

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

        class SyntheticData(aas.MultiLanguageProperty):

            def __init__(
                self,
                value: aas.LangStringSet,
                id_short: Optional[str] = r"SyntheticData",
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = global_ref(
                    r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/SyntheticData/1/0"
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
            ):

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"Information, if the dataset is synthetic, real or mixed"}
                    )

                if qualifier is None:
                    qualifier = ()

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
            dataCollectors: Optional[DataCollectors] = None,
            enviromentConditions: Optional[EnviromentConditions] = None,
            syntheticData: Optional[Union[aas.LangStringSet, SyntheticData]] = None,
            id_short: Optional[str] = r"BoundaryConditions",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = global_ref(
                r"https://admin-shell.io/idta/AIDataset/BoundaryConditions/1/0"
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
        ):

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={r"en": r"Boundary conditions in which the dataset was created"}
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if syntheticData is not None and not isinstance(syntheticData, aas.SubmodelElement):
                syntheticData = self.SyntheticData(syntheticData)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(dataCollectors, enviromentConditions, syntheticData)

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
        uRIOfTheProduct: Union[str, URIOfTheProduct],
        version: Union[str, Version],
        contactInformation: Union[aas.Reference, ContactInformation],
        storage: Union[str, Storage],
        sizeInformation: SizeInformation,
        metaData: MetaData,
        labeled: Optional[Labeled] = None,
        metrics: Optional[Metrics] = None,
        boundaryConditions: Optional[BoundaryConditions] = None,
        id_short: Optional[str] = r"AIDataset",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = global_ref(
            r"https://admin-shell.io/idta/SubmodelTemplate/AIDataset/1/0"
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.INSTANCE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if description is None:
            description = aas.MultiLanguageTextType(dict_={r"en": r"Categories and Information of the aidataset@en "})

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Build a submodel element if a raw value was passed in the argument

        if uRIOfTheProduct is not None and not isinstance(uRIOfTheProduct, aas.SubmodelElement):
            uRIOfTheProduct = self.URIOfTheProduct(uRIOfTheProduct)

        # Build a submodel element if a raw value was passed in the argument

        if version is not None and not isinstance(version, aas.SubmodelElement):
            version = self.Version(version)

        # Build a submodel element if a raw value was passed in the argument

        if contactInformation is not None and not isinstance(contactInformation, aas.SubmodelElement):
            contactInformation = self.ContactInformation(contactInformation)

        # Build a submodel element if a raw value was passed in the argument

        if storage is not None and not isinstance(storage, aas.SubmodelElement):
            storage = self.Storage(storage)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            uRIOfTheProduct,
            version,
            contactInformation,
            storage,
            labeled,
            sizeInformation,
            metaData,
            metrics,
            boundaryConditions,
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
