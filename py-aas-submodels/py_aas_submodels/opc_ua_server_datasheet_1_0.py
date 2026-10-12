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


class BlobMetadata(TypedDict, total=False):
    """Metadata of aas.Blob, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


class FileMetadata(TypedDict, total=False):
    """Metadata of aas.File, passed as keyword arguments to its generated classes"""

    id_short: Optional[str]
    display_name: Optional[aas.MultiLanguageNameType]
    category: Optional[str]
    description: Optional[aas.MultiLanguageTextType]
    semantic_id: Optional[aas.Reference]
    qualifier: Iterable[aas.Qualifier]
    extension: Iterable[aas.Extension]
    supplemental_semantic_id: Iterable[aas.Reference]
    embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification]


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


class UAServerDataSheet(aas.Submodel):

    class Configuration(aas.SubmodelElementCollection):

        class NodeSets(GeneratedSubmodelElementList):

            class Nodesets_item(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": None,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Provides a placeholder for a nodeset file that an OPC UA server uses to create AddressSpace during configuration. The nodeset can be part of the machine’s AASX file, in an OPC cloud library or in another downloadable endpoint. "
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/NodeSetFile"),
                    }

                def __init__(
                    self, value: str, content_type: Optional[str] = r"text/xml", **kwargs: Unpack[FileMetadata]
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"NodeSets",
                    "type_value_list_element": aas.File,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Provides a container for nodeset files that is intended for configuring the server. By default, the UA nodeset is always included during configuration as base nodeset."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/NodeSets"),
                }

            def __init__(
                self,
                nodesets_items: Optional[Iterable[Nodesets_item]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(nodesets_items, str):
                    raise TypeError("nodesets_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(nodesets_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class AllowAnonymousUser(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"AllowAnonymousUser",
                    "value_type": bool,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates to the client application that the server allows or denies anonymous users."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/AllowAnonymous"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SupportSecurityModeNone(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SupportSecurityModeNone",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates to the client application that a server supports none security mode."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityModeNone"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SupportSecurityModeSign(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SupportSecurityModeSign",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates to the client application that a server supports sign security mode"}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityModeSign"),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SupportSecurityModeSignEncrypt(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SupportSecurityModeSignEncrypt",
                    "value_type": int,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates to the client application that a server supports sign and encrypt security mode."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityModeSignEncrypt"
                    ),
                }

            def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SupportSecurityPolicyUris(GeneratedSubmodelElementList):

            class Supportsecuritypolicyuris_item(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": None,
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Indicates the security policy uri supported by the server. For example, if the server supports basic128Rsa15, the value will be  http://opcfoundation.org/UA/SecurityPolicy#Basic128Rsa15."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityPolicyUri"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"SupportSecurityPolicyUris",
                    "type_value_list_element": aas.Property,
                    "value_type_list_element": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides a container for list of security policies that the server supports."}
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SupportSecurityPolicyUris"
                    ),
                }

            def __init__(
                self,
                supportsecuritypolicyuris_items: Optional[Iterable[Union[str, Supportsecuritypolicyuris_item]]] = None,
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(supportsecuritypolicyuris_items, str):
                    raise TypeError("supportsecuritypolicyuris_items takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if supportsecuritypolicyuris_items:
                    supportsecuritypolicyuris_items = [
                        i if isinstance(i, aas.SubmodelElement) else self.Supportsecuritypolicyuris_item(i)
                        for i in supportsecuritypolicyuris_items
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    supportsecuritypolicyuris_items, number_repeated=False
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class SupportRedundancy(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SupportRedundancy",
                    "value_type": bool,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates to the client application that the server supports Redundancy. If the value is true, the type of redundancy supported can be found in RedundancySupport node (i=851)."
                        }
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SupportRedundancy"),
                }

            def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Configuration",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates entry point for the configuration parameter of an OPC UA server application. "
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/Configuration"),
            }

        def __init__(
            self,
            nodeSets: Optional[Union[Iterable[NodeSets.Nodesets_item], NodeSets]] = None,
            allowAnonymousUser: Optional[Union[bool, AllowAnonymousUser]] = None,
            supportSecurityModeNone: Optional[Union[int, SupportSecurityModeNone]] = None,
            supportSecurityModeSign: Optional[Union[int, SupportSecurityModeSign]] = None,
            supportSecurityModeSignEncrypt: Optional[Union[int, SupportSecurityModeSignEncrypt]] = None,
            supportSecurityPolicyUris: Optional[
                Union[
                    Iterable[Union[str, SupportSecurityPolicyUris.Supportsecuritypolicyuris_item]],
                    SupportSecurityPolicyUris,
                ]
            ] = None,
            supportRedundancy: Optional[Union[bool, SupportRedundancy]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(nodeSets, str):
                raise TypeError("nodeSets takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if nodeSets is not None and not isinstance(nodeSets, aas.SubmodelElement):
                nodeSets = self.NodeSets(nodeSets)

            # Build a submodel element if a raw value was passed in the argument

            if allowAnonymousUser is not None and not isinstance(allowAnonymousUser, aas.SubmodelElement):
                allowAnonymousUser = self.AllowAnonymousUser(allowAnonymousUser)

            # Build a submodel element if a raw value was passed in the argument

            if supportSecurityModeNone is not None and not isinstance(supportSecurityModeNone, aas.SubmodelElement):
                supportSecurityModeNone = self.SupportSecurityModeNone(supportSecurityModeNone)

            # Build a submodel element if a raw value was passed in the argument

            if supportSecurityModeSign is not None and not isinstance(supportSecurityModeSign, aas.SubmodelElement):
                supportSecurityModeSign = self.SupportSecurityModeSign(supportSecurityModeSign)

            # Build a submodel element if a raw value was passed in the argument

            if supportSecurityModeSignEncrypt is not None and not isinstance(
                supportSecurityModeSignEncrypt, aas.SubmodelElement
            ):
                supportSecurityModeSignEncrypt = self.SupportSecurityModeSignEncrypt(supportSecurityModeSignEncrypt)

            # A str would be split into its characters
            if isinstance(supportSecurityPolicyUris, str):
                raise TypeError("supportSecurityPolicyUris takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if supportSecurityPolicyUris is not None and not isinstance(supportSecurityPolicyUris, aas.SubmodelElement):
                supportSecurityPolicyUris = self.SupportSecurityPolicyUris(supportSecurityPolicyUris)

            # Build a submodel element if a raw value was passed in the argument

            if supportRedundancy is not None and not isinstance(supportRedundancy, aas.SubmodelElement):
                supportRedundancy = self.SupportRedundancy(supportRedundancy)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                nodeSets,
                allowAnonymousUser,
                supportSecurityModeNone,
                supportSecurityModeSign,
                supportSecurityModeSignEncrypt,
                supportSecurityPolicyUris,
                supportRedundancy,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class Identification(aas.SubmodelElementCollection):

        class ProductUri(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductUri",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"This is a URI that identifies the OPC UA server."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAY811#001"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ManufacturerName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ManufacturerName",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates the name of the OPC UA Server application manufacturer."}
                    ),
                    "semantic_id": global_ref(r"0173-1#02-AAO677#002"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class ProductName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"ProductName",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates the name of the OPC UA Server application."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/ProductName"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class SoftwareVersion(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"SoftwareVersion",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates the software version of the OPC UA server application."}
                    ),
                    "semantic_id": global_ref(r"0112/2///61987#ABA601#008"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BuildNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"BuildNumber",
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Indicates the build number of the OPC UA server application."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/BuildNumber"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BuildDate(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"BuildDate",
                    "value_type": xsd.DateTime,
                    "description": aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Indicates the build date of the OPC UA Server application as UTC time with format YYYY-MM-DDTHH:MM:SS.sss."
                        }
                    ),
                    "semantic_id": global_ref(
                        r"https://admin-shell.io/idta/SoftwareNameplate/1/0/SoftwareNameplate/SoftwareNameplateType/BuildDate"
                    ),
                }

            def __init__(self, value: xsd.DateTime, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"Identification",
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates the entry point for Identification parameters of an OPC UA server application. The Identification uses BuildInfo structure defined in OPC UA Part 5 "
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/Identification"),
            }

        def __init__(
            self,
            productUri: Optional[Union[str, ProductUri]] = None,
            manufacturerName: Optional[Union[str, ManufacturerName]] = None,
            productName: Optional[Union[str, ProductName]] = None,
            softwareVersion: Optional[Union[str, SoftwareVersion]] = None,
            buildNumber: Optional[Union[str, BuildNumber]] = None,
            buildDate: Optional[Union[xsd.DateTime, BuildDate]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if productUri is not None and not isinstance(productUri, aas.SubmodelElement):
                productUri = self.ProductUri(productUri)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(manufacturerName, aas.SubmodelElement):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if productName is not None and not isinstance(productName, aas.SubmodelElement):
                productName = self.ProductName(productName)

            # Build a submodel element if a raw value was passed in the argument

            if softwareVersion is not None and not isinstance(softwareVersion, aas.SubmodelElement):
                softwareVersion = self.SoftwareVersion(softwareVersion)

            # Build a submodel element if a raw value was passed in the argument

            if buildNumber is not None and not isinstance(buildNumber, aas.SubmodelElement):
                buildNumber = self.BuildNumber(buildNumber)

            # Build a submodel element if a raw value was passed in the argument

            if buildDate is not None and not isinstance(buildDate, aas.SubmodelElement):
                buildDate = self.BuildDate(buildDate)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                productUri, manufacturerName, productName, softwareVersion, buildNumber, buildDate
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class EndpointDescriptions(GeneratedSubmodelElementList):

        class Endpointdescriptions_item(aas.SubmodelElementCollection):

            class EndpointUri(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EndpointUri",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Defines the URL for the server endpoint. "}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/EndpointUri"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Server(aas.SubmodelElementCollection):

                class ApplicationUri(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ApplicationUri",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Defines a URI that uniquely identifies the application instance. "}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/ApplicationUri"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ProductUri(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ProductUri",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"This is a URI that identifies the OPC UA server."}
                            ),
                            "semantic_id": global_ref(r"0173-1#02-AAY811#001"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ApplicationName(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ApplicationName",
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Defines a localized descriptive name for the server application."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/ApplicationName"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ApplicationType(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ApplicationType",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Defines the type of application as an enumeration. Acceptable values for this term are Server, Client, ClientAndServer, DiscoveryServer. For UAServerDataSheet Submodel, the focus is on OPC UA server so only Server and ClientAndServer value are valid for this Submodel."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/ApplicationType"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class GatewayServerUri(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"GatewayServerUri",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Defines the URI that identifies the gateway server that is linked with the discovery Uris. If the server can be accessed directly, this term is not defined. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/GatewayServerUri"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DiscoveryProfileUri(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DiscoveryProfileUri",
                            "value_type": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={
                                    r"en": r"Defines the URI that identifies the discovery profile that is supported by the URLs. "
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/DiscoveryProfileUri"
                            ),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DiscoveryUrls(GeneratedSubmodelElementList):

                    class Discoveryurls_item(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": None,
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={r"en": r"Defines the discovery Url of the server application."}
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/DiscoveryUrl"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementListMetadata:
                        return {
                            "id_short": r"DiscoveryUrls",
                            "type_value_list_element": aas.Property,
                            "value_type_list_element": str,
                            "description": aas.MultiLanguageTextType(
                                dict_={r"en": r"Provides a list of discovery endpoints used by the server application."}
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/DiscoveryUrls"
                            ),
                        }

                    def __init__(
                        self,
                        discoveryurls_items: Optional[Iterable[Union[str, Discoveryurls_item]]] = None,
                        **kwargs: Unpack[SubmodelElementListMetadata],
                    ):

                        # A str would be split into its characters
                        if isinstance(discoveryurls_items, str):
                            raise TypeError("discoveryurls_items takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if discoveryurls_items:
                            discoveryurls_items = [
                                i if isinstance(i, aas.SubmodelElement) else self.Discoveryurls_item(i)
                                for i in discoveryurls_items
                            ]

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            discoveryurls_items, number_repeated=False
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Server",
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Defines the description of the server that the endpoint belongs to. "}
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/Server"),
                    }

                def __init__(
                    self,
                    applicationUri: Union[str, ApplicationUri],
                    productUri: Optional[Union[str, ProductUri]] = None,
                    applicationName: Optional[Union[aas.MultiLanguageTextType, ApplicationName]] = None,
                    applicationType: Optional[Union[str, ApplicationType]] = None,
                    gatewayServerUri: Optional[Union[str, GatewayServerUri]] = None,
                    discoveryProfileUri: Optional[Union[str, DiscoveryProfileUri]] = None,
                    discoveryUrls: Optional[
                        Union[Iterable[Union[str, DiscoveryUrls.Discoveryurls_item]], DiscoveryUrls]
                    ] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if applicationUri is not None and not isinstance(applicationUri, aas.SubmodelElement):
                        applicationUri = self.ApplicationUri(applicationUri)

                    # Build a submodel element if a raw value was passed in the argument

                    if productUri is not None and not isinstance(productUri, aas.SubmodelElement):
                        productUri = self.ProductUri(productUri)

                    # Build a submodel element if a raw value was passed in the argument

                    if applicationName is not None and not isinstance(applicationName, aas.SubmodelElement):
                        applicationName = self.ApplicationName(applicationName)

                    # Build a submodel element if a raw value was passed in the argument

                    if applicationType is not None and not isinstance(applicationType, aas.SubmodelElement):
                        applicationType = self.ApplicationType(applicationType)

                    # Build a submodel element if a raw value was passed in the argument

                    if gatewayServerUri is not None and not isinstance(gatewayServerUri, aas.SubmodelElement):
                        gatewayServerUri = self.GatewayServerUri(gatewayServerUri)

                    # Build a submodel element if a raw value was passed in the argument

                    if discoveryProfileUri is not None and not isinstance(discoveryProfileUri, aas.SubmodelElement):
                        discoveryProfileUri = self.DiscoveryProfileUri(discoveryProfileUri)

                    # A str would be split into its characters
                    if isinstance(discoveryUrls, str):
                        raise TypeError("discoveryUrls takes several elements, got a str")

                    # Build a submodel element if a raw value was passed in the argument

                    if discoveryUrls is not None and not isinstance(discoveryUrls, aas.SubmodelElement):
                        discoveryUrls = self.DiscoveryUrls(discoveryUrls)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        applicationUri,
                        productUri,
                        applicationName,
                        applicationType,
                        gatewayServerUri,
                        discoveryProfileUri,
                        discoveryUrls,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class ServerCertificate(aas.Blob):

                @staticmethod
                def template_defaults() -> BlobMetadata:
                    return {
                        "id_short": r"ServerCertificate",
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"When a server is instantiated, a certificate is issued and the certificate contains information that a client can use to validate a server when establishing a session. The server certificate uses Application Instance Certificate model of the OPC UA part 2 [8] and 4[9] as byte64 encoded string."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/UAServerDatasheet/1/0/Servercertificate"
                        ),
                    }

                def __init__(
                    self,
                    value: Optional[bytes] = None,
                    content_type: Optional[str] = r"text/plain",
                    **kwargs: Unpack[BlobMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            class SecurityMode(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SecurityMode",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Defines the type of security mode attached to the endpoint description. The mode can be one of the following values: None, Sign, SignAndEncrypt, Invalid."
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityMode"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SecurityPolicyUri(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SecurityPolicyUri",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Defines the security policy to use when securing messages."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityPolicyUri"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class UserIdentityTokens(GeneratedSubmodelElementList):

                class Useridentitytokens_item(aas.SubmodelElementCollection):

                    class PolicyId(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"PolicyId",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"PolicyId is provided by a server application to defines an identifier for the token policy. "
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/PolicyId"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TokenType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"TokenType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Indicates the kind of user identity token required. This term us an enumeration with one of the following values Anonymous,Username,Certificate,IssueToken."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/TokenType"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class IssuedTokenType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"IssuedTokenType",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Specified only when TokenType is IssuedToken to indicates the URI for the type of token."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/IssuedTokenType"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class IssuerEndpointUri(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"IssuerEndpointUri",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Defines the endpoint of the authorization service. The value provided here depends on the IssuedTokenType term.  "
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/IssuerEndpointUri"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class SecurityPolicyUri(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"SecurityPolicyUri",
                                "value_type": str,
                                "description": aas.MultiLanguageTextType(
                                    dict_={
                                        r"en": r"Defines the security policy to use when encrypting or signing the UserIdentityToken when it is passed to the Server in the active session request."
                                    }
                                ),
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityPolicyUri"
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
                                    r"en": r"Defines an identity token that can be used to access the server application."
                                }
                            ),
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/UAServerDatasheet/1/0/UserIdentityToken"
                            ),
                        }

                    def __init__(
                        self,
                        policyId: Optional[Union[str, PolicyId]] = None,
                        tokenType: Optional[Union[str, TokenType]] = None,
                        issuedTokenType: Optional[Union[str, IssuedTokenType]] = None,
                        issuerEndpointUri: Optional[Union[str, IssuerEndpointUri]] = None,
                        securityPolicyUri: Optional[Union[str, SecurityPolicyUri]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if policyId is not None and not isinstance(policyId, aas.SubmodelElement):
                            policyId = self.PolicyId(policyId)

                        # Build a submodel element if a raw value was passed in the argument

                        if tokenType is not None and not isinstance(tokenType, aas.SubmodelElement):
                            tokenType = self.TokenType(tokenType)

                        # Build a submodel element if a raw value was passed in the argument

                        if issuedTokenType is not None and not isinstance(issuedTokenType, aas.SubmodelElement):
                            issuedTokenType = self.IssuedTokenType(issuedTokenType)

                        # Build a submodel element if a raw value was passed in the argument

                        if issuerEndpointUri is not None and not isinstance(issuerEndpointUri, aas.SubmodelElement):
                            issuerEndpointUri = self.IssuerEndpointUri(issuerEndpointUri)

                        # Build a submodel element if a raw value was passed in the argument

                        if securityPolicyUri is not None and not isinstance(securityPolicyUri, aas.SubmodelElement):
                            securityPolicyUri = self.SecurityPolicyUri(securityPolicyUri)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            policyId, tokenType, issuedTokenType, issuerEndpointUri, securityPolicyUri
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"UserIdentityTokens",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "description": aas.MultiLanguageTextType(
                            dict_={r"en": r"Defines the list of user identity tokens that the server will accept."}
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/UAServerDatasheet/1/0/UserIdentityTokens"
                        ),
                    }

                def __init__(
                    self,
                    useridentitytokens_items: Optional[Iterable[Useridentitytokens_item]] = None,
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(useridentitytokens_items, str):
                        raise TypeError("useridentitytokens_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        useridentitytokens_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TransportProfileUri(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TransportProfileUri",
                        "value_type": str,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"Defines the URI of the transport profile supported by the server endpoint. Because the transport profiles can be updated in the future, this value is intended to support both future and present transport profile uri officially defined by OPC UA."
                            }
                        ),
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/UAServerDatasheet/1/0/TransportProfileUri"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class SecurityLevel(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"SecurityLevel",
                        "value_type": int,
                        "description": aas.MultiLanguageTextType(
                            dict_={
                                r"en": r"A numeric value that indicates how secure the EndpointDescription is compared to other EndpointDescriptions for the same Server. A value of 0 indicates that the EndpointDescription is not recommended and is only supported for backward compatibility. A higher value indicates better security. "
                            }
                        ),
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/SecurityLevel"),
                    }

                def __init__(self, value: int, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": None,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Provides information on how to access an OPC UA server. "}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/EndpointDescription"),
                }

            def __init__(
                self,
                endpointUri: Union[str, EndpointUri],
                server: Optional[Server] = None,
                serverCertificate: Optional[ServerCertificate] = None,
                securityMode: Optional[Union[str, SecurityMode]] = None,
                securityPolicyUri: Optional[Union[str, SecurityPolicyUri]] = None,
                userIdentityTokens: Optional[
                    Union[Iterable[UserIdentityTokens.Useridentitytokens_item], UserIdentityTokens]
                ] = None,
                transportProfileUri: Optional[Union[str, TransportProfileUri]] = None,
                securityLevel: Optional[Union[int, SecurityLevel]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if endpointUri is not None and not isinstance(endpointUri, aas.SubmodelElement):
                    endpointUri = self.EndpointUri(endpointUri)

                # Build a submodel element if a raw value was passed in the argument

                if securityMode is not None and not isinstance(securityMode, aas.SubmodelElement):
                    securityMode = self.SecurityMode(securityMode)

                # Build a submodel element if a raw value was passed in the argument

                if securityPolicyUri is not None and not isinstance(securityPolicyUri, aas.SubmodelElement):
                    securityPolicyUri = self.SecurityPolicyUri(securityPolicyUri)

                # A str would be split into its characters
                if isinstance(userIdentityTokens, str):
                    raise TypeError("userIdentityTokens takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if userIdentityTokens is not None and not isinstance(userIdentityTokens, aas.SubmodelElement):
                    userIdentityTokens = self.UserIdentityTokens(userIdentityTokens)

                # Build a submodel element if a raw value was passed in the argument

                if transportProfileUri is not None and not isinstance(transportProfileUri, aas.SubmodelElement):
                    transportProfileUri = self.TransportProfileUri(transportProfileUri)

                # Build a submodel element if a raw value was passed in the argument

                if securityLevel is not None and not isinstance(securityLevel, aas.SubmodelElement):
                    securityLevel = self.SecurityLevel(securityLevel)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    endpointUri,
                    server,
                    serverCertificate,
                    securityMode,
                    securityPolicyUri,
                    userIdentityTokens,
                    transportProfileUri,
                    securityLevel,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"EndpointDescriptions",
                "type_value_list_element": aas.SubmodelElementCollection,
                "description": aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Indicates the entry point of an online OPC UA server access. The Endpoint description uses the EndpointDescription structure defined in OPC UA Part 4 [9]. "
                    }
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/EndpointDescriptions"),
            }

        def __init__(
            self,
            endpointdescriptions_items: Optional[Iterable[Endpointdescriptions_item]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(endpointdescriptions_items, str):
                raise TypeError("endpointdescriptions_items takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(endpointdescriptions_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DiscoveryUrls(GeneratedSubmodelElementList):

        class Discoveryurls_item(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": None,
                    "value_type": str,
                    "description": aas.MultiLanguageTextType(
                        dict_={r"en": r"Defines the discovery Url of the server application."}
                    ),
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/DiscoveryUrl"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementListMetadata:
            return {
                "id_short": r"DiscoveryUrls",
                "type_value_list_element": aas.Property,
                "value_type_list_element": str,
                "description": aas.MultiLanguageTextType(
                    dict_={r"en": r"Provides a list of discovery endpoints used by the server application."}
                ),
                "semantic_id": global_ref(r"https://admin-shell.io/idta/UAServerDatasheet/1/0/DiscoveryUrls"),
            }

        def __init__(
            self,
            discoveryurls_items: Optional[Iterable[Union[str, Discoveryurls_item]]] = None,
            **kwargs: Unpack[SubmodelElementListMetadata],
        ):

            # A str would be split into its characters
            if isinstance(discoveryurls_items, str):
                raise TypeError("discoveryurls_items takes several elements, got a str")

            # Build submodel elements from raw values passed in the argument
            if discoveryurls_items:
                discoveryurls_items = [
                    i if isinstance(i, aas.SubmodelElement) else self.Discoveryurls_item(i) for i in discoveryurls_items
                ]

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(discoveryurls_items, number_repeated=False)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"UAServerDataSheet",
            "description": aas.MultiLanguageTextType(
                dict_={r"en": r"Definition of the Submodel OPC UA Server Datasheet identified by its semanticId. "}
            ),
            "administration": aas.AdministrativeInformation(
                version=r"1", revision=r"0", creator=None, template_id=None, embedded_data_specifications=[]
            ),
            "semantic_id": aas.ModelReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.SUBMODEL,
                        value=r"https://admin-shell.io/idta/SubmodelTemplate/opcuaserverdatasheet/1/0",
                    ),
                ),
                type_=aas.Submodel,
                referred_semantic_id=None,
            ),
        }

    def __init__(
        self,
        id_: str,
        configuration: Configuration,
        identification: Identification,
        endpointDescriptions: Optional[
            Union[Iterable[EndpointDescriptions.Endpointdescriptions_item], EndpointDescriptions]
        ] = None,
        discoveryUrls: Optional[Union[Iterable[Union[str, DiscoveryUrls.Discoveryurls_item]], DiscoveryUrls]] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # A str would be split into its characters
        if isinstance(endpointDescriptions, str):
            raise TypeError("endpointDescriptions takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if endpointDescriptions is not None and not isinstance(endpointDescriptions, aas.SubmodelElement):
            endpointDescriptions = self.EndpointDescriptions(endpointDescriptions)

        # A str would be split into its characters
        if isinstance(discoveryUrls, str):
            raise TypeError("discoveryUrls takes several elements, got a str")

        # Build a submodel element if a raw value was passed in the argument

        if discoveryUrls is not None and not isinstance(discoveryUrls, aas.SubmodelElement):
            discoveryUrls = self.DiscoveryUrls(discoveryUrls)

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            configuration, identification, endpointDescriptions, discoveryUrls
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
