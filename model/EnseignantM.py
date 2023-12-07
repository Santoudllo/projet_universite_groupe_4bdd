from MembreM import Membre

class Enseignant(Membre):

    def __init__(self) -> None:
        super().__init__()
        self.__specialite: str = None
        self.__matriculeEns : str = None
        self.__cours_enseignes: list = []

    def setSpecialite(self, specialite) -> str:
        
        self.__specialite = specialite

    def getSpecialite(self) -> str:
        
        return self.__specialite
    
    def setMatriculeEns(self, matriculeEns) -> str:
       
        self.__matriculeEns = matriculeEns

    def getMatriculeEns(self) -> str:
        
        return self.__matriculeEns

    def setCoursEnseignes(self, cours_enseignes) -> list:
        
        self.__cours_enseignes = cours_enseignes

    def getCoursEnseignes(self) -> list:
        
        return self.__cours_enseignes