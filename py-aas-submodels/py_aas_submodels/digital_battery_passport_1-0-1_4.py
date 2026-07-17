
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class MaterialComposition(Submodel):

    

    class BatteryChemistry(SubmodelElementCollection):

        class ShortName(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ShortName',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'short name'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#shortName'),), referred_semantic_id=None),
                                
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
            
                
                

        class ClearName(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ClearName',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'clear name'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#clearName'),), referred_semantic_id=None),
                                
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
            
                
                
            
            
        def __init__(
                self,
                
                            

                    
                shortName: Union[str, ShortName],
                    

                    
                clearName: Union[str, ClearName],
                    


                    

                    


                            id_short: Optional[str]=r'BatteryChemistry',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery chemistry'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryChemistry'),), referred_semantic_id=None),
                            
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
            if shortName and not isinstance(shortName, SubmodelElement):
                shortName=self. ShortName(shortName)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if clearName and not isinstance(clearName, SubmodelElement):
                clearName=self. ClearName(clearName)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [shortName,clearName]:
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
        
            
            



    class BatteryMaterials(SubmodelElementList):

        

        class Batterymaterials_item(SubmodelElementCollection):

            

            class BatteryMaterialLocation(SubmodelElementCollection):

                class ComponentName(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ComponentName',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'component name'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentName'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/EitherOr', value_type=str, value=r'BatteryMaterialLocationComponent', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/EitherOr/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                    
                        
                        

                class ComponentId(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ComponentId',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'component ID'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentId'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/EitherOr', value_type=str, value=r'BatteryMaterialLocationComponent', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/EitherOr/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                        
                                    

                            

                            


                            
                        componentName: Optional[Union[str, ComponentName]] = None,
                            

                            
                        componentId: Optional[Union[str, ComponentId]] = None,
                            


                                    id_short: Optional[str]=r'BatteryMaterialLocation',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery material location'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialLocation'),), referred_semantic_id=None),
                                    
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
                    if componentName and not isinstance(componentName, SubmodelElement):
                        componentName=self. ComponentName(componentName)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if componentId and not isinstance(componentId, SubmodelElement):
                        componentId=self. ComponentId(componentId)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [componentName,componentId]:
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
                
                    
                    

            class BatteryMaterialIdentifier(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'BatteryMaterialIdentifier',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery material identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialIdentifier'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://www.cas.org/cas-data/cas-registry'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-ABH034#003'),), referred_semantic_id=None)),
                                    
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
                
                    
                    

            class BatteryMaterialName(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'BatteryMaterialName',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery material name'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialName'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAN920#003'),), referred_semantic_id=None),),
                                    
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
                
                    
                    

            class BatteryMaterialMass(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'BatteryMaterialMass',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery material mass'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterialMass'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'2.35', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    

            class IsCriticalRawMaterial(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: bool,
                                    
                                    
                                    id_short: Optional[str]=r'IsCriticalRawMaterial',
                                    
                                    value_type: DataTypeDefXsd=bool,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'is critical raw material'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#isCriticalRawMaterial'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    batteryMaterialLocation: BatteryMaterialLocation,
                        

                        
                    batteryMaterialIdentifier: Union[str, BatteryMaterialIdentifier],
                        

                        
                    batteryMaterialName: Union[str, BatteryMaterialName],
                        

                        

                        
                    isCriticalRawMaterial: Union[bool, IsCriticalRawMaterial],
                        


                        

                        

                        

                        
                    batteryMaterialMass: Optional[Union[Float, BatteryMaterialMass]] = None,
                        

                        


                                id_short: Optional[str]=r'batterymaterials_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery material'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#BatteryMaterial'),), referred_semantic_id=None),
                                
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
                if batteryMaterialIdentifier and not isinstance(batteryMaterialIdentifier, SubmodelElement):
                    batteryMaterialIdentifier=self. BatteryMaterialIdentifier(batteryMaterialIdentifier)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if batteryMaterialName and not isinstance(batteryMaterialName, SubmodelElement):
                    batteryMaterialName=self. BatteryMaterialName(batteryMaterialName)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if batteryMaterialMass and not isinstance(batteryMaterialMass, SubmodelElement):
                    batteryMaterialMass=self. BatteryMaterialMass(batteryMaterialMass)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if isCriticalRawMaterial and not isinstance(isCriticalRawMaterial, SubmodelElement):
                    isCriticalRawMaterial=self. IsCriticalRawMaterial(isCriticalRawMaterial)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [batteryMaterialLocation,batteryMaterialIdentifier,batteryMaterialName,batteryMaterialMass,isCriticalRawMaterial]:
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
                
                            

                    
                batterymaterials_items: Iterable[Batterymaterials_item],
                    


                    


                            id_short: Optional[str]=r'BatteryMaterials',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery materials'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#batteryMaterials'),), referred_semantic_id=None),
                            
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
            for se_arg in [batterymaterials_items]:
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

            



    class HazardousSubstances(SubmodelElementList):

        

        class Hazardoussubstances_item(SubmodelElementCollection):

            class HazardousSubstanceClass(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'HazardousSubstanceClass',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance class'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceClass'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'AcuteToxicity', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    

            class HazardousSubstanceName(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'HazardousSubstanceName',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance name'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceName'),), referred_semantic_id=None),
                                    
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
                
                    
                    

            class HazardousSubstanceConcentration(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: float,
                                    
                                    
                                    id_short: Optional[str]=r'HazardousSubstanceConcentration',
                                    
                                    value_type: DataTypeDefXsd=float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance concentration'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceConcentration'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'0.12', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    



            class HazardousSubstanceImpact(SubmodelElementList):

                class Hazardoussubstanceimpact_item(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'hazardoussubstanceimpact_item',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'impact'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#Impact'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue', value_type=str, value=r'H302 Harmful if swallowed', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                        
                                    

                            


                            
                        hazardoussubstanceimpact_items: Optional[Iterable[Union[str, Hazardoussubstanceimpact_item]]] = None,
                            


                                    id_short: Optional[str]=r'HazardousSubstanceImpact',
                                    
                                    type_value_list_element: SubmodelElement=Property,
                                    
                                    semantic_id_list_element: Optional[Reference]=None,
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=str,
                                    
                                    order_relevant: bool=False,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance impact'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceImpact'),), referred_semantic_id=None),
                                    
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
                    if hazardoussubstanceimpact_items and all([isinstance(i, str) for i in hazardoussubstanceimpact_items]):
                        hazardoussubstanceimpact_items=[self. Hazardoussubstanceimpact_item(i) for i in hazardoussubstanceimpact_items]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [hazardoussubstanceimpact_items]:
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

                    



            class HazardousSubstanceLocation(SubmodelElementCollection):

                class ComponentName(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ComponentName',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'component name'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentName'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/EitherOr', value_type=str, value=r'HazardousSubstanceLocationComponent', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/EitherOr/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                    
                        
                        

                class ComponentId(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ComponentId',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'component ID'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#componentId'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/EitherOr', value_type=str, value=r'HazardousSubstanceLocationComponent', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/EitherOr/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                        
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
                        
                                    

                            

                            


                            
                        componentName: Optional[Union[str, ComponentName]] = None,
                            

                            
                        componentId: Optional[Union[str, ComponentId]] = None,
                            


                                    id_short: Optional[str]=r'HazardousSubstanceLocation',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance location'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceLocation'),), referred_semantic_id=None),
                                    
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
                    if componentName and not isinstance(componentName, SubmodelElement):
                        componentName=self. ComponentName(componentName)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if componentId and not isinstance(componentId, SubmodelElement):
                        componentId=self. ComponentId(componentId)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [componentName,componentId]:
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
                
                    
                    

            class HazardousSubstanceIdentifier(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'HazardousSubstanceIdentifier',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstanceIdentifier'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://www.cas.org/cas-data/cas-registry'),), referred_semantic_id=None),),
                                    
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
                    
                                

                        

                        
                    hazardousSubstanceName: Union[str, HazardousSubstanceName],
                        

                        

                        

                        

                        
                    hazardousSubstanceIdentifier: Union[str, HazardousSubstanceIdentifier],
                        


                        
                    hazardousSubstanceClass: Optional[Union[str, HazardousSubstanceClass]] = None,
                        

                        

                        
                    hazardousSubstanceConcentration: Optional[Union[float, HazardousSubstanceConcentration]] = None,
                        

                        
                    hazardousSubstanceImpact: Optional[Union[Iterable[str], HazardousSubstanceImpact]] = None,
                        

                        
                    hazardousSubstanceLocation: Optional[HazardousSubstanceLocation] = None,
                        

                        


                                id_short: Optional[str]=r'hazardoussubstances_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substance'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#HazardousSubstance'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if hazardousSubstanceClass and not isinstance(hazardousSubstanceClass, SubmodelElement):
                    hazardousSubstanceClass=self. HazardousSubstanceClass(hazardousSubstanceClass)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if hazardousSubstanceName and not isinstance(hazardousSubstanceName, SubmodelElement):
                    hazardousSubstanceName=self. HazardousSubstanceName(hazardousSubstanceName)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if hazardousSubstanceConcentration and not isinstance(hazardousSubstanceConcentration, SubmodelElement):
                    hazardousSubstanceConcentration=self. HazardousSubstanceConcentration(hazardousSubstanceConcentration)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if hazardousSubstanceImpact and not isinstance(hazardousSubstanceImpact, SubmodelElement):
                    hazardousSubstanceImpact=self. HazardousSubstanceImpact(hazardousSubstanceImpact)
                    

                    

                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if hazardousSubstanceIdentifier and not isinstance(hazardousSubstanceIdentifier, SubmodelElement):
                    hazardousSubstanceIdentifier=self. HazardousSubstanceIdentifier(hazardousSubstanceIdentifier)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [hazardousSubstanceClass,hazardousSubstanceName,hazardousSubstanceConcentration,hazardousSubstanceImpact,hazardousSubstanceLocation,hazardousSubstanceIdentifier]:
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
                
                            

                    


                    
                hazardoussubstances_items: Optional[Iterable[Hazardoussubstances_item]] = None,
                    


                            id_short: Optional[str]=r'HazardousSubstances',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'hazardous substances'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.1#hazardousSubstances'),), referred_semantic_id=None),
                            
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
            for se_arg in [hazardoussubstances_items]:
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
                        
                        

                
            batteryChemistry: BatteryChemistry,
                

                
            batteryMaterials: BatteryMaterials,
                

                
            hazardousSubstances: HazardousSubstances,
                


                

                

                


                        id_short: Optional[str]=r'MaterialComposition',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'material composition'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Mandatory data: Battery chemistry; critical raw materials; materials used in the cathode, anode, and 
            electrolyte; hazardous substances; impact of substances on the environment and on human health or 
            safety.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02035-6', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.material_composition:1.0.0#MaterialComposition'),), referred_semantic_id=None),
                        
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
        for se_arg in [batteryChemistry,batteryMaterials,hazardousSubstances]:
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
    
        
        