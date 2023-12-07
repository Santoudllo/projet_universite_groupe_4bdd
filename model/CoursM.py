class Cours:

    def __init__(self) -> None:
        
        self.__coursId : int = None
        self.__nomCours : str = None
        self.__idEnseignant : int = None
    
    def setCoursId(self, cours_id) -> int:

        self.__coursId = cours_id

    def getCoursId(self) -> int:

        return self.__coursId
    
    def setNomCours(self, nom_cours) -> str:

        self.__nomCours = nom_cours

    def setNomCours(self) -> str:

        return self.__nomCours
    
    def setIdEnseignant(self, id_enseignant) -> int:

        self.__idEnseignant = id_enseignant

    def getIdEnseignant(self) -> int:

        return self.__idEnseignant
    
    