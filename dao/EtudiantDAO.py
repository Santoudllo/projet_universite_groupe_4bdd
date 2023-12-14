from dao import ModelDAO
from model.EtudiantM import Etudiant


class EtudiantDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            self.cursor.execute("INSERT INTO etudiant (id, matriculeetu, notes)

    def insertList(self, objInsList) -> int:
        pass

    def findOne(self, findKey) -> object:
        pass

    def findAll(self) -> list:
        pass

    def findAllByOne(self, findKey) -> list:
        pass

    def findAllByLike(self, findKey) -> list:
        pass

    def update(self, cleAnc, objUpd) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attributePrivilege(self, privileges : str, tables : str, role : str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass

    