from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class EquipmentUnderControl(aas.Submodel):

    class EUCSpecification(aas.SubmodelElementCollection):

        class TagName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TagName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/TagName/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"tag name"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the tag that the device represents"
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

        class PIDName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"PIDName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/PIDName/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(dict_={r"en": r"PID name"})

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the EUC that the SIF protects"
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

        class TagDescription(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"TagDescription",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/TagDescription/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"tag description"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives relevant information about the tag that the device represents"
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

        class Boundary(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"Boundary",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/EquipmentUnderControl/EUCBoundary/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"EUC boundary"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the EUC that the SIF protects"
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

        class EUCControlSystem(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"EUCControlSystem",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/EUCControlSystem/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"EUC control system"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the EUC that the SIF protects"
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

        class ProcessSafetyTime(aas.Property):

            def __init__(
                self,
                value: xsd.Decimal,
                id_short: Optional[str] = r"ProcessSafetyTime",
                value_type: aas.DataTypeDefXsd = xsd.Decimal,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/ProcessSafetyTime/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"process safety time"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the EUC that the SIF protects"
                        }
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"unit",
                            value_type=str,
                            value=r"seconds",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
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

        class LinkedSIF(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"LinkedSIF",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/EquipmentUnderControl/ReferenceToSIF/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"reference to SIF"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"SRS requirement(s) according to IEC 61511"}
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

        def __init__(
            self,
            tagName: Union[str, TagName],
            tagDescription: Union[str, TagDescription],
            processSafetyTime: Union[xsd.Decimal, ProcessSafetyTime],
            pIDName: Optional[Union[str, PIDName]] = None,
            boundary: Optional[Union[str, Boundary]] = None,
            eUCControlSystem: Optional[Iterable[Union[str, EUCControlSystem]]] = None,
            linkedSIF: Optional[Iterable[Union[aas.Reference, LinkedSIF]]] = None,
            id_short: Optional[str] = r"EUCSpecification",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/EUCSpecification/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"EUC specification"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"gives information about the EUC that the SIF protects"
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if tagName is not None and not isinstance(tagName, aas.SubmodelElement):
                tagName = self.TagName(tagName)

            # Build a submodel element if a raw value was passed in the argument

            if pIDName is not None and not isinstance(pIDName, aas.SubmodelElement):
                pIDName = self.PIDName(pIDName)

            # Build a submodel element if a raw value was passed in the argument

            if tagDescription is not None and not isinstance(
                tagDescription, aas.SubmodelElement
            ):
                tagDescription = self.TagDescription(tagDescription)

            # Build a submodel element if a raw value was passed in the argument

            if boundary is not None and not isinstance(boundary, aas.SubmodelElement):
                boundary = self.Boundary(boundary)

            # A str would be split into its characters
            if isinstance(eUCControlSystem, str):
                raise TypeError("eUCControlSystem takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if eUCControlSystem:
                eUCControlSystem = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.EUCControlSystem(i)
                    )
                    for i in eUCControlSystem
                ]

            # Build a submodel element if a raw value was passed in the argument

            if processSafetyTime is not None and not isinstance(
                processSafetyTime, aas.SubmodelElement
            ):
                processSafetyTime = self.ProcessSafetyTime(processSafetyTime)

            # A str would be split into its characters
            if isinstance(linkedSIF, str):
                raise TypeError("linkedSIF takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if linkedSIF:
                linkedSIF = [
                    i if isinstance(i, aas.SubmodelElement) else self.LinkedSIF(i)
                    for i in linkedSIF
                ]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                tagName,
                pIDName,
                tagDescription,
                boundary,
                eUCControlSystem,
                processSafetyTime,
                linkedSIF,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

    class HazardousEvent(aas.SubmodelElementCollection):

        class HazardousEventDescription(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"HazardousEventDescription",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/HazardousEventDescription/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"hazardous event description"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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

        class HazardID(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"HazardID",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/HazardID/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"hazard ID"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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

        class IndependentProtectionLayer(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"IndependentProtectionLayer",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/IndependentProtectionLayer/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"independent protection layer"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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
            hazardousEventDescription: Union[str, HazardousEventDescription],
            hazardID: Union[str, HazardID],
            independentProtectionLayer: Optional[
                Iterable[Union[str, IndependentProtectionLayer]]
            ] = None,
            id_short: Optional[str] = r"HazardousEvent",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/HazardousEvent/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"hazardous event"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"gives information about the EUC that the SIF protects"
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if hazardousEventDescription is not None and not isinstance(
                hazardousEventDescription, aas.SubmodelElement
            ):
                hazardousEventDescription = self.HazardousEventDescription(
                    hazardousEventDescription
                )

            # Build a submodel element if a raw value was passed in the argument

            if hazardID is not None and not isinstance(hazardID, aas.SubmodelElement):
                hazardID = self.HazardID(hazardID)

            # A str would be split into its characters
            if isinstance(independentProtectionLayer, str):
                raise TypeError(
                    "independentProtectionLayer takes several elements, got a str"
                )

            # Build submodel elements from raw values passed in the argument
            if independentProtectionLayer:
                independentProtectionLayer = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.IndependentProtectionLayer(i)
                    )
                    for i in independentProtectionLayer
                ]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                hazardousEventDescription,
                hazardID,
                independentProtectionLayer,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

    class HazardFromCombinedSafeProcessStates(aas.SubmodelElementCollection):

        class HazardousEventDescription(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"HazardousEventDescription",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/HazardousEventDescription/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"hazardous event description"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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

        class HazardID(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"HazardID",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/HazardID/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"hazard ID"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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

        class MeasuresToAvoidHazardFromCombinedSafeProcessStates(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[
                    str
                ] = r"MeasuresToAvoidHazardFromCombinedSafeProcessStates",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/EquipmentUnderControl/MeasureToAvoidHazardFromCombinedSafeProcessStates/1/0",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={
                            r"en": r"measure to avoid hazard from combined safe process states"
                        }
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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

        class ReferenceToHazardousEvent(aas.ReferenceElement):

            def __init__(
                self,
                value: aas.Reference,
                id_short: Optional[str] = r"ReferenceToHazardousEvent",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/ReferenceToHazardousEvent/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"reference to hazardous event"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={r"en": r"gives information about the SIF"}
                    )

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"SMT/Cardinality",
                            value_type=str,
                            value=r"OneToMany",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=None,
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class IndependentProtectionLayer(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"IndependentProtectionLayer",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://admin-shell.io/idta/cds/IndependentProtectionLayer/1",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if display_name is None:
                    display_name = aas.MultiLanguageNameType(
                        dict_={r"en": r"independent protection layer"}
                    )

                if description is None:
                    description = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"gives information about the hazardous event related to the SIF"
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
            hazardousEventDescription: Union[str, HazardousEventDescription],
            hazardID: Union[str, HazardID],
            referenceToHazardousEvent: Iterable[
                Union[aas.Reference, ReferenceToHazardousEvent]
            ],
            measuresToAvoidHazardFromCombinedSafeProcessStates: Optional[
                Iterable[Union[str, MeasuresToAvoidHazardFromCombinedSafeProcessStates]]
            ] = None,
            independentProtectionLayer: Optional[
                Iterable[Union[str, IndependentProtectionLayer]]
            ] = None,
            id_short: Optional[str] = r"HazardFromCombinedSafeProcessStates",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/HazardFromCombinedSafeProcessStates/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"hazard from combined safe process states"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"gives information about the EUC that the SIF protects"
                    }
                )

            if qualifier is None:
                qualifier = ()

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if hazardousEventDescription is not None and not isinstance(
                hazardousEventDescription, aas.SubmodelElement
            ):
                hazardousEventDescription = self.HazardousEventDescription(
                    hazardousEventDescription
                )

            # Build a submodel element if a raw value was passed in the argument

            if hazardID is not None and not isinstance(hazardID, aas.SubmodelElement):
                hazardID = self.HazardID(hazardID)

            # A str would be split into its characters
            if isinstance(measuresToAvoidHazardFromCombinedSafeProcessStates, str):
                raise TypeError(
                    "measuresToAvoidHazardFromCombinedSafeProcessStates takes several elements, got a str"
                )

            # Build submodel elements from raw values passed in the argument
            if measuresToAvoidHazardFromCombinedSafeProcessStates:
                measuresToAvoidHazardFromCombinedSafeProcessStates = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.MeasuresToAvoidHazardFromCombinedSafeProcessStates(i)
                    )
                    for i in measuresToAvoidHazardFromCombinedSafeProcessStates
                ]

            # A str would be split into its characters
            if isinstance(referenceToHazardousEvent, str):
                raise TypeError(
                    "referenceToHazardousEvent takes several elements, got a str"
                )

            # Build submodel elements from raw values passed in the argument
            if referenceToHazardousEvent:
                referenceToHazardousEvent = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.ReferenceToHazardousEvent(i)
                    )
                    for i in referenceToHazardousEvent
                ]

            # A str would be split into its characters
            if isinstance(independentProtectionLayer, str):
                raise TypeError(
                    "independentProtectionLayer takes several elements, got a str"
                )

            # Build submodel elements from raw values passed in the argument
            if independentProtectionLayer:
                independentProtectionLayer = [
                    (
                        i
                        if isinstance(i, aas.SubmodelElement)
                        else self.IndependentProtectionLayer(i)
                    )
                    for i in independentProtectionLayer
                ]

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                hazardousEventDescription,
                hazardID,
                measuresToAvoidHazardFromCombinedSafeProcessStates,
                referenceToHazardousEvent,
                independentProtectionLayer,
            ]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, aas.SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(
                        f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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

    class SILAllocationReport(aas.File):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"SILAllocationReport",
            content_type: Optional[str] = r"application/octet-stream",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/SILAllocationReport/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"SIL allocation report"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"gives information about the EUC that the SIF protects"
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

    class HazardAndRiskAssessmentReport(aas.File):

        def __init__(
            self,
            value: str,
            id_short: Optional[str] = r"HazardAndRiskAssessmentReport",
            content_type: Optional[str] = r"application/octet-stream",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"https://admin-shell.io/idta/cds/HazardAndRiskAssessmentReport/1",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if display_name is None:
                display_name = aas.MultiLanguageNameType(
                    dict_={r"en": r"hazard and risk assessment report"}
                )

            if description is None:
                description = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"gives information about the EUC that the SIF protects"
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

    def __init__(
        self,
        id_: str,
        eUCSpecification: EUCSpecification,
        hazardousEvent: Iterable[HazardousEvent],
        hazardFromCombinedSafeProcessStates: Iterable[
            HazardFromCombinedSafeProcessStates
        ],
        sILAllocationReport: Optional[Iterable[SILAllocationReport]] = None,
        hazardAndRiskAssessmentReport: Optional[
            Iterable[HazardAndRiskAssessmentReport]
        ] = None,
        id_short: Optional[str] = r"EquipmentUnderControl",
        display_name: Optional[aas.MultiLanguageNameType] = None,
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = None,
        administration: Optional[aas.AdministrativeInformation] = None,
        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/SubmodelTemplate/EquipmentUnderControl/1/0",
                ),
            ),
            referred_semantic_id=None,
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
                    r"en": r"The submodel Equipment Under Control is a collection of properties about the functional safety requirements and information for the lifecycle of a device of an equipment under control protected by one or more protection layer(s) / safety instrumented function(s)."
                }
            )

        if administration is None:
            administration = aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/idta-02096-1-0",
                embedded_data_specifications=[],
            )

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # A str would be split into its characters
        if isinstance(hazardousEvent, str):
            raise TypeError("hazardousEvent takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(hazardFromCombinedSafeProcessStates, str):
            raise TypeError(
                "hazardFromCombinedSafeProcessStates takes several elements, got a str"
            )

        # A str would be split into its characters
        if isinstance(sILAllocationReport, str):
            raise TypeError("sILAllocationReport takes several elements, got a str")

        # A str would be split into its characters
        if isinstance(hazardAndRiskAssessmentReport, str):
            raise TypeError(
                "hazardAndRiskAssessmentReport takes several elements, got a str"
            )

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [
            eUCSpecification,
            hazardousEvent,
            hazardFromCombinedSafeProcessStates,
            sILAllocationReport,
            hazardAndRiskAssessmentReport,
        ]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, aas.SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(
                    f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
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
