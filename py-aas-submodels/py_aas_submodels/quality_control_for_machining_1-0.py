
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class QualityControlForMachining(Submodel):

    

    class QualityFeatures(SubmodelElementCollection):

        
            
            
        def __init__(
                self,
                
                            



                            id_short: Optional[str]=r'QualityFeatures',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Quality criteria of the item and their properties',r'de': r'Qualitätskriterien des Artikels und deren Eigenschaften'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/QualityFeatures/1/0'),), referred_semantic_id=None),
                            
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
        
            
            



    class ProductionCriteria(SubmodelElementCollection):

        class TechnicalData(ReferenceElement):

            
                
                
            def __init__(
                    self,
                    
                                value: Reference,
                                
                                
                                id_short: Optional[str]=r'TechnicalData',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to the AAS Submodel Technical Data for Industrial
                    Equipment in Manufacturing',r'de': r'Referenz auf das AAS Submodel Technical Data for Industrial
                    Equipment in Manufacturing"'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/TechnicalData/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                



        class ProductionJobOrderParameters(SubmodelElementCollection):

            class ProductionStart(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: datetime,
                                    
                                    
                                    id_short: Optional[str]=r'ProductionStart',
                                    
                                    value_type: DataTypeDefXsd=datetime,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Date and time when production started for the production order',r'de': r'Datum und Uhrzeit des Starts der Produktion für den Produktionsauftrag'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ProductionStart/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61360_4#ADA031#001'),), referred_semantic_id=None),),
                                    
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
                
                    
                    

            class ProductionEnd(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: datetime,
                                    
                                    
                                    id_short: Optional[str]=r'ProductionEnd',
                                    
                                    value_type: DataTypeDefXsd=datetime,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Date and time when production ended for the production order',r'de': r'Datum und Uhrzeit des Endes der Produktion für den Produktionsauftrag'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ProductionEnd/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61360_4#ADA031#001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class JobName(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'JobName',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Human readable name of the job. Array shall always contain the same text, potentially in different languages.',r'de': r'Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class JobOrderNumber(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'JobOrderNumber',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.',r'de': r'Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class PlannedPartsPerRun(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'PlannedPartsPerRun',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The number of parts produced by one run',r'de': r'Die Anzahl der Teile, die in einem Lauf produziert werden'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class PlannedOrderQuantity(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'PlannedOrderQuantity',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The planned order quantity shall be the planned quantity of products for a production order (lot size, production order quantity). [Source: ISO 22400]',r'de': r'Die geplante Auftragsmenge ist die geplante Produktmenge für einen Produktionsauftrag (Losgröße, Produktionsauftragsmenge). [Quelle: ISO 22400]'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PlannedOrderQuantity/1/0'),), referred_semantic_id=None),
                                    
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
                
                    
                    

            class ActualPartsInRun(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: int,
                                    
                                    
                                    id_short: Optional[str]=r'ActualPartsInRun',
                                    
                                    value_type: DataTypeDefXsd=int,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The number of parts actually measuerd by one run',r'de': r'Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class JobFinished(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: bool,
                                    
                                    
                                    id_short: Optional[str]=r'JobFinished',
                                    
                                    value_type: DataTypeDefXsd=bool,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Status order completed. True: yes, false: no',r'de': r'Status Auftrag beendet. True: ja, false: nein'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                    
                                

                        
                    productionStart: Union[datetime, ProductionStart],
                        

                        

                        

                        
                    jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
                        

                        

                        
                    plannedOrderQuantity: Union[int, PlannedOrderQuantity],
                        

                        

                        


                        

                        
                    productionEnd: Optional[Union[datetime, ProductionEnd]] = None,
                        

                        
                    jobName: Optional[Union[str, JobName]] = None,
                        

                        

                        
                    plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
                        

                        

                        
                    actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
                        

                        
                    jobFinished: Optional[Union[bool, JobFinished]] = None,
                        


                                id_short: Optional[str]=r'ProductionJobOrderParameters',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Production order information',r'de': r'Informationen zum Produktionsauftrag'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ProductionJobOrderParameters/1/0'),), referred_semantic_id=None),
                                
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
                if productionStart and not isinstance(productionStart, SubmodelElement):
                    productionStart=self. ProductionStart(productionStart)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if productionEnd and not isinstance(productionEnd, SubmodelElement):
                    productionEnd=self. ProductionEnd(productionEnd)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if jobName and not isinstance(jobName, SubmodelElement):
                    jobName=self. JobName(jobName)
                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if jobOrderNumber and all([isinstance(i, str) for i in jobOrderNumber]):
                    jobOrderNumber=[self. JobOrderNumber(i) for i in jobOrderNumber]
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if plannedPartsPerRun and not isinstance(plannedPartsPerRun, SubmodelElement):
                    plannedPartsPerRun=self. PlannedPartsPerRun(plannedPartsPerRun)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if plannedOrderQuantity and not isinstance(plannedOrderQuantity, SubmodelElement):
                    plannedOrderQuantity=self. PlannedOrderQuantity(plannedOrderQuantity)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if actualPartsInRun and not isinstance(actualPartsInRun, SubmodelElement):
                    actualPartsInRun=self. ActualPartsInRun(actualPartsInRun)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if jobFinished and not isinstance(jobFinished, SubmodelElement):
                    jobFinished=self. JobFinished(jobFinished)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [productionStart,productionEnd,jobName,jobOrderNumber,plannedPartsPerRun,plannedOrderQuantity,actualPartsInRun,jobFinished]:
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
                
                            

                    

                    
                productionJobOrderParameters: ProductionJobOrderParameters,
                    


                    
                technicalData: Optional[Union[Reference, TechnicalData]] = None,
                    

                    


                            id_short: Optional[str]=r'ProductionCriteria',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information on production-relevant criteria in connection with the production of a specific component',r'de': r'Informationen zu produktionsrevelvanten Kriterien im Zusammenhang mit der Fertigung eines konkreten Bauteils'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ProductionCriteria/1/0'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if technicalData and not isinstance(technicalData, SubmodelElement):
                technicalData=self. TechnicalData(technicalData)
                

                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [technicalData,productionJobOrderParameters]:
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
        
            
            



    class PartInformation(SubmodelElementCollection):

        class DigitalNameplate(ReferenceElement):

            
                
                
            def __init__(
                    self,
                    
                                value: Reference,
                                
                                
                                id_short: Optional[str]=r'DigitalNameplate',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to the component’s Digital Nameplate submodel, including details such as serial number, product family, product type, and manufacturer.',r'de': r'Referenz zum Submodel Digital Nameplate des Bauteils, mit Informationen zur Seriennummer, Produktfamilie, Produkttyp und Hersteller'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/DigitalNameplate/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class PartIdentifier(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: AnyURI,
                                
                                
                                id_short: Optional[str]=r'PartIdentifier',
                                
                                value_type: DataTypeDefXsd=AnyURI,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to the AAS of the component: IRDI of the management shell of the component, which is carried in the machine to assign the manufacturing data for the component',r'de': r'Referenz auf die AAS des Bauteils: IRDI der Verwaltungschale des Bauteils, die in der Maschine zur Zuordnung der Fertigungsdaten für das Bauteil mitgeführt wird'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PartIdentifier/1/0'),), referred_semantic_id=None),
                                
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
            
                
                

        class PartNumber(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: int,
                                
                                
                                id_short: Optional[str]=r'PartNumber',
                                
                                value_type: DataTypeDefXsd=int,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Consecutive number of the manufactured component in the batch from the CNC',r'de': r'Fortlaufende Nummer des gefertigten Bauteil im Los aus der CNC'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PartNumber/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61360_4#ADA029#001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class OrderNumber(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'OrderNumber',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Identifier to identify the order. Shall be provided if defined in OutputInfo.',r'de': r'Bezeichner zur Identifizierung der Bestellung. Wird bereitgestellt, wenn in Output Info definiert.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/OrderNumber/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class LotNumber(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'LotNumber',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Identifier to identify the production lot. Shall be provided if defined in OutputInfo.',r'de': r'Bezeichner zur Identifizierung des Fertigungsloses. Wird bereitgestellt, wenn in Output Info definiert.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/LotNumber/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class SubmodelReference3D(ReferenceElement):

            
                
                
            def __init__(
                    self,
                    
                                value: Reference,
                                
                                
                                id_short: Optional[str]=r'SubmodelReference3D',
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to IDTA Submodel Provision of 3D Models',r'de': r'Reference auf IDTA Submodel Provision of 3D Models'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/3DSubmodelReference/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class DrawingReference2D(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'DrawingReference2D',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to a pdf-file containing the 2D drawing intended as a reference for humans, not for automation, as unambiguous interpretation cannot be guaranteed. All drawings referenced in the submodel have to be included in a single PDF document.',r'de': r'Referenz zum pdf-Dokument einer 2D Zeichnung als Nachschlagewerk für Menschen, nicht für Automatisierung gedacht, da Eindeutigkeit nicht gewährleistet werden kann. Es wird vorausgesetzt, dass alle im Submodel referenzierten Zeichnungen in einem pdf Dokument enthalten sind.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/DrawingReference2D/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class CADFileReference3D(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'CADFileReference3D',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to a file which contains a §D CAD  model, elg. STL-file',r'de': r'Referenz auf eine Datei die ein §D CAD Modell enthält, z.B. STL-file'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/CADFileReference3D/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
                
                            

                    

                    
                partIdentifier: Union[AnyURI, PartIdentifier],
                    

                    

                    

                    

                    

                    

                    


                    
                digitalNameplate: Optional[Union[Reference, DigitalNameplate]] = None,
                    

                    

                    
                partNumber: Optional[Union[int, PartNumber]] = None,
                    

                    
                orderNumber: Optional[Union[str, OrderNumber]] = None,
                    

                    
                lotNumber: Optional[Union[str, LotNumber]] = None,
                    

                    
                submodelReference3D: Optional[Union[Reference, SubmodelReference3D]] = None,
                    

                    
                drawingReference2D: Optional[Union[str, DrawingReference2D]] = None,
                    

                    
                cADFileReference3D: Optional[Union[str, CADFileReference3D]] = None,
                    


                            id_short: Optional[str]=r'PartInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Production information about the component',r'de': r'Produktionsinformationen zu dem Bauteil'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PartInformation/1/0'),), referred_semantic_id=None),
                            
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
            if digitalNameplate and not isinstance(digitalNameplate, SubmodelElement):
                digitalNameplate=self. DigitalNameplate(digitalNameplate)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if partIdentifier and not isinstance(partIdentifier, SubmodelElement):
                partIdentifier=self. PartIdentifier(partIdentifier)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if partNumber and not isinstance(partNumber, SubmodelElement):
                partNumber=self. PartNumber(partNumber)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if orderNumber and not isinstance(orderNumber, SubmodelElement):
                orderNumber=self. OrderNumber(orderNumber)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if lotNumber and not isinstance(lotNumber, SubmodelElement):
                lotNumber=self. LotNumber(lotNumber)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if submodelReference3D and not isinstance(submodelReference3D, SubmodelElement):
                submodelReference3D=self. SubmodelReference3D(submodelReference3D)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if drawingReference2D and not isinstance(drawingReference2D, SubmodelElement):
                drawingReference2D=self. DrawingReference2D(drawingReference2D)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if cADFileReference3D and not isinstance(cADFileReference3D, SubmodelElement):
                cADFileReference3D=self. CADFileReference3D(cADFileReference3D)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [digitalNameplate,partIdentifier,partNumber,orderNumber,lotNumber,submodelReference3D,drawingReference2D,cADFileReference3D]:
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
        
            
            



    class MetrologyJobResults(SubmodelElementCollection):

        class JobStart(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: datetime,
                                
                                
                                id_short: Optional[str]=r'JobStart',
                                
                                value_type: DataTypeDefXsd=datetime,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Date time of job start',r'de': r'Datum und Zeit des Starts des Auftrags'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobStart/1/0'),), referred_semantic_id=None),
                                
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
            
                
                

        class JobEnd(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: datetime,
                                
                                
                                id_short: Optional[str]=r'JobEnd',
                                
                                value_type: DataTypeDefXsd=datetime,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Date time of job end',r'de': r'Datum und Zeit des Endes des Auftrags'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobEnd/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class JobName(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'JobName',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Human readable name of the job. Array shall always contain the same text, potentially in different languages.',r'de': r'Für Menschen lesbarer Name des Jobs. Das Array muss immer denselben Text enthalten, möglicherweise in verschiedenen Sprachen.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobName/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class JobOrderNumber(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'JobOrderNumber',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The OrderNumbers are used to reference company internal ERP orders the job order belongs to. Shall be provided in JobOrderParameters if any planned produced material uses OrderNumber as Identification and shall contain all those OrderNumbers.',r'de': r'Die Bestellnummern werden verwendet, um unternehmensinterne ERP-Bestellungen zu referenzieren, zu denen der Auftrag gehört. Wird in JobOrderParameters angegeben, wenn ein geplantes produziertes Material die Bestellnummer als Identifikation verwendet, und muss alle diese Bestellnummern enthalten.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobOrderNumber/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class PlannedPartsPerRun(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: int,
                                
                                
                                id_short: Optional[str]=r'PlannedPartsPerRun',
                                
                                value_type: DataTypeDefXsd=int,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The number of parts planned to be measured by one run',r'de': r'Die Anzahl der Teile, die in einem Lauf gemessen werden sollen'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/PlannedPartsPerRun/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class ActualPartsInRun(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: int,
                                
                                
                                id_short: Optional[str]=r'ActualPartsInRun',
                                
                                value_type: DataTypeDefXsd=int,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The number of parts actually measuerd by one run',r'de': r'Die Anzahl der Teile, die in einem Lauf tatsächlich gemessen werden'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/ActualPartsInRun/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class JobFinished(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: bool,
                                
                                
                                id_short: Optional[str]=r'JobFinished',
                                
                                value_type: DataTypeDefXsd=bool,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=None,
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Status order completed. True: yes, false: no',r'de': r'Status Auftrag beendet. True: ja, false: nein'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/JobFinished/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
                
                            

                    
                jobStart: Union[datetime, JobStart],
                    

                    

                    

                    
                jobOrderNumber: Iterable[Union[str, JobOrderNumber]],
                    

                    

                    

                    


                    

                    
                jobEnd: Optional[Union[datetime, JobEnd]] = None,
                    

                    
                jobName: Optional[Union[str, JobName]] = None,
                    

                    

                    
                plannedPartsPerRun: Optional[Union[int, PlannedPartsPerRun]] = None,
                    

                    
                actualPartsInRun: Optional[Union[int, ActualPartsInRun]] = None,
                    

                    
                jobFinished: Optional[Union[bool, JobFinished]] = None,
                    


                            id_short: Optional[str]=r'MetrologyJobResults',
                            
                            display_name: Optional[MultiLanguageNameType]=None,
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information and measurements on the results of a quality assessment order',r'de': r'Informationen und Messwerte zu Ergebnissen eines Qualitätsbewertungsauftrag'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/QualityControlForMachining/MetrologyJobResults/1/0'),), referred_semantic_id=None),
                            
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
            if jobStart and not isinstance(jobStart, SubmodelElement):
                jobStart=self. JobStart(jobStart)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if jobEnd and not isinstance(jobEnd, SubmodelElement):
                jobEnd=self. JobEnd(jobEnd)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if jobName and not isinstance(jobName, SubmodelElement):
                jobName=self. JobName(jobName)
                

                

                
                    
            # Build a list of submodel elements if a raw values were passed in the argument
            if jobOrderNumber and all([isinstance(i, str) for i in jobOrderNumber]):
                jobOrderNumber=[self. JobOrderNumber(i) for i in jobOrderNumber]
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if plannedPartsPerRun and not isinstance(plannedPartsPerRun, SubmodelElement):
                plannedPartsPerRun=self. PlannedPartsPerRun(plannedPartsPerRun)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if actualPartsInRun and not isinstance(actualPartsInRun, SubmodelElement):
                actualPartsInRun=self. ActualPartsInRun(actualPartsInRun)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if jobFinished and not isinstance(jobFinished, SubmodelElement):
                jobFinished=self. JobFinished(jobFinished)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [jobStart,jobEnd,jobName,jobOrderNumber,plannedPartsPerRun,actualPartsInRun,jobFinished]:
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
                        
                        

                
            qualityFeatures: QualityFeatures,
                

                

                
            partInformation: PartInformation,
                

                
            metrologyJobResults: Iterable[MetrologyJobResults],
                


                

                
            productionCriteria: Optional[ProductionCriteria] = None,
                

                

                


                        id_short: Optional[str]=r'QualityControlForMachining',
                        
                        display_name: Optional[MultiLanguageNameType]=None,
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The Submodel Quality Control for Machining allows the collection of quality relevant information about parts produced in cyclical manufacturing processes. The focus is on looking at the production result and on machining manufacturing processes of milling, turning and drilling. However, the Submodel can also be used for other manufacturing processes.',r'de': r'Das Teilmodell Quality Control for Machining erlaubt die Erfassung von qualitätsrelevanten Informationen über in zyklischen Fertigungsprozessen produzierte Bauteile. Der Fokus liegt auf der Betrachtung des Produktionsresultats und auf den zerspanenden Fertigungsverfahren Fräsen, Drehen, Bohren. Das Teilmodell kann jedoch auch für andere Fertigungsverfahren verwendet werden.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02049', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=None,
                        
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
        for se_arg in [qualityFeatures,productionCriteria,partInformation,metrologyJobResults]:
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
    
        
        