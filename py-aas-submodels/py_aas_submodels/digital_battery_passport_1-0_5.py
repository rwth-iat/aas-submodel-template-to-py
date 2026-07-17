
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class CarbonFootprint(Submodel):

    

    class ProductCarbonFootprints(SubmodelElementList):

        

        class Productcarbonfootprints_item(SubmodelElementCollection):

            

            class PcfCalculationMethods(SubmodelElementList):

                class Pcfcalculationmethods_item(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'pcfcalculationmethods_item',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Folgenabschätzungsmethode / Berechnungsmethode',r'en': r'PCF calculation method'}),
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG854#003'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                        
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
                        
                                    

                            
                        pcfcalculationmethods_items: Union[str, Pcfcalculationmethods_item],
                            


                            


                                    id_short: Optional[str]=r'PcfCalculationMethods',
                                    
                                    type_value_list_element: SubmodelElement=Property,
                                    
                                    semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG854#003'),), referred_semantic_id=None),
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=str,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Folgenabschätzungsmethoden',r'en': r'PCF calculation methods'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'de': r'Normen, Standards, Verfahren zur Ermittlung der Treibhausgas-Emissionen eines Produkts',r'en': r'Standards, methods for determining the greenhouse gas emissions of a product.

                        This Value List is based on ECLASS 15 with IRDI 0173-1#09-AAO115#003. The full list can be found in Section 2.5 in "Product Carbon Footprint 1.0 (IDTA-02023)".
                        '}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/PcfCalculationMethods/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#pcfCalculationMethods'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if pcfcalculationmethods_items and not isinstance(pcfcalculationmethods_items, SubmodelElement):
                        pcfcalculationmethods_items=self. Pcfcalculationmethods_item(pcfcalculationmethods_items)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [pcfcalculationmethods_items]:
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

                    

            class PcfCO2eq(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: Decimal,
                                    
                                    
                                    id_short: Optional[str]=r'PcfCO2eq',
                                    
                                    value_type: DataTypeDefXsd=Decimal,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'CO2-Äquivalent',r'en': r'PCF co 2 eq'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'DIN DKE Spec 99100 chapter reference: 6.3.2'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG855#003'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#pcfCo2eq'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class ReferenceImpactUnitForCalculation(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'ReferenceImpactUnitForCalculation',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Referenzeinheit für die Berechnung',r'en': r'reference impact unit for calculation'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': 'If a normalized product carbon footprint (PCF) value is provided, the reference value for calculation should be a specific unit such as \'kWh\'. 
                        If the total PCF value is provided the reference value for calculation should be \'piece\'.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG856#003'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#referenceImpactUnitForCalculation'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                    
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
                
                    
                    

            class QuantityOfMeasureForCalculation(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: float,
                                    
                                    
                                    id_short: Optional[str]=r'QuantityOfMeasureForCalculation',
                                    
                                    value_type: DataTypeDefXsd=float,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Mengenangabe für die Berechnung',r'en': r'quantity of measure for calculation'}),
                                    
                                    category: Optional[str]=r'PARAMETER',
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'If a normalized product carbon footprint (PCF) value is provided, the quantity of measure for calculation should be 1.
                        If the total PCF value is provided the quantity of measure for calculation should be 1.'}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG857#003'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#quantityOfMeasureForCalculation'),), referred_semantic_id=None),),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                    
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
                
                    
                    



            class LifeCyclePhases(SubmodelElementList):

                class Lifecyclephases_item(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'lifecyclephases_item',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Lebenszyklusphase',r'en': r'life cycle phase'}),
                                        
                                        category: Optional[str]=r'PARAMETER',
                                        
                                        description: Optional[MultiLanguageTextType]=None,
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG858#004'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                        
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
                        
                                    

                            
                        lifecyclephases_items: Union[str, Lifecyclephases_item],
                            


                            


                                    id_short: Optional[str]=r'LifeCyclePhases',
                                    
                                    type_value_list_element: SubmodelElement=Property,
                                    
                                    semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG858#004'),), referred_semantic_id=None),
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=str,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Lebenszyklusphasen',r'en': r'life cycle phases'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'List of life cycle stages of the product according to the quantification requirements of the standard to which the PCF carbon footprint statement refers.

                        The string value in the value list is based on DIN DKE SPEC 99100: "A1 - raw material supply (and upstream production)" (6.3.5 required lify cycle mapping), "A3 - production" (6.3.4 Contribution of main product production/manufacturing lifecycle stage), "A4 - transport to final destination" (6.3.5 Contribution of distribution lifecycle stage), "C3 - recycling, waste treatment" (6.3.6 Contribution of end of life and recycling lifecycle stage)

                        Please note that the model should always contain at least one Product Carbon Footprint entry that reflects the total PCF value (including all life cycle phases) of the battery.
                        '}),
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/LifeCyclePhases/1/0'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.carbon_footprint:1.0.0#lifeCyclePhases'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABG858#003'),), referred_semantic_id=None)),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        
                            
                    # Build a submodel element if a raw value was passed in the argument
                    if lifecyclephases_items and not isinstance(lifecyclephases_items, SubmodelElement):
                        lifecyclephases_items=self. Lifecyclephases_item(lifecyclephases_items)
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [lifecyclephases_items]:
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

                    

            class PerformanceClass(Property):

                
                    
                    
                def __init__(
                        self,
                        
                                    value: str,
                                    
                                    
                                    id_short: Optional[str]=r'PerformanceClass',
                                    
                                    value_type: DataTypeDefXsd=str,
                                    
                                    value_id: Optional[Reference]=None,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'performance class'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#performanceClass'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    
                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
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
                
                    
                    



            class WebLinkToPublicCarbonFootprintStudy(SubmodelElementList):

                class Weblinktopubliccarbonfootprintstudy_item(Property):

                    
                        
                        
                    def __init__(
                            self,
                            
                                        value: str,
                                        
                                        
                                        id_short: Optional[str]=r'weblinktopubliccarbonfootprintstudy_item',
                                        
                                        value_type: DataTypeDefXsd=str,
                                        
                                        value_id: Optional[Reference]=None,
                                        
                                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'document identifier'}),
                                        
                                        category: Optional[str]=None,
                                        
                                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Document identifier of the document (e.g., PDF) that can be found in the HandoverDocumentation Submodel.

                            DIN DKE Spec 99100 chapter reference: 6.3.8 '}),
                                        
                                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.handover_documentation:2.0.0#DocumentIdentifier'),), referred_semantic_id=None),
                                        
                                        qualifier: Iterable[Qualifier]=None,
                                        
                                        extension: Iterable[Extension]=(),
                                        
                                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO099#004'),), referred_semantic_id=None),),
                                        
                                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                        
                                        
                                        
                    ):
                        
                        if qualifier is None:
                            qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'OneToMany', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                        
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
                        
                                    

                            
                        weblinktopubliccarbonfootprintstudy_items: Iterable[Union[str, Weblinktopubliccarbonfootprintstudy_item]],
                            


                            


                                    id_short: Optional[str]=r'WebLinkToPublicCarbonFootprintStudy',
                                    
                                    type_value_list_element: SubmodelElement=Property,
                                    
                                    semantic_id_list_element: Optional[Reference]=None,
                                    
                                    value_type_list_element: Optional[DataTypeDefXsd]=str,
                                    
                                    order_relevant: bool=True,
                                    
                                    display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'web link to public carbon footprint study'}),
                                    
                                    category: Optional[str]=None,
                                    
                                    description: Optional[MultiLanguageTextType]=None,
                                    
                                    semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#webLinkToPublicCarbonFootprintStudy'),), referred_semantic_id=None),
                                    
                                    qualifier: Iterable[Qualifier]=None,
                                    
                                    extension: Iterable[Extension]=(),
                                    
                                    supplemental_semantic_id: Iterable[Reference]=(),
                                    
                                    embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                    
                                    

                                    
                ):
                    
                    if qualifier is None:
                        qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
                    
                    if embedded_data_specifications is None:
                        embedded_data_specifications = []
                    
                    




                        

                        
                            
                    # Build a list of submodel elements if a raw values were passed in the argument
                    if weblinktopubliccarbonfootprintstudy_items and all([isinstance(i, str) for i in weblinktopubliccarbonfootprintstudy_items]):
                        weblinktopubliccarbonfootprintstudy_items=[self. Weblinktopubliccarbonfootprintstudy_item(i) for i in weblinktopubliccarbonfootprintstudy_items]
                        


                    # Add all passed/initialized submodel elements to a single list
                    embedded_submodel_elements = []
                    for se_arg in [weblinktopubliccarbonfootprintstudy_items]:
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
                    
                                

                        
                    pcfCalculationMethods: Union[Iterable[str], PcfCalculationMethods],
                        

                        
                    pcfCO2eq: Union[Decimal, PcfCO2eq],
                        

                        
                    referenceImpactUnitForCalculation: Union[str, ReferenceImpactUnitForCalculation],
                        

                        
                    quantityOfMeasureForCalculation: Union[float, QuantityOfMeasureForCalculation],
                        

                        
                    lifeCyclePhases: Union[Iterable[str], LifeCyclePhases],
                        

                        
                    performanceClass: Union[str, PerformanceClass],
                        

                        
                    webLinkToPublicCarbonFootprintStudy: Union[Iterable[str], WebLinkToPublicCarbonFootprintStudy],
                        


                        

                        

                        

                        

                        

                        

                        


                                id_short: Optional[str]=r'productcarbonfootprints_item',
                                
                                display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Produkt CO2-Fußabdruck',r'en': r'product carbon footprint'}),
                                
                                category: Optional[str]=None,
                                
                                description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use.'}),
                                
                                semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0'),), referred_semantic_id=None),
                                
                                qualifier: Iterable[Qualifier]=None,
                                
                                extension: Iterable[Extension]=(),
                                
                                supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#ProductCarbonFootprint'),), referred_semantic_id=None),),
                                
                                embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                                
                                

                                
            ):
                
                if qualifier is None:
                    qualifier = ()
                
                if embedded_data_specifications is None:
                    embedded_data_specifications = []
                
                




                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if pcfCalculationMethods and not isinstance(pcfCalculationMethods, SubmodelElement):
                    pcfCalculationMethods=self. PcfCalculationMethods(pcfCalculationMethods)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if pcfCO2eq and not isinstance(pcfCO2eq, SubmodelElement):
                    pcfCO2eq=self. PcfCO2eq(pcfCO2eq)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if referenceImpactUnitForCalculation and not isinstance(referenceImpactUnitForCalculation, SubmodelElement):
                    referenceImpactUnitForCalculation=self. ReferenceImpactUnitForCalculation(referenceImpactUnitForCalculation)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if quantityOfMeasureForCalculation and not isinstance(quantityOfMeasureForCalculation, SubmodelElement):
                    quantityOfMeasureForCalculation=self. QuantityOfMeasureForCalculation(quantityOfMeasureForCalculation)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if lifeCyclePhases and not isinstance(lifeCyclePhases, SubmodelElement):
                    lifeCyclePhases=self. LifeCyclePhases(lifeCyclePhases)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if performanceClass and not isinstance(performanceClass, SubmodelElement):
                    performanceClass=self. PerformanceClass(performanceClass)
                    

                    

                    
                        
                # Build a submodel element if a raw value was passed in the argument
                if webLinkToPublicCarbonFootprintStudy and not isinstance(webLinkToPublicCarbonFootprintStudy, SubmodelElement):
                    webLinkToPublicCarbonFootprintStudy=self. WebLinkToPublicCarbonFootprintStudy(webLinkToPublicCarbonFootprintStudy)
                    


                # Add all passed/initialized submodel elements to a single list
                embedded_submodel_elements = []
                for se_arg in [pcfCalculationMethods,pcfCO2eq,referenceImpactUnitForCalculation,quantityOfMeasureForCalculation,lifeCyclePhases,performanceClass,webLinkToPublicCarbonFootprintStudy]:
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
                
                            

                    
                productcarbonfootprints_items: Productcarbonfootprints_item,
                    


                    


                            id_short: Optional[str]=r'ProductCarbonFootprints',
                            
                            type_value_list_element: SubmodelElement=SubmodelElementCollection,
                            
                            semantic_id_list_element: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprint/1/0'),), referred_semantic_id=None),
                            
                            value_type_list_element: Optional[DataTypeDefXsd]=None,
                            
                            order_relevant: bool=True,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'Produkt CO2-Fußabdruck',r'en': r'product carbon footprints'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Balance of greenhouse gas emissions along the entire life cycle of a product in a defined application and in relation to a defined unit of use.'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/ProductCarbonFootprints/1/0'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#CarbonFootprintBattery'),), referred_semantic_id=None),),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            

                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'One', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
            
            if embedded_data_specifications is None:
                embedded_data_specifications = []
            
            




                

                


            # Add all passed/initialized submodel elements to a single list
            embedded_submodel_elements = []
            for se_arg in [productcarbonfootprints_items]:
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
                        
                        

                
            productCarbonFootprints: ProductCarbonFootprints,
                


                


                        id_short: Optional[str]=r'CarbonFootprint',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'de': r'C02 Footprint',r'en': r'carbon footprint'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The Submodel provides the means to access the Carbon Footprint of the asset.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02023-1-0', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/CarbonFootprint/CarbonFootprint/1/0'),), referred_semantic_id=None),
                        
                        qualifier: Iterable[Qualifier]=None,
                        
                        kind: ModellingKind=ModellingKind.TEMPLATE,
                        
                        extension: Iterable[Extension]=(),
                        
                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.carbon_footprint:1.0.0#CarbonFootprintBattery'),), referred_semantic_id=None),),
                        
                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                        
                        

                        
    ):
        
        if qualifier is None:
            qualifier = ()
        
        if embedded_data_specifications is None:
            embedded_data_specifications = []
        
        




            

            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [productCarbonFootprints]:
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
    
        
        