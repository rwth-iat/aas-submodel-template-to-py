
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class TechnicalData(Submodel):

    

    class GeneralInformation(SubmodelElementCollection):

        class ManufacturerName(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ManufacturerName',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Legally valid designation of the natural or judicial body which is directly responsible for the design, production, packaging and labeling of a product in respect to its being brought into the market.

                    DIN DKE Spec 99100 chapter reference: 6.1.2.4 c) '}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO677#004'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAO677-004'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#manufacturerName'),), referred_semantic_id=None)),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'ExampleValue', value_type=str, value=r'Example Company', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
                                value_type = value_type,
                                
                                value_id = value_id,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                

        class CompanyLogo(File):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'CompanyLogo',
                                
                                content_type: Optional[str]=r'image/png',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Imagefile for logo of manufacturer provided in common format (.png, .jpg).'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABI776#002'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABI776-002'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#companyLogo'),), referred_semantic_id=None)),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
                                content_type = content_type,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                

        class ManufacturerIdentifier(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ManufacturerIdentifier',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#manufacturerIdentifier'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
                                value_type = value_type,
                                
                                value_id = value_id,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                

        class BatteryCategory(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'BatteryCategory',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'A battery passport must include the battery category.

                    The battery category must be provided on the battery label.

                    The battery must be categorised by its intended use in (string values):
                    - "lmt"
                    - "ev" 
                    - "industrial", or
                    - "stationary"

                    DIN DKE Spec 99100 chapter reference: 6.1.3.5

                    '}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryCategory'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAR724#007'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
                                value_type = value_type,
                                
                                value_id = value_id,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                

        class BatteryMass(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: Float,
                                
                                
                                id_short: Optional[str]=r'BatteryMass',
                                
                                value_type: DataTypeDefXsd=Float,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#batteryMass'),), type_=ConceptDescription, referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAF040#010'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
                                value_type = value_type,
                                
                                value_id = value_id,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class ProductImages(SubmodelElementList):

            class Productimages_item(File):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'productimages_item',
                                    
                                    content_type: Optional[str]=r'image/png',
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Image file for associated product provided in common format (.png, .jpg).'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001/0173-1#01-AHY911#001'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.shared:3.1.0#ResourceWithContentType'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    content_type = content_type,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    productimages_items: Iterable[Productimages_item],
                        


                        


                                id_short: Optional[str]=r'ProductImages',
                                
                                type_value_list_element: SubmodelElement=File,
                                
                                semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001/0173-1#01-AHY911#001'),), referred_semantic_id=None),
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=None,
                                
                                order_relevant: bool=True,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'List for image file(s) for associated product provided in common format (.png, .jpg).'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABM220-001'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.generic.technical_data:2.0.0#productImages'),), referred_semantic_id=None)),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [productimages_items]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                type_value_list_element = type_value_list_element,
                                
                                semantic_id_list_element = semantic_id_list_element,
                                
                                value_type_list_element = value_type_list_element,
                                
                                order_relevant = order_relevant,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            def _check_constraints(self, new, existing) -> None:
                # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                saved_id_short = new.id_short
                new.id_short = None

                # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                if not isinstance(new, self.type_value_list_element):
                    raise base.AASConstraintViolation(108, "All first level elements must be of the type specified in "
                                                           f"type_value_list_element={self.type_value_list_element.__name__}, "
                                                           f"got {new!r}")

                if self.semantic_id_list_element is not None and new.semantic_id is not None \
                        and new.semantic_id != self.semantic_id_list_element:
                    # Constraint AASd-115 specifies that if the semantic_id of an item is not specified
                    # but semantic_id_list_element is, the semantic_id of the new is assumed to be identical.
                    # Not really a constraint...
                    # TODO: maybe set the semantic_id of new to semantic_id_list_element if it is None
                    raise base.AASConstraintViolation(107, f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                                                           "is specified all first level children must have the same "
                                                           f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}")

                # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                # is either Property or Range. Thus, `new` must have the value_type property.
                # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                if isinstance(self.type_value_list_element, Property) or isinstance(self.type_value_list_element, Range) \
                        and not isinstance(new.value_type, self.value_type_list_element):  # type: ignore
                    raise base.AASConstraintViolation(109, "All first level elements must have the value_type "  # type: ignore
                                                           "specified by value_type_list_element="
                                                           f"{self.value_type_list_element.__name__}, got "  # type: ignore
                                                           f"{new!r} with value_type={new.value_type.__name__}")  # type: ignore

                # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                if new.semantic_id is not None and self.semantic_id_list_element is None:
                    for item in existing:
                        if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                            raise base.AASConstraintViolation(114, f"Element to be added {new!r} has semantic_id "
                                                                   f"{new.semantic_id!r}, while already contained element "
                                                                   f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                                                   "aren't equal.")

                # Re-assign id_short
                new.id_short = saved_id_short

                



        class WarrantyInformation(SubmodelElementCollection):

            class WarrantyPeriod(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'WarrantyPeriod',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'warranty period'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyPeriod'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAX540#004'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    warrantyPeriod: Union[str, WarrantyPeriod],
                        


                        


                                id_short: Optional[str]=r'WarrantyInformation',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'warranty information'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.1#warrantyInformation'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO677#004'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = ()
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if warrantyPeriod and not isinstance(warrantyPeriod, SubmodelElement):
                    warrantyPeriod=self. WarrantyPeriod(warrantyPeriod)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [warrantyPeriod]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                
            
            
        def __init__(
                self,
                
                            

                    
                manufacturerName: Union[str, ManufacturerName],
                    

                    

                    
                manufacturerIdentifier: Union[str, ManufacturerIdentifier],
                    

                    
                batteryCategory: Union[str, BatteryCategory],
                    

                    
                batteryMass: Union[Float, BatteryMass],
                    

                    

                    
                warrantyInformation: WarrantyInformation,
                    


                    

                    
                companyLogo: Optional[CompanyLogo] = None,
                    

                    

                    

                    

                    
                productImages: Optional[ProductImages] = None,
                    

                    


                            id_short: Optional[str]=r'GeneralInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK161#002/0173-1#01-AHX838#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#generalInformation'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
                manufacturerName=self. ManufacturerName(manufacturerName)
                

                

                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerIdentifier and not isinstance(manufacturerIdentifier, SubmodelElement):
                manufacturerIdentifier=self. ManufacturerIdentifier(manufacturerIdentifier)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if batteryCategory and not isinstance(batteryCategory, SubmodelElement):
                batteryCategory=self. BatteryCategory(batteryCategory)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if batteryMass and not isinstance(batteryMass, SubmodelElement):
                batteryMass=self. BatteryMass(batteryMass)
                

                

                

                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [manufacturerName,companyLogo,manufacturerIdentifier,batteryCategory,batteryMass,productImages,warrantyInformation]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                    
            super().__init__(
                value=embedded_submodel_elements,

                            

                            id_short = id_short,
                            
                            display_name = display_name,
                            
                            category = category,
                            
                            description = description,
                            
                            semantic_id = semantic_id,
                            
                            qualifier = qualifier,
                            
                            extension = extension,
                            
                            supplemental_semantic_id = supplemental_semantic_id,
                            
                            embedded_data_specifications = embedded_data_specifications,
                            
                            
                            
            )
        
            
            



    class TechnicalPropertyAreas(SubmodelElementCollection):

        

        class CapacityEnergyVoltage(SubmodelElementCollection):

            class NominalVoltage(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'NominalVoltage',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'voltage - NOM

                        DIN DKE Spec 99100 chapter reference: 6.7.2.11'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL588#001'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#nominalVoltage'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class MinVoltage(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'MinVoltage',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'voltage - MIN

                        DIN DKE Spec 99100 chapter reference: 6.7.2.9'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL587#001'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#minimumVoltage'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class MaxVoltage(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'MaxVoltage',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'voltage - MAX

                        DIN DKE Spec 99100 chapter reference: 6.7.2.10'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL589#001'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumVoltage'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class RatedCapacity(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'RatedCapacity',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'rated capacity

                        DIN DKE Spec 99100 chapter reference: 6.7.2.2'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL869#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedCapacity'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class CapacityFade(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'CapacityFade',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'capacity fade

                        DIN DKE Spec 99100 chapter reference: 6.7.2.4'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL828#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityFade'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class CertifiedUsableBatteryEnergy(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'CertifiedUsableBatteryEnergy',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Certified usable battery energy (UBE certified)

                        DIN DKE Spec 99100 chapter reference: 6.7.2.5'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL829#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#ratedEnergy'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    nominalVoltage: Union[Float, NominalVoltage],
                        

                        
                    minVoltage: Union[Float, MinVoltage],
                        

                        
                    maxVoltage: Union[Float, MaxVoltage],
                        

                        
                    ratedCapacity: Union[Float, RatedCapacity],
                        

                        

                        


                        

                        

                        

                        

                        
                    capacityFade: Optional[Union[Float, CapacityFade]] = None,
                        

                        
                    certifiedUsableBatteryEnergy: Optional[Union[Float, CertifiedUsableBatteryEnergy]] = None,
                        


                                id_short: Optional[str]=r'CapacityEnergyVoltage',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information on battery capacity, energy and voltage.

                    DIN DKE Spec 99100 chapter reference: 6.7.2'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityEnergyVoltage'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if nominalVoltage and not isinstance(nominalVoltage, SubmodelElement):
                    nominalVoltage=self. NominalVoltage(nominalVoltage)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if minVoltage and not isinstance(minVoltage, SubmodelElement):
                    minVoltage=self. MinVoltage(minVoltage)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if maxVoltage and not isinstance(maxVoltage, SubmodelElement):
                    maxVoltage=self. MaxVoltage(maxVoltage)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if ratedCapacity and not isinstance(ratedCapacity, SubmodelElement):
                    ratedCapacity=self. RatedCapacity(ratedCapacity)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if capacityFade and not isinstance(capacityFade, SubmodelElement):
                    capacityFade=self. CapacityFade(capacityFade)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if certifiedUsableBatteryEnergy and not isinstance(certifiedUsableBatteryEnergy, SubmodelElement):
                    certifiedUsableBatteryEnergy=self. CertifiedUsableBatteryEnergy(certifiedUsableBatteryEnergy)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [nominalVoltage,minVoltage,maxVoltage,ratedCapacity,capacityFade,certifiedUsableBatteryEnergy]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class RoundTripEnergyEfficiency(SubmodelElementCollection):

            class InitialRoundTripEnergyEfficiency(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'InitialRoundTripEnergyEfficiency',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'initial round trip energy efficiency

                        DIN DKE Spec 99100 chapter reference: 6.7.4.2'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL833#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialRoundTripEnergyEfficiency'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class RoundTripEnergyEfficiencyAt50PercentOfCycleLife(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'RoundTripEnergyEfficiencyAt50PercentOfCycleLife',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'round trip energy efficiency at 50% of cycle life

                        DIN DKE Spec 99100 chapter reference:  6.7.4.3'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL866#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEfficiencyAt50PercentCycleLife'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class EnergyRoundTripEfficiencyFade(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'EnergyRoundTripEfficiencyFade',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'round trip energy efficiency fade

                        DIN DKE Spec 99100 chapter reference:  6.7.4.5'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL827#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#energyRoundTripEfficiencyFade'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InitialSelfDischargingRate(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'InitialSelfDischargingRate',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'initial self-discharging rate

                        DIN DKE Spec 99100 chapter reference:  6.7.4.6'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL834#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialSelfDischargingRate'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    initialRoundTripEnergyEfficiency: Union[int, InitialRoundTripEnergyEfficiency],
                        

                        
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife: Union[int, RoundTripEnergyEfficiencyAt50PercentOfCycleLife],
                        

                        

                        


                        

                        

                        
                    energyRoundTripEfficiencyFade: Optional[Union[Float, EnergyRoundTripEfficiencyFade]] = None,
                        

                        
                    initialSelfDischargingRate: Optional[Union[int, InitialSelfDischargingRate]] = None,
                        


                                id_short: Optional[str]=r'RoundTripEnergyEfficiency',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information regarding round trip energy efficiency.

                    DIN DKE Spec 99100 chapter reference: 6.7.4'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#roundTripEnergyEfficiency'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if initialRoundTripEnergyEfficiency and not isinstance(initialRoundTripEnergyEfficiency, SubmodelElement):
                    initialRoundTripEnergyEfficiency=self. InitialRoundTripEnergyEfficiency(initialRoundTripEnergyEfficiency)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if roundTripEnergyEfficiencyAt50PercentOfCycleLife and not isinstance(roundTripEnergyEfficiencyAt50PercentOfCycleLife, SubmodelElement):
                    roundTripEnergyEfficiencyAt50PercentOfCycleLife=self. RoundTripEnergyEfficiencyAt50PercentOfCycleLife(roundTripEnergyEfficiencyAt50PercentOfCycleLife)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if energyRoundTripEfficiencyFade and not isinstance(energyRoundTripEfficiencyFade, SubmodelElement):
                    energyRoundTripEfficiencyFade=self. EnergyRoundTripEfficiencyFade(energyRoundTripEfficiencyFade)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if initialSelfDischargingRate and not isinstance(initialSelfDischargingRate, SubmodelElement):
                    initialSelfDischargingRate=self. InitialSelfDischargingRate(initialSelfDischargingRate)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [initialRoundTripEnergyEfficiency,roundTripEnergyEfficiencyAt50PercentOfCycleLife,energyRoundTripEfficiencyFade,initialSelfDischargingRate]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class Resistance(SubmodelElementCollection):

            class InitialInternalResistanceOnBatteryCellLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InitialInternalResistanceOnBatteryCellLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Internal battery cell and pack resistance - Internal resistance (in Ohm)

                        DIN DKE Spec 99100 chapter reference: 6.7.5.2'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL844#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryCell'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InitialInternalResistanceOnBatteryPackLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InitialInternalResistanceOnBatteryPackLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Initial (Pre-Use) internal resistance on battery pack level. 

                        DIN DKE Spec 99100 chapter reference: 6.7.5.2'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL846#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryPack'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InitialInternalResistanceOnBatteryModuleLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InitialInternalResistanceOnBatteryModuleLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Initial internal resistance on battery module level

                        DIN DKE Spec 99100 chapter reference: 6.7.5.2'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL832#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InternalResistanceIncreaseOfBatteryCellLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InternalResistanceIncreaseOfBatteryCellLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'initial internal resistance on battery cell level

                        DIN DKE Spec 99100 chapter reference: 6.7.5.3'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryCell'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL831#002'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InternalResistanceIncreaseOfBatteryPackLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InternalResistanceIncreaseOfBatteryPackLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'initial internal resistance on battery pack level

                        DIN DKE Spec 99100 chapter reference: 6.7.5.3'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#internalResistanceIncreaseOfBatteryPack'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL831#001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class InternalResistanceIncreaseOfBatteryModuleLevel(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'InternalResistanceIncreaseOfBatteryModuleLevel',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#initialInternalResistanceOfBatteryModule'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL836#001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    initialInternalResistanceOnBatteryCellLevel: Union[Float, InitialInternalResistanceOnBatteryCellLevel],
                        

                        
                    initialInternalResistanceOnBatteryPackLevel: Union[Float, InitialInternalResistanceOnBatteryPackLevel],
                        

                        

                        

                        
                    internalResistanceIncreaseOfBatteryPackLevel: Union[Float, InternalResistanceIncreaseOfBatteryPackLevel],
                        

                        


                        

                        

                        
                    initialInternalResistanceOnBatteryModuleLevel: Optional[Union[Float, InitialInternalResistanceOnBatteryModuleLevel]] = None,
                        

                        
                    internalResistanceIncreaseOfBatteryCellLevel: Optional[Union[Float, InternalResistanceIncreaseOfBatteryCellLevel]] = None,
                        

                        

                        
                    internalResistanceIncreaseOfBatteryModuleLevel: Optional[Union[Float, InternalResistanceIncreaseOfBatteryModuleLevel]] = None,
                        


                                id_short: Optional[str]=r'Resistance',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Data elements regarding internal resistance and electrochemical impedance.

                    DIN DKE Spec 99100 chapter reference: 6.7.5

                    '}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#resistance'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if initialInternalResistanceOnBatteryCellLevel and not isinstance(initialInternalResistanceOnBatteryCellLevel, SubmodelElement):
                    initialInternalResistanceOnBatteryCellLevel=self. InitialInternalResistanceOnBatteryCellLevel(initialInternalResistanceOnBatteryCellLevel)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if initialInternalResistanceOnBatteryPackLevel and not isinstance(initialInternalResistanceOnBatteryPackLevel, SubmodelElement):
                    initialInternalResistanceOnBatteryPackLevel=self. InitialInternalResistanceOnBatteryPackLevel(initialInternalResistanceOnBatteryPackLevel)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if initialInternalResistanceOnBatteryModuleLevel and not isinstance(initialInternalResistanceOnBatteryModuleLevel, SubmodelElement):
                    initialInternalResistanceOnBatteryModuleLevel=self. InitialInternalResistanceOnBatteryModuleLevel(initialInternalResistanceOnBatteryModuleLevel)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if internalResistanceIncreaseOfBatteryCellLevel and not isinstance(internalResistanceIncreaseOfBatteryCellLevel, SubmodelElement):
                    internalResistanceIncreaseOfBatteryCellLevel=self. InternalResistanceIncreaseOfBatteryCellLevel(internalResistanceIncreaseOfBatteryCellLevel)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if internalResistanceIncreaseOfBatteryPackLevel and not isinstance(internalResistanceIncreaseOfBatteryPackLevel, SubmodelElement):
                    internalResistanceIncreaseOfBatteryPackLevel=self. InternalResistanceIncreaseOfBatteryPackLevel(internalResistanceIncreaseOfBatteryPackLevel)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if internalResistanceIncreaseOfBatteryModuleLevel and not isinstance(internalResistanceIncreaseOfBatteryModuleLevel, SubmodelElement):
                    internalResistanceIncreaseOfBatteryModuleLevel=self. InternalResistanceIncreaseOfBatteryModuleLevel(internalResistanceIncreaseOfBatteryModuleLevel)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [initialInternalResistanceOnBatteryCellLevel,initialInternalResistanceOnBatteryPackLevel,initialInternalResistanceOnBatteryModuleLevel,internalResistanceIncreaseOfBatteryCellLevel,internalResistanceIncreaseOfBatteryPackLevel,internalResistanceIncreaseOfBatteryModuleLevel]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class PowerCapability(SubmodelElementCollection):

            class MaximumPermittedBatteryPower(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'MaximumPermittedBatteryPower',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'maximum permitted battery power

                        DIN DKE Spec 99100 chapter reference:  6.7.3.5'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL843#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#maximumPermittedBatteryPower'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class PowerFade(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'PowerFade',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Power fade

                        DIN DKE Spec 99100 chapter reference: 6.7.3.4'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL852#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerFade'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class RatioNorminalBatteryPowerAndBatteryEnergy(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'RatioNorminalBatteryPowerAndBatteryEnergy',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityRatio'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    



            class OriginalPowerCapability(SubmodelElementList):

                

                class Originalpowercapability_item(SubmodelElementCollection):

                    class AtSoc(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: UnsignedInt,
                                            
                                            
                                            id_short: Optional[str]=r'atSoc',
                                            
                                            value_type: DataTypeDefXsd=UnsignedInt,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=None,
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=None,
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#atSoC'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL821#001'),), referred_semantic_id=None),),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            
                                    
                            super().__init__(
                                
                                            value = value,
                                            
                                            
                                            id_short = id_short,
                                            
                                            value_type = value_type,
                                            
                                            value_id = value_id,
                                            
                                            display_name = display_name,
                                            
                                            category = category,
                                            
                                            description = description,
                                            
                                            semantic_id = semantic_id,
                                            
                                            qualifier = qualifier,
                                            
                                            extension = extension,
                                            
                                            supplemental_semantic_id = supplemental_semantic_id,
                                            
                                            embedded_data_specifications = embedded_data_specifications,
                                            
                                            
                                            
                            )
                        
                            
                            

                    class PowerCapabilityAt(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: Float,
                                            
                                            
                                            id_short: Optional[str]=r'powerCapabilityAt',
                                            
                                            value_type: DataTypeDefXsd=Float,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=None,
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=None,
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapabilityAt'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL853#001'),), referred_semantic_id=None),),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            
                                    
                            super().__init__(
                                
                                            value = value,
                                            
                                            
                                            id_short = id_short,
                                            
                                            value_type = value_type,
                                            
                                            value_id = value_id,
                                            
                                            display_name = display_name,
                                            
                                            category = category,
                                            
                                            description = description,
                                            
                                            semantic_id = semantic_id,
                                            
                                            qualifier = qualifier,
                                            
                                            extension = extension,
                                            
                                            supplemental_semantic_id = supplemental_semantic_id,
                                            
                                            embedded_data_specifications = embedded_data_specifications,
                                            
                                            
                                            
                            )
                        
                            
                            
                        
                        
                    def __init__(
                            self,
                            
                                        

                                
                            atSoc: Union[UnsignedInt, AtSoc],
                                

                                
                            powerCapabilityAt: Union[Float, PowerCapabilityAt],
                                


                                

                                


                                        id_short: Optional[str]=r'originalpowercapability_item',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Power capability measured at a reference condition, for example at 80% or 20% state of charge (SoC).

                            DIN DKE Spec 99100 chapter reference: 6.7.3.2'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if atSoc and not isinstance(atSoc, SubmodelElement):
                            atSoc=self. AtSoc(atSoc)
                            

                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if powerCapabilityAt and not isinstance(powerCapabilityAt, SubmodelElement):
                            powerCapabilityAt=self. PowerCapabilityAt(powerCapabilityAt)
                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [atSoc,powerCapabilityAt]:
                            if se_arg is None:
                                continue
                            elif isinstance(se_arg, SubmodelElement):
                                embedded_submodel_elements.append(se_arg)
                            elif isinstance(se_arg, Iterable):
                                for n, element in enumerate(se_arg):
                                    element.id_short = f"{element.id_short}{n}"
                                    embedded_submodel_elements.append(element)
                            else:
                                raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                                
                        super().__init__(
                            value=embedded_submodel_elements,

                                        

                                        id_short = id_short,
                                        
                                        display_name = display_name,
                                        
                                        category = category,
                                        
                                        description = description,
                                        
                                        semantic_id = semantic_id,
                                        
                                        qualifier = qualifier,
                                        
                                        extension = extension,
                                        
                                        supplemental_semantic_id = supplemental_semantic_id,
                                        
                                        embedded_data_specifications = embedded_data_specifications,
                                        
                                        
                                        
                        )
                    
                        
                        
                    
                    
                def __init__(
                        self,
                        
                                    

                            
                        originalpowercapability_items: Iterable[Originalpowercapability_item],
                            


                            


                                    id_short: Optional[str]=r'OriginalPowerCapability',
                                    
                                    type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                    
                                    semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#PowerCapabilityAt'),), referred_semantic_id=None),
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=None,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL853#002'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#originalPowerCapability'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [originalpowercapability_items]:
                        if se_arg is None:
                            continue
                        elif isinstance(se_arg, SubmodelElement):
                            embedded_submodel_elements.append(se_arg)
                        elif isinstance(se_arg, Iterable):
                            for n, element in enumerate(se_arg):
                                element.id_short = f"{element.id_short}{n}"
                                embedded_submodel_elements.append(element)
                        else:
                            raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                            
                    super().__init__(
                        value=embedded_submodel_elements,

                                    

                                    id_short = id_short,
                                    
                                    type_value_list_element = type_value_list_element,
                                    
                                    semantic_id_list_element = semantic_id_list_element,
                                    
                                    value_type_list_element = value_type_list_element,
                                    
                                    order_relevant = order_relevant,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                def _check_constraints(self, new, existing) -> None:
                    # Since the id_short contains randomness, unset it temporarily for pretty and predictable error messages.
                    # This also prevents the random id_short from remaining set in case a constraint violation is encountered.
                    saved_id_short = new.id_short
                    new.id_short = None

                    # We relax constraint AASd-108here: It is allowed to add subclasses of the specified in type_value_list_element
                    if not isinstance(new, self.type_value_list_element):
                        raise base.AASConstraintViolation(108, "All first level elements must be of the type specified in "
                                                               f"type_value_list_element={self.type_value_list_element.__name__}, "
                                                               f"got {new!r}")

                    if self.semantic_id_list_element is not None and new.semantic_id is not None \
                            and new.semantic_id != self.semantic_id_list_element:
                        # Constraint AASd-115 specifies that if the semantic_id of an item is not specified
                        # but semantic_id_list_element is, the semantic_id of the new is assumed to be identical.
                        # Not really a constraint...
                        # TODO: maybe set the semantic_id of new to semantic_id_list_element if it is None
                        raise base.AASConstraintViolation(107, f"If semantic_id_list_element={self.semantic_id_list_element!r} "
                                                               "is specified all first level children must have the same "
                                                               f"semantic_id, got {new!r} with semantic_id={new.semantic_id!r}")

                    # If we got here we know that `new` is an instance of type_value_list_element and that type_value_list_element
                    # is either Property or Range. Thus, `new` must have the value_type property.
                    # Furthermore, value_type_list_element cannot be None, as this is already checked in __init__().
                    if isinstance(self.type_value_list_element, Property) or isinstance(self.type_value_list_element, Range) \
                            and not isinstance(new.value_type, self.value_type_list_element):  # type: ignore
                        raise base.AASConstraintViolation(109, "All first level elements must have the value_type "  # type: ignore
                                                               "specified by value_type_list_element="
                                                               f"{self.value_type_list_element.__name__}, got "  # type: ignore
                                                               f"{new!r} with value_type={new.value_type.__name__}")  # type: ignore

                    # If semantic_id_list_element is not None that would already enforce the semantic_id for all first level
                    # elements. Thus, we only need to perform this check if semantic_id_list_element is None.
                    if new.semantic_id is not None and self.semantic_id_list_element is None:
                        for item in existing:
                            if item.semantic_id is not None and new.semantic_id != item.semantic_id:
                                raise base.AASConstraintViolation(114, f"Element to be added {new!r} has semantic_id "
                                                                       f"{new.semantic_id!r}, while already contained element "
                                                                       f"{item!r} has semantic_id {item.semantic_id!r}, which "
                                                                       "aren't equal.")

                    # Re-assign id_short
                    new.id_short = saved_id_short

                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    maximumPermittedBatteryPower: Union[Float, MaximumPermittedBatteryPower],
                        

                        
                    powerFade: Union[Float, PowerFade],
                        

                        

                        
                    originalPowerCapability: OriginalPowerCapability,
                        


                        

                        

                        
                    ratioNorminalBatteryPowerAndBatteryEnergy: Optional[Union[Float, RatioNorminalBatteryPowerAndBatteryEnergy]] = None,
                        

                        


                                id_short: Optional[str]=r'PowerCapability',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information regarding power capability.

                    DIN DKE Spec 99100 chapter reference: 6.7.3'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#powerCapability'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if maximumPermittedBatteryPower and not isinstance(maximumPermittedBatteryPower, SubmodelElement):
                    maximumPermittedBatteryPower=self. MaximumPermittedBatteryPower(maximumPermittedBatteryPower)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if powerFade and not isinstance(powerFade, SubmodelElement):
                    powerFade=self. PowerFade(powerFade)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if ratioNorminalBatteryPowerAndBatteryEnergy and not isinstance(ratioNorminalBatteryPowerAndBatteryEnergy, SubmodelElement):
                    ratioNorminalBatteryPowerAndBatteryEnergy=self. RatioNorminalBatteryPowerAndBatteryEnergy(ratioNorminalBatteryPowerAndBatteryEnergy)
                    

                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [maximumPermittedBatteryPower,powerFade,ratioNorminalBatteryPowerAndBatteryEnergy,originalPowerCapability]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class Temperature(SubmodelElementCollection):

            class TemperatureRangeIdleState_LowerBoundary(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'TemperatureRangeIdleState_LowerBoundary',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'temperature range idle state (lower boundary)

                        DIN DKE Spec 99100 chapter reference:  6.7.7.3'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL842#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateLowerBoundary'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class TemperatureRangeIdleState_UpperBoundary(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'TemperatureRangeIdleState_UpperBoundary',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'temperature range idle state (upper boundary)

                        DIN DKE Spec 99100 chapter reference: 6.7.7.4'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL871#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperatureRangeIdleStateUpperBoundary'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    temperatureRangeIdleState_LowerBoundary: Union[Float, TemperatureRangeIdleState_LowerBoundary],
                        

                        
                    temperatureRangeIdleState_UpperBoundary: Union[Float, TemperatureRangeIdleState_UpperBoundary],
                        


                        

                        


                                id_short: Optional[str]=r'Temperature',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information regarding temperature conditions.

                    DIN DKE Spec 99100 chapter reference: 6.7.7'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#temperature'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if temperatureRangeIdleState_LowerBoundary and not isinstance(temperatureRangeIdleState_LowerBoundary, SubmodelElement):
                    temperatureRangeIdleState_LowerBoundary=self. TemperatureRangeIdleState_LowerBoundary(temperatureRangeIdleState_LowerBoundary)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if temperatureRangeIdleState_UpperBoundary and not isinstance(temperatureRangeIdleState_UpperBoundary, SubmodelElement):
                    temperatureRangeIdleState_UpperBoundary=self. TemperatureRangeIdleState_UpperBoundary(temperatureRangeIdleState_UpperBoundary)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [temperatureRangeIdleState_LowerBoundary,temperatureRangeIdleState_UpperBoundary]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                



        class Lifetime(SubmodelElementCollection):

            class ExpectedLifetimeInCalendarYears(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: UnsignedInt,
                                    
                                    
                                    id_short: Optional[str]=r'ExpectedLifetimeInCalendarYears',
                                    
                                    value_type: DataTypeDefXsd=UnsignedInt,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedLifetime'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class ExpectedNumberOfCycles(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: UnsignedInt,
                                    
                                    
                                    id_short: Optional[str]=r'ExpectedNumberOfCycles',
                                    
                                    value_type: DataTypeDefXsd=UnsignedInt,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#expectedNumberOfCycles'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL830#001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class CapacityThresholdExhaustion(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'CapacityThresholdExhaustion',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'capacity threshold for exhaustion'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'interpreted as minimum percentage of rated capacity, above which the battery is still considered operational as EV battery in its current life. The value has to be provided by the economic operator. This metric may serve as indicator for a necessary end of current life as EV and may be understood in the context of warranty.

                        DIN DKE Spec 99100 chapter reference:  6.7.6.9'}),
                                    
                                    semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'0173-1#02-ABL838#002'),), type_=ConceptDescription, referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#capacityThresholdForExhaustion'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    

            class CRateOfRelevantCycleLifeTest(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Decimal,
                                    
                                    
                                    id_short: Optional[str]=r'CRateOfRelevantCycleLifeTest',
                                    
                                    value_type: DataTypeDefXsd=Decimal,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'This data attribute is a measurement parameter for “Expected lifetime: Number of charge-discharge cycles”: Applied charge and discharge rate in terms of rated capacity (C-rate) of relevant cycle-life reference test.

                        DIN DKE Spec 99100 chapter reference:  6.7.6.6'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#cRateLifeCycleTest'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    value = value,
                                    
                                    
                                    id_short = id_short,
                                    
                                    value_type = value_type,
                                    
                                    value_id = value_id,
                                    
                                    display_name = display_name,
                                    
                                    category = category,
                                    
                                    description = description,
                                    
                                    semantic_id = semantic_id,
                                    
                                    qualifier = qualifier,
                                    
                                    extension = extension,
                                    
                                    supplemental_semantic_id = supplemental_semantic_id,
                                    
                                    embedded_data_specifications = embedded_data_specifications,
                                    
                                    
                                    
                    )
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    expectedLifetimeInCalendarYears: Union[UnsignedInt, ExpectedLifetimeInCalendarYears],
                        

                        
                    expectedNumberOfCycles: Union[UnsignedInt, ExpectedNumberOfCycles],
                        

                        

                        
                    cRateOfRelevantCycleLifeTest: Union[Decimal, CRateOfRelevantCycleLifeTest],
                        


                        

                        

                        
                    capacityThresholdExhaustion: Optional[Union[Float, CapacityThresholdExhaustion]] = None,
                        

                        


                                id_short: Optional[str]=r'Lifetime',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information regarding battery lifetime.

                    DIN DKE Spec 99100 chapter reference: 6.7.6'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#lifetime'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if expectedLifetimeInCalendarYears and not isinstance(expectedLifetimeInCalendarYears, SubmodelElement):
                    expectedLifetimeInCalendarYears=self. ExpectedLifetimeInCalendarYears(expectedLifetimeInCalendarYears)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if expectedNumberOfCycles and not isinstance(expectedNumberOfCycles, SubmodelElement):
                    expectedNumberOfCycles=self. ExpectedNumberOfCycles(expectedNumberOfCycles)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if capacityThresholdExhaustion and not isinstance(capacityThresholdExhaustion, SubmodelElement):
                    capacityThresholdExhaustion=self. CapacityThresholdExhaustion(capacityThresholdExhaustion)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if cRateOfRelevantCycleLifeTest and not isinstance(cRateOfRelevantCycleLifeTest, SubmodelElement):
                    cRateOfRelevantCycleLifeTest=self. CRateOfRelevantCycleLifeTest(cRateOfRelevantCycleLifeTest)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [expectedLifetimeInCalendarYears,expectedNumberOfCycles,capacityThresholdExhaustion,cRateOfRelevantCycleLifeTest]:
                    if se_arg is None:
                        continue
                    elif isinstance(se_arg, SubmodelElement):
                        embedded_submodel_elements.append(se_arg)
                    elif isinstance(se_arg, Iterable):
                        for n, element in enumerate(se_arg):
                            element.id_short = f"{element.id_short}{n}"
                            embedded_submodel_elements.append(element)
                    else:
                        raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                        
                super().__init__(
                    value=embedded_submodel_elements,

                                

                                id_short = id_short,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                
            
            
        def __init__(
                self,
                
                            

                    
                capacityEnergyVoltage: CapacityEnergyVoltage,
                    

                    
                roundTripEnergyEfficiency: RoundTripEnergyEfficiency,
                    

                    
                resistance: Resistance,
                    

                    
                powerCapability: PowerCapability,
                    

                    
                temperature: Temperature,
                    

                    
                lifetime: Lifetime,
                    


                    

                    

                    

                    

                    

                    


                            id_short: Optional[str]=r'TechnicalPropertyAreas',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK163#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK163-002'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#technicalPropertyAreas'),), referred_semantic_id=None)),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                

                

                

                

                

                

                

                

                

                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [capacityEnergyVoltage,roundTripEnergyEfficiency,resistance,powerCapability,temperature,lifetime]:
                if se_arg is None:
                    continue
                elif isinstance(se_arg, SubmodelElement):
                    embedded_submodel_elements.append(se_arg)
                elif isinstance(se_arg, Iterable):
                    for n, element in enumerate(se_arg):
                        element.id_short = f"{element.id_short}{n}"
                        embedded_submodel_elements.append(element)
                else:
                    raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                    
            super().__init__(
                value=embedded_submodel_elements,

                            

                            id_short = id_short,
                            
                            display_name = display_name,
                            
                            category = category,
                            
                            description = description,
                            
                            semantic_id = semantic_id,
                            
                            qualifier = qualifier,
                            
                            extension = extension,
                            
                            supplemental_semantic_id = supplemental_semantic_id,
                            
                            embedded_data_specifications = embedded_data_specifications,
                            
                            
                            
            )
        
            
            
        
        
    def __init__(
            self,
            
                        id_: str,
                        
                        

                
            generalInformation: GeneralInformation,
                

                
            technicalPropertyAreas: TechnicalPropertyAreas,
                


                

                


                        id_short: Optional[str]=r'TechnicalData',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'technical data'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Technical data of the battery.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'IDTA-02003-2-0', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/digitalbatterypassport/TechnicalData/1/0'),), referred_semantic_id=None),
                        
                        qualifier: Iterable[Qualifier]=None,
                        
                        kind: ModellingKind=ModellingKind.TEMPLATE,
                        
                        extension: Iterable[Extension]=(),
                        
                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#01-AHX837#002'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.technical_data:1.0.0#TechnicalData'),), referred_semantic_id=None)),
                        
                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                        
                        

                        
    ):
        
        if qualifier is None:
            qualifier = ()
        
        if embedded_data_specifications is None:
            embedded_data_specifications = []
        
        




            

            

            

            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [generalInformation,technicalPropertyAreas]:
            if se_arg is None:
                continue
            elif isinstance(se_arg, SubmodelElement):
                embedded_submodel_elements.append(se_arg)
            elif isinstance(se_arg, Iterable):
                for n, element in enumerate(se_arg):
                    element.id_short = f"{element.id_short}{n}"
                    embedded_submodel_elements.append(element)
            else:
                raise TypeError(f"Unknown type of value in submodel_element_args: {type(se_arg)}")

                
        super().__init__(
            submodel_element=embedded_submodel_elements,

                        id_ = id_,
                        
                        

                        id_short = id_short,
                        
                        display_name = display_name,
                        
                        category = category,
                        
                        description = description,
                        
                        administration = administration,
                        
                        semantic_id = semantic_id,
                        
                        qualifier = qualifier,
                        
                        kind = kind,
                        
                        extension = extension,
                        
                        supplemental_semantic_id = supplemental_semantic_id,
                        
                        embedded_data_specifications = embedded_data_specifications,
                        
                        
                        
        )
    
        
        