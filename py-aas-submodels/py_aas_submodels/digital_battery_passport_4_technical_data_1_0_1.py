from typing import Any, ForwardRef, Iterable, Optional, Tuple, Union
from basyx.aas import model as aas
from basyx.aas.model import datatypes as xsd


class TechnicalData(aas.Submodel):

    class GeneralInformation(aas.SubmodelElementCollection):

        class ManufacturerName(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerName",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market.\n\nDIN DKE Spec 99100 chapter reference: 6.1.2.4 c) "
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-AAO677#004",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-AAO677-004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#manufacturerName",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                        aas.Qualifier(
                            type_=r"ExampleValue",
                            value_type=str,
                            value=r"Example Company",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
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

        class CompanyLogo(aas.File):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"CompanyLogo",
                content_type: Optional[str] = r"image/png",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"Imagefile for logo of manufacturer provided in common format (.png, .jpg)."
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABI776#002",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABI776-002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#companyLogo",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

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

        class ManufacturerIdentifier(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"ManufacturerIdentifier",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#manufacturerIdentifier",
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

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
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

        class BatteryCategory(aas.Property):

            def __init__(
                self,
                value: str,
                id_short: Optional[str] = r"BatteryCategory",
                value_type: aas.DataTypeDefXsd = str,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": 'A battery passport must include the battery category.\n\nThe battery category must be provided on the battery label.\n\nThe battery must be categorised by its intended use in (string values):\n- "lmt"\n- "ev" \n- "industrial", or\n- "stationary"\n\nDIN DKE Spec 99100 chapter reference: 6.1.3.5\n\n'
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryCategory",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAR724#007",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
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

        class BatteryMass(aas.Property):

            def __init__(
                self,
                value: xsd.Float,
                id_short: Optional[str] = r"BatteryMass",
                value_type: aas.DataTypeDefXsd = xsd.Float,
                value_id: Optional[aas.Reference] = None,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = r"PARAMETER",
                description: Optional[aas.MultiLanguageTextType] = None,
                semantic_id: Optional[aas.Reference] = aas.ModelReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryMass",
                        ),
                    ),
                    type_=aas.ConceptDescription,
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAF040#010",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
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

        class ProductImages(aas.SubmodelElementList):

            class Productimages_item(aas.File):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = None,
                    content_type: Optional[str] = r"image/png",
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": r"Image file for associated product provided in common format (.png, .jpg)."
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABM220#001/0173-1#01-AHY911#001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.shared:3.1.0#ResourceWithContentType",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"SMT/Cardinality",
                                value_type=str,
                                value=r"OneToMany",
                                value_id=None,
                                kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

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
                productimages_items: Iterable[Productimages_item],
                id_short: Optional[str] = r"ProductImages",
                type_value_list_element: aas.SubmodelElement = aas.File,
                semantic_id_list_element: Optional[
                    aas.Reference
                ] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABM220#001/0173-1#01-AHY911#001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                order_relevant: bool = True,
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": r"List for image file(s) for associated product provided in common format (.png, .jpg)."
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"0173-1#02-ABM220#001",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"https://api.eclass-cdp.com/0173-1-02-ABM220-001",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#productImages",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"ZeroToOne",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # A str would be split into its characters
                if isinstance(productimages_items, str):
                    raise TypeError(
                        "productimages_items takes several elements, got a str"
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [productimages_items]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, aas.SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        embedded_submodel_elements.extend(se_arg)
                    else:
                        raise TypeError(
                            f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                        )

                super().__init__(
                    value=embedded_submodel_elements,
                    id_short=id_short,
                    type_value_list_element=type_value_list_element,
                    semantic_id_list_element=semantic_id_list_element,
                    value_type_list_element=value_type_list_element,
                    order_relevant=order_relevant,
                    display_name=display_name,
                    category=category,
                    description=description,
                    semantic_id=semantic_id,
                    qualifier=qualifier,
                    extension=extension,
                    supplemental_semantic_id=supplemental_semantic_id,
                    embedded_data_specifications=embedded_data_specifications,
                )

            def _check_constraints(self, new, existing) -> None:
                # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                saved_id_short = new.id_short
                new.id_short = None

                # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
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
                if (
                    new.semantic_id is not None
                    and self.semantic_id_list_element is None
                ):
                    for item in existing:
                        if (
                            item.semantic_id is not None
                            and new.semantic_id != item.semantic_id
                        ):
                            raise aas.AASConstraintViolation(
                                114,
                                f"Element to be added {new!r} has semantic_id "
                                f"{new.semantic_id!r}, while already contained element "
                                f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                "aren't equal.",
                            )

                # Re-assign id_short
                new.id_short = saved_id_short

        class WarrantyInformation(aas.SubmodelElementCollection):

            class WarrantyPeriod(aas.Property):

                def __init__(
                    self,
                    value: str,
                    id_short: Optional[str] = r"WarrantyPeriod",
                    value_type: aas.DataTypeDefXsd = str,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(dict_={r"en": r"warranty period"}),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyPeriod",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-AAX540#004",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                warrantyPeriod: Union[str, WarrantyPeriod],
                id_short: Optional[str] = r"WarrantyInformation",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(dict_={r"en": r"warranty information"}),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyInformation",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-AAO677#004",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = ()

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if warrantyPeriod is not None and not isinstance(
                    warrantyPeriod, aas.SubmodelElement
                ):
                    warrantyPeriod = self.WarrantyPeriod(warrantyPeriod)

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [warrantyPeriod]:
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

        def __init__(
            self,
            manufacturerName: Union[str, ManufacturerName],
            manufacturerIdentifier: Union[str, ManufacturerIdentifier],
            batteryCategory: Union[str, BatteryCategory],
            batteryMass: Union[xsd.Float, BatteryMass],
            warrantyInformation: WarrantyInformation,
            companyLogo: Optional[CompanyLogo] = None,
            productImages: Optional[
                Union[Iterable[ProductImages.Productimages_item], ProductImages]
            ] = None,
            id_short: Optional[str] = r"GeneralInformation",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABK161#002/0173-1#01-AHX838#002",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#generalInformation",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerName is not None and not isinstance(
                manufacturerName, aas.SubmodelElement
            ):
                manufacturerName = self.ManufacturerName(manufacturerName)

            # Build a submodel element if a raw value was passed in the argument

            if manufacturerIdentifier is not None and not isinstance(
                manufacturerIdentifier, aas.SubmodelElement
            ):
                manufacturerIdentifier = self.ManufacturerIdentifier(
                    manufacturerIdentifier
                )

            # Build a submodel element if a raw value was passed in the argument

            if batteryCategory is not None and not isinstance(
                batteryCategory, aas.SubmodelElement
            ):
                batteryCategory = self.BatteryCategory(batteryCategory)

            # Build a submodel element if a raw value was passed in the argument

            if batteryMass is not None and not isinstance(
                batteryMass, aas.SubmodelElement
            ):
                batteryMass = self.BatteryMass(batteryMass)

            # A str would be split into its characters
            if isinstance(productImages, str):
                raise TypeError("productImages takes several elements, got a str")

            # Build a submodel element if a raw value was passed in the argument

            if productImages is not None and not isinstance(
                productImages, aas.SubmodelElement
            ):
                productImages = self.ProductImages(productImages)

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                manufacturerName,
                companyLogo,
                manufacturerIdentifier,
                batteryCategory,
                batteryMass,
                productImages,
                warrantyInformation,
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

    class TechnicalPropertyAreas(aas.SubmodelElementCollection):

        class CapacityEnergyVoltage(aas.SubmodelElementCollection):

            class NominalVoltage(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"NominalVoltage",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "voltage - NOM\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.11"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL588#001",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#nominalVoltage",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class MinVoltage(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"MinVoltage",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "voltage - MIN\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.9"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL587#001",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#minimumVoltage",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class MaxVoltage(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"MaxVoltage",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "voltage - MAX\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.10"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL589#001",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumVoltage",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class RatedCapacity(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"RatedCapacity",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "rated capacity\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.2"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL869#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedCapacity",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class CapacityFade(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"CapacityFade",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "capacity fade\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.4"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL828#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityFade",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class CertifiedUsableBatteryEnergy(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"CertifiedUsableBatteryEnergy",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Certified usable battery energy (UBE certified)\n\nDIN DKE Spec 99100 chapter reference: 6.7.2.5"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL829#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedEnergy",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                nominalVoltage: Union[xsd.Float, NominalVoltage],
                minVoltage: Union[xsd.Float, MinVoltage],
                maxVoltage: Union[xsd.Float, MaxVoltage],
                ratedCapacity: Union[xsd.Float, RatedCapacity],
                capacityFade: Optional[Union[xsd.Float, CapacityFade]] = None,
                certifiedUsableBatteryEnergy: Optional[
                    Union[xsd.Float, CertifiedUsableBatteryEnergy]
                ] = None,
                id_short: Optional[str] = r"CapacityEnergyVoltage",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information on battery capacity, energy and voltage.\n\nDIN DKE Spec 99100 chapter reference: 6.7.2"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityEnergyVoltage",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if nominalVoltage is not None and not isinstance(
                    nominalVoltage, aas.SubmodelElement
                ):
                    nominalVoltage = self.NominalVoltage(nominalVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if minVoltage is not None and not isinstance(
                    minVoltage, aas.SubmodelElement
                ):
                    minVoltage = self.MinVoltage(minVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if maxVoltage is not None and not isinstance(
                    maxVoltage, aas.SubmodelElement
                ):
                    maxVoltage = self.MaxVoltage(maxVoltage)

                # Build a submodel element if a raw value was passed in the argument

                if ratedCapacity is not None and not isinstance(
                    ratedCapacity, aas.SubmodelElement
                ):
                    ratedCapacity = self.RatedCapacity(ratedCapacity)

                # Build a submodel element if a raw value was passed in the argument

                if capacityFade is not None and not isinstance(
                    capacityFade, aas.SubmodelElement
                ):
                    capacityFade = self.CapacityFade(capacityFade)

                # Build a submodel element if a raw value was passed in the argument

                if certifiedUsableBatteryEnergy is not None and not isinstance(
                    certifiedUsableBatteryEnergy, aas.SubmodelElement
                ):
                    certifiedUsableBatteryEnergy = self.CertifiedUsableBatteryEnergy(
                        certifiedUsableBatteryEnergy
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    nominalVoltage,
                    minVoltage,
                    maxVoltage,
                    ratedCapacity,
                    capacityFade,
                    certifiedUsableBatteryEnergy,
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

        class RoundTripEnergyEfficiency(aas.SubmodelElementCollection):

            class InitialRoundTripEnergyEfficiency(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"InitialRoundTripEnergyEfficiency",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "initial round trip energy efficiency\n\nDIN DKE Spec 99100 chapter reference: 6.7.4.2"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL833#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialRoundTripEnergyEfficiency",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class RoundTripEnergyEfficiencyAt50PercentOfCycleLife(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[
                        str
                    ] = r"RoundTripEnergyEfficiencyAt50PercentOfCycleLife",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "round trip energy efficiency at 50% of cycle life\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.3"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL866#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEfficiencyAt50PercentCycleLife",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class EnergyRoundTripEfficiencyFade(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"EnergyRoundTripEfficiencyFade",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "round trip energy efficiency fade\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.5"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL827#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#energyRoundTripEfficiencyFade",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InitialSelfDischargingRate(aas.Property):

                def __init__(
                    self,
                    value: int,
                    id_short: Optional[str] = r"InitialSelfDischargingRate",
                    value_type: aas.DataTypeDefXsd = int,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "initial self-discharging rate\n\nDIN DKE Spec 99100 chapter reference:  6.7.4.6"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL834#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialSelfDischargingRate",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                initialRoundTripEnergyEfficiency: Union[
                    int, InitialRoundTripEnergyEfficiency
                ],
                roundTripEnergyEfficiencyAt50PercentOfCycleLife: Union[
                    int, RoundTripEnergyEfficiencyAt50PercentOfCycleLife
                ],
                energyRoundTripEfficiencyFade: Optional[
                    Union[xsd.Float, EnergyRoundTripEfficiencyFade]
                ] = None,
                initialSelfDischargingRate: Optional[
                    Union[int, InitialSelfDischargingRate]
                ] = None,
                id_short: Optional[str] = r"RoundTripEnergyEfficiency",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information regarding round trip energy efficiency.\n\nDIN DKE Spec 99100 chapter reference: 6.7.4"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEnergyEfficiency",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if initialRoundTripEnergyEfficiency is not None and not isinstance(
                    initialRoundTripEnergyEfficiency, aas.SubmodelElement
                ):
                    initialRoundTripEnergyEfficiency = (
                        self.InitialRoundTripEnergyEfficiency(
                            initialRoundTripEnergyEfficiency
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife is not None
                    and not isinstance(
                        roundTripEnergyEfficiencyAt50PercentOfCycleLife,
                        aas.SubmodelElement,
                    )
                ):
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife = (
                        self.RoundTripEnergyEfficiencyAt50PercentOfCycleLife(
                            roundTripEnergyEfficiencyAt50PercentOfCycleLife
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if energyRoundTripEfficiencyFade is not None and not isinstance(
                    energyRoundTripEfficiencyFade, aas.SubmodelElement
                ):
                    energyRoundTripEfficiencyFade = self.EnergyRoundTripEfficiencyFade(
                        energyRoundTripEfficiencyFade
                    )

                # Build a submodel element if a raw value was passed in the argument

                if initialSelfDischargingRate is not None and not isinstance(
                    initialSelfDischargingRate, aas.SubmodelElement
                ):
                    initialSelfDischargingRate = self.InitialSelfDischargingRate(
                        initialSelfDischargingRate
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    initialRoundTripEnergyEfficiency,
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife,
                    energyRoundTripEfficiencyFade,
                    initialSelfDischargingRate,
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

        class Resistance(aas.SubmodelElementCollection):

            class InitialInternalResistanceOnBatteryCellLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InitialInternalResistanceOnBatteryCellLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Internal battery cell and pack resistance - Internal resistance (in Ohm)\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL844#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryCell",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InitialInternalResistanceOnBatteryPackLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InitialInternalResistanceOnBatteryPackLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Initial (Pre-Use) internal resistance on battery pack level. \n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL846#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryPack",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InitialInternalResistanceOnBatteryModuleLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InitialInternalResistanceOnBatteryModuleLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Initial internal resistance on battery module level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.2"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL832#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InternalResistanceIncreaseOfBatteryCellLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InternalResistanceIncreaseOfBatteryCellLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "initial internal resistance on battery cell level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.3"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryCell",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL831#002",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InternalResistanceIncreaseOfBatteryPackLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InternalResistanceIncreaseOfBatteryPackLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "initial internal resistance on battery pack level\n\nDIN DKE Spec 99100 chapter reference: 6.7.5.3"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryPack",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL831#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class InternalResistanceIncreaseOfBatteryModuleLevel(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"InternalResistanceIncreaseOfBatteryModuleLevel",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL836#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                initialInternalResistanceOnBatteryCellLevel: Union[
                    xsd.Float, InitialInternalResistanceOnBatteryCellLevel
                ],
                initialInternalResistanceOnBatteryPackLevel: Union[
                    xsd.Float, InitialInternalResistanceOnBatteryPackLevel
                ],
                internalResistanceIncreaseOfBatteryPackLevel: Union[
                    xsd.Float, InternalResistanceIncreaseOfBatteryPackLevel
                ],
                initialInternalResistanceOnBatteryModuleLevel: Optional[
                    Union[xsd.Float, InitialInternalResistanceOnBatteryModuleLevel]
                ] = None,
                internalResistanceIncreaseOfBatteryCellLevel: Optional[
                    Union[xsd.Float, InternalResistanceIncreaseOfBatteryCellLevel]
                ] = None,
                internalResistanceIncreaseOfBatteryModuleLevel: Optional[
                    Union[xsd.Float, InternalResistanceIncreaseOfBatteryModuleLevel]
                ] = None,
                id_short: Optional[str] = r"Resistance",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Data elements regarding internal resistance and electrochemical impedance.\n\nDIN DKE Spec 99100 chapter reference: 6.7.5\n\n"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#resistance",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if (
                    initialInternalResistanceOnBatteryCellLevel is not None
                    and not isinstance(
                        initialInternalResistanceOnBatteryCellLevel, aas.SubmodelElement
                    )
                ):
                    initialInternalResistanceOnBatteryCellLevel = (
                        self.InitialInternalResistanceOnBatteryCellLevel(
                            initialInternalResistanceOnBatteryCellLevel
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    initialInternalResistanceOnBatteryPackLevel is not None
                    and not isinstance(
                        initialInternalResistanceOnBatteryPackLevel, aas.SubmodelElement
                    )
                ):
                    initialInternalResistanceOnBatteryPackLevel = (
                        self.InitialInternalResistanceOnBatteryPackLevel(
                            initialInternalResistanceOnBatteryPackLevel
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    initialInternalResistanceOnBatteryModuleLevel is not None
                    and not isinstance(
                        initialInternalResistanceOnBatteryModuleLevel,
                        aas.SubmodelElement,
                    )
                ):
                    initialInternalResistanceOnBatteryModuleLevel = (
                        self.InitialInternalResistanceOnBatteryModuleLevel(
                            initialInternalResistanceOnBatteryModuleLevel
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    internalResistanceIncreaseOfBatteryCellLevel is not None
                    and not isinstance(
                        internalResistanceIncreaseOfBatteryCellLevel,
                        aas.SubmodelElement,
                    )
                ):
                    internalResistanceIncreaseOfBatteryCellLevel = (
                        self.InternalResistanceIncreaseOfBatteryCellLevel(
                            internalResistanceIncreaseOfBatteryCellLevel
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    internalResistanceIncreaseOfBatteryPackLevel is not None
                    and not isinstance(
                        internalResistanceIncreaseOfBatteryPackLevel,
                        aas.SubmodelElement,
                    )
                ):
                    internalResistanceIncreaseOfBatteryPackLevel = (
                        self.InternalResistanceIncreaseOfBatteryPackLevel(
                            internalResistanceIncreaseOfBatteryPackLevel
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    internalResistanceIncreaseOfBatteryModuleLevel is not None
                    and not isinstance(
                        internalResistanceIncreaseOfBatteryModuleLevel,
                        aas.SubmodelElement,
                    )
                ):
                    internalResistanceIncreaseOfBatteryModuleLevel = (
                        self.InternalResistanceIncreaseOfBatteryModuleLevel(
                            internalResistanceIncreaseOfBatteryModuleLevel
                        )
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    initialInternalResistanceOnBatteryCellLevel,
                    initialInternalResistanceOnBatteryPackLevel,
                    initialInternalResistanceOnBatteryModuleLevel,
                    internalResistanceIncreaseOfBatteryCellLevel,
                    internalResistanceIncreaseOfBatteryPackLevel,
                    internalResistanceIncreaseOfBatteryModuleLevel,
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

        class PowerCapability(aas.SubmodelElementCollection):

            class MaximumPermittedBatteryPower(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"MaximumPermittedBatteryPower",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "maximum permitted battery power\n\nDIN DKE Spec 99100 chapter reference:  6.7.3.5"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL843#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumPermittedBatteryPower",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class PowerFade(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"PowerFade",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "Power fade\n\nDIN DKE Spec 99100 chapter reference: 6.7.3.4"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL852#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerFade",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class RatioNorminalBatteryPowerAndBatteryEnergy(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"RatioNorminalBatteryPowerAndBatteryEnergy",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityRatio",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class OriginalPowerCapability(aas.SubmodelElementList):

                class Originalpowercapability_item(aas.SubmodelElementCollection):

                    class AtSoc(aas.Property):

                        def __init__(
                            self,
                            value: xsd.UnsignedInt,
                            id_short: Optional[str] = r"atSoc",
                            value_type: aas.DataTypeDefXsd = xsd.UnsignedInt,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#atSoC",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABL821#001",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
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

                    class PowerCapabilityAt(aas.Property):

                        def __init__(
                            self,
                            value: xsd.Float,
                            id_short: Optional[str] = r"powerCapabilityAt",
                            value_type: aas.DataTypeDefXsd = xsd.Float,
                            value_id: Optional[aas.Reference] = None,
                            display_name: Optional[aas.MultiLanguageNameType] = None,
                            category: Optional[str] = None,
                            description: Optional[aas.MultiLanguageTextType] = None,
                            semantic_id: Optional[
                                aas.Reference
                            ] = aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityAt",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            qualifier: Iterable[aas.Qualifier] = None,
                            extension: Iterable[aas.Extension] = (),
                            supplemental_semantic_id: Iterable[aas.Reference] = (
                                aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"0173-1#02-ABL853#001",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                            ),
                            embedded_data_specifications: Iterable[
                                aas.EmbeddedDataSpecification
                            ] = None,
                        ):

                            if qualifier is None:
                                qualifier = (
                                    aas.Qualifier(
                                        type_=r"SMT/Cardinality",
                                        value_type=str,
                                        value=r"One",
                                        value_id=None,
                                        kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                        semantic_id=aas.ExternalReference(
                                            key=(
                                                aas.Key(
                                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                                ),
                                            ),
                                            referred_semantic_id=None,
                                        ),
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

                    def __init__(
                        self,
                        atSoc: Union[xsd.UnsignedInt, AtSoc],
                        powerCapabilityAt: Union[xsd.Float, PowerCapabilityAt],
                        id_short: Optional[str] = None,
                        display_name: Optional[aas.MultiLanguageNameType] = None,
                        category: Optional[str] = None,
                        description: Optional[
                            aas.MultiLanguageTextType
                        ] = aas.MultiLanguageTextType(
                            dict_={
                                r"en": "Power capability measured at a reference condition, for example at 80% or 20% state of charge (SoC).\n\nDIN DKE Spec 99100 chapter reference: 6.7.3.2"
                            }
                        ),
                        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt",
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

                        if qualifier is None:
                            qualifier = (
                                aas.Qualifier(
                                    type_=r"SMT/Cardinality",
                                    value_type=str,
                                    value=r"OneToMany",
                                    value_id=None,
                                    kind=aas.QualifierKind.TEMPLATE_QUALIFIER,
                                    semantic_id=aas.ExternalReference(
                                        key=(
                                            aas.Key(
                                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                                value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                            ),
                                        ),
                                        referred_semantic_id=None,
                                    ),
                                    supplemental_semantic_id=(),
                                ),
                            )

                        if embedded_data_specifications is None:
                            embedded_data_specifications = []

                        # Build a submodel element if a raw value was passed in the argument

                        if atSoc is not None and not isinstance(
                            atSoc, aas.SubmodelElement
                        ):
                            atSoc = self.AtSoc(atSoc)

                        # Build a submodel element if a raw value was passed in the argument

                        if powerCapabilityAt is not None and not isinstance(
                            powerCapabilityAt, aas.SubmodelElement
                        ):
                            powerCapabilityAt = self.PowerCapabilityAt(
                                powerCapabilityAt
                            )

                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [atSoc, powerCapabilityAt]:
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

                def __init__(
                    self,
                    originalpowercapability_items: Iterable[
                        Originalpowercapability_item
                    ],
                    id_short: Optional[str] = r"OriginalPowerCapability",
                    type_value_list_element: aas.SubmodelElement = aas.SubmodelElementCollection,
                    semantic_id_list_element: Optional[
                        aas.Reference
                    ] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    value_type_list_element: Optional[aas.DataTypeDefXsd] = None,
                    order_relevant: bool = True,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL853#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#originalPowerCapability",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
                                supplemental_semantic_id=(),
                            ),
                        )

                    if embedded_data_specifications is None:
                        embedded_data_specifications = []

                    # A str would be split into its characters
                    if isinstance(originalpowercapability_items, str):
                        raise TypeError(
                            "originalpowercapability_items takes several elements, got a str"
                        )

                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [originalpowercapability_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, aas.SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            embedded_submodel_elements.extend(se_arg)
                        else:
                            raise TypeError(
                                f"Unknown type of value in submodel_element_args: {se_arg.__class__}"
                            )

                    super().__init__(
                        value=embedded_submodel_elements,
                        id_short=id_short,
                        type_value_list_element=type_value_list_element,
                        semantic_id_list_element=semantic_id_list_element,
                        value_type_list_element=value_type_list_element,
                        order_relevant=order_relevant,
                        display_name=display_name,
                        category=category,
                        description=description,
                        semantic_id=semantic_id,
                        qualifier=qualifier,
                        extension=extension,
                        supplemental_semantic_id=supplemental_semantic_id,
                        embedded_data_specifications=embedded_data_specifications,
                    )

                def _check_constraints(self, new, existing) -> None:
                    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                    saved_id_short = new.id_short
                    new.id_short = None

                    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
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
                    if (
                        new.semantic_id is not None
                        and self.semantic_id_list_element is None
                    ):
                        for item in existing:
                            if (
                                item.semantic_id is not None
                                and new.semantic_id != item.semantic_id
                            ):
                                raise aas.AASConstraintViolation(
                                    114,
                                    f"Element to be added {new!r} has semantic_id "
                                    f"{new.semantic_id!r}, while already contained element "
                                    f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                    "aren't equal.",
                                )

                    # Re-assign id_short
                    new.id_short = saved_id_short

            def __init__(
                self,
                maximumPermittedBatteryPower: Union[
                    xsd.Float, MaximumPermittedBatteryPower
                ],
                powerFade: Union[xsd.Float, PowerFade],
                originalPowerCapability: Union[
                    Iterable[OriginalPowerCapability.Originalpowercapability_item],
                    OriginalPowerCapability,
                ],
                ratioNorminalBatteryPowerAndBatteryEnergy: Optional[
                    Union[xsd.Float, RatioNorminalBatteryPowerAndBatteryEnergy]
                ] = None,
                id_short: Optional[str] = r"PowerCapability",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information regarding power capability.\n\nDIN DKE Spec 99100 chapter reference: 6.7.3"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapability",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if maximumPermittedBatteryPower is not None and not isinstance(
                    maximumPermittedBatteryPower, aas.SubmodelElement
                ):
                    maximumPermittedBatteryPower = self.MaximumPermittedBatteryPower(
                        maximumPermittedBatteryPower
                    )

                # Build a submodel element if a raw value was passed in the argument

                if powerFade is not None and not isinstance(
                    powerFade, aas.SubmodelElement
                ):
                    powerFade = self.PowerFade(powerFade)

                # Build a submodel element if a raw value was passed in the argument

                if (
                    ratioNorminalBatteryPowerAndBatteryEnergy is not None
                    and not isinstance(
                        ratioNorminalBatteryPowerAndBatteryEnergy, aas.SubmodelElement
                    )
                ):
                    ratioNorminalBatteryPowerAndBatteryEnergy = (
                        self.RatioNorminalBatteryPowerAndBatteryEnergy(
                            ratioNorminalBatteryPowerAndBatteryEnergy
                        )
                    )

                # A str would be split into its characters
                if isinstance(originalPowerCapability, str):
                    raise TypeError(
                        "originalPowerCapability takes several elements, got a str"
                    )

                # Build a submodel element if a raw value was passed in the argument

                if originalPowerCapability is not None and not isinstance(
                    originalPowerCapability, aas.SubmodelElement
                ):
                    originalPowerCapability = self.OriginalPowerCapability(
                        originalPowerCapability
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    maximumPermittedBatteryPower,
                    powerFade,
                    ratioNorminalBatteryPowerAndBatteryEnergy,
                    originalPowerCapability,
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

        class Temperature(aas.SubmodelElementCollection):

            class TemperatureRangeIdleState_LowerBoundary(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"TemperatureRangeIdleState_LowerBoundary",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "temperature range idle state (lower boundary)\n\nDIN DKE Spec 99100 chapter reference:  6.7.7.3"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL842#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateLowerBoundary",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class TemperatureRangeIdleState_UpperBoundary(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[
                        str
                    ] = r"TemperatureRangeIdleState_UpperBoundary",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "temperature range idle state (upper boundary)\n\nDIN DKE Spec 99100 chapter reference: 6.7.7.4"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL871#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateUpperBoundary",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                temperatureRangeIdleState_LowerBoundary: Union[
                    xsd.Float, TemperatureRangeIdleState_LowerBoundary
                ],
                temperatureRangeIdleState_UpperBoundary: Union[
                    xsd.Float, TemperatureRangeIdleState_UpperBoundary
                ],
                id_short: Optional[str] = r"Temperature",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information regarding temperature conditions.\n\nDIN DKE Spec 99100 chapter reference: 6.7.7"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperature",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if (
                    temperatureRangeIdleState_LowerBoundary is not None
                    and not isinstance(
                        temperatureRangeIdleState_LowerBoundary, aas.SubmodelElement
                    )
                ):
                    temperatureRangeIdleState_LowerBoundary = (
                        self.TemperatureRangeIdleState_LowerBoundary(
                            temperatureRangeIdleState_LowerBoundary
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if (
                    temperatureRangeIdleState_UpperBoundary is not None
                    and not isinstance(
                        temperatureRangeIdleState_UpperBoundary, aas.SubmodelElement
                    )
                ):
                    temperatureRangeIdleState_UpperBoundary = (
                        self.TemperatureRangeIdleState_UpperBoundary(
                            temperatureRangeIdleState_UpperBoundary
                        )
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    temperatureRangeIdleState_LowerBoundary,
                    temperatureRangeIdleState_UpperBoundary,
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

        class Lifetime(aas.SubmodelElementCollection):

            class ExpectedLifetimeInCalendarYears(aas.Property):

                def __init__(
                    self,
                    value: xsd.UnsignedInt,
                    id_short: Optional[str] = r"ExpectedLifetimeInCalendarYears",
                    value_type: aas.DataTypeDefXsd = xsd.UnsignedInt,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedLifetime",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class ExpectedNumberOfCycles(aas.Property):

                def __init__(
                    self,
                    value: xsd.UnsignedInt,
                    id_short: Optional[str] = r"ExpectedNumberOfCycles",
                    value_type: aas.DataTypeDefXsd = xsd.UnsignedInt,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[aas.MultiLanguageTextType] = None,
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedNumberOfCycles",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"0173-1#02-ABL830#001",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class CapacityThresholdExhaustion(aas.Property):

                def __init__(
                    self,
                    value: xsd.Float,
                    id_short: Optional[str] = r"CapacityThresholdExhaustion",
                    value_type: aas.DataTypeDefXsd = xsd.Float,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[
                        aas.MultiLanguageNameType
                    ] = aas.MultiLanguageNameType(
                        dict_={r"en": r"capacity threshold for exhaustion"}
                    ),
                    category: Optional[str] = r"PARAMETER",
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "interpreted as minimum percentage of rated capacity, above which the battery is still considered operational as EV battery in its current life. The value has to be provided by the economic operator. This metric may serve as indicator for a necessary end of current life as EV and may be understood in the context of warranty.\n\nDIN DKE Spec 99100 chapter reference:  6.7.6.9"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ModelReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.CONCEPT_DESCRIPTION,
                                value=r"0173-1#02-ABL838#002",
                            ),
                        ),
                        type_=aas.ConceptDescription,
                        referred_semantic_id=None,
                    ),
                    qualifier: Iterable[aas.Qualifier] = None,
                    extension: Iterable[aas.Extension] = (),
                    supplemental_semantic_id: Iterable[aas.Reference] = (
                        aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityThresholdForExhaustion",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                    ),
                    embedded_data_specifications: Iterable[
                        aas.EmbeddedDataSpecification
                    ] = None,
                ):

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"ZeroToOne",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            class CRateOfRelevantCycleLifeTest(aas.Property):

                def __init__(
                    self,
                    value: xsd.Decimal,
                    id_short: Optional[str] = r"CRateOfRelevantCycleLifeTest",
                    value_type: aas.DataTypeDefXsd = xsd.Decimal,
                    value_id: Optional[aas.Reference] = None,
                    display_name: Optional[aas.MultiLanguageNameType] = None,
                    category: Optional[str] = None,
                    description: Optional[
                        aas.MultiLanguageTextType
                    ] = aas.MultiLanguageTextType(
                        dict_={
                            r"en": "This data attribute is a measurement parameter for “Expected lifetime: Number of charge-discharge cycles”: Applied charge and discharge rate in terms of rated capacity (C-rate) of relevant cycle-life reference test.\n\nDIN DKE Spec 99100 chapter reference:  6.7.6.6"
                        }
                    ),
                    semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#cRateLifeCycleTest",
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

                    if qualifier is None:
                        qualifier = (
                            aas.Qualifier(
                                type_=r"Cardinality",
                                value_type=str,
                                value=r"One",
                                value_id=None,
                                kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                                semantic_id=aas.ExternalReference(
                                    key=(
                                        aas.Key(
                                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                            value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                        ),
                                    ),
                                    referred_semantic_id=None,
                                ),
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

            def __init__(
                self,
                expectedLifetimeInCalendarYears: Union[
                    xsd.UnsignedInt, ExpectedLifetimeInCalendarYears
                ],
                expectedNumberOfCycles: Union[xsd.UnsignedInt, ExpectedNumberOfCycles],
                cRateOfRelevantCycleLifeTest: Union[
                    xsd.Decimal, CRateOfRelevantCycleLifeTest
                ],
                capacityThresholdExhaustion: Optional[
                    Union[xsd.Float, CapacityThresholdExhaustion]
                ] = None,
                id_short: Optional[str] = r"Lifetime",
                display_name: Optional[aas.MultiLanguageNameType] = None,
                category: Optional[str] = None,
                description: Optional[
                    aas.MultiLanguageTextType
                ] = aas.MultiLanguageTextType(
                    dict_={
                        r"en": "Information regarding battery lifetime.\n\nDIN DKE Spec 99100 chapter reference: 6.7.6"
                    }
                ),
                semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#lifetime",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                qualifier: Iterable[aas.Qualifier] = None,
                extension: Iterable[aas.Extension] = (),
                supplemental_semantic_id: Iterable[aas.Reference] = (
                    aas.ExternalReference(
                        key=(
                            aas.Key(
                                type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                value=r"0173-1#02-ABL358#002/0173-1#01-AHX773#002",
                            ),
                        ),
                        referred_semantic_id=None,
                    ),
                ),
                embedded_data_specifications: Iterable[
                    aas.EmbeddedDataSpecification
                ] = None,
            ):

                if qualifier is None:
                    qualifier = (
                        aas.Qualifier(
                            type_=r"Cardinality",
                            value_type=str,
                            value=r"One",
                            value_id=None,
                            kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                            semantic_id=aas.ExternalReference(
                                key=(
                                    aas.Key(
                                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                        value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                    ),
                                ),
                                referred_semantic_id=None,
                            ),
                            supplemental_semantic_id=(),
                        ),
                    )

                if embedded_data_specifications is None:
                    embedded_data_specifications = []

                # Build a submodel element if a raw value was passed in the argument

                if expectedLifetimeInCalendarYears is not None and not isinstance(
                    expectedLifetimeInCalendarYears, aas.SubmodelElement
                ):
                    expectedLifetimeInCalendarYears = (
                        self.ExpectedLifetimeInCalendarYears(
                            expectedLifetimeInCalendarYears
                        )
                    )

                # Build a submodel element if a raw value was passed in the argument

                if expectedNumberOfCycles is not None and not isinstance(
                    expectedNumberOfCycles, aas.SubmodelElement
                ):
                    expectedNumberOfCycles = self.ExpectedNumberOfCycles(
                        expectedNumberOfCycles
                    )

                # Build a submodel element if a raw value was passed in the argument

                if capacityThresholdExhaustion is not None and not isinstance(
                    capacityThresholdExhaustion, aas.SubmodelElement
                ):
                    capacityThresholdExhaustion = self.CapacityThresholdExhaustion(
                        capacityThresholdExhaustion
                    )

                # Build a submodel element if a raw value was passed in the argument

                if cRateOfRelevantCycleLifeTest is not None and not isinstance(
                    cRateOfRelevantCycleLifeTest, aas.SubmodelElement
                ):
                    cRateOfRelevantCycleLifeTest = self.CRateOfRelevantCycleLifeTest(
                        cRateOfRelevantCycleLifeTest
                    )

                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [
                    expectedLifetimeInCalendarYears,
                    expectedNumberOfCycles,
                    capacityThresholdExhaustion,
                    cRateOfRelevantCycleLifeTest,
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

        def __init__(
            self,
            capacityEnergyVoltage: CapacityEnergyVoltage,
            roundTripEnergyEfficiency: RoundTripEnergyEfficiency,
            resistance: Resistance,
            powerCapability: PowerCapability,
            temperature: Temperature,
            lifetime: Lifetime,
            id_short: Optional[str] = r"TechnicalPropertyAreas",
            display_name: Optional[aas.MultiLanguageNameType] = None,
            category: Optional[str] = None,
            description: Optional[aas.MultiLanguageTextType] = None,
            semantic_id: Optional[aas.Reference] = aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#02-ABK163#002",
                    ),
                ),
                referred_semantic_id=None,
            ),
            qualifier: Iterable[aas.Qualifier] = None,
            extension: Iterable[aas.Extension] = (),
            supplemental_semantic_id: Iterable[aas.Reference] = (
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"https://api.eclass-cdp.com/0173-1-02-ABK163-002",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
                aas.ExternalReference(
                    key=(
                        aas.Key(
                            type_=aas.KeyTypes.GLOBAL_REFERENCE,
                            value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#technicalPropertyAreas",
                        ),
                    ),
                    referred_semantic_id=None,
                ),
            ),
            embedded_data_specifications: Iterable[
                aas.EmbeddedDataSpecification
            ] = None,
        ):

            if qualifier is None:
                qualifier = (
                    aas.Qualifier(
                        type_=r"Cardinality",
                        value_type=str,
                        value=r"One",
                        value_id=None,
                        kind=aas.QualifierKind.CONCEPT_QUALIFIER,
                        semantic_id=aas.ExternalReference(
                            key=(
                                aas.Key(
                                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                                    value=r"https://admin-shell.io/SubmodelTemplates/Cardinality/1/0",
                                ),
                            ),
                            referred_semantic_id=None,
                        ),
                        supplemental_semantic_id=(),
                    ),
                )

            if embedded_data_specifications is None:
                embedded_data_specifications = []

            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [
                capacityEnergyVoltage,
                roundTripEnergyEfficiency,
                resistance,
                powerCapability,
                temperature,
                lifetime,
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

    def __init__(
        self,
        id_: str,
        generalInformation: GeneralInformation,
        technicalPropertyAreas: TechnicalPropertyAreas,
        id_short: Optional[str] = r"TechnicalData",
        display_name: Optional[aas.MultiLanguageNameType] = aas.MultiLanguageNameType(
            dict_={r"en": r"technical data"}
        ),
        category: Optional[str] = None,
        description: Optional[aas.MultiLanguageTextType] = aas.MultiLanguageTextType(
            dict_={r"en": r"Technical data of the battery."}
        ),
        administration: Optional[
            aas.AdministrativeInformation
        ] = aas.AdministrativeInformation(
            version=r"1",
            revision=r"0",
            creator=None,
            template_id=r"IDTA-02003-2-0",
            embedded_data_specifications=[],
        ),
        semantic_id: Optional[aas.Reference] = aas.ExternalReference(
            key=(
                aas.Key(
                    type_=aas.KeyTypes.GLOBAL_REFERENCE,
                    value=r"https://admin-shell.io/idta/digitalbatterypassport/TechnicalData/1/0",
                ),
            ),
            referred_semantic_id=None,
        ),
        qualifier: Iterable[aas.Qualifier] = None,
        kind: aas.ModellingKind = aas.ModellingKind.TEMPLATE,
        extension: Iterable[aas.Extension] = (),
        supplemental_semantic_id: Iterable[aas.Reference] = (
            aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"0173-1#01-AHX837#002",
                    ),
                ),
                referred_semantic_id=None,
            ),
            aas.ExternalReference(
                key=(
                    aas.Key(
                        type_=aas.KeyTypes.GLOBAL_REFERENCE,
                        value=r"urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#TechnicalData",
                    ),
                ),
                referred_semantic_id=None,
            ),
        ),
        embedded_data_specifications: Iterable[aas.EmbeddedDataSpecification] = None,
    ):

        if qualifier is None:
            qualifier = ()

        if embedded_data_specifications is None:
            embedded_data_specifications = []

        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [generalInformation, technicalPropertyAreas]:
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
