
from typing import *
import inspect
from basyx.aas.model import *
from basyx.aas.model.datatypes import *



class BatteryNameplate(Submodel):

    class URIOfTheProduct(Property):

        
            
            
        def __init__(
                self,
                
                            value: AnyURI,
                            
                            
                            id_short: Optional[str]=r'URIOfTheProduct',
                            
                            value_type: DataTypeDefXsd=AnyURI,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'URI of the product'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The battery passport identifier is the unique identifier of a battery passport. 

                DIN DKE Spec 99100 chapter reference: 6.1.2.1'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61987#ABN590#002'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABH173#003'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#uriOfTheProduct'),), referred_semantic_id=None)),
                            
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
        
            
            

    class ManufacturerName(MultiLanguageProperty):

        
            
            
        def __init__(
                self,
                
                            value: LangStringSet,
                            
                            
                            id_short: Optional[str]=r'ManufacturerName',
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'manufacturer name'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Information identifying the manufacturer with a name.


                DIN DKE Spec 99100 chapter reference: 6.1.2.4'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61987#ABA565#009'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAO677#004'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#manufacturerName'),), referred_semantic_id=None)),
                            
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
        
            
            



    class AddressInformation(SubmodelElementCollection):

        
            
            
        def __init__(
                self,
                
                            



                            id_short: Optional[str]=r'AddressInformation',
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'address information'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The manufacturer information postal address, indicating a single contact point. Web address, if available; and web address, if available. 


                DIN DKE Spec 99100 chapter reference: 6.1.2.3


                Note: This is drop-in of the ContactInformation Submodel'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/smt-dropin/smt-dropin-use/1/0'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61360_7#AAS002#001'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAQ837#008/0173-1#01-ADR448#008'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#addressInformation'),), referred_semantic_id=None)),
                            
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
        
            
            

    class SerialNumber(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'SerialNumber',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'serial number'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The battery identifier should be serialised, i.e., identifying each battery via a serial number.


                DIN DKE Spec 99100 chapter reference: 6.1.2.2'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61987#ABA951#009'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAM556#004'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#serialNumber'),), referred_semantic_id=None)),
                            
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
        
            
            

    class DateOfManufacture(Property):

        
            
            
        def __init__(
                self,
                
                            value: Date,
                            
                            
                            id_short: Optional[str]=r'DateOfManufacture',
                            
                            value_type: DataTypeDefXsd=Date,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'date of manufacture'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The manufacturing date should not only relate to the battery model, but to the battery item.
                The date code should comply with DINISO8601-1:2020-12 and ISO8601-2:2019.


                DIN DKE Spec 99100 chapter reference: 6.1.3.2'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0112/2///61987#ABB757#007'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAR972#004'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#dateOfManufacture'),), referred_semantic_id=None)),
                            
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
        
            
            

    class DateOfPuttingIntoService(Property):

        
            
            
        def __init__(
                self,
                
                            value: Date,
                            
                            
                            id_short: Optional[str]=r'DateOfPuttingIntoService',
                            
                            value_type: DataTypeDefXsd=Date,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'date of putting into service'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#dateOfPuttingIntoService'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.TEMPLATE_QUALIFIER, semantic_id=None, supplemental_semantic_id=()),)
            
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
        
            
            

    class UniqueFacilityIdentifier(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'UniqueFacilityIdentifier',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'unique facility identifier'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'The manufacturing place should be uniquely identifiable.


                DIN DKE Spec 99100 chapter reference: 6.1.3.1'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0#uniqueFacilityIdentifier'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-AAV646#003'),), referred_semantic_id=None)),
                            
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
        
            
            

    class LifeCycleStage(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'LifeCycleStage',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'life cycle stage'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': 'A battery passport must include information on the life cycle status of the battery.

                The status of the battery must be defined as \'original\' (0173-1#07-ACC020#001), \'repurposed\'(0173-1#07-ACC021#001), \'re-used\'(0173-1#07-ACC022#001), \'remanufactured\' (0173-1#07-ACC023#001) or \'waste\' (0173-1#07-ACC024#001).

                A new battery passport must be issued when a battery was subject to remanufacturing, repurpose or one of the treatment operations preparing for re-use and preparing for repurpose and is placed on the market again.


                DIN DKE Spec 99100 chapter reference: 6.1.3.7'}),
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'0173-1#02-ABL841#001'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#batteryStatus'),), referred_semantic_id=None),),
                            
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
        
            
            

    class OperatorIdentifier(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'OperatorIdentifier',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'operator identifier'}),
                            
                            category: Optional[str]=None,
                            
                            description: Optional[MultiLanguageTextType]=None,
                            
                            semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0#operatorIdentifier'),), referred_semantic_id=None),
                            
                            qualifier: Iterable[Qualifier]=None,
                            
                            extension: Iterable[Extension]=(),
                            
                            supplemental_semantic_id: Iterable[Reference]=(),
                            
                            embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                            
                            
                            
        ):
            
            if qualifier is None:
                qualifier = (Qualifier(type_=r'SMT/Cardinality', value_type=str, value=r'ZeroToOne', value_id=None, kind=QualifierKind.CONCEPT_QUALIFIER, semantic_id=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/SubmodelTemplates/Cardinality/1/0'),), referred_semantic_id=None), supplemental_semantic_id=()),)
            
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
        
            
            

    class ManufacturerIdentifier(Property):

        
            
            
        def __init__(
                self,
                
                            value: str,
                            
                            
                            id_short: Optional[str]=r'ManufacturerIdentifier',
                            
                            value_type: DataTypeDefXsd=str,
                            
                            value_id: Optional[Reference]=None,
                            
                            display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'manufacturer identifier'}),
                            
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
        
            
            
        
        
    def __init__(
            self,
            
                        id_: str,
                        
                        

                
            uRIOfTheProduct: Union[AnyURI, URIOfTheProduct],
                

                
            manufacturerName: Union[LangStringSet, ManufacturerName],
                

                
            addressInformation: AddressInformation,
                

                
            serialNumber: Union[str, SerialNumber],
                

                
            dateOfManufacture: Union[Date, DateOfManufacture],
                

                

                
            uniqueFacilityIdentifier: Union[str, UniqueFacilityIdentifier],
                

                
            lifeCycleStage: Union[str, LifeCycleStage],
                

                

                
            manufacturerIdentifier: Union[str, ManufacturerIdentifier],
                


                

                

                

                

                

                
            dateOfPuttingIntoService: Optional[Union[Date, DateOfPuttingIntoService]] = None,
                

                

                

                
            operatorIdentifier: Optional[Union[str, OperatorIdentifier]] = None,
                

                


                        id_short: Optional[str]=r'BatteryNameplate',
                        
                        display_name: Optional[MultiLanguageNameType]=MultiLanguageNameType(dict_={r'en': r'battery nameplate'}),
                        
                        category: Optional[str]=None,
                        
                        description: Optional[MultiLanguageTextType]=MultiLanguageTextType(dict_={r'en': r'Contains the static nameplate attributes attached to the battery.'}),
                        
                        administration: Optional[AdministrativeInformation]=AdministrativeInformation(version=r'1', revision=r'0', creator=None, template_id=r'https://admin-shell.io/idta-02035-1', embedded_data_specifications=[]),
                        
                        semantic_id: Optional[Reference]=ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/digitalbatterypassport/nameplate/1/0/Nameplate'),), referred_semantic_id=None),
                        
                        qualifier: Iterable[Qualifier]=None,
                        
                        kind: ModellingKind=ModellingKind.TEMPLATE,
                        
                        extension: Iterable[Extension]=(),
                        
                        supplemental_semantic_id: Iterable[Reference]=(ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.digital_nameplate:3.0.0'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'urn:samm:io.admin-shell.idta.batterypass.digital_nameplate:1.0.0'),), referred_semantic_id=None), ExternalReference(key=(Key(type_=KeyTypes.GLOBAL_REFERENCE, value=r'https://admin-shell.io/idta/nameplate/3/0/Nameplate'),), referred_semantic_id=None)),
                        
                        embedded_data_specifications: Iterable[EmbeddedDataSpecification]=None,
                        
                        

                        
    ):
        
        if qualifier is None:
            qualifier = ()
        
        if embedded_data_specifications is None:
            embedded_data_specifications = []
        
        




            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if uRIOfTheProduct and not isinstance(uRIOfTheProduct, SubmodelElement):
            uRIOfTheProduct=self. URIOfTheProduct(uRIOfTheProduct)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if manufacturerName and not isinstance(manufacturerName, SubmodelElement):
            manufacturerName=self. ManufacturerName(manufacturerName)
            

            

            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if serialNumber and not isinstance(serialNumber, SubmodelElement):
            serialNumber=self. SerialNumber(serialNumber)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if dateOfManufacture and not isinstance(dateOfManufacture, SubmodelElement):
            dateOfManufacture=self. DateOfManufacture(dateOfManufacture)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if dateOfPuttingIntoService and not isinstance(dateOfPuttingIntoService, SubmodelElement):
            dateOfPuttingIntoService=self. DateOfPuttingIntoService(dateOfPuttingIntoService)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if uniqueFacilityIdentifier and not isinstance(uniqueFacilityIdentifier, SubmodelElement):
            uniqueFacilityIdentifier=self. UniqueFacilityIdentifier(uniqueFacilityIdentifier)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if lifeCycleStage and not isinstance(lifeCycleStage, SubmodelElement):
            lifeCycleStage=self. LifeCycleStage(lifeCycleStage)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if operatorIdentifier and not isinstance(operatorIdentifier, SubmodelElement):
            operatorIdentifier=self. OperatorIdentifier(operatorIdentifier)
            

            

            
                
        # Build a submodel element if a raw value was passed in the argument
        if manufacturerIdentifier and not isinstance(manufacturerIdentifier, SubmodelElement):
            manufacturerIdentifier=self. ManufacturerIdentifier(manufacturerIdentifier)
            


        # Add all passed/initialized submodel elements to a single list
        embedded_submodel_elements = []
        for se_arg in [uRIOfTheProduct,manufacturerName,addressInformation,serialNumber,dateOfManufacture,dateOfPuttingIntoService,uniqueFacilityIdentifier,lifeCycleStage,operatorIdentifier,manufacturerIdentifier]:
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
    
        
        