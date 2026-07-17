
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class Circularity(Submodel):

    

    class DismantlingAndRemovalInformation(SubmodelElementList):

        class Dismantlingandremovalinformation_item(Property):

            
                
                
            def __init__(
                    self,
                    
                                value: str,
                                
                                
                                id_short: Optional[str]=r'dismantlingandremovalinformation_item',
                                
                                value_type: DataTypeDefXsd=str,
                                
                                value_id: Optional[Reference]=None,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                
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
            
                
                
            
            
        def __init__(
                self,
                
                            

                    
                dismantlingandremovalinformation_items: Iterable[Union[str, Dismantlingandremovalinformation_item]],
                    


                    


                            id_short: Optional[str]=r'DismantlingAndRemovalInformation',
                            
                            type_value_list_element: SubmodelElement=Property,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=str,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'dismantling and removal information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#dismantlingAndRemovalInformation'),), referred_semantic_id=None),
                            
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
            if dismantlingandremovalinformation_items and all([isinstance(i, str) for i in dismantlingandremovalinformation_items]):
                dismantlingandremovalinformation_items=[self. Dismantlingandremovalinformation_item(i) for i in dismantlingandremovalinformation_items]
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [dismantlingandremovalinformation_items]:
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

            



    class SparePartSources(SubmodelElementList):

        

        class Sparepartsources_item(SubmodelElementCollection):

            class NameOfSupplier(MultiLanguageProperty):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: LangStringSet,
                                    
                                    
                                    id_short: Optional[str]=r'NameOfSupplier',
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'name of supplier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#company'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAW001#001'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    



            class AddressOfSupplier(SubmodelElementCollection):

                class NationalCode(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'NationalCode',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Länderkürzel',r'en': r'national code'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#nationalCode'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO134#002'),), referred_semantic_id=None),),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class PostalCode(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'PostalCode',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'postal code'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#postalCode'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://schema.org/postalCode'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO129#002'),), referred_semantic_id=None)),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                    
                        
                        

                class Street(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'Street',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'street',r'de': r'Straße'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#street'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://schema.org/streetAddress'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO128#002'),), referred_semantic_id=None)),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                        
                                    

                            
                        nationalCode: Union[LangStringSet, NationalCode],
                            

                            
                        postalCode: Union[LangStringSet, PostalCode],
                            

                            
                        street: Union[LangStringSet, Street],
                            


                            

                            

                            


                                    id_short: Optional[str]=r'AddressOfSupplier',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'address of supplier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#addressOfSupplier'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://schema.org/PostalAddress'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if nationalCode and not isinstance(nationalCode, SubmodelElement):
                        nationalCode=self. NationalCode(nationalCode)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if postalCode and not isinstance(postalCode, SubmodelElement):
                        postalCode=self. PostalCode(postalCode)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if street and not isinstance(street, SubmodelElement):
                        street=self. Street(street)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [nationalCode,postalCode,street]:
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
                
                    
                    



            class EmailAddressOfSupplier(SubmodelElementCollection):

                class EmailAddress(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'EmailAddress',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'email address'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#emailAddress'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO198#002'),), referred_semantic_id=None),),
                                        
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
                    
                        
                        

                class PublicKey(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'PublicKey',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'public key'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Public part of an unsymmetrical key pair to sign or encrypt text or messages.'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#publicKey'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO200#002'),), referred_semantic_id=None),),
                                        
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
                    
                        
                        

                class TypeOfEmailAddress(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'TypeOfEmailAddress',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'type of email address'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#typeOfEmailAddress'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO199#003'),), referred_semantic_id=None),),
                                        
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
                    
                        
                        

                class TypeOfPublicKey(MultiLanguageProperty):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: LangStringSet,
                                        
                                        
                                        id_short: Optional[str]=r'TypeOfPublicKey',
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'type of public key'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#typeOfPublicKey'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAO201#002'),), referred_semantic_id=None),),
                                        
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
                        
                                    

                            
                        emailAddress: Union[str, EmailAddress],
                            

                            

                            

                            


                            

                            
                        publicKey: Optional[Union[LangStringSet, PublicKey]] = None,
                            

                            
                        typeOfEmailAddress: Optional[Union[str, TypeOfEmailAddress]] = None,
                            

                            
                        typeOfPublicKey: Optional[Union[LangStringSet, TypeOfPublicKey]] = None,
                            


                                    id_short: Optional[str]=r'EmailAddressOfSupplier',
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'email address of supplier',r'de': r'Email'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#email'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAQ836#005'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if emailAddress and not isinstance(emailAddress, SubmodelElement):
                        emailAddress=self. EmailAddress(emailAddress)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if publicKey and not isinstance(publicKey, SubmodelElement):
                        publicKey=self. PublicKey(publicKey)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if typeOfEmailAddress and not isinstance(typeOfEmailAddress, SubmodelElement):
                        typeOfEmailAddress=self. TypeOfEmailAddress(typeOfEmailAddress)
                        

                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if typeOfPublicKey and not isinstance(typeOfPublicKey, SubmodelElement):
                        typeOfPublicKey=self. TypeOfPublicKey(typeOfPublicKey)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [emailAddress,publicKey,typeOfEmailAddress,typeOfPublicKey]:
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
                
                    
                    

            class SupplierWebAddress(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'SupplierWebAddress',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'supplier web address'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.contact_information:1.0.0#addressOfAdditionalLink'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-AAQ326#002'),), referred_semantic_id=None),),
                                    
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
                
                    
                    



            class Components(SubmodelElementList):

                

                class Components_item(SubmodelElementCollection):

                    class PartName(Property):

                        
                            
                            
                        def __init__(
                                self,
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'PartName',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'part name'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=None,
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#partName'),), referred_semantic_id=None),
                                            
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
                                
                                            value: str,
                                            
                                            
                                            id_short: Optional[str]=r'PartNumber',
                                            
                                            value_type: DataTypeDefXsd=str,
                                            
                                            value_id: Optional[Reference]=None,
                                            
                                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'part number'}),
                                            
                                            category: Optional[str]=None,
                                            
                                            description: Optional[MultiLanguageTextType]=None,
                                            
                                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#partNumber'),), referred_semantic_id=None),
                                            
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
                            
                                        

                                
                            partName: Union[str, PartName],
                                

                                
                            partNumber: Union[str, PartNumber],
                                


                                

                                


                                        id_short: Optional[str]=r'components_item',
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Component'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Components available at supplier'}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#Component'),), referred_semantic_id=None),
                                        
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
                        if partName and not isinstance(partName, SubmodelElement):
                            partName=self. PartName(partName)
                            

                            

                            
                                
                        # Build a submodel element if a raw value was passed in the argument
                        if partNumber and not isinstance(partNumber, SubmodelElement):
                            partNumber=self. PartNumber(partNumber)
                            


                        # Add all passed/initialized submodel elements to a single list
                        embedded_submodel_elements = []
                        for se_arg in [partName,partNumber]:
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
                        
                                    

                            
                        components_items: Iterable[Components_item],
                            


                            


                                    id_short: Optional[str]=r'Components',
                                    
                                    type_value_list_element: SubmodelElement=SubmodelElementCollection,
                                    
                                    semantic_id_list_element: Optional[Reference]=None,
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=None,
                                    
                                    order_relevant: bool=False,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'components'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#components'),), referred_semantic_id=None),
                                    
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
                    for se_arg in [components_items]:
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
                    
                                

                        
                    nameOfSupplier: Union[LangStringSet, NameOfSupplier],
                        

                        
                    addressOfSupplier: AddressOfSupplier,
                        

                        
                    emailAddressOfSupplier: EmailAddressOfSupplier,
                        

                        
                    supplierWebAddress: Union[str, SupplierWebAddress],
                        

                        
                    components: Components,
                        


                        

                        

                        

                        

                        


                                id_short: Optional[str]=r'sparepartsources_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'spare part supplier'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#SparePartSupplier'),), referred_semantic_id=None),
                                
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
                if nameOfSupplier and not isinstance(nameOfSupplier, SubmodelElement):
                    nameOfSupplier=self. NameOfSupplier(nameOfSupplier)
                    

                    

                    

                    

                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if supplierWebAddress and not isinstance(supplierWebAddress, SubmodelElement):
                    supplierWebAddress=self. SupplierWebAddress(supplierWebAddress)
                    

                    

                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [nameOfSupplier,addressOfSupplier,emailAddressOfSupplier,supplierWebAddress,components]:
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
                
                            

                    


                    
                sparepartsources_items: Optional[Iterable[Sparepartsources_item]] = None,
                    


                            id_short: Optional[str]=r'SparePartSources',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'spare part sources'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#sparePartSources'),), referred_semantic_id=None),
                            
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
            for se_arg in [sparepartsources_items]:
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

            



    class RecycledContentInformation(SubmodelElementList):

        

        class Recycledcontentinformation_item(SubmodelElementCollection):

            class PreConsumerShare(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'PreConsumerShare',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'pre consumer share'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#preConsumerShare'),), referred_semantic_id=None),
                                    
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
                
                    
                    

            class RecycledMaterial(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'RecycledMaterial',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'recycled material'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#recycledMaterial'),), referred_semantic_id=None),
                                    
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
                
                    
                    

            class PostConsumerShare(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Float,
                                    
                                    
                                    id_short: Optional[str]=r'PostConsumerShare',
                                    
                                    value_type: DataTypeDefXsd=Float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'post consumer share'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#postConsumerShare'),), referred_semantic_id=None),
                                    
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
                    
                                

                        

                        
                    recycledMaterial: Union[str, RecycledMaterial],
                        

                        


                        
                    preConsumerShare: Optional[Union[Float, PreConsumerShare]] = None,
                        

                        

                        
                    postConsumerShare: Optional[Union[Float, PostConsumerShare]] = None,
                        


                                id_short: Optional[str]=r'recycledcontentinformation_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'recycled content'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#RecycledContent'),), referred_semantic_id=None),
                                
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
                if preConsumerShare and not isinstance(preConsumerShare, SubmodelElement):
                    preConsumerShare=self. PreConsumerShare(preConsumerShare)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if recycledMaterial and not isinstance(recycledMaterial, SubmodelElement):
                    recycledMaterial=self. RecycledMaterial(recycledMaterial)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if postConsumerShare and not isinstance(postConsumerShare, SubmodelElement):
                    postConsumerShare=self. PostConsumerShare(postConsumerShare)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [preConsumerShare,recycledMaterial,postConsumerShare]:
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
                
                            

                    
                recycledcontentinformation_items: Iterable[Recycledcontentinformation_item],
                    


                    


                            id_short: Optional[str]=r'RecycledContentInformation',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=None,
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=False,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'recycled content information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#recycledContent'),), referred_semantic_id=None),
                            
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
            for se_arg in [recycledcontentinformation_items]:
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

            



    class SafetyMeasures(SubmodelElementCollection):

        

        class SafetyInstructions(SubmodelElementList):

            class Safetyinstructions_item(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'safetyinstructions_item',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    safetyinstructions_items: Iterable[Union[str, Safetyinstructions_item]],
                        


                        


                                id_short: Optional[str]=r'SafetyInstructions',
                                
                                type_value_list_element: SubmodelElement=Property,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=str,
                                
                                order_relevant: bool=False,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'safety instructions'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#safetyInstructions'),), referred_semantic_id=None),
                                
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
                if safetyinstructions_items and all([isinstance(i, str) for i in safetyinstructions_items]):
                    safetyinstructions_items=[self. Safetyinstructions_item(i) for i in safetyinstructions_items]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [safetyinstructions_items]:
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

                



        class ExtinguishingAgents(SubmodelElementList):

            class Extinguishingagents_item(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'extinguishingagents_item',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'extinguishing agent'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#ExtinguishingAgent'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    extinguishingagents_items: Iterable[Union[str, Extinguishingagents_item]],
                        


                        


                                id_short: Optional[str]=r'ExtinguishingAgents',
                                
                                type_value_list_element: SubmodelElement=Property,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=str,
                                
                                order_relevant: bool=False,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'extinguishing agents'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#extinguishingAgents'),), referred_semantic_id=None),
                                
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
                if extinguishingagents_items and all([isinstance(i, str) for i in extinguishingagents_items]):
                    extinguishingagents_items=[self. Extinguishingagents_item(i) for i in extinguishingagents_items]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [extinguishingagents_items]:
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
                
                            

                    
                safetyInstructions: Union[Iterable[str], SafetyInstructions],
                    

                    
                extinguishingAgents: Union[Iterable[str], ExtinguishingAgents],
                    


                    

                    


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
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if safetyInstructions and not isinstance(safetyInstructions, SubmodelElement):
                safetyInstructions=self. SafetyInstructions(safetyInstructions)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if extinguishingAgents and not isinstance(extinguishingAgents, SubmodelElement):
                extinguishingAgents=self. ExtinguishingAgents(extinguishingAgents)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [safetyInstructions,extinguishingAgents]:
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

        

        class WastePrevention(SubmodelElementList):

            class Wasteprevention_item(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'wasteprevention_item',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    wasteprevention_items: Iterable[Union[str, Wasteprevention_item]],
                        


                        


                                id_short: Optional[str]=r'WastePrevention',
                                
                                type_value_list_element: SubmodelElement=Property,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=str,
                                
                                order_relevant: bool=False,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'waste prevention'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#wastePrevention'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-ABL855#001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if wasteprevention_items and all([isinstance(i, str) for i in wasteprevention_items]):
                    wasteprevention_items=[self. Wasteprevention_item(i) for i in wasteprevention_items]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [wasteprevention_items]:
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

                



        class SeparateCollection(SubmodelElementList):

            class Separatecollection_item(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'separatecollection_item',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    separatecollection_items: Iterable[Union[str, Separatecollection_item]],
                        


                        


                                id_short: Optional[str]=r'SeparateCollection',
                                
                                type_value_list_element: SubmodelElement=Property,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=str,
                                
                                order_relevant: bool=False,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'separate collection'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#separateCollection'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-ABL854#001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if separatecollection_items and all([isinstance(i, str) for i in separatecollection_items]):
                    separatecollection_items=[self. Separatecollection_item(i) for i in separatecollection_items]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [separatecollection_items]:
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

                



        class InformationOnCollection(SubmodelElementList):

            class Informationoncollection_item(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'informationoncollection_item',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                    
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
                
                    
                    
                
                
            def __init__(
                    self,
                    
                                

                        
                    informationoncollection_items: Iterable[Union[str, Informationoncollection_item]],
                        


                        


                                id_short: Optional[str]=r'InformationOnCollection',
                                
                                type_value_list_element: SubmodelElement=Property,
                                
                                semantic_id_list_element: Optional[Reference]=None,
                                
                                value_type_list_element: Optional[DataTypeDefXsd]=str,
                                
                                order_relevant: bool=False,
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'information on collection'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=None,
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.circularity:1.0.0#informationOnCollection'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:irdi:0173-1#02-ABL856#001'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a list of submodel elements if a raw values were passed in the argument
                if informationoncollection_items and all([isinstance(i, str) for i in informationoncollection_items]):
                    informationoncollection_items=[self. Informationoncollection_item(i) for i in informationoncollection_items]
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [informationoncollection_items]:
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
                
                            

                    
                wastePrevention: Union[Iterable[str], WastePrevention],
                    

                    
                separateCollection: Union[Iterable[str], SeparateCollection],
                    

                    
                informationOnCollection: Union[Iterable[str], InformationOnCollection],
                    


                    

                    

                    


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
            
            




                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if wastePrevention and not isinstance(wastePrevention, SubmodelElement):
                wastePrevention=self. WastePrevention(wastePrevention)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if separateCollection and not isinstance(separateCollection, SubmodelElement):
                separateCollection=self. SeparateCollection(separateCollection)
                

                

                
                    
            # Build a submodel element if a raw value was passed in the argument
            if informationOnCollection and not isinstance(informationOnCollection, SubmodelElement):
                informationOnCollection=self. InformationOnCollection(informationOnCollection)
                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [wastePrevention,separateCollection,informationOnCollection]:
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
                        
                        

                
            dismantlingAndRemovalInformation: Union[Iterable[str], DismantlingAndRemovalInformation],
                

                
            sparePartSources: SparePartSources,
                

                
            recycledContentInformation: RecycledContentInformation,
                

                
            safetyMeasures: SafetyMeasures,
                

                
            endOfLifeInformation: EndOfLifeInformation,
                

                
            renewableContent: Union[Float, RenewableContent],
                


                

                

                

                

                

                


                        id_short: Optional[str]=r'Circularity',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'Circularity'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Dismantling information (including at least: exploded diagrams of the battery system/pack showing the location of battery cells; disassembly sequences; type and number of fastening techniques to be unlocked; tools required for disassembly; warnings if risk of damaging parts exists; amount of cells used and layout); part numbers for components and contact details of sources for replacement spares; safety measures 
               
               (Annex XIII (2b-d)); usable extinguishing agent (Annex VI, Part A(9)). Bibliography includes the Digital Battery Passport Guideline.'}),
                        
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
        if dismantlingAndRemovalInformation and not isinstance(dismantlingAndRemovalInformation, SubmodelElement):
            dismantlingAndRemovalInformation=self. DismantlingAndRemovalInformation(dismantlingAndRemovalInformation)
            

            

            

            

            

            

            

            

            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if renewableContent and not isinstance(renewableContent, SubmodelElement):
            renewableContent=self. RenewableContent(renewableContent)
            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [dismantlingAndRemovalInformation,sparePartSources,recycledContentInformation,safetyMeasures,endOfLifeInformation,renewableContent]:
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
    
        
        