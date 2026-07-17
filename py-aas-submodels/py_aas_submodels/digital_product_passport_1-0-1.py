
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class DppMetadata(Submodel):

    class DigitalProductPassportId(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'digitalProductPassportId',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Unique Product Passport Identifier (DPP ID)'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Unique identifier of an instance of the digital product'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/digitalProductPassportId/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'https://www.example.org/dpp/1234545', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class UniqueProductIdentifier(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'uniqueProductIdentifier',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Unique Product Identifier'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Unique string of characters for the identification of a product, that also enables a web link to the digital product passport.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/uniqueProductIdentifier/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'https://www.example.org/1234545', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class Granularity(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'granularity',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Granularity'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The granularity of the Product. There are three values: ‘Model‘, ‘Item‘ and ‘Batch‘.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/granularity/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/aas/3/2/AssetKind'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Item', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class DppSchemaVersion(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'dppSchemaVersion',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'DPP Schema Version'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference standard the DPP instance schema refers to.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/dppSchemaVersion/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'ENXXX:v1.0', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class DppStatus(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'dppStatus',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'DPP Status'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Status of the DPP instance as digital resource.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/dppStatus/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'Active', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class LastUpdate(Property):

        
            
            
        def __init__(
                self,
                
                            value: datetime,
                            
                            
                            id_short: Optional[str]=r'lastUpdate',
                            
                            value_type: DataTypeDefXsd=datetime,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Last Update'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Date and time of the latest update to the DPP instance.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/lastUpdate/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'<https://admin-shell.io/aas/3/2/AdministrativeInformation/updatedAt'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=datetime, value=datetime(), value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class EconomicOperatorId(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'economicOperatorId',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Economic Operator ID'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Unique string of characters for the identification of an actor involved in a product’s life cycle.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/economicOperatorId/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'gxx:ppp456789', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            

    class FacilityId(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'facilityId',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Facility ID'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Unique string of characters for the identification of locations or buildings involved in a product’s value chain or used by actors involved in a product’s life cycle.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/facilityId/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'gxx:xxx987654', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
            
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
        
            
            



    class ContentSpecificationIds(SubmodelElementList):

        class Contentspecificationids_item(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'contentspecificationids_item',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Content Specification ID'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/contentSpecificationId/1'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'https://admin-shell-io/idta/digitalproductpassport/Circularity/1', value_id=None, kind=QualifierKind.VALUE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                
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
                
                            

                    
                contentspecificationids_items: Iterable[Union[str, Contentspecificationids_item]],
                    


                    


                            id_short: Optional[str]=r'contentSpecificationIds',
                            
                            type_value_list_element: SubmodelElement=Property,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=str,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Content Specification IDs'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to horizontal or product-type related content specifications for the DPP.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/cds/contentSpecificationIds/1'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a list of submodel elements if a raw values were passed in the argument
            if contentspecificationids_items and all([isinstance(i, str) for i in contentspecificationids_items]):
                contentspecificationids_items=[self. Contentspecificationids_item(i) for i in contentspecificationids_items]
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [contentspecificationids_items]:
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
            
                        id_: str,
                        
                        

                
            digitalProductPassportId: Union[str, DigitalProductPassportId],
                

                
            uniqueProductIdentifier: Union[str, UniqueProductIdentifier],
                

                
            granularity: Union[str, Granularity],
                

                
            dppSchemaVersion: Union[str, DppSchemaVersion],
                

                
            dppStatus: Union[str, DppStatus],
                

                
            lastUpdate: Union[datetime, LastUpdate],
                

                
            economicOperatorId: Union[str, EconomicOperatorId],
                

                

                


                

                

                

                

                

                

                

                
            facilityId: Optional[Union[str, FacilityId]] = None,
                

                
            contentSpecificationIds: Optional[Union[Iterable[str], ContentSpecificationIds]] = None,
                


                        id_short: Optional[str]=r'DppMetadata',
                        
                        display_name: Optional[MultiLanguageNameType]=None,
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'
               Digital record of product characteristics throughout its life cycle.
               
               SOURCE: FprEN 18223:2026(en)   
               '}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=None, embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/cds/dppMetadata/1'),), type_=Submodel, referred_semantic_id=None),
                        
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
        
        




            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if digitalProductPassportId and not isinstance(digitalProductPassportId, SubmodelElement):
            digitalProductPassportId=self. DigitalProductPassportId(digitalProductPassportId)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if uniqueProductIdentifier and not isinstance(uniqueProductIdentifier, SubmodelElement):
            uniqueProductIdentifier=self. UniqueProductIdentifier(uniqueProductIdentifier)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if granularity and not isinstance(granularity, SubmodelElement):
            granularity=self. Granularity(granularity)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if dppSchemaVersion and not isinstance(dppSchemaVersion, SubmodelElement):
            dppSchemaVersion=self. DppSchemaVersion(dppSchemaVersion)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if dppStatus and not isinstance(dppStatus, SubmodelElement):
            dppStatus=self. DppStatus(dppStatus)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if lastUpdate and not isinstance(lastUpdate, SubmodelElement):
            lastUpdate=self. LastUpdate(lastUpdate)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if economicOperatorId and not isinstance(economicOperatorId, SubmodelElement):
            economicOperatorId=self. EconomicOperatorId(economicOperatorId)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if facilityId and not isinstance(facilityId, SubmodelElement):
            facilityId=self. FacilityId(facilityId)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if contentSpecificationIds and not isinstance(contentSpecificationIds, SubmodelElement):
            contentSpecificationIds=self. ContentSpecificationIds(contentSpecificationIds)
            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [digitalProductPassportId,uniqueProductIdentifier,granularity,dppSchemaVersion,dppStatus,lastUpdate,economicOperatorId,facilityId,contentSpecificationIds]:
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
    
        
        