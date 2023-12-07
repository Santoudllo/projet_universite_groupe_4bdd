from MembreM import Membre

class Etudiant(Membre):

    def __init__(self) -> None:
        super().__init__() # __super__ take all the properties of the parent class
        self.__matriculeEtu: str = None
        self.__notes: list = []

    def setMatricule(self, matriculeEtu) -> str:
        self.__matriculeEtu = matriculeEtu

    def getMatricule(self) -> str:
        return self.__matriculeEtu

    def setNotes(self, notes) -> list:
        self.__notes = notes

    def getNotes(self) -> list:
        return self.__notes