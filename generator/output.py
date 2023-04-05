
from typing import *
import inspect
from basyx.aas.model import *


class Nameplate(Submodel):

    class ManufacturerName(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ManufacturerName',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO677#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ManufacturerProductDesignation(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ManufacturerProductDesignation',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAW338#001', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ContactInformation(SubmodelElementCollectionUnordered):

        
        def __init__(
                self,
                
                                
                id_short: str='ContactInformation',
                value: Any=(MultiLanguageProperty(id_short='NationalCode', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO134#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), Property(id_short='TimeZone', value_type=str, value='Z', value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/TimeZone', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='CityTown', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO132#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='Company', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAW001#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='Department', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO127#003', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='Phone', value=(MultiLanguageProperty(id_short='TelephoneNumber', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO136#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='AvailableTime', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/AvailableTime/', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation/Phone', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='Fax', value=(MultiLanguageProperty(id_short='FaxNumber', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO195#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAQ834#005', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='Email', value=(MultiLanguageProperty(id_short='PublicKey', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO200#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='TypeOfPublicKey', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO201#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAQ836#005', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='Street', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO128#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='Zipcode', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO129#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='POBox', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO130#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='ZipCodeOfPOBox', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO131#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='StateCounty', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO133#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='NameOfContact', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO205#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='FirstName', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO206#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='MiddleNames', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO207#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='Title', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO208#003', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='AcademicTitle', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO209#003', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='FurtherDetailsOfContact', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO210#002', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)),
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation', id_type=KeyType.IRI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ManufacturerProductRoot(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ManufacturerProductRoot',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAU732#001', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ManufacturerProductFamily(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ManufacturerProductFamily',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAU731#001', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ManufacturerProductType(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ManufacturerProductType',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO057#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class OrderCodeOfManufacturer(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='OrderCodeOfManufacturer',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO227#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class ProductArticleNumberOfManufacturer(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='ProductArticleNumberOfManufacturer',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAO676#003', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class DateOfManufacture(Property):

        
        def __init__(
                self,
                
                                
                id_short: str='DateOfManufacture',
                value_type: Any=Date,
                value: Any=Date(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAR972#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value_type = value_type,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class HardwareVersion(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='HardwareVersion',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAN270#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class FirmwareVersion(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='FirmwareVersion',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM985#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class SoftwareVersion(MultiLanguageProperty):

        
        def __init__(
                self,
                
                                
                id_short: str='SoftwareVersion',
                value: Any=dict(),
                value_id: Any=None,
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM737#002', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        value_id = value_id,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class Markings(SubmodelElementCollectionUnordered):

        
        def __init__(
                self,
                
                                
                id_short: str='Markings',
                value: Any=(SubmodelElementCollectionUnordered(id_short='Marking', value=(SubmodelElementCollectionUnordered(id_short='ExplosionSafeties', value=(SubmodelElementCollectionUnordered(id_short='ExplosionSafety', value=(MultiLanguageProperty(id_short='TypeOfApproval', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM812#003', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), MultiLanguageProperty(id_short='ApprovalAgencyTestingAgency', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM632#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), ReferenceElement(id_short='InstructionsControlDrawing', value=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0112/2///61987#ABO102#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), Property(id_short='SpecificConditionsForUse', value_type=str, value='X', value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/SpecificConditionsForUse', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), Property(id_short='IncompleteDevice', value_type=str, value='U', value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/IncompleteDevice', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='AmbientConditions', value=(MultiLanguageProperty(id_short='EquipmentProtectionLevel', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM668#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/AmbientConditions', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='ProcessConditions', value=(MultiLanguageProperty(id_short='EquipmentProtectionLevel', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM668#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ProcessConditions', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='ExternalElectricalCircuit', value=(MultiLanguageProperty(id_short='EquipmentProtectionLevel', value=dict(), value_id=None, category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAM668#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='SafetyRelatedPropertiesForPassiveBehaviour', value=(), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAQ380#006', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE), SubmodelElementCollectionUnordered(id_short='SafetyRelatedPropertiesForActiveBehaviour', value=(), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#02-AAQ381#006', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety/ExternalElectricalCircuit', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties/ExplosionSafety', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate/Markings/Marking/ExplosionSafeties', id_type=KeyType.IRI))), qualifier=set(), kind=ModelingKind.TEMPLATE)), category=None, description=dict(), semantic_id=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#01-AHD206#001', id_type=KeyType.IRDI))), qualifier=set(), kind=ModelingKind.TEMPLATE)),
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#01-AGZ673#001', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            

    class AssetSpecificProperties(SubmodelElementCollectionUnordered):

        
        def __init__(
                self,
                
                                
                id_short: str='AssetSpecificProperties',
                value: Any=(),
                category: Any=None,
                description: Any=dict(),
                semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='0173-1#01-AGZ672#001', id_type=KeyType.IRDI))),
                qualifier: Any=set(),
                kind: Any=ModelingKind.TEMPLATE,
                                
                            
        ):
            
                    
            super().__init__(
                
                                
                                        id_short = id_short,
                                        value = value,
                                        category = category,
                                        description = description,
                                        semantic_id = semantic_id,
                                        qualifier = qualifier,
                                        kind = kind,
                                
                            
            )
        
                
            
    def __init__(
            self,
            
            manufacturerName: ManufacturerName,
            manufacturerProductDesignation: ManufacturerProductDesignation,
            contactInformation: ContactInformation,
            manufacturerProductRoot: ManufacturerProductRoot,
            manufacturerProductFamily: ManufacturerProductFamily,
            manufacturerProductType: ManufacturerProductType,
            orderCodeOfManufacturer: OrderCodeOfManufacturer,
            productArticleNumberOfManufacturer: ProductArticleNumberOfManufacturer,
            dateOfManufacture: DateOfManufacture,
            hardwareVersion: HardwareVersion,
            firmwareVersion: FirmwareVersion,
            softwareVersion: SoftwareVersion,
            markings: Markings,
            assetSpecificProperties: AssetSpecificProperties,
                            
            identification: Any=Identifier(id_='www.example.com/ids/sm/1225_9020_5022_1974', id_type=IdentifierType.IRI),
            id_short: Any='Nameplate',
            category: Any=None,
            description: Any=dict(),
            administration: Any=None,
            semantic_id: Any=Reference(key=(Key(type_=KeyElements.CONCEPT_DESCRIPTION, local=True, value='https://admin-shell.io/zvei/nameplate/2/0/Nameplate', id_type=KeyType.IRI))),
            qualifier: Any=set(),
            kind: Any=ModelingKind.TEMPLATE,
                            
                        
    ):
        submodel_element = [manufacturerName,manufacturerProductDesignation,contactInformation,manufacturerProductRoot,manufacturerProductFamily,manufacturerProductType,orderCodeOfManufacturer,productArticleNumberOfManufacturer,dateOfManufacture,hardwareVersion,firmwareVersion,softwareVersion,markings,assetSpecificProperties]

                
        super().__init__(
            submodel_element=[se for se in submodel_element if isinstance(se, SubmodelElement)],















                                    identification = identification,
                                    id_short = id_short,
                                    category = category,
                                    description = description,
                                    administration = administration,
                                    semantic_id = semantic_id,
                                    qualifier = qualifier,
                                    kind = kind,
                            
                        
        )
    
            
        )