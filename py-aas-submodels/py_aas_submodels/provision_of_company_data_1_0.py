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


class CompanyData(aas.Submodel):

    class CompanyIdentification(aas.SubmodelElementCollection):

        class CompanyName(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CompanyName",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CompanyName/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CompanyDescription(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"CompanyDescription",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CompanyDescription/1/0"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class HomepageURL(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"HomepageURL",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/HomepageURL/1/0"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class VATNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"VATNumber",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/VATNumber/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class TaxNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"TaxNumber",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/TaxNumber/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class DUNS(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"DUNS",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/DUNS/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class CommercialRegisterNumber(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"CommercialRegisterNumber",
                    "value_type": str,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CommercialRegisterNumber/1/0"),
                }

            def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class FoundingYear(aas.Property):

            @staticmethod
            def template_defaults() -> PropertyMetadata:
                return {
                    "id_short": r"FoundingYear",
                    "value_type": xsd.GYear,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/FoundingYear/1/0"),
                }

            def __init__(self, value: xsd.GYear, **kwargs: Unpack[PropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class OrderCurrency(aas.MultiLanguageProperty):

            @staticmethod
            def template_defaults() -> MultiLanguagePropertyMetadata:
                return {
                    "id_short": r"OrderCurrency",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/OrderCurrency/1/0"),
                }

            def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class MainProductGroups(GeneratedSubmodelElementList):

            class Mainproductgroups_item(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": None,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/MainProductGroup/1/0"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"MainProductGroups",
                    "type_value_list_element": aas.MultiLanguageProperty,
                    "order_relevant": False,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/MainProductGroups/1/0"),
                }

            def __init__(
                self,
                mainproductgroups_items: Iterable[Union[aas.MultiLanguageTextType, Mainproductgroups_item]],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(mainproductgroups_items, str):
                    raise TypeError("mainproductgroups_items takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if mainproductgroups_items:
                    mainproductgroups_items = [
                        i if isinstance(i, aas.SubmodelElement) else self.Mainproductgroups_item(i)
                        for i in mainproductgroups_items
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(mainproductgroups_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class Industries(GeneratedSubmodelElementList):

            class Industries_item(aas.MultiLanguageProperty):

                @staticmethod
                def template_defaults() -> MultiLanguagePropertyMetadata:
                    return {
                        "id_short": None,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Industry/1/0"),
                    }

                def __init__(self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"Industries",
                    "type_value_list_element": aas.MultiLanguageProperty,
                    "order_relevant": False,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Industries/1/0"),
                }

            def __init__(
                self,
                industries_items: Iterable[Union[aas.MultiLanguageTextType, Industries_item]],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(industries_items, str):
                    raise TypeError("industries_items takes several elements, got a str")

                # Build submodel elements from raw values passed in the argument
                if industries_items:
                    industries_items = [
                        i if isinstance(i, aas.SubmodelElement) else self.Industries_item(i) for i in industries_items
                    ]

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(industries_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class CompanyLogo(aas.File):

            @staticmethod
            def template_defaults() -> FileMetadata:
                return {"id_short": r"CompanyLogo", "semantic_id": global_ref(r"0173-1#02-ABI776#002")}

            def __init__(self, value: str, content_type: Optional[str] = r"image/png", **kwargs: Unpack[FileMetadata]):

                super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CompanyIdentification",
                "semantic_id": aas.ModelReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                            value=r"https://admin-shell.io/idta/CompanyData/CompanyIdentification/1/0",
                        ),
                    ),
                    type_=aas.ConceptDescription,
                    referred_semantic_id=None,
                ),
            }

        def __init__(
            self,
            companyName: Union[str, CompanyName],
            companyDescription: Optional[Union[aas.MultiLanguageTextType, CompanyDescription]] = None,
            homepageURL: Optional[Union[aas.MultiLanguageTextType, HomepageURL]] = None,
            vATNumber: Optional[Union[str, VATNumber]] = None,
            taxNumber: Optional[Union[str, TaxNumber]] = None,
            dUNS: Optional[Union[str, DUNS]] = None,
            commercialRegisterNumber: Optional[Union[str, CommercialRegisterNumber]] = None,
            foundingYear: Optional[Union[xsd.GYear, FoundingYear]] = None,
            orderCurrency: Optional[Union[aas.MultiLanguageTextType, OrderCurrency]] = None,
            mainProductGroups: Optional[
                Union[
                    Iterable[Union[aas.MultiLanguageTextType, MainProductGroups.Mainproductgroups_item]],
                    MainProductGroups,
                ]
            ] = None,
            industries: Optional[
                Union[Iterable[Union[aas.MultiLanguageTextType, Industries.Industries_item]], Industries]
            ] = None,
            companyLogo: Optional[CompanyLogo] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if companyName is not None and not isinstance(companyName, aas.SubmodelElement):
                companyName = self.CompanyName(companyName)

            # Build a submodel element if a raw value was passed in the argument

            if companyDescription is not None and not isinstance(companyDescription, aas.SubmodelElement):
                companyDescription = self.CompanyDescription(companyDescription)

            # Build a submodel element if a raw value was passed in the argument

            if homepageURL is not None and not isinstance(homepageURL, aas.SubmodelElement):
                homepageURL = self.HomepageURL(homepageURL)

            # Build a submodel element if a raw value was passed in the argument

            if vATNumber is not None and not isinstance(vATNumber, aas.SubmodelElement):
                vATNumber = self.VATNumber(vATNumber)

            # Build a submodel element if a raw value was passed in the argument

            if taxNumber is not None and not isinstance(taxNumber, aas.SubmodelElement):
                taxNumber = self.TaxNumber(taxNumber)

            # Build a submodel element if a raw value was passed in the argument

            if dUNS is not None and not isinstance(dUNS, aas.SubmodelElement):
                dUNS = self.DUNS(dUNS)

            # Build a submodel element if a raw value was passed in the argument

            if commercialRegisterNumber is not None and not isinstance(commercialRegisterNumber, aas.SubmodelElement):
                commercialRegisterNumber = self.CommercialRegisterNumber(commercialRegisterNumber)

            # Build a submodel element if a raw value was passed in the argument

            if foundingYear is not None and not isinstance(foundingYear, aas.SubmodelElement):
                foundingYear = self.FoundingYear(foundingYear)

            # Build a submodel element if a raw value was passed in the argument

            if orderCurrency is not None and not isinstance(orderCurrency, aas.SubmodelElement):
                orderCurrency = self.OrderCurrency(orderCurrency)

            # A str would be split into its characters
            if isinstance(mainProductGroups, str):
                raise TypeError("mainProductGroups takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if mainProductGroups is not None and not isinstance(mainProductGroups, aas.SubmodelElement):
                mainProductGroups = self.MainProductGroups(mainProductGroups)

            # A str would be split into its characters
            if isinstance(industries, str):
                raise TypeError("industries takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if industries is not None and not isinstance(industries, aas.SubmodelElement):
                industries = self.Industries(industries)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                companyName,
                companyDescription,
                homepageURL,
                vATNumber,
                taxNumber,
                dUNS,
                commercialRegisterNumber,
                foundingYear,
                orderCurrency,
                mainProductGroups,
                industries,
                companyLogo,
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BankAccounts(aas.SubmodelElementCollection):

        class MainAccount(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"MainAccount",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/MainAccount/1/0"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BankAccount(aas.SubmodelElementCollection):

            class AccountHolder(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"AccountHolder",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/AccountHolder/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BankAccountType(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BankAccountType",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BankAccountType/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class IBAN(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"IBAN",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/IBAN/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BIC(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BIC",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BIC/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"BankAccount",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BankAccount/1/0"),
                }

            def __init__(
                self,
                accountHolder: Union[str, AccountHolder],
                iBAN: Union[str, IBAN],
                bIC: Union[str, BIC],
                bankAccountType: Optional[Union[str, BankAccountType]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if accountHolder is not None and not isinstance(accountHolder, aas.SubmodelElement):
                    accountHolder = self.AccountHolder(accountHolder)

                # Build a submodel element if a raw value was passed in the argument

                if bankAccountType is not None and not isinstance(bankAccountType, aas.SubmodelElement):
                    bankAccountType = self.BankAccountType(bankAccountType)

                # Build a submodel element if a raw value was passed in the argument

                if iBAN is not None and not isinstance(iBAN, aas.SubmodelElement):
                    iBAN = self.IBAN(iBAN)

                # Build a submodel element if a raw value was passed in the argument

                if bIC is not None and not isinstance(bIC, aas.SubmodelElement):
                    bIC = self.BIC(bIC)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(accountHolder, bankAccountType, iBAN, bIC)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BankAccounts",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BankAccounts/1/0"),
            }

        def __init__(
            self,
            mainAccount: Union[aas.Reference, MainAccount],
            bankAccount: Iterable[BankAccount],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if mainAccount is not None and not isinstance(mainAccount, aas.SubmodelElement):
                mainAccount = self.MainAccount(mainAccount)

            # A str would be split into its characters
            if isinstance(bankAccount, str):
                raise TypeError("bankAccount takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(mainAccount, bankAccount)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class DigitalInterfaces(aas.SubmodelElementCollection):

        class CompanySystems(aas.SubmodelElementCollection):

            class ERPSystem(aas.SubmodelElementCollection):

                class ERPName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ERPName",
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ERPName/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ERPVersion(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ERPVersion",
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ERPVersion/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ERPReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"ERPReference",
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ERPReference/1/0"),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"ERPSystem",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ERPSystem/1/0"),
                    }

                def __init__(
                    self,
                    eRPName: Optional[Union[str, ERPName]] = None,
                    eRPVersion: Optional[Union[str, ERPVersion]] = None,
                    eRPReference: Optional[Union[aas.Reference, ERPReference]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if eRPName is not None and not isinstance(eRPName, aas.SubmodelElement):
                        eRPName = self.ERPName(eRPName)

                    # Build a submodel element if a raw value was passed in the argument

                    if eRPVersion is not None and not isinstance(eRPVersion, aas.SubmodelElement):
                        eRPVersion = self.ERPVersion(eRPVersion)

                    # Build a submodel element if a raw value was passed in the argument

                    if eRPReference is not None and not isinstance(eRPReference, aas.SubmodelElement):
                        eRPReference = self.ERPReference(eRPReference)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(eRPName, eRPVersion, eRPReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class EmailSystem(aas.SubmodelElementCollection):

                class EmailSystemName(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"EmailSystemName",
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EmailSystemName/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class EmailSystemReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"EmailSystemReference",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/EmailSystemReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"EmailSystem",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EmailSystem/1/0"),
                    }

                def __init__(
                    self,
                    emailSystemName: Optional[Union[str, EmailSystemName]] = None,
                    emailSystemReference: Optional[Union[aas.Reference, EmailSystemReference]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if emailSystemName is not None and not isinstance(emailSystemName, aas.SubmodelElement):
                        emailSystemName = self.EmailSystemName(emailSystemName)

                    # Build a submodel element if a raw value was passed in the argument

                    if emailSystemReference is not None and not isinstance(emailSystemReference, aas.SubmodelElement):
                        emailSystemReference = self.EmailSystemReference(emailSystemReference)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(emailSystemName, emailSystemReference)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class CADTools(GeneratedSubmodelElementList):

                class Cadtools_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CADTool/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"CADTools",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CADTools/1/0"),
                    }

                def __init__(
                    self,
                    cadtools_items: Iterable[Union[str, Cadtools_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(cadtools_items, str):
                        raise TypeError("cadtools_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if cadtools_items:
                        cadtools_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Cadtools_item(i) for i in cadtools_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(cadtools_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CompanySystems",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CompanySystems/1/0"),
                }

            def __init__(
                self,
                eRPSystem: Optional[ERPSystem] = None,
                emailSystem: Optional[EmailSystem] = None,
                cADTools: Optional[Union[Iterable[Union[str, CADTools.Cadtools_item]], CADTools]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(cADTools, str):
                    raise TypeError("cADTools takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if cADTools is not None and not isinstance(cADTools, aas.SubmodelElement):
                    cADTools = self.CADTools(cADTools)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(eRPSystem, emailSystem, cADTools)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class DataExchange(aas.SubmodelElementCollection):

            class EncryptedDataTransmission(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EncryptedDataTransmission",
                        "value_type": bool,
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/EncryptedDataTransmission/1/0"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class OutgoingEInvoiceFormat(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"OutgoingEInvoiceFormat",
                        "value_type": str,
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/OutgoingEInvoiceFormat/1/0"
                        ),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EDI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EDI",
                        "value_type": bool,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EDI/1/0"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class WebEDI(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"WebEDI",
                        "value_type": bool,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/WebEDI/1/0"),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class CADFormats(GeneratedSubmodelElementList):

                class Cadformats_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CADFormat/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"CADFormats",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "order_relevant": False,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CADFormats/1/0"),
                    }

                def __init__(
                    self,
                    cadformats_items: Iterable[Union[str, Cadformats_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(cadformats_items, str):
                        raise TypeError("cadformats_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if cadformats_items:
                        cadformats_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Cadformats_item(i)
                            for i in cadformats_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(cadformats_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"DataExchange",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/DataExchange/1/0"),
                }

            def __init__(
                self,
                encryptedDataTransmission: Optional[Union[bool, EncryptedDataTransmission]] = None,
                outgoingEInvoiceFormat: Optional[Union[str, OutgoingEInvoiceFormat]] = None,
                eDI: Optional[Union[bool, EDI]] = None,
                webEDI: Optional[Union[bool, WebEDI]] = None,
                cADFormats: Optional[Union[Iterable[Union[str, CADFormats.Cadformats_item]], CADFormats]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if encryptedDataTransmission is not None and not isinstance(
                    encryptedDataTransmission, aas.SubmodelElement
                ):
                    encryptedDataTransmission = self.EncryptedDataTransmission(encryptedDataTransmission)

                # Build a submodel element if a raw value was passed in the argument

                if outgoingEInvoiceFormat is not None and not isinstance(outgoingEInvoiceFormat, aas.SubmodelElement):
                    outgoingEInvoiceFormat = self.OutgoingEInvoiceFormat(outgoingEInvoiceFormat)

                # Build a submodel element if a raw value was passed in the argument

                if eDI is not None and not isinstance(eDI, aas.SubmodelElement):
                    eDI = self.EDI(eDI)

                # Build a submodel element if a raw value was passed in the argument

                if webEDI is not None and not isinstance(webEDI, aas.SubmodelElement):
                    webEDI = self.WebEDI(webEDI)

                # A str would be split into its characters
                if isinstance(cADFormats, str):
                    raise TypeError("cADFormats takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if cADFormats is not None and not isinstance(cADFormats, aas.SubmodelElement):
                    cADFormats = self.CADFormats(cADFormats)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    encryptedDataTransmission, outgoingEInvoiceFormat, eDI, webEDI, cADFormats
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"DigitalInterfaces",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/DigitalInterfaces/1/0"),
            }

        def __init__(
            self,
            companySystems: Optional[CompanySystems] = None,
            dataExchange: Optional[DataExchange] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(companySystems, dataExchange)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class BusinessReportFigures(aas.SubmodelElementCollection):

        class LastReport(aas.ReferenceElement):

            @staticmethod
            def template_defaults() -> ReferenceElementMetadata:
                return {
                    "id_short": r"LastReport",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/LastReport/1/0"),
                }

            def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                super().__init__(value=value, **(self.template_defaults() | kwargs))

        class BusinessReportFigure(aas.SubmodelElementCollection):

            class FinancialYear(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"FinancialYear",
                        "value_type": xsd.GYear,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/FinancialYear/1/0"),
                    }

                def __init__(self, value: xsd.GYear, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class BeginOfReporttimeFrame(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BeginOfReporttimeFrame",
                        "value_type": xsd.Date,
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/BeginOfReporttimeFrame/1/0"
                        ),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EndOfReporttimeFrame(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EndOfReporttimeFrame",
                        "value_type": xsd.Date,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EndOfReporttimeFrame/1/0"),
                    }

                def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class YearOfPublication(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"YearOfPublication",
                        "value_type": xsd.GYear,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/YearOfPublication/1/0"),
                    }

                def __init__(self, value: xsd.GYear, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Turnover(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"Turnover",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Turnover/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class InvestmentVolume(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"InvestmentVolume",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/InvestmentVolume/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EquityRatio(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"EquityRatio",
                        "value_type": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EquityRatio/1/0"),
                    }

                def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class Customers(aas.SubmodelElementCollection):

                class TotalNumberCustomers(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"TotalNumberCustomers",
                            "value_type": xsd.PositiveInteger,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/TotalNumberCustomers/1/0"
                            ),
                        }

                    def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ReferenceCustomer(aas.SubmodelElementCollection):

                    class ReferenceToCustomer(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"ReferenceToCustomer",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/ReferenceToCustomer/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CustomerWebsite(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CustomerWebsite",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/CustomerWebsite/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": r"ReferenceCustomer",
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ReferenceCustomer/1/0"),
                        }

                    def __init__(
                        self,
                        referenceToCustomer: Optional[Union[aas.Reference, ReferenceToCustomer]] = None,
                        customerWebsite: Optional[Union[xsd.AnyURI, CustomerWebsite]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if referenceToCustomer is not None and not isinstance(referenceToCustomer, aas.SubmodelElement):
                            referenceToCustomer = self.ReferenceToCustomer(referenceToCustomer)

                        # Build a submodel element if a raw value was passed in the argument

                        if customerWebsite is not None and not isinstance(customerWebsite, aas.SubmodelElement):
                            customerWebsite = self.CustomerWebsite(customerWebsite)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(referenceToCustomer, customerWebsite)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"Customers",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Customers/1/0"),
                    }

                def __init__(
                    self,
                    totalNumberCustomers: Optional[Union[xsd.PositiveInteger, TotalNumberCustomers]] = None,
                    referenceCustomer: Optional[Iterable[ReferenceCustomer]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if totalNumberCustomers is not None and not isinstance(totalNumberCustomers, aas.SubmodelElement):
                        totalNumberCustomers = self.TotalNumberCustomers(totalNumberCustomers)

                    # A str would be split into its characters
                    if isinstance(referenceCustomer, str):
                        raise TypeError("referenceCustomer takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(totalNumberCustomers, referenceCustomer)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class TotalEmployees(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"TotalEmployees",
                        "value_type": xsd.PositiveInteger,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/TotalEmployees/1/0"),
                    }

                def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class ConsolidatedDataFile(aas.File):

                @staticmethod
                def template_defaults() -> FileMetadata:
                    return {
                        "id_short": r"ConsolidatedDataFile",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ConsolidatedDataFile/1/0"),
                    }

                def __init__(
                    self,
                    value: str,
                    content_type: Optional[str] = r"application/unknown",
                    **kwargs: Unpack[FileMetadata],
                ):

                    super().__init__(value=value, content_type=content_type, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"BusinessReportFigure",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BusinessReportFigure/1/0"),
                }

            def __init__(
                self,
                financialYear: Union[xsd.GYear, FinancialYear],
                beginOfReporttimeFrame: Union[xsd.Date, BeginOfReporttimeFrame],
                endOfReporttimeFrame: Union[xsd.Date, EndOfReporttimeFrame],
                yearOfPublication: Optional[Union[xsd.GYear, YearOfPublication]] = None,
                turnover: Optional[Union[str, Turnover]] = None,
                investmentVolume: Optional[Union[str, InvestmentVolume]] = None,
                equityRatio: Optional[Union[str, EquityRatio]] = None,
                customers: Optional[Customers] = None,
                totalEmployees: Optional[Union[xsd.PositiveInteger, TotalEmployees]] = None,
                consolidatedDataFile: Optional[ConsolidatedDataFile] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if financialYear is not None and not isinstance(financialYear, aas.SubmodelElement):
                    financialYear = self.FinancialYear(financialYear)

                # Build a submodel element if a raw value was passed in the argument

                if beginOfReporttimeFrame is not None and not isinstance(beginOfReporttimeFrame, aas.SubmodelElement):
                    beginOfReporttimeFrame = self.BeginOfReporttimeFrame(beginOfReporttimeFrame)

                # Build a submodel element if a raw value was passed in the argument

                if endOfReporttimeFrame is not None and not isinstance(endOfReporttimeFrame, aas.SubmodelElement):
                    endOfReporttimeFrame = self.EndOfReporttimeFrame(endOfReporttimeFrame)

                # Build a submodel element if a raw value was passed in the argument

                if yearOfPublication is not None and not isinstance(yearOfPublication, aas.SubmodelElement):
                    yearOfPublication = self.YearOfPublication(yearOfPublication)

                # Build a submodel element if a raw value was passed in the argument

                if turnover is not None and not isinstance(turnover, aas.SubmodelElement):
                    turnover = self.Turnover(turnover)

                # Build a submodel element if a raw value was passed in the argument

                if investmentVolume is not None and not isinstance(investmentVolume, aas.SubmodelElement):
                    investmentVolume = self.InvestmentVolume(investmentVolume)

                # Build a submodel element if a raw value was passed in the argument

                if equityRatio is not None and not isinstance(equityRatio, aas.SubmodelElement):
                    equityRatio = self.EquityRatio(equityRatio)

                # Build a submodel element if a raw value was passed in the argument

                if totalEmployees is not None and not isinstance(totalEmployees, aas.SubmodelElement):
                    totalEmployees = self.TotalEmployees(totalEmployees)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    financialYear,
                    beginOfReporttimeFrame,
                    endOfReporttimeFrame,
                    yearOfPublication,
                    turnover,
                    investmentVolume,
                    equityRatio,
                    customers,
                    totalEmployees,
                    consolidatedDataFile,
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"BusinessReportFigures",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/BusinessReportFigures/1/0"),
            }

        def __init__(
            self,
            lastReport: Union[aas.Reference, LastReport],
            businessReportFigure: Iterable[BusinessReportFigure],
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # Build a submodel element if a raw value was passed in the argument

            if lastReport is not None and not isinstance(lastReport, aas.SubmodelElement):
                lastReport = self.LastReport(lastReport)

            # A str would be split into its characters
            if isinstance(businessReportFigure, str):
                raise TypeError("businessReportFigure takes several elements, got a str")

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(lastReport, businessReportFigure)

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    class CompanyGovernance(aas.SubmodelElementCollection):

        class CorporatePolicies(aas.SubmodelElementCollection):

            class CodeOfConduct(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"CodeOfConduct",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CodeOfConduct/1/0"),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class GeneralTermsAndConditions(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"GeneralTermsAndConditions",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/GeneralTermsAndConditions/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class QualityAssuranceAgreements(aas.ReferenceElement):

                @staticmethod
                def template_defaults() -> ReferenceElementMetadata:
                    return {
                        "id_short": r"QualityAssuranceAgreements",
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/QualityAssuranceAgreements/1/0"
                        ),
                    }

                def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"CorporatePolicies",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CorporatePolicies/1/0"),
                }

            def __init__(
                self,
                codeOfConduct: Optional[Union[aas.Reference, CodeOfConduct]] = None,
                generalTermsAndConditions: Optional[Union[aas.Reference, GeneralTermsAndConditions]] = None,
                qualityAssuranceAgreements: Optional[Union[aas.Reference, QualityAssuranceAgreements]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if codeOfConduct is not None and not isinstance(codeOfConduct, aas.SubmodelElement):
                    codeOfConduct = self.CodeOfConduct(codeOfConduct)

                # Build a submodel element if a raw value was passed in the argument

                if generalTermsAndConditions is not None and not isinstance(
                    generalTermsAndConditions, aas.SubmodelElement
                ):
                    generalTermsAndConditions = self.GeneralTermsAndConditions(generalTermsAndConditions)

                # Build a submodel element if a raw value was passed in the argument

                if qualityAssuranceAgreements is not None and not isinstance(
                    qualityAssuranceAgreements, aas.SubmodelElement
                ):
                    qualityAssuranceAgreements = self.QualityAssuranceAgreements(qualityAssuranceAgreements)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    codeOfConduct, generalTermsAndConditions, qualityAssuranceAgreements
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class IndustryStandards(aas.SubmodelElementCollection):

            class Memberships(GeneratedSubmodelElementList):

                class Memberships_item(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": None,
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Association/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Memberships",
                        "type_value_list_element": aas.Property,
                        "value_type_list_element": str,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Memberships/1/0"),
                    }

                def __init__(
                    self,
                    memberships_items: Iterable[Union[str, Memberships_item]],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(memberships_items, str):
                        raise TypeError("memberships_items takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if memberships_items:
                        memberships_items = [
                            i if isinstance(i, aas.SubmodelElement) else self.Memberships_item(i)
                            for i in memberships_items
                        ]

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(memberships_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Certifications(GeneratedSubmodelElementList):

                class Certifications_item(aas.SubmodelElementCollection):

                    class CertificationStandard(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CertificationStandard",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/CertificationStandard/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ApprovalAgency(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ApprovalAgency",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/ApprovalAgency/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CertificateNumber(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CertificateNumber",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/CertificateNumber/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class IssueDate(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"IssueDate",
                                "value_type": xsd.Date,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/IssueDate/1/0"),
                            }

                        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class ExpiryDate(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"ExpiryDate",
                                "value_type": xsd.Date,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ExpiryDate/1/0"),
                            }

                        def __init__(self, value: xsd.Date, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CertificationDocument(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"CertificationDocument",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/CertificationDocument/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class CertificationURL(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"CertificationURL",
                                "value_type": xsd.AnyURI,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/CertificationURL/1/0"
                                ),
                            }

                        def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Certification/1/0"),
                        }

                    def __init__(
                        self,
                        certificationStandard: Optional[Union[str, CertificationStandard]] = None,
                        approvalAgency: Optional[Union[str, ApprovalAgency]] = None,
                        certificateNumber: Optional[Union[str, CertificateNumber]] = None,
                        issueDate: Optional[Union[xsd.Date, IssueDate]] = None,
                        expiryDate: Optional[Union[xsd.Date, ExpiryDate]] = None,
                        certificationDocument: Optional[Iterable[Union[aas.Reference, CertificationDocument]]] = None,
                        certificationURL: Optional[Union[xsd.AnyURI, CertificationURL]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if certificationStandard is not None and not isinstance(
                            certificationStandard, aas.SubmodelElement
                        ):
                            certificationStandard = self.CertificationStandard(certificationStandard)

                        # Build a submodel element if a raw value was passed in the argument

                        if approvalAgency is not None and not isinstance(approvalAgency, aas.SubmodelElement):
                            approvalAgency = self.ApprovalAgency(approvalAgency)

                        # Build a submodel element if a raw value was passed in the argument

                        if certificateNumber is not None and not isinstance(certificateNumber, aas.SubmodelElement):
                            certificateNumber = self.CertificateNumber(certificateNumber)

                        # Build a submodel element if a raw value was passed in the argument

                        if issueDate is not None and not isinstance(issueDate, aas.SubmodelElement):
                            issueDate = self.IssueDate(issueDate)

                        # Build a submodel element if a raw value was passed in the argument

                        if expiryDate is not None and not isinstance(expiryDate, aas.SubmodelElement):
                            expiryDate = self.ExpiryDate(expiryDate)

                        # A str would be split into its characters
                        if isinstance(certificationDocument, str):
                            raise TypeError("certificationDocument takes several elements, got a str")

                        # Build submodel elements from raw values passed in the argument
                        if certificationDocument:
                            certificationDocument = [
                                i if isinstance(i, aas.SubmodelElement) else self.CertificationDocument(i)
                                for i in certificationDocument
                            ]

                        # Build a submodel element if a raw value was passed in the argument

                        if certificationURL is not None and not isinstance(certificationURL, aas.SubmodelElement):
                            certificationURL = self.CertificationURL(certificationURL)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            certificationStandard,
                            approvalAgency,
                            certificateNumber,
                            issueDate,
                            expiryDate,
                            certificationDocument,
                            certificationURL,
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Certifications",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Certifications/1/0"),
                    }

                def __init__(
                    self,
                    certifications_items: Iterable[Certifications_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(certifications_items, str):
                        raise TypeError("certifications_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(certifications_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"IndustryStandards",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/IndustryStandards/1/0"),
                }

            def __init__(
                self,
                memberships: Optional[Union[Iterable[Union[str, Memberships.Memberships_item]], Memberships]] = None,
                certifications: Optional[Union[Iterable[Certifications.Certifications_item], Certifications]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # A str would be split into its characters
                if isinstance(memberships, str):
                    raise TypeError("memberships takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if memberships is not None and not isinstance(memberships, aas.SubmodelElement):
                    memberships = self.Memberships(memberships)

                # A str would be split into its characters
                if isinstance(certifications, str):
                    raise TypeError("certifications takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if certifications is not None and not isinstance(certifications, aas.SubmodelElement):
                    certifications = self.Certifications(certifications)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(memberships, certifications)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class RiskManagement(aas.SubmodelElementCollection):

            class BusinessContinuityPlan(aas.Property):

                @staticmethod
                def template_defaults() -> PropertyMetadata:
                    return {
                        "id_short": r"BusinessContinuityPlan",
                        "value_type": bool,
                        "semantic_id": global_ref(
                            r"https://admin-shell.io/idta/CompanyData/BusinessContinuityPlan/1/0"
                        ),
                    }

                def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                    super().__init__(value=value, **(self.template_defaults() | kwargs))

            class EmployeeTrainings(GeneratedSubmodelElementList):

                class Employeetrainings_item(aas.SubmodelElementCollection):

                    class TypeOfTraining(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"TypeOfTraining",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/TypeOfTraining/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class TrainingDocumentation(aas.ReferenceElement):

                        @staticmethod
                        def template_defaults() -> ReferenceElementMetadata:
                            return {
                                "id_short": r"TrainingDocumentation",
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/TrainingDocumentation/1/0"
                                ),
                            }

                        def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EmployeeTraining/1/0"),
                        }

                    def __init__(
                        self,
                        typeOfTraining: Union[str, TypeOfTraining],
                        trainingDocumentation: Optional[Union[aas.Reference, TrainingDocumentation]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if typeOfTraining is not None and not isinstance(typeOfTraining, aas.SubmodelElement):
                            typeOfTraining = self.TypeOfTraining(typeOfTraining)

                        # Build a submodel element if a raw value was passed in the argument

                        if trainingDocumentation is not None and not isinstance(
                            trainingDocumentation, aas.SubmodelElement
                        ):
                            trainingDocumentation = self.TrainingDocumentation(trainingDocumentation)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(typeOfTraining, trainingDocumentation)

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"EmployeeTrainings",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/EmployeeTrainings/1/0"),
                    }

                def __init__(
                    self,
                    employeetrainings_items: Iterable[Employeetrainings_item],
                    **kwargs: Unpack[SubmodelElementListMetadata],
                ):

                    # A str would be split into its characters
                    if isinstance(employeetrainings_items, str):
                        raise TypeError("employeetrainings_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        employeetrainings_items, number_repeated=False
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class SecurityPolicies(aas.SubmodelElementCollection):

                class InformationSecurityPolicy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"InformationSecurityPolicy",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/InformationSecurityPolicy/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DataProtectionPolicy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DataProtectionPolicy",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/DataProtectionPolicy/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PasswordPolicy(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PasswordPolicy",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/PasswordPolicy/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AuthorizationConcept(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AuthorizationConcept",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/AuthorizationConcept/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class AccessControlProcess(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"AccessControlProcess",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/AccessControlProcess/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class UserAccessInventory(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"UserAccessInventory",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/UserAccessInventory/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class PermissionDocumentation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"PermissionDocumentation",
                            "value_type": bool,
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/PermissionDocumentation/1/0"
                            ),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class LockingSystem(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"LockingSystem",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/LockingSystem/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class KeyAllocation(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"KeyAllocation",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/KeyAllocation/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VisitorLog(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VisitorLog",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/VisitorLog/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VisitorEscort(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VisitorEscort",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/VisitorEscort/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class VisitorBadge(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"VisitorBadge",
                            "value_type": bool,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/VisitorBadge/1/0"),
                        }

                    def __init__(self, value: bool, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class CustomerAudits(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"CustomerAudits",
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CustomerAudits/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": r"SecurityPolicies",
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/SecurityPolicies/1/0"),
                    }

                def __init__(
                    self,
                    informationSecurityPolicy: Optional[Union[bool, InformationSecurityPolicy]] = None,
                    dataProtectionPolicy: Optional[Union[bool, DataProtectionPolicy]] = None,
                    passwordPolicy: Optional[Union[bool, PasswordPolicy]] = None,
                    authorizationConcept: Optional[Union[bool, AuthorizationConcept]] = None,
                    accessControlProcess: Optional[Union[bool, AccessControlProcess]] = None,
                    userAccessInventory: Optional[Union[bool, UserAccessInventory]] = None,
                    permissionDocumentation: Optional[Union[bool, PermissionDocumentation]] = None,
                    lockingSystem: Optional[Union[bool, LockingSystem]] = None,
                    keyAllocation: Optional[Union[bool, KeyAllocation]] = None,
                    visitorLog: Optional[Union[bool, VisitorLog]] = None,
                    visitorEscort: Optional[Union[bool, VisitorEscort]] = None,
                    visitorBadge: Optional[Union[bool, VisitorBadge]] = None,
                    customerAudits: Optional[Union[str, CustomerAudits]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if informationSecurityPolicy is not None and not isinstance(
                        informationSecurityPolicy, aas.SubmodelElement
                    ):
                        informationSecurityPolicy = self.InformationSecurityPolicy(informationSecurityPolicy)

                    # Build a submodel element if a raw value was passed in the argument

                    if dataProtectionPolicy is not None and not isinstance(dataProtectionPolicy, aas.SubmodelElement):
                        dataProtectionPolicy = self.DataProtectionPolicy(dataProtectionPolicy)

                    # Build a submodel element if a raw value was passed in the argument

                    if passwordPolicy is not None and not isinstance(passwordPolicy, aas.SubmodelElement):
                        passwordPolicy = self.PasswordPolicy(passwordPolicy)

                    # Build a submodel element if a raw value was passed in the argument

                    if authorizationConcept is not None and not isinstance(authorizationConcept, aas.SubmodelElement):
                        authorizationConcept = self.AuthorizationConcept(authorizationConcept)

                    # Build a submodel element if a raw value was passed in the argument

                    if accessControlProcess is not None and not isinstance(accessControlProcess, aas.SubmodelElement):
                        accessControlProcess = self.AccessControlProcess(accessControlProcess)

                    # Build a submodel element if a raw value was passed in the argument

                    if userAccessInventory is not None and not isinstance(userAccessInventory, aas.SubmodelElement):
                        userAccessInventory = self.UserAccessInventory(userAccessInventory)

                    # Build a submodel element if a raw value was passed in the argument

                    if permissionDocumentation is not None and not isinstance(
                        permissionDocumentation, aas.SubmodelElement
                    ):
                        permissionDocumentation = self.PermissionDocumentation(permissionDocumentation)

                    # Build a submodel element if a raw value was passed in the argument

                    if lockingSystem is not None and not isinstance(lockingSystem, aas.SubmodelElement):
                        lockingSystem = self.LockingSystem(lockingSystem)

                    # Build a submodel element if a raw value was passed in the argument

                    if keyAllocation is not None and not isinstance(keyAllocation, aas.SubmodelElement):
                        keyAllocation = self.KeyAllocation(keyAllocation)

                    # Build a submodel element if a raw value was passed in the argument

                    if visitorLog is not None and not isinstance(visitorLog, aas.SubmodelElement):
                        visitorLog = self.VisitorLog(visitorLog)

                    # Build a submodel element if a raw value was passed in the argument

                    if visitorEscort is not None and not isinstance(visitorEscort, aas.SubmodelElement):
                        visitorEscort = self.VisitorEscort(visitorEscort)

                    # Build a submodel element if a raw value was passed in the argument

                    if visitorBadge is not None and not isinstance(visitorBadge, aas.SubmodelElement):
                        visitorBadge = self.VisitorBadge(visitorBadge)

                    # Build a submodel element if a raw value was passed in the argument

                    if customerAudits is not None and not isinstance(customerAudits, aas.SubmodelElement):
                        customerAudits = self.CustomerAudits(customerAudits)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        informationSecurityPolicy,
                        dataProtectionPolicy,
                        passwordPolicy,
                        authorizationConcept,
                        accessControlProcess,
                        userAccessInventory,
                        permissionDocumentation,
                        lockingSystem,
                        keyAllocation,
                        visitorLog,
                        visitorEscort,
                        visitorBadge,
                        customerAudits,
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            class Insurances(GeneratedSubmodelElementList):

                class Insurances_item(aas.SubmodelElementCollection):

                    class InsuranceCompany(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"InsuranceCompany",
                                "value_type": str,
                                "semantic_id": global_ref(
                                    r"https://admin-shell.io/idta/CompanyData/InsuranceCompany/1/0"
                                ),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class InsuranceType(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"InsuranceType",
                                "value_type": str,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/InsuranceType/1/0"),
                            }

                        def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    class InsuranceSum(aas.Property):

                        @staticmethod
                        def template_defaults() -> PropertyMetadata:
                            return {
                                "id_short": r"InsuranceSum",
                                "value_type": xsd.PositiveInteger,
                                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/InsuranceSum/1/0"),
                            }

                        def __init__(self, value: xsd.PositiveInteger, **kwargs: Unpack[PropertyMetadata]):

                            super().__init__(value=value, **(self.template_defaults() | kwargs))

                    @staticmethod
                    def template_defaults() -> SubmodelElementCollectionMetadata:
                        return {
                            "id_short": None,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Insurance/1/0"),
                        }

                    def __init__(
                        self,
                        insuranceType: Union[str, InsuranceType],
                        insuranceCompany: Optional[Union[str, InsuranceCompany]] = None,
                        insuranceSum: Optional[Union[xsd.PositiveInteger, InsuranceSum]] = None,
                        **kwargs: Unpack[SubmodelElementCollectionMetadata],
                    ):

                        # Build a submodel element if a raw value was passed in the argument

                        if insuranceCompany is not None and not isinstance(insuranceCompany, aas.SubmodelElement):
                            insuranceCompany = self.InsuranceCompany(insuranceCompany)

                        # Build a submodel element if a raw value was passed in the argument

                        if insuranceType is not None and not isinstance(insuranceType, aas.SubmodelElement):
                            insuranceType = self.InsuranceType(insuranceType)

                        # Build a submodel element if a raw value was passed in the argument

                        if insuranceSum is not None and not isinstance(insuranceSum, aas.SubmodelElement):
                            insuranceSum = self.InsuranceSum(insuranceSum)

                        # Add all passed/initialized submodel elements to a single list

                        embedded_submodel_elements = collect_submodel_elements(
                            insuranceCompany, insuranceType, insuranceSum
                        )

                        super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementListMetadata:
                    return {
                        "id_short": r"Insurances",
                        "type_value_list_element": aas.SubmodelElementCollection,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Insurances/1/0"),
                    }

                def __init__(
                    self, insurances_items: Iterable[Insurances_item], **kwargs: Unpack[SubmodelElementListMetadata]
                ):

                    # A str would be split into its characters
                    if isinstance(insurances_items, str):
                        raise TypeError("insurances_items takes several elements, got a str")

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(insurances_items, number_repeated=False)

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementCollectionMetadata:
                return {
                    "id_short": r"RiskManagement",
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/RiskManagement/1/0"),
                }

            def __init__(
                self,
                businessContinuityPlan: Optional[Union[bool, BusinessContinuityPlan]] = None,
                employeeTrainings: Optional[
                    Union[Iterable[EmployeeTrainings.Employeetrainings_item], EmployeeTrainings]
                ] = None,
                securityPolicies: Optional[SecurityPolicies] = None,
                insurances: Optional[Union[Iterable[Insurances.Insurances_item], Insurances]] = None,
                **kwargs: Unpack[SubmodelElementCollectionMetadata],
            ):

                # Build a submodel element if a raw value was passed in the argument

                if businessContinuityPlan is not None and not isinstance(businessContinuityPlan, aas.SubmodelElement):
                    businessContinuityPlan = self.BusinessContinuityPlan(businessContinuityPlan)

                # A str would be split into its characters
                if isinstance(employeeTrainings, str):
                    raise TypeError("employeeTrainings takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if employeeTrainings is not None and not isinstance(employeeTrainings, aas.SubmodelElement):
                    employeeTrainings = self.EmployeeTrainings(employeeTrainings)

                # A str would be split into its characters
                if isinstance(insurances, str):
                    raise TypeError("insurances takes several elements, got a str")

                # Build a submodel element if a raw value was passed in the argument

                if insurances is not None and not isinstance(insurances, aas.SubmodelElement):
                    insurances = self.Insurances(insurances)

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(
                    businessContinuityPlan, employeeTrainings, securityPolicies, insurances
                )

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        class LegalCompliance(GeneratedSubmodelElementList):

            class Legalcompliance_item(aas.SubmodelElementCollection):

                class ComplianceStatus(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"ComplianceStatus",
                            "value_type": str,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/ComplianceStatus/1/0"),
                        }

                    def __init__(self, value: str, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class ComplianceStatement(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"ComplianceStatement",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/ComplianceStatement/1/0"
                            ),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DocumentationURI(aas.Property):

                    @staticmethod
                    def template_defaults() -> PropertyMetadata:
                        return {
                            "id_short": r"DocumentationURI",
                            "value_type": xsd.AnyURI,
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/DocumentationURI /1/0"),
                        }

                    def __init__(self, value: xsd.AnyURI, **kwargs: Unpack[PropertyMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class DocumentationReference(aas.ReferenceElement):

                    @staticmethod
                    def template_defaults() -> ReferenceElementMetadata:
                        return {
                            "id_short": r"DocumentationReference",
                            "semantic_id": global_ref(
                                r"https://admin-shell.io/idta/CompanyData/DocumentationReference/1/0"
                            ),
                        }

                    def __init__(self, value: aas.Reference, **kwargs: Unpack[ReferenceElementMetadata]):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                class RegulationName(aas.MultiLanguageProperty):

                    @staticmethod
                    def template_defaults() -> MultiLanguagePropertyMetadata:
                        return {
                            "id_short": r"RegulationName",
                            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/RegulationName/1/0"),
                        }

                    def __init__(
                        self, value: aas.MultiLanguageTextType, **kwargs: Unpack[MultiLanguagePropertyMetadata]
                    ):

                        super().__init__(value=value, **(self.template_defaults() | kwargs))

                @staticmethod
                def template_defaults() -> SubmodelElementCollectionMetadata:
                    return {
                        "id_short": None,
                        "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/Regulation/1/0"),
                    }

                def __init__(
                    self,
                    complianceStatus: Union[str, ComplianceStatus],
                    regulationName: Union[aas.MultiLanguageTextType, RegulationName],
                    complianceStatement: Optional[Union[aas.MultiLanguageTextType, ComplianceStatement]] = None,
                    documentationURI: Optional[Iterable[Union[xsd.AnyURI, DocumentationURI]]] = None,
                    documentationReference: Optional[Iterable[Union[aas.Reference, DocumentationReference]]] = None,
                    **kwargs: Unpack[SubmodelElementCollectionMetadata],
                ):

                    # Build a submodel element if a raw value was passed in the argument

                    if complianceStatus is not None and not isinstance(complianceStatus, aas.SubmodelElement):
                        complianceStatus = self.ComplianceStatus(complianceStatus)

                    # Build a submodel element if a raw value was passed in the argument

                    if complianceStatement is not None and not isinstance(complianceStatement, aas.SubmodelElement):
                        complianceStatement = self.ComplianceStatement(complianceStatement)

                    # A str would be split into its characters
                    if isinstance(documentationURI, str):
                        raise TypeError("documentationURI takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if documentationURI:
                        documentationURI = [
                            i if isinstance(i, aas.SubmodelElement) else self.DocumentationURI(i)
                            for i in documentationURI
                        ]

                    # A str would be split into its characters
                    if isinstance(documentationReference, str):
                        raise TypeError("documentationReference takes several elements, got a str")

                    # Build submodel elements from raw values passed in the argument
                    if documentationReference:
                        documentationReference = [
                            i if isinstance(i, aas.SubmodelElement) else self.DocumentationReference(i)
                            for i in documentationReference
                        ]

                    # Build a submodel element if a raw value was passed in the argument

                    if regulationName is not None and not isinstance(regulationName, aas.SubmodelElement):
                        regulationName = self.RegulationName(regulationName)

                    # Add all passed/initialized submodel elements to a single list

                    embedded_submodel_elements = collect_submodel_elements(
                        complianceStatus, complianceStatement, documentationURI, documentationReference, regulationName
                    )

                    super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

            @staticmethod
            def template_defaults() -> SubmodelElementListMetadata:
                return {
                    "id_short": r"LegalCompliance",
                    "type_value_list_element": aas.SubmodelElementCollection,
                    "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/LegalCompliance/1/0"),
                }

            def __init__(
                self,
                legalcompliance_items: Iterable[Legalcompliance_item],
                **kwargs: Unpack[SubmodelElementListMetadata],
            ):

                # A str would be split into its characters
                if isinstance(legalcompliance_items, str):
                    raise TypeError("legalcompliance_items takes several elements, got a str")

                # Add all passed/initialized submodel elements to a single list

                embedded_submodel_elements = collect_submodel_elements(legalcompliance_items, number_repeated=False)

                super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

        @staticmethod
        def template_defaults() -> SubmodelElementCollectionMetadata:
            return {
                "id_short": r"CompanyGovernance",
                "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/CompanyGovernance/1/0"),
            }

        def __init__(
            self,
            corporatePolicies: Optional[CorporatePolicies] = None,
            industryStandards: Optional[IndustryStandards] = None,
            riskManagement: Optional[RiskManagement] = None,
            legalCompliance: Optional[Union[Iterable[LegalCompliance.Legalcompliance_item], LegalCompliance]] = None,
            **kwargs: Unpack[SubmodelElementCollectionMetadata],
        ):

            # A str would be split into its characters
            if isinstance(legalCompliance, str):
                raise TypeError("legalCompliance takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if legalCompliance is not None and not isinstance(legalCompliance, aas.SubmodelElement):
                legalCompliance = self.LegalCompliance(legalCompliance)

            # Add all passed/initialized submodel elements to a single list

            embedded_submodel_elements = collect_submodel_elements(
                corporatePolicies, industryStandards, riskManagement, legalCompliance
            )

            super().__init__(value=embedded_submodel_elements, **(self.template_defaults() | kwargs))

    @staticmethod
    def template_defaults() -> SubmodelMetadata:
        return {
            "id_short": r"CompanyData",
            "description": aas.MultiLanguageTextType(dict_={r"en": r"Contains information about a company"}),
            "administration": aas.AdministrativeInformation(
                version=r"1",
                revision=r"0",
                creator=None,
                template_id=r"https://admin-shell.io/IDTA_02068",
                embedded_data_specifications=[],
            ),
            "semantic_id": global_ref(r"https://admin-shell.io/idta/CompanyData/1/0/CompanyData"),
        }

    def __init__(
        self,
        id_: str,
        companyIdentification: CompanyIdentification,
        bankAccounts: Optional[BankAccounts] = None,
        digitalInterfaces: Optional[DigitalInterfaces] = None,
        businessReportFigures: Optional[BusinessReportFigures] = None,
        companyGovernance: Optional[CompanyGovernance] = None,
        **kwargs: Unpack[SubmodelMetadata],
    ):

        # Add all passed/initialized submodel elements to a single list

        embedded_submodel_elements = collect_submodel_elements(
            companyIdentification, bankAccounts, digitalInterfaces, businessReportFigures, companyGovernance
        )

        super().__init__(submodel_element=embedded_submodel_elements, id_=id_, **(self.template_defaults() | kwargs))
