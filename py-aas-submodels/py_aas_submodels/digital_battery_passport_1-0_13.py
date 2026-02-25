
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class Circularity(Submodel):

    

    class SafetyMeasures(SubmodelElementCollection):

        
            
            
        def __init__(
                self,
                
                            



                            id_short: Optional[str]=r'SafetyMeasures',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'safety measures'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#safetyMeasures'),), referred_semantic_id=None),
                            
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
        
            
            



    class EndOfLifeInformation(SubmodelElementCollection):

        
            
            
        def __init__(
                self,
                
                            



                            id_short: Optional[str]=r'EndOfLifeInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'end of life information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#endOfLifeInformation'),), referred_semantic_id=None),
                            
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
        
            
            

    class RenewableContent(Property):

        
            
            
        def __init__(
                self,
                
                            value: Float,
                            
                            
                            id_short: Optional[str]=r'RenewableContent',
                            
                            value_type: DataTypeDefXsd=Float,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'renewable content'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#renewableContent'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-ABL867#001'),), referred_semantic_id=None),),
                            
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
            
                        id_: str,
                        
                        

                
            safetyMeasures: SafetyMeasures,
                

                
            endOfLifeInformation: EndOfLifeInformation,
                

                
            renewableContent: Union[Float, RenewableContent],
                


                

                

                


                        id_short: Optional[str]=r'Circularity',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Circularity'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Dismantling information (including at least: exploded diagrams of the battery system/pack showing the location of battery cells; disassembly sequences; type and number of fastening techniques to be unlocked; tools required for disassembly; warnings if risk of damaging parts exists; amount of cells used and layout); part numbers for components and contact details of sources for replacement spares; safety measures 
               
               (Annex XIII (2b-d)); usable extinguishing agent (Annex VI, Part A(9)).'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02035-7', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#Circularity'),), referred_semantic_id=None),
                        
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
        if renewableContent and not isinstance(renewableContent, SubmodelElement):
            renewableContent=self. RenewableContent(renewableContent)
            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [safetyMeasures,endOfLifeInformation,renewableContent]:
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
    
        
        