
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
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer name',r'de': r'Herstellername'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO677#004'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAO677-004'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
                                
                                content_type: str=r'image/png',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Company logo',r'de': r'Firmenlogo'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABI776#002'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABI776-002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class ManufacturerProductDesignation(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'ManufacturerProductDesignation',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer product designation',r'de': r'Herstellerproduktbezeichnung'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAW338#003'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAW338-003'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class ManufacturerArticleNumber(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ManufacturerArticleNumber',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer article number',r'de': r'Herstellerartikelnummer'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO676#005'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAO676-005'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class ManufacturerOrderCode(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'ManufacturerOrderCode',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Manufacturer order code',r'de': r'Bestellcode des Herstellers'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO227#004'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAO227-004'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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

            

            class Productimages_item(SubmodelElementCollection):

                class ImageFile(File):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ImageFile',
                                        
                                        content_type: str=r'image/png',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product image',r'de': r'Bildname Sachaufnahme'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK291#002'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ImageNote(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'ImageNote',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Image note',r'de': r'Bildhinweis'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL423#001'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABL423-001'),), referred_semantic_id=None),),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                        
                                    

                            
                        imageFile: ImageFile,
                            

                            


                            

                            
                        imageNote: Optional[Union[LangStringSet, ImageNote]] = None,
                            


                                    id_short: Optional[str]=r'productimages_item',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product image',r'de': r'Produktbild'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001/0173-1#01-AHY911#001'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001~0/0173-1#01-AHY911#001'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABM220-001/0173-1-01-AHY911-001')), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = ()
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if imageNote and not isinstance(imageNote, SubmodelElement):
                        imageNote=self. ImageNote(imageNote)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [imageFile,imageNote]:
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
                    
                                

                        
                    productimages_items: Productimages_item,
                        


                        


                                id_short: Optional[str]=r'ProductImages',
                                
                                type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                
                                semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001/0173-1#01-AHY911#001'),), referred_semantic_id=None),
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=None,
                                
                                order_relevant: bool=True,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product images',r'de': r'Produktbilder'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM220#001'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABM220-001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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

                
            
            
        def __init__(
                self,
                
                            

                    
                manufacturerName: Union[str, ManufacturerName],
                    

                    

                    
                manufacturerProductDesignation: Union[LangStringSet, ManufacturerProductDesignation],
                    

                    
                manufacturerArticleNumber: Union[str, ManufacturerArticleNumber],
                    

                    
                manufacturerOrderCode: Union[str, ManufacturerOrderCode],
                    

                    


                    

                    
                companyLogo: Optional[CompanyLogo] = None,
                    

                    

                    

                    

                    
                productImages: Optional[ProductImages] = None,
                    


                            id_short: Optional[str]=r'GeneralInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'General information',r'de': r'Allgemeine Informationen'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK161#002/0173-1#01-AHX838#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/ 0173-1-02-ABK161-002/0173-1-01-AHX838-002'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
                manufacturerName=self. ManufacturerName(manufacturerName)
                

                

                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerProductDesignation and not isinstance(manufacturerProductDesignation, SubmodelElement):
                manufacturerProductDesignation=self. ManufacturerProductDesignation(manufacturerProductDesignation)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerArticleNumber and not isinstance(manufacturerArticleNumber, SubmodelElement):
                manufacturerArticleNumber=self. ManufacturerArticleNumber(manufacturerArticleNumber)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if manufacturerOrderCode and not isinstance(manufacturerOrderCode, SubmodelElement):
                manufacturerOrderCode=self. ManufacturerOrderCode(manufacturerOrderCode)
                

                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [manufacturerName,companyLogo,manufacturerProductDesignation,manufacturerArticleNumber,manufacturerOrderCode,productImages]:
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
        
            
            



    class ProductClassifications(SubmodelElementList):

        

        class Productclassifications_item(SubmodelElementCollection):

            class ClassificationSystem(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ClassificationSystem',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Classification system',r'de': r'Klassifikationssystem'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL424#001'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABL424-001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue/ECLASS', value_type=str, value=r'ECLASS', value_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#07-ABB367#003'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-07-ABB367-003')), referred_semantic_id=None), kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue/CDD', value_type=str, value=r'IEC CDD', value_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#07-ACB994#001'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-07-ACB994-001')), referred_semantic_id=None), kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue/UNSPSC', value_type=str, value=r'UNSPSC', value_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#07-ABB368#003'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-07-ABB368-003')), referred_semantic_id=None), kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()), Qualifier(type_=r'SMT/ExampleValue/CustomerSpecific', value_type=str, value=r'customer specific', value_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#07-ACB894#001'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-07-ACB894-001')), referred_semantic_id=None), kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/AllowedValue/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()))
                    
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
                
                    
                    

            class ClassificationSystemVersion(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ClassificationSystemVersion',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Classification system version',r'de': r'Version der Klassifikationssystem'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAR710#003'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-AAR710-003'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ClassificationSystemUrl(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ClassificationSystemUrl',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Classification system URL',r'de': r'URL des Klassifikationssystems'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/ProduktClassification/ClassificationSystemUrl/2/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ProductClassId(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ProductClassId',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product class ID',r'de': r'Produktklassen ID'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG776#003'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABG776-003'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ProductClassCodedName(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ProductClassCodedName',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product Class Coded Name',r'de': r'Produktklasse Coded Name'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK128#002'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK128-002'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ProductClassName(MultiLanguageProperty):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: LangStringSet,
                                    
                                    
                                    id_short: Optional[str]=r'ProductClassName',
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product class name',r'de': r'Produktklasse Name'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK273#002'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK273-002'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ReferenceToTechnicalPropertyArea(ReferenceElement):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Reference,
                                    
                                    
                                    id_short: Optional[str]=r'ReferenceToTechnicalPropertyArea',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Reference to technical property area',r'de': r'Referenz auf einen technsichen Merkmalsbereich'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABL358-002'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                    
                                

                        
                    classificationSystem: Union[str, ClassificationSystem],
                        

                        

                        

                        
                    productClassId: Union[str, ProductClassId],
                        

                        
                    productClassCodedName: Union[str, ProductClassCodedName],
                        

                        

                        


                        

                        
                    classificationSystemVersion: Optional[Union[str, ClassificationSystemVersion]] = None,
                        

                        
                    classificationSystemUrl: Optional[Union[str, ClassificationSystemUrl]] = None,
                        

                        

                        

                        
                    productClassName: Optional[Union[LangStringSet, ProductClassName]] = None,
                        

                        
                    referenceToTechnicalPropertyArea: Optional[Union[Reference, ReferenceToTechnicalPropertyArea]] = None,
                        


                                id_short: Optional[str]=r'productclassifications_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Produkt classification',r'de': r'Produktklassifikation'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK162#002/0173-1#01-AHX839#002'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK162#002~0/0173-1#01-AHX839#002'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK162-002/0173-1-01-AHX839-002')), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = ()
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if classificationSystem and not isinstance(classificationSystem, SubmodelElement):
                    classificationSystem=self. ClassificationSystem(classificationSystem)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if classificationSystemVersion and not isinstance(classificationSystemVersion, SubmodelElement):
                    classificationSystemVersion=self. ClassificationSystemVersion(classificationSystemVersion)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if classificationSystemUrl and not isinstance(classificationSystemUrl, SubmodelElement):
                    classificationSystemUrl=self. ClassificationSystemUrl(classificationSystemUrl)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if productClassId and not isinstance(productClassId, SubmodelElement):
                    productClassId=self. ProductClassId(productClassId)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if productClassCodedName and not isinstance(productClassCodedName, SubmodelElement):
                    productClassCodedName=self. ProductClassCodedName(productClassCodedName)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if productClassName and not isinstance(productClassName, SubmodelElement):
                    productClassName=self. ProductClassName(productClassName)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if referenceToTechnicalPropertyArea and not isinstance(referenceToTechnicalPropertyArea, SubmodelElement):
                    referenceToTechnicalPropertyArea=self. ReferenceToTechnicalPropertyArea(referenceToTechnicalPropertyArea)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [classificationSystem,classificationSystemVersion,classificationSystemUrl,productClassId,productClassCodedName,productClassName,referenceToTechnicalPropertyArea]:
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
                
                            

                    
                productclassifications_items: Productclassifications_item,
                    


                    


                            id_short: Optional[str]=r'ProductClassifications',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK162#002/0173-1#01-AHX839#002'),), referred_semantic_id=None),
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Product classifications',r'de': r'Produktklassifikationen'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK162#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK162-002'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [productclassifications_items]:
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

            



    class TechnicalPropertyAreas(SubmodelElementList):

        

        class Technicalpropertyareas_item(SubmodelElementCollection):

            

            class Section(SubmodelElementCollection):

                

                class Section(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'Section',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySMC(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySMC',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySML(SubmodelElementList):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySML',
                                        
                                        type_value_list_element: SubmodelElement=SubmodelElement,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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

                        

                class ArbitraryProperty(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryProperty',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryMLP(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryMLP',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryRange(Range):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        min: str,
                                        
                                        max: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryRange',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        
                    
                    
                def __init__(
                        self,
                        
                                    

                            

                            

                            

                            

                            

                            


                            
                        section: Optional[Iterable[Section]] = None,
                            

                            
                        arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                            

                            
                        arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                            

                            
                        arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                            

                            
                        arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                            

                            
                        arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                            


                                    id_short: Optional[str]=r'Section',
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: Using displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        

                        

                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                        arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                        arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                        arbitraryRange=[self. str](i) for i in arbitraryRange]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                    
                    



            class ArbitrarySMC(SubmodelElementCollection):

                

                class Section(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'Section',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySMC(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySMC',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySML(SubmodelElementList):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySML',
                                        
                                        type_value_list_element: SubmodelElement=SubmodelElement,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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

                        

                class ArbitraryProperty(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryProperty',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryMLP(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryMLP',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryRange(Range):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        min: str,
                                        
                                        max: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryRange',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        
                    
                    
                def __init__(
                        self,
                        
                                    

                            

                            

                            

                            

                            

                            


                            
                        section: Optional[Iterable[Section]] = None,
                            

                            
                        arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                            

                            
                        arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                            

                            
                        arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                            

                            
                        arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                            

                            
                        arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                            


                                    id_short: Optional[str]=r'ArbitrarySMC',
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        

                        

                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                        arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                        arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                        arbitraryRange=[self. str](i) for i in arbitraryRange]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                    
                    



            class ArbitrarySML(SubmodelElementList):

                
                    
                    
                def __init__(
                        self,
                        
                                    



                                    id_short: Optional[str]=r'ArbitrarySML',
                                    
                                    type_value_list_element: SubmodelElement=SubmodelElement,
                                    
                                    semantic_id_list_element: Optional[Reference]=None,
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=None,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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

                    

            class ArbitraryProperty(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryProperty',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ArbitraryMLP(MultiLanguageProperty):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: LangStringSet,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryMLP',
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ArbitraryRange(Range):

                
                    
                    
                def __init__(
                        self,
                        
                                    min: str,
                                    
                                    max: str,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryRange',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        

                        

                        

                        

                        

                        


                        
                    section: Optional[Iterable[Section]] = None,
                        

                        
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                        

                        
                    arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                        

                        
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                        

                        
                    arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                        

                        
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                        


                                id_short: Optional[str]=r'technicalpropertyareas_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Technical property area',r'de': r'Technischer Merkmalsbereich'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002~0/0173-1#01-AHX773#002'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABL358-002/0173-1-01-AHX773-002')), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = ()
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    

                    

                    

                    

                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                    arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                    arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                    arbitraryRange=[self. str](i) for i in arbitraryRange]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                            

                    
                technicalpropertyareas_items: Technicalpropertyareas_item,
                    


                    


                            id_short: Optional[str]=r'TechnicalPropertyAreas',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL358#002/0173-1#01-AHX773#002'),), referred_semantic_id=None),
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=True,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Technical property areas',r'de': r'Technsiche Merkmalsbereiche'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK163#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/ 0173-1-02-ABK163-002'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [technicalpropertyareas_items]:
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

            



    class FurtherInformation(SubmodelElementCollection):

        class TextStatement(MultiLanguageProperty):

            
                
                
            def __init__(
                    self,
                    
                                value: LangStringSet,
                                
                                
                                id_short: Optional[str]=r'TextStatement',
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Text statement',r'de': r'Anweisung im Text'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK134#002'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK134-002'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
            
                
                

        class ValidDate(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: Date,
                                
                                
                                id_short: Optional[str]=r'ValidDate',
                                
                                value_type: DataTypeDefXsd=Date,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Validity date',r'de': r'Verfallsdatum'}),
                                
                                category: Optional[str]=r'PARAMETER',
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL775#001'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1#02-ABL775#001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                
                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
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
                
                            

                    

                    
                validDate: Union[Date, ValidDate],
                    


                    
                textStatement: Optional[Iterable[Union[LangStringSet, TextStatement]]] = None,
                    

                    


                            id_short: Optional[str]=r'FurtherInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Further information',r'de': r'Weitere Informationen'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABK164#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABK164-002'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                
                    
            # Build a list of submodel elements if a raw values were passed in the argument
            if textStatement and all([isinstance(i, LangStringSet) for i in textStatement]):
                textStatement=[self. TextStatement(i) for i in textStatement]
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if validDate and not isinstance(validDate, SubmodelElement):
                validDate=self. ValidDate(validDate)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [textStatement,validDate]:
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
        
            
            



    class SpecificDescriptions(SubmodelElementList):

        

        class Specificdescriptions_item(SubmodelElementCollection):

            

            class Section(SubmodelElementCollection):

                

                class Section(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'Section',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySMC(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySMC',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySML(SubmodelElementList):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySML',
                                        
                                        type_value_list_element: SubmodelElement=SubmodelElement,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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

                        

                class ArbitraryProperty(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryProperty',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryMLP(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryMLP',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryRange(Range):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        min: str,
                                        
                                        max: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryRange',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        
                    
                    
                def __init__(
                        self,
                        
                                    

                            

                            

                            

                            

                            

                            


                            
                        section: Optional[Iterable[Section]] = None,
                            

                            
                        arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                            

                            
                        arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                            

                            
                        arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                            

                            
                        arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                            

                            
                        arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                            


                                    id_short: Optional[str]=r'Section',
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: Using displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        

                        

                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                        arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                        arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                        arbitraryRange=[self. str](i) for i in arbitraryRange]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                    
                    



            class ArbitrarySMC(SubmodelElementCollection):

                

                class Section(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'Section',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySMC(SubmodelElementCollection):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySMC',
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        



                class ArbitrarySML(SubmodelElementList):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        



                                        id_short: Optional[str]=r'ArbitrarySML',
                                        
                                        type_value_list_element: SubmodelElement=SubmodelElement,
                                        
                                        semantic_id_list_element: Optional[Reference]=None,
                                        
                                        value_type_list_element: Optional[DataTypeDefXsd]=None,
                                        
                                        order_relevant: bool=True,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        

                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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

                        

                class ArbitraryProperty(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryProperty',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryMLP(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryMLP',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class ArbitraryRange(Range):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        min: str,
                                        
                                        max: str,
                                        
                                        
                                        id_short: Optional[str]=r'ArbitraryRange',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        display_name: Optional[MultiLanguageNameType]=None,
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        
                    
                    
                def __init__(
                        self,
                        
                                    

                            

                            

                            

                            

                            

                            


                            
                        section: Optional[Iterable[Section]] = None,
                            

                            
                        arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                            

                            
                        arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                            

                            
                        arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                            

                            
                        arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                            

                            
                        arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                            


                                    id_short: Optional[str]=r'ArbitrarySMC',
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        

                        

                        

                        

                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                        arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                        arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                        

                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                        arbitraryRange=[self. str](i) for i in arbitraryRange]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                    
                    



            class ArbitrarySML(SubmodelElementList):

                
                    
                    
                def __init__(
                        self,
                        
                                    



                                    id_short: Optional[str]=r'ArbitrarySML',
                                    
                                    type_value_list_element: SubmodelElement=SubmodelElement,
                                    
                                    semantic_id_list_element: Optional[Reference]=None,
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=None,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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

                    

            class ArbitraryProperty(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryProperty',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ArbitraryMLP(MultiLanguageProperty):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: LangStringSet,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryMLP',
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ArbitraryRange(Range):

                
                    
                    
                def __init__(
                        self,
                        
                                    min: str,
                                    
                                    max: str,
                                    
                                    
                                    id_short: Optional[str]=r'ArbitraryRange',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    display_name: Optional[MultiLanguageNameType]=None,
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Note: The use of a displayName is recommended.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SMT/General/Arbitrary'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        

                        

                        

                        

                        

                        


                        
                    section: Optional[Iterable[Section]] = None,
                        

                        
                    arbitrarySMC: Optional[Iterable[ArbitrarySMC]] = None,
                        

                        
                    arbitrarySML: Optional[Iterable[ArbitrarySML]] = None,
                        

                        
                    arbitraryProperty: Optional[Iterable[Union[str, ArbitraryProperty]]] = None,
                        

                        
                    arbitraryMLP: Optional[Iterable[Union[LangStringSet, ArbitraryMLP]]] = None,
                        

                        
                    arbitraryRange: Optional[Iterable[Union[Tuple[str, str], ArbitraryRange]]] = None,
                        


                                id_short: Optional[str]=r'specificdescriptions_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Specific description',r'de': r'Spezifische Beschreibung'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM221#001/0173-1#01-AHY912#001'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM221#001~0/0173-1#01-AHY912#001'), Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABM221-001/0173-1-01-AHY912-001')), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'Naming', value_type=str, value=r'Name of SMC is use case or application', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Naming/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    

                    

                    

                    

                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryProperty and all([isinstance(i, str) for i in arbitraryProperty]):
                    arbitraryProperty=[self. ArbitraryProperty(i) for i in arbitraryProperty]
                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryMLP and all([isinstance(i, LangStringSet) for i in arbitraryMLP]):
                    arbitraryMLP=[self. ArbitraryMLP(i) for i in arbitraryMLP]
                    

                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if arbitraryRange and all([isinstance(i, Tuple[str) for i in arbitraryRange]):
                    arbitraryRange=[self. str](i) for i in arbitraryRange]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [section,arbitrarySMC,arbitrarySML,arbitraryProperty,arbitraryMLP,arbitraryRange]:
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
                
                            

                    
                specificdescriptions_items: Specificdescriptions_item,
                    


                    


                            id_short: Optional[str]=r'SpecificDescriptions',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM221#001/0173-1#01-AHY912#001'),), referred_semantic_id=None),
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=True,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Specific description',r'de': r'Spezifische Beschreibung'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABM221#001'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-02-ABM221-001'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/SMT/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [specificdescriptions_items]:
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
                        
                        

                
            generalInformation: GeneralInformation,
                

                

                

                

                


                

                
            productClassifications: Optional[ProductClassifications] = None,
                

                
            technicalPropertyAreas: Optional[TechnicalPropertyAreas] = None,
                

                
            furtherInformation: Optional[FurtherInformation] = None,
                

                
            specificDescriptions: Optional[SpecificDescriptions] = None,
                


                        id_short: Optional[str]=r'TechnicalData',
                        
                        display_name: Optional[MultiLanguageNameType]=None,
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Submodel containing technical data of the asset and associated product classificatons',r'de': r'Teilmodell, das die technischen Daten des Assets und die zugehörigen Produktklassifizierungen enthält'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'2', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02003-2-0', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ModelReference(key=(Key(type_=KeyTypes.SUBMODEL, value=r'0173-1#01-AHX837#002'),), type_=Submodel, referred_semantic_id=None),
                        
                        qualifier: Iterable[Qualifier]=None,
                        
                        kind: ModellingKind=ModellingKind.TEMPLATE,
                        
                        extension: Iterable[Extension]=(),
                        
                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://api.eclass-cdp.com/0173-1-01-AHX837-002'),), referred_semantic_id=None),),
                        
                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                        
                        

                        
    ):
        
        if qualifier is None:
            qualifier = ()
        
        if embedded_data_specifications is None:
            embedded_data_specifications = []
        
        




            

            

            

            

            

            

            

            

            

            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [generalInformation,productClassifications,technicalPropertyAreas,furtherInformation,specificDescriptions]:
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
    
        
        