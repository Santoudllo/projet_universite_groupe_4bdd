from dao import ModelDAO
from model.EtudiantM import Etudiant


class EtudiantDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            self.cursor.execute("INSERT INTO etudiant (id, matriculeetu, notes")
            self.cursor.execute("VALUES (%s, %s, %s)", (objIns.getId(), objIns.getMatriculeEtu(), objIns.getNotes()))
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return 0
        finally:
            self.cursor.close()


    def insertList(self, objInsList) -> int:
        try:
            self.cursor.executemany("INSERT INTO etudiant (id, matriculeetu, notes")
            self.cursor.executemany("VALUES (%s, %s, %s)", objInsList)
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return 0
        finally:
            self.cursor.close()


    def findOne(self, findKey) -> object:
        try:
            self.cursor.execute("SELECT * FROM etudiant WHERE matriculeetu = %s", (findKey,))
            result = self.cursor.fetchone()
            return Etudiant(result[0], result[1], result[2])
        except Exception as e:
            print(e)
            return None
        finally:
            self.cursor.close()

    def findAll(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM etudiant")
            result = self.cursor.fetchall()
            etudiants = []
            for row in result:
                etudiants.append(Etudiant(row[0], row[1], row[2]))
            return etudiants
        except Exception as e:
            print(e)
            return None
        finally:
            self.cursor.close()

    def findAllByOne(self, findKey) -> list:
        try:
            self.cursor.execute("SELECT * FROM etudiant WHERE matriculeetu = %s", (findKey,))
            result = self.cursor.fetchall()
            etudiants = []
            for row in result:
                etudiants.append(Etudiant(row[0], row[1], row[2]))
            return etudiants
        except Exception as e:
            print(e)
            return None
        finally:
            self.cursor.close()

    def findAllByLike(self, findKey) -> list:
        try:
            self.cursor.execute("SELECT * FROM etudiant WHERE matriculeetu LIKE %s", (findKey,))
            result = self.cursor.fetchall()
            etudiants = []
            for row in result:
                etudiants.append(Etudiant(row[0], row[1], row[2]))
            return etudiants
        except Exception as e:
            print(e)
            return None
        finally:
            self.cursor.close()

    def update(self, cleAnc, objUpd) -> int:
        try:
            self.cursor.execute("UPDATE etudiant SET notes = %s WHERE matriculeetu = %s", (objUpd.getNotes(), cleAnc))
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return 0
        finally:
            self.cursor.close()


    def deleteOne(self, cleSup) -> int:
        try:
            self.cursor.execute("DELETE FROM etudiant WHERE matriculeetu = %s", (cleSup,))
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            return 0
        finally:
            self.cursor.close()

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attributePrivilege(self, privileges : str, tables : str, role : str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass

    