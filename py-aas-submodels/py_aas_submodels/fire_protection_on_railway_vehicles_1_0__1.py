
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class RailwayFireProtection(Submodel):

    

    class ManufacturerInformation(SubmodelElementCollection):

        class ManufacturerName(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'ManufacturerName',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer name'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'name of the organization legally responsible for manufacturing the product or component.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ManufacturerName/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Generic Manufacturing Corp.', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
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
            
                
                

        class ManufacturerProductDesignation(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'ManufacturerProductDesignation',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer product designation'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'designation assigned by the manufacturer to identify the product or component within its product portfolio.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ManufacturerProductDesignation/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Modular FireSafe Component X100', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
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
            
                
                

        class OrderCodeOfManufacturer(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'OrderCodeOfManufacturer',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Order code of manufacturer'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'ordering identifier defined by the manufacturer to uniquely reference the product or component for purchasing purposes.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/OrderCodeOfManufacturer/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'ORD-XS-000123', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
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
            
                
                

        class ProductArticleNumberOfManufacturer(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ProductArticleNumberOfManufacturer',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product article number of manufacturer'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'article number used by the manufacturer to uniquely identify the product or component in catalogs and information systems'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ProductArticleNumberOfManufacturer/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'PAN-4587-AX9', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
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
                
                            

                    
                manufacturerName: Union[LangStringSet, ManufacturerName],
                    

                    
                manufacturerProductDesignation: Union[LangStringSet, ManufacturerProductDesignation],
                    

                    
                orderCodeOfManufacturer: Union[str, OrderCodeOfManufacturer],
                    

                    
                productArticleNumberOfManufacturer: Union[str, ProductArticleNumberOfManufacturer],
                    


                    

                    

                    

                    


                            id_short: Optional[str]=r'ManufacturerInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'identifies the material or component and its manufacturer, including product designation and reference identifiers, ensuring unambiguous attribution of the fire protection data.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ManufacturerInformation/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
                manufacturerName=self. ManufacturerName(manufacturerName)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerProductDesignation and not isinstance(manufacturerProductDesignation, SubmodelElement):
                manufacturerProductDesignation=self. ManufacturerProductDesignation(manufacturerProductDesignation)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if orderCodeOfManufacturer and not isinstance(orderCodeOfManufacturer, SubmodelElement):
                orderCodeOfManufacturer=self. OrderCodeOfManufacturer(orderCodeOfManufacturer)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if productArticleNumberOfManufacturer and not isinstance(productArticleNumberOfManufacturer, SubmodelElement):
                productArticleNumberOfManufacturer=self. ProductArticleNumberOfManufacturer(productArticleNumberOfManufacturer)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [manufacturerName,manufacturerProductDesignation,orderCodeOfManufacturer,productArticleNumberOfManufacturer]:
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
        
            
            



    class FireProtectionCertificates(SubmodelElementCollection):

        

        class RequirementsSets(SubmodelElementList):

            

            class Requirementssets_item(SubmodelElementCollection):

                class HazardLevel(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'HazardLevel',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Hazard level'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'hazard level indicating the achieved fire hazard classification of the product, component, or material according to the applicable fire protection standard.

                            Following values can be assigned:

                            "Compliant: Hazard Level 1"

                            "Compliant: Hazard Level 2"

                            "Compliant: Hazard Level 3"

                            "Approved Functional Necessity Report"

                            "Missing Test Results"

                            "Not Compliant"'}),
                                        
                                        semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.CONCEPT_DESCRIPTION, value=r'https://admin-shell.io/RailwayFireProtection/Submodel/1/HazardLevel'),), type_=ConceptDescription, referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Compliant: Hazard Level 3', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                    
                        
                        



                class ReportReferences(SubmodelElementList):

                    class Reportreferences_item(ReferenceElement):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: Reference,
                                            
                                            
                                            id_short: Optional[str]=r'reportreferences_item',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report reference'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'reference linking a requirement to the corresponding verification report or certificate'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ReportReference/1'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'file://report.pdf', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            
                                    
                            super().__init__(
                                
                                            value = value,
                                            
                                            
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
                            
                                        

                                
                            reportreferences_items: Iterable[Union[Reference, Reportreferences_item]],
                                


                                


                                        id_short: Optional[str]=r'ReportReferences',
                                        
                                        type_value_list_element: SubmodelElement=ReferenceElement,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report references'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'list of references to reports providing evidence for compliance with requirements'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ReportReferences/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            
                                
                        # Build a list of submodel elements if a raw values were passed in the argument
                        if reportreferences_items and all([isinstance(i, Reference) for i in reportreferences_items]):
                            reportreferences_items=[self. Reportreferences_item(i) for i in reportreferences_items]
                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [reportreferences_items]:
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

                        

                class Requirement(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'Requirement',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Requirement'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'individual fire protection requirement to be fulfilled according to the applicable standard'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Requirement/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'R1 requirement for hazard level HL3 according to EN 45545-2', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                        
                                    

                            
                        hazardLevel: Union[str, HazardLevel],
                            

                            
                        reportReferences: ReportReferences,
                            

                            
                        requirement: Union[str, Requirement],
                            


                            

                            

                            


                                    id_short: Optional[str]=r'requirementssets_item',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Requirement set'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'collection of fire protection requirements applicable to a specific product, component, or material.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/RequirementsSet/1'),), referred_semantic_id=None),
                                    
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
                    if hazardLevel and not isinstance(hazardLevel, SubmodelElement):
                        hazardLevel=self. HazardLevel(hazardLevel)
                        

                        

                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if requirement and not isinstance(requirement, SubmodelElement):
                        requirement=self. Requirement(requirement)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [hazardLevel,reportReferences,requirement]:
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
                    
                                

                        
                    requirementssets_items: Iterable[Requirementssets_item],
                        


                        


                                id_short: Optional[str]=r'RequirementsSets',
                                
                                type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=None,
                                
                                order_relevant: bool=True,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Requirements sets'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'list of requirement sets defining applicable fire protection requirements'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/RequirementsSets/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [requirementssets_items]:
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

                



        class Reports(SubmodelElementList):

            

            class Reports_item(SubmodelElementCollection):

                class ReportFile(File):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ReportFile',
                                        
                                        content_type: Optional[str]=r'application/pdf',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report file'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'digital file containing the report document, such as a test report or certificate'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ReportFile/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'/aasx/files/datasheet_en.pdf', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                    
                        
                        



                class Tests(SubmodelElementList):

                    

                    class Tests_item(SubmodelElementCollection):

                        class TestProcedure(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'TestProcedure',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test procedure'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'description of the test method or procedure applied to verify fire protection requirements'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestProcedure/1'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'cone calorimeter test according to EN ISO 5660-1', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                                
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
                            
                                
                                

                        class TestResult(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'TestResult',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test result'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'outcome of the performed fire protection test, indicating conformity or non‑conformity'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestResult/1'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'requirement R1 fulfilled for hazard level HL3', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                                
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
                            
                                
                                

                        class TestDate(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: Date,
                                                
                                                
                                                id_short: Optional[str]=r'TestDate',
                                                
                                                value_type: DataTypeDefXsd=Date,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test date'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'date on which the fire protection test was performed'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestDate/1'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=Date, value=Date(), value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                                
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
                            
                                
                                

                        class TestComment(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'TestComment',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test comment'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'additional remarks or observations related to the performed test'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestComment/1'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'measured heat release rate and MARHE values within specified limits', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                                
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
                            
                                
                                

                        class TestReportNumber(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'TestReportNumber',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test report number'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'unique identifier assigned to the fire protection test report by the issuing body'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestReportNumber/1'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'FR-TEST-2026-00123', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                                
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
                                
                                            

                                    
                                testProcedure: Union[str, TestProcedure],
                                    

                                    
                                testResult: Union[str, TestResult],
                                    

                                    
                                testDate: Union[Date, TestDate],
                                    

                                    

                                    
                                testReportNumber: Union[str, TestReportNumber],
                                    


                                    

                                    

                                    

                                    
                                testComment: Optional[Union[str, TestComment]] = None,
                                    

                                    


                                            id_short: Optional[str]=r'tests_item',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Test'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'collection of test-related information'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Test/1'),), referred_semantic_id=None),
                                            
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
                            if testProcedure and not isinstance(testProcedure, SubmodelElement):
                                testProcedure=self. TestProcedure(testProcedure)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if testResult and not isinstance(testResult, SubmodelElement):
                                testResult=self. TestResult(testResult)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if testDate and not isinstance(testDate, SubmodelElement):
                                testDate=self. TestDate(testDate)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if testComment and not isinstance(testComment, SubmodelElement):
                                testComment=self. TestComment(testComment)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if testReportNumber and not isinstance(testReportNumber, SubmodelElement):
                                testReportNumber=self. TestReportNumber(testReportNumber)
                                


                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [testProcedure,testResult,testDate,testComment,testReportNumber]:
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
                            
                                        

                                
                            tests_items: Iterable[Tests_item],
                                


                                


                                        id_short: Optional[str]=r'Tests',
                                        
                                        type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Tests'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'list of tests performed to verify conformity with specified fire protection requirements.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Tests/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [tests_items]:
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

                        

                class ReportComment(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ReportComment',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report comment'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'additional remarks or notes related to the report and its content'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ReportComment/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'test results demonstrate compliance with EN 45545-2 requirements for the intended application', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                    
                        
                        



                class LabInformation(SubmodelElementCollection):

                    class LabName(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'LabName',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Lab name'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'name of the laboratory that carried out the fire protection test'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/LabName/1'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Independent Fire Testing Laboratory Ltd.', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                            
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
                        
                            
                            



                    class LabAddress(SubmodelElementCollection):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            



                                            id_short: Optional[str]=r'LabAddress',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Lab address'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'reference to the address or contact information of the testing laboratory


                                drop‑in definition of the Contact Information 1.0 Submodel; all or a subset of the defined elements of the Contact Information 1.0 Submodel may be used within this SMC.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/LabAddress/1'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/smt-dropin/smt-dropin-use/1/0'),), referred_semantic_id=None),),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            

                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            





                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in []:
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
                        
                            
                            

                    class LabAccreditation(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'LabAccreditation',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Lab accreditation'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'information about the laboratory’s accreditation according to relevant standards or schemes'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/LabAccreditation/1'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'accredited according to ISO/IEC 17025 for fire testing methods (EN ISO 5660-1, EN ISO 5659-2)', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                            
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
                        
                            
                            

                    class ReportAuthor(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'ReportAuthor',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report author'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'name of the person or organization responsible for creating or issuing the report'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/ReportAuthor/1'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Fire Testing Laboratory Certification Body', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                            
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
                            
                                        

                                
                            labName: Union[str, LabName],
                                

                                
                            labAddress: LabAddress,
                                

                                

                                


                                

                                

                                
                            labAccreditation: Optional[Union[str, LabAccreditation]] = None,
                                

                                
                            reportAuthor: Optional[Union[str, ReportAuthor]] = None,
                                


                                        id_short: Optional[str]=r'LabInformation',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Lab information'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'collection of information describing the laboratory responsible for performing the tests'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/LabInformation/1'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if labName and not isinstance(labName, SubmodelElement):
                            labName=self. LabName(labName)
                            

                            

                            

                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if labAccreditation and not isinstance(labAccreditation, SubmodelElement):
                            labAccreditation=self. LabAccreditation(labAccreditation)
                            

                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if reportAuthor and not isinstance(reportAuthor, SubmodelElement):
                            reportAuthor=self. ReportAuthor(reportAuthor)
                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [labName,labAddress,labAccreditation,reportAuthor]:
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
                        
                                    

                            
                        reportFile: ReportFile,
                            

                            
                        tests: Tests,
                            

                            

                            
                        labInformation: LabInformation,
                            


                            

                            

                            
                        reportComment: Optional[Union[str, ReportComment]] = None,
                            

                            


                                    id_short: Optional[str]=r'reports_item',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Report'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'collection of a report providing verification evidence for fire protection compliance.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Report/1'),), referred_semantic_id=None),
                                    
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
                    if reportComment and not isinstance(reportComment, SubmodelElement):
                        reportComment=self. ReportComment(reportComment)
                        

                        

                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [reportFile,tests,reportComment,labInformation]:
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
                    
                                

                        
                    reports_items: Iterable[Reports_item],
                        


                        


                                id_short: Optional[str]=r'Reports',
                                
                                type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=None,
                                
                                order_relevant: bool=True,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Reports'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'list of reports providing verification evidence for fire protection compliance.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Reports/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [reports_items]:
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
                
                            

                    
                requirementsSets: RequirementsSets,
                    

                    
                reports: Reports,
                    


                    

                    


                            id_short: Optional[str]=r'FireProtectionCertificates',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Fire certificate inventory list'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'structures fire protection compliance by linking applicable requirements with their verification evidence, such as test reports and certificates in accordance with EN 45545‑2.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/FireProtectionCertificates/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                

                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [requirementsSets,reports]:
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
        
            
            



    class Material(SubmodelElementCollection):

        class MaterialName(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'MaterialName',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'name of the material used'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/MaterialName/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'flame-retardant polymer composite', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
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
            
                
                

        class MaterialManufacturer(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'MaterialManufacturer',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'name of the organization responsible for producing the'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/MaterialManufacturer/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Advanced Materials Solutions Ltd.', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                value = value,
                                
                                
                                id_short = id_short,
                                
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
            
                
                



        class Masses(SubmodelElementCollection):

            class TotalMassPerUnit(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'TotalMassPerUnit',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'total mass of the material per defined unit, used for fire behavior assessment'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TotalMassPerUnit/1'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=Float, value=Float(), value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    

            class CombustibleMassPerUnit(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'CombustibleMassPerUnit',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'portion of the material mass per unit that is combustible'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/CombustibleMassPerUnit/1'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=Float, value=Float(), value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    

            class Unit(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'Unit',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'unit of measure for the stated masses; should be one of kg, kg/m, kg/m² or kg/m³'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Unit/1'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'kg/m²', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                    
                                

                        
                    totalMassPerUnit: Union[Float, TotalMassPerUnit],
                        

                        
                    combustibleMassPerUnit: Union[Float, CombustibleMassPerUnit],
                        

                        
                    unit: Union[str, Unit],
                        


                        

                        

                        


                                id_short: Optional[str]=r'Masses',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'mass-related characteristics of the material, used for fire behavior assessment'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Masses/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if totalMassPerUnit and not isinstance(totalMassPerUnit, SubmodelElement):
                    totalMassPerUnit=self. TotalMassPerUnit(totalMassPerUnit)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if combustibleMassPerUnit and not isinstance(combustibleMassPerUnit, SubmodelElement):
                    combustibleMassPerUnit=self. CombustibleMassPerUnit(combustibleMassPerUnit)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if unit and not isinstance(unit, SubmodelElement):
                    unit=self. Unit(unit)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [totalMassPerUnit,combustibleMassPerUnit,unit]:
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
            
                
                

        class MaterialCharacteristics(Range):

            
                
                
            def __init__(
                    self,
                    
                                min: Int,
                                
                                max: Int,
                                
                                
                                id_short: Optional[str]=r'MaterialCharacteristics',
                                
                                value_type: DataTypeDefXsd=Int,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Material characteristics'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'normalized index (0–100) derived from fire performance parameters according to EN 45545‑2'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/MaterialCharacteristics/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                
                        
                super().__init__(
                    
                                min = min,
                                
                                max = max,
                                
                                
                                id_short = id_short,
                                
                                value_type = value_type,
                                
                                display_name = display_name,
                                
                                category = category,
                                
                                description = description,
                                
                                semantic_id = semantic_id,
                                
                                qualifier = qualifier,
                                
                                extension = extension,
                                
                                supplemental_semantic_id = supplemental_semantic_id,
                                
                                embedded_data_specifications = embedded_data_specifications,
                                
                                
                                
                )
            
                
                

        class TestedMaterialCombinationDescription(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'TestedMaterialCombinationDescription',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Tested material combination description'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'description of the material combination as tested in fire protection assessments'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/TestedMaterialCombinationDescription/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'multi-layer assembly consisting of polymer composite panel with surface coating and insulation substrate', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
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
                
                            

                    

                    

                    
                masses: Masses,
                    

                    
                materialCharacteristics: Union[Tuple[Int, Int], MaterialCharacteristics],
                    

                    


                    
                materialName: Optional[Union[LangStringSet, MaterialName]] = None,
                    

                    
                materialManufacturer: Optional[Union[LangStringSet, MaterialManufacturer]] = None,
                    

                    

                    

                    
                testedMaterialCombinationDescription: Optional[Union[str, TestedMaterialCombinationDescription]] = None,
                    


                            id_short: Optional[str]=r'Material',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Material information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'describes the fire‑relevant characteristics of the materials used, providing the technical basis for fire behavior assessment and interpretation of test results.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/Material/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if materialName and not isinstance(materialName, SubmodelElement):
                materialName=self. MaterialName(materialName)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if materialManufacturer and not isinstance(materialManufacturer, SubmodelElement):
                materialManufacturer=self. MaterialManufacturer(materialManufacturer)
                

                

                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if materialCharacteristics and not isinstance(materialCharacteristics, SubmodelElement):
                materialCharacteristics=self. MaterialCharacteristics(materialCharacteristics)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if testedMaterialCombinationDescription and not isinstance(testedMaterialCombinationDescription, SubmodelElement):
                testedMaterialCombinationDescription=self. TestedMaterialCombinationDescription(testedMaterialCombinationDescription)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [materialName,materialManufacturer,masses,materialCharacteristics,testedMaterialCombinationDescription]:
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
                        
                        

                
            manufacturerInformation: ManufacturerInformation,
                

                
            fireProtectionCertificates: FireProtectionCertificates,
                

                
            material: Material,
                


                

                

                


                        id_short: Optional[str]=r'RailwayFireProtection',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Railway Fire Protection Submodel'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Contains the fire protection information associated with the product or component.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=None, embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/RailwayFireProtection/1'),), referred_semantic_id=None),
                        
                        qualifier: Iterable[Qualifier]=None,
                        
                        kind: ModellingKind=ModellingKind.TEMPLATE,
                        
                        extension: Iterable[Extension]=(),
                        
                        supplemental_semantic_id: Iterable[Reference]=(),
                        
                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                        
                        

                        
    ):
        
        if qualifier is None:
            qualifier = ()
        
        if embedded_data_specifications is None:
            embedded_data_specifications = []
        
        




            

            

            

            

            

            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [manufacturerInformation,fireProtectionCertificates,material]:
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
    
        
        