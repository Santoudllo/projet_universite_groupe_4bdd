from dao import ModelDAO
from model.ProgrammeEtudeM import ProgrammeEtude


class ProgrammeEtudeDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            self.cursor.executemany("INSERT INTO programme_etude (id, nom, idcours, idenseignant)")
            self.cursor.executemany("VALUES (%s, %s, %s, %s)", objIns)
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.insert() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()

    def insertList(self, objInsList) -> int:
        try:
            self.cursor.executemany("INSERT INTO programme_etude (id, nom, idcours, idenseignant)")
            self.cursor.executemany("VALUES (%s, %s, %s, %s)", objInsList)
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.insertList() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()

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

    