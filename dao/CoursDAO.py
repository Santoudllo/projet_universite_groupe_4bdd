from dao import ModelDAO
from model.CoursM import Cours


class CoursDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            self.cursor.execute(f"INSERT INTO cours VALUES ({objIns.idCours}, '{objIns.titre}', '{objIns.description}', '{objIns.dateDebut}', '{objIns.dateFin}', {objIns.idProgramme})")
            self.cnx.commit()
            return 1

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

    