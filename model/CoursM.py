from model.EnseignantM import Enseignant

class Cours:

    def __init__(self) -> None:
        
        self.__coursId : int = None
        self.__nomCours : str = None
        self.__matriculeEns : Enseignant = None
    
    def setCoursId(self, cours_id) -> int:

        self.__coursId = cours_id

    def getCoursId(self) -> int:

        return self.__coursId
    
    def setNomCours(self, nom_cours) -> str:

        self.__nomCours = nom_cours

    def setNomCours(self) -> str:

        return self.__nomCours
    
    def setIdEnseignant(self, matriculeEns : Enseignant):

        self.__matriculeEns = matriculeEns

    def getIdEnseignant(self) -> Enseignant:

        return self.__matriculeEns
    
    