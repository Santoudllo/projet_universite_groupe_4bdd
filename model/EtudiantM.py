class Etudiant():

    def __init__(self) -> None:
        
        self.__id : int = None
        self.__matriculeEtu: str = None
        self.__notes: list = []

    def setId(self, id) -> int:
        self.__id = id
    
    def getId(self) -> int:
        return self.__id

    def setMatricule(self, matriculeEtu) -> str:
        self.__matriculeEtu = matriculeEtu

    def getMatricule(self) -> str:
        return self.__matriculeEtu

    def setNotes(self, notes) -> list:
        self.__notes = notes

    def getNotes(self) -> list:
        return self.__notes