from model.EnseignantM import Enseignant

class ProgrammeEtude:

    def __init__(self) -> None:
        
        self.__id : int = None
        self.__nom : str = None
        self.__idCours : int = None
        self.___matriculeEns : Enseignant = None    

    def setId(self, id) -> int:
        
        self.__id = id

    def getId(self) -> int:
        
        return self.__id
    
    def setNom(self, nom) -> str:
        
        self.__nom = nom
    
    def getNom(self) -> str:
        
        return self.__nom
    
    def setIdCours(self, idCours) -> int:
        
        self.__idCours = idCours
    
    def getIdCours(self) -> int:
        
        return self.__idCours
    
    def setIdEnseignant(self, matriculeEns : Enseignant):
        
        self.___matriculeEns = matriculeEns
    
    def getIdEnseignant(self) -> Enseignant:
        
        return self.___matriculeEns