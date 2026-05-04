
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class CapabilityDescription(Submodel):

    

    class CapabilitySet(SubmodelElementCollection):

        

        class CapabilityContainer(SubmodelElementCollection):

            class Capability(Capability):

                
                    
                    
                def __init__(
                        self,
                        
                                    
                                    id_short: Optional[str]=r'Capability',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'[A capability is a] implementation-independent specification of a function in industrial production to achieve an effect in the physical or virtual world. '}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/Capability/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'Required', value_type=str, value=r'[1, 0]', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Required/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'Offered', value_type=str, value=r'[1, 0]', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/Offered/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'NotAssigned', value_type=str, value=r'[1, 0]', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityRoleQualifier/NotAssigned/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    
                            
                    super().__init__(
                        
                                    
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
                
                    
                    

            class CapabilityComment(MultiLanguageProperty):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: LangStringSet,
                                    
                                    
                                    id_short: Optional[str]=r'CapabilityComment',
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Comment'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Individual comment of the capability.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityComment/1/0'),), referred_semantic_id=None),
                                    
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
                
                    
                    



            class PropertySet(SubmodelElementCollection):

                

                class PropertyContainer(SubmodelElementCollection):

                    class SameProperty(RelationshipElement):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            
                                            id_short: Optional[str]=r'SameProperty',
                                            
                                            first: Reference=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:example:capability-description:same-property:first'),), referred_semantic_id=None),
                                            
                                            second: Reference=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:example:capability-description:same-property:second'),), referred_semantic_id=None),
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Same Property'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relationship of the Property described in the Property container as first element and the identical property as second element in another Submodel or an external information source.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/SameProperty/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            
                                    
                            super().__init__(
                                
                                            
                                            id_short = id_short,
                                            
                                            first = first,
                                            
                                            second = second,
                                            
                                            display_name = display_name,
                                            
                                            category = category,
                                            
                                            description = description,
                                            
                                            semantic_id = semantic_id,
                                            
                                            qualifier = qualifier,
                                            
                                            extension = extension,
                                            
                                            supplemental_semantic_id = supplemental_semantic_id,
                                            
                                            embedded_data_specifications = embedded_data_specifications,
                                            
                                            
                                            
                            )
                        
                            
                            

                    class PropertyRange(Range):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            min: str,
                                            
                                            max: str,
                                            
                                            
                                            id_short: Optional[str]=r'PropertyRange',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Range'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Range made of min and max values forming an interval. A valueId shall be set to define the semantic for the values.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityPropertyEnumType/Range/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
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
                        
                            
                            

                    class PropertyProperty(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'PropertyProperty',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Property'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Property with a value describing an information data point. A valueId shall be set to define the semantic for the value.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityPropertyType/Property/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
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
                        
                            
                            

                    class PropertyMultiLanguageProperty(MultiLanguageProperty):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: LangStringSet,
                                            
                                            
                                            id_short: Optional[str]=r'PropertyMultiLanguageProperty',
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Multi Language Property'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Property with a value for one or more language entries with corresponding text describing an information data point. A valueId shall be set to define the semantic for the value.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityPropertyType/MultiLanguageProperty/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
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
                        
                            
                            

                    class PropertyComment(MultiLanguageProperty):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: LangStringSet,
                                            
                                            
                                            id_short: Optional[str]=r'PropertyComment',
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Comment'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'General description of the property.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyComment/1/0'),), referred_semantic_id=None),
                                            
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
                            
                                        

                                

                                

                                

                                

                                


                                
                            sameProperty: Optional[Iterable[SameProperty]] = None,
                                

                                
                            propertyRange: Optional[Iterable[Union[Tuple[str, str], PropertyRange]]] = None,
                                

                                
                            propertyProperty: Optional[Iterable[Union[str, PropertyProperty]]] = None,
                                

                                
                            propertyMultiLanguageProperty: Optional[Iterable[Union[LangStringSet, PropertyMultiLanguageProperty]]] = None,
                                

                                
                            propertyComment: Optional[Union[LangStringSet, PropertyComment]] = None,
                                


                                        id_short: Optional[str]=r'PropertyContainer',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Container'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information for a certain property as defined by CapabilityPropertyType and its descriptive elements.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyContainer/1/0'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            

                            

                            
                                
                        # Build a list of submodel elements if a raw values were passed in the argument
                        if propertyRange and all([isinstance(i, Tuple[str) for i in propertyRange]):
                            propertyRange=[self. str](i) for i in propertyRange]
                            

                            

                            
                                
                        # Build a list of submodel elements if a raw values were passed in the argument
                        if propertyProperty and all([isinstance(i, str) for i in propertyProperty]):
                            propertyProperty=[self. PropertyProperty(i) for i in propertyProperty]
                            

                            

                            
                                
                        # Build a list of submodel elements if a raw values were passed in the argument
                        if propertyMultiLanguageProperty and all([isinstance(i, LangStringSet) for i in propertyMultiLanguageProperty]):
                            propertyMultiLanguageProperty=[self. PropertyMultiLanguageProperty(i) for i in propertyMultiLanguageProperty]
                            

                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if propertyComment and not isinstance(propertyComment, SubmodelElement):
                            propertyComment=self. PropertyComment(propertyComment)
                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [sameProperty,propertyRange,propertyProperty,propertyMultiLanguageProperty,propertyComment]:
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
                        
                                    

                            
                        propertyContainer: Iterable[PropertyContainer],
                            


                            


                                    id_short: Optional[str]=r'PropertySet',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Set'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Set of properties describing the capability in more detail, if existing.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertySet/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [propertyContainer]:
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
                
                    
                    



            class CapabilityRelations(SubmodelElementCollection):

                class CapabilityRealizedBy(RelationshipElement):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        
                                        id_short: Optional[str]=r'CapabilityRealizedBy',
                                        
                                        first: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                        
                                        second: Reference=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:example:capability-description:capability-realized-by:skill'),), referred_semantic_id=None),
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Realized By'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relationship between the Capability element in the CapabilityContainer as first element and a Skill implementation, not defined in this Submodel template, as second element.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityRealizedBy/1/0'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        
                                
                        super().__init__(
                            
                                        
                                        id_short = id_short,
                                        
                                        first = first,
                                        
                                        second = second,
                                        
                                        display_name = display_name,
                                        
                                        category = category,
                                        
                                        description = description,
                                        
                                        semantic_id = semantic_id,
                                        
                                        qualifier = qualifier,
                                        
                                        extension = extension,
                                        
                                        supplemental_semantic_id = supplemental_semantic_id,
                                        
                                        embedded_data_specifications = embedded_data_specifications,
                                        
                                        
                                        
                        )
                    
                        
                        



                class ComposedOfSet(SubmodelElementCollection):

                    

                    class ComposedOfContainer(SubmodelElementCollection):

                        class CapabilityComposedOf(RelationshipElement):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                
                                                id_short: Optional[str]=r'CapabilityComposedOf',
                                                
                                                first: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                                
                                                second: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Composed Of'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relationship between a composed capability as first element and one of its minimum two subordinate capabilities as second element.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityComposedOf/1/0'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'TwoToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                                
                                if embedded_data_specifications is None:
                                    embedded_data_specifications = []
                                
                                
                                        
                                super().__init__(
                                    
                                                
                                                id_short = id_short,
                                                
                                                first = first,
                                                
                                                second = second,
                                                
                                                display_name = display_name,
                                                
                                                category = category,
                                                
                                                description = description,
                                                
                                                semantic_id = semantic_id,
                                                
                                                qualifier = qualifier,
                                                
                                                extension = extension,
                                                
                                                supplemental_semantic_id = supplemental_semantic_id,
                                                
                                                embedded_data_specifications = embedded_data_specifications,
                                                
                                                
                                                
                                )
                            
                                
                                

                        class ComposedOfComment(MultiLanguageProperty):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: LangStringSet,
                                                
                                                
                                                id_short: Optional[str]=r'ComposedOfComment',
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Composed Of Comment'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Comment to describe the composition in human readable form.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ComposedOfComment/1/0'),), referred_semantic_id=None),
                                                
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
                                
                                            

                                    
                                capabilityComposedOf: CapabilityComposedOf,
                                    

                                    


                                    

                                    
                                composedOfComment: Optional[Union[LangStringSet, ComposedOfComment]] = None,
                                    


                                            id_short: Optional[str]=r'ComposedOfContainer',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Composed Of Container'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Container corresponding to one composition for the Capability in the CapabilityContainer.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ComposedOfContainer/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            

                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            




                                

                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if composedOfComment and not isinstance(composedOfComment, SubmodelElement):
                                composedOfComment=self. ComposedOfComment(composedOfComment)
                                


                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [capabilityComposedOf,composedOfComment]:
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
                            
                                        

                                
                            composedOfContainer: Iterable[ComposedOfContainer],
                                


                                


                                        id_short: Optional[str]=r'ComposedOfSet',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Composed Of Set'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If composition(s) for the Capability element in the CapabilityContainer exists, this set has to be created.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ComposedOfSet/1/0'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [composedOfContainer]:
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
                    
                        
                        



                class GeneralizedBySet(SubmodelElementCollection):

                    class CapabilityGeneralizedBy(RelationshipElement):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            
                                            id_short: Optional[str]=r'CapabilityGeneralizedBy',
                                            
                                            first: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                            
                                            second: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Generalized By'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relationship between the Capability as first element, described in the CapabilityContainer, and a more general Capability as second element.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityGeneralizedBy/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            
                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            
                                    
                            super().__init__(
                                
                                            
                                            id_short = id_short,
                                            
                                            first = first,
                                            
                                            second = second,
                                            
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
                            
                                        

                                
                            capabilityGeneralizedBy: Iterable[CapabilityGeneralizedBy],
                                


                                


                                        id_short: Optional[str]=r'GeneralizedBySet',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Generalized By Set'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If generalization(s) for the Capability element in the CapabilityContainer exists, this set has to be created.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/GeneralizedBySet/1/0'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [capabilityGeneralizedBy]:
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
                    
                        
                        



                class ConstraintSet(SubmodelElementCollection):

                    

                    class PropertyConstraintContainer(SubmodelElementCollection):

                        class BasicConstraint(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'BasicConstraint',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Basic Constraint'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Property element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/BasicConstraint/1/0'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'PredicateRelationTemplate', value_type=str, value=r'ALL', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                                
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
                            
                                
                                



                        class CustomConstraint(SubmodelElementCollection):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                



                                                id_short: Optional[str]=r'CustomConstraint',
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Custom Constraint'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'SubmodelElement which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties. This can be freely defined for the purpose of constraining a property and is not specified in this Submodel Template.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/CustomConstraint/1/0'),), referred_semantic_id=None),
                                                
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
                            
                                
                                

                        class OperationConstraint(ReferenceElement):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: Reference,
                                                
                                                
                                                id_short: Optional[str]=r'OperationConstraint',
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Operation Constraint'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Reference to an (external) Operation element which can be used to validate the constraint for the considered Properties in this PropertyConstraintContainer against other properties.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintType/OperationConstraint/1/0'),), referred_semantic_id=None),
                                                
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
                                                
                                                display_name = display_name,
                                                
                                                category = category,
                                                
                                                description = description,
                                                
                                                semantic_id = semantic_id,
                                                
                                                qualifier = qualifier,
                                                
                                                extension = extension,
                                                
                                                supplemental_semantic_id = supplemental_semantic_id,
                                                
                                                embedded_data_specifications = embedded_data_specifications,
                                                
                                                
                                                
                                )
                            
                                
                                

                        class ConstraintType(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'ConstraintType',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Constraint Type'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Abstract Enum type of allowed SubmodelElements for these Properties constraints. Exactly one of the SubmodelElements below must be instanciated, e.g., similar to SubmodelElementList with exactly one element.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ConstraintType/1/0'),), referred_semantic_id=None),
                                                
                                                qualifier: Iterable[Qualifier]=None,
                                                
                                                extension: Iterable[Extension]=(),
                                                
                                                supplemental_semantic_id: Iterable[Reference]=(),
                                                
                                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                
                                                
                                                
                            ):
                                
                                if qualifier is None:
                                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'FormChoices', value_type=str, value=r'OperationConstraint;OCLConstraint;BasicConstraint;CustomConstraint', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                                
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
                            
                                
                                

                        class PropertyConditionalType(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'PropertyConditionalType',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Conditional Type'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Defines the type of the property conditions as defined in the ConceptDescription with the same name (PropertyConditionalType).'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyConditionalType/1/0'),), referred_semantic_id=None),
                                                
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
                            
                                
                                



                        class ConstraintPropertyRelations(SubmodelElementCollection):

                            class ConstraintHasProperty(RelationshipElement):

                                
                                    
                                    
                                def __init__(
                                        self,
                                        
                                                    
                                                    id_short: Optional[str]=r'ConstraintHasProperty',
                                                    
                                                    first: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityRelations'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'ConstraintSet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'PropertyConstraintContainer'), Key(type_=KeyTypes.PROPERTY, value=r'BasicConstraint')), type_=Property, referred_semantic_id=None),
                                                    
                                                    second: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'PropertySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'PropertyContainer'), Key(type_=KeyTypes.PROPERTY, value=r'PropertyProperty')), type_=Property, referred_semantic_id=None),
                                                    
                                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Constraint Has Property'}),
                                                    
                                                    category: Optional[str]=None,
                                                    
                                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relates the PropertyConstraint as first element to a Property from a PropertyContainer as second element.'}),
                                                    
                                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ConstraintHasProperty/1/0'),), referred_semantic_id=None),
                                                    
                                                    qualifier: Iterable[Qualifier]=None,
                                                    
                                                    extension: Iterable[Extension]=(),
                                                    
                                                    supplemental_semantic_id: Iterable[Reference]=(),
                                                    
                                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                                    
                                                    
                                                    
                                ):
                                    
                                    if qualifier is None:
                                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                                    
                                    if embedded_data_specifications is None:
                                        embedded_data_specifications = []
                                    
                                    
                                            
                                    super().__init__(
                                        
                                                    
                                                    id_short = id_short,
                                                    
                                                    first = first,
                                                    
                                                    second = second,
                                                    
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
                                    
                                                

                                        
                                    constraintHasProperty: Iterable[ConstraintHasProperty],
                                        


                                        


                                                id_short: Optional[str]=r'ConstraintPropertyRelations',
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Constraint Property Relations'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Contains all relationships for the constraint in the PropertyConstraintContainer.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ConstraintPropertyRelations/1/0'),), referred_semantic_id=None),
                                                
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
                                for se_arg in [constraintHasProperty]:
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
                                
                                            

                                    
                                basicConstraint: Union[str, BasicConstraint],
                                    

                                    
                                customConstraint: CustomConstraint,
                                    

                                    
                                operationConstraint: Union[Reference, OperationConstraint],
                                    

                                    
                                constraintType: Union[str, ConstraintType],
                                    

                                    
                                propertyConditionalType: Union[str, PropertyConditionalType],
                                    

                                    
                                constraintPropertyRelations: ConstraintPropertyRelations,
                                    


                                    

                                    

                                    

                                    

                                    

                                    


                                            id_short: Optional[str]=r'PropertyConstraintContainer',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Property Constraint Container'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If one or more constraints exist for a Capability Property, then for every constraint a PropertyConstraintContainer has to be created.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/PropertyConstraintContainer/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            

                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            




                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if basicConstraint and not isinstance(basicConstraint, SubmodelElement):
                                basicConstraint=self. BasicConstraint(basicConstraint)
                                

                                

                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if operationConstraint and not isinstance(operationConstraint, SubmodelElement):
                                operationConstraint=self. OperationConstraint(operationConstraint)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if constraintType and not isinstance(constraintType, SubmodelElement):
                                constraintType=self. ConstraintType(constraintType)
                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if propertyConditionalType and not isinstance(propertyConditionalType, SubmodelElement):
                                propertyConditionalType=self. PropertyConditionalType(propertyConditionalType)
                                

                                

                                


                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [basicConstraint,customConstraint,operationConstraint,constraintType,propertyConditionalType,constraintPropertyRelations]:
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
                        
                            
                            



                    class TransitionConstraintContainer(SubmodelElementCollection):

                        class TransitionConstrainedBy(RelationshipElement):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                
                                                id_short: Optional[str]=r'TransitionConstrainedBy',
                                                
                                                first: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                                
                                                second: Reference=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/CapabilityDescription/1/0/Submodel'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilitySet'), Key(type_=KeyTypes.SUBMODEL_ELEMENT_COLLECTION, value=r'CapabilityContainer'), Key(type_=KeyTypes.CAPABILITY, value=r'Capability')), type_=Capability, referred_semantic_id=None),
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Transition Constrained By'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Relates the constrained Capability as first element to a constraining Capability from another CapabilityContainer as second element.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/TransitionConstrainedBy/1/0'),), referred_semantic_id=None),
                                                
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
                                    
                                                
                                                id_short = id_short,
                                                
                                                first = first,
                                                
                                                second = second,
                                                
                                                display_name = display_name,
                                                
                                                category = category,
                                                
                                                description = description,
                                                
                                                semantic_id = semantic_id,
                                                
                                                qualifier = qualifier,
                                                
                                                extension = extension,
                                                
                                                supplemental_semantic_id = supplemental_semantic_id,
                                                
                                                embedded_data_specifications = embedded_data_specifications,
                                                
                                                
                                                
                                )
                            
                                
                                

                        class TransitionConditionalType(Property):

                            
                                
                                
                            def __init__(
                                    self,
                                    
                                                value: str,
                                                
                                                
                                                id_short: Optional[str]=r'TransitionConditionalType',
                                                
                                                value_type: DataTypeDefXsd=str,
                                                
                                                value_id: Optional[Reference]=None,
                                                
                                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Transition Conditional Type'}),
                                                
                                                category: Optional[str]=None,
                                                
                                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Defines the element TransitionConstrainedBy of TransitionConstraintType.'}),
                                                
                                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/TransitionConditionalType/1/0'),), referred_semantic_id=None),
                                                
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
                                
                                            

                                    
                                transitionConstrainedBy: TransitionConstrainedBy,
                                    

                                    
                                transitionConditionalType: Union[str, TransitionConditionalType],
                                    


                                    

                                    


                                            id_short: Optional[str]=r'TransitionConstraintContainer',
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Transition Constraint Container'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If one or more constraints exist for a Capability, then for every transitional constraint a TransitionConstraintContainer has to be created.'}),
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/TransitionConstraintContainer/1/0'),), referred_semantic_id=None),
                                            
                                            qualifier: Iterable[Qualifier]=None,
                                            
                                            extension: Iterable[Extension]=(),
                                            
                                            supplemental_semantic_id: Iterable[Reference]=(),
                                            
                                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                            
                                            

                                            
                        ):
                            
                            if qualifier is None:
                                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                            
                            if embedded_data_specifications is None:
                                embedded_data_specifications = []
                            
                            




                                

                                

                                

                                
                                    
                            # Build a submodel element if a raw value was passed in the argument
                            if transitionConditionalType and not isinstance(transitionConditionalType, SubmodelElement):
                                transitionConditionalType=self. TransitionConditionalType(transitionConditionalType)
                                


                            # Add all passed/initialized submodel elements to a single list
                            embedded_submodel_elements = []
                            for se_arg in [transitionConstrainedBy,transitionConditionalType]:
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
                            
                                        

                                

                                


                                
                            propertyConstraintContainer: Optional[Iterable[PropertyConstraintContainer]] = None,
                                

                                
                            transitionConstraintContainer: Optional[Iterable[TransitionConstraintContainer]] = None,
                                


                                        id_short: Optional[str]=r'ConstraintSet',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Constraint Set'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If constraint(s) for the Capability element in the CapabilityContainer exists, this set has to be created.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/ConstraintSet/1/0'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
                        if embedded_data_specifications is None:
                            embedded_data_specifications = []
                        
                        




                            

                            

                            

                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [propertyConstraintContainer,transitionConstraintContainer]:
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
                        
                                    

                            

                            

                            

                            


                            
                        capabilityRealizedBy: Optional[Iterable[CapabilityRealizedBy]] = None,
                            

                            
                        composedOfSet: Optional[ComposedOfSet] = None,
                            

                            
                        generalizedBySet: Optional[Iterable[GeneralizedBySet]] = None,
                            

                            
                        constraintSet: Optional[Iterable[ConstraintSet]] = None,
                            


                                    id_short: Optional[str]=r'CapabilityRelations',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Relations'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Collection of relationships for the capability, if existing.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityRelations/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        

                        

                        

                        

                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [capabilityRealizedBy,composedOfSet,generalizedBySet,constraintSet]:
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
                    
                                

                        
                    capability: Capability,
                        

                        

                        

                        


                        

                        
                    capabilityComment: Optional[Union[LangStringSet, CapabilityComment]] = None,
                        

                        
                    propertySet: Optional[Iterable[PropertySet]] = None,
                        

                        
                    capabilityRelations: Optional[CapabilityRelations] = None,
                        


                                id_short: Optional[str]=r'CapabilityContainer',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Container'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'A Container for one capability and all its additional descriptive elements.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilityContainer/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if capabilityComment and not isinstance(capabilityComment, SubmodelElement):
                    capabilityComment=self. CapabilityComment(capabilityComment)
                    

                    

                    

                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [capability,capabilityComment,propertySet,capabilityRelations]:
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
                
                            

                    
                capabilityContainer: Iterable[CapabilityContainer],
                    


                    


                            id_short: Optional[str]=r'CapabilitySet',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Capability Set'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'A Set of CapabilityContainer for a Use Case for the asset.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CapabilityDescription/CapabilitySet/1/0'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'EditIdShort', value_type=str, value=r'True', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()))
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [capabilityContainer]:
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
                        
                        

                
            capabilitySet: Iterable[CapabilitySet],
                


                


                        id_short: Optional[str]=r'CapabilityDescription',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Submodel Template Capability Description'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Definition of the Submodel CapabilityDescription identified by its semanticId. The Submodel idShort can be picked freely.'}),
                        
                        administration: Optional[AdministrativeInformation]=None,
                        
                        semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'https://admin-shell.io/idta/SubmodelTemplate/CapabilityDescription/1/0'),), type_=Submodel, referred_semantic_id=None),
                        
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
        for se_arg in [capabilitySet]:
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
    
        
        