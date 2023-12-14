from dao import ModelDAO
from model.EnseignantM import Enseignant


class EnseignantDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            self.cursor.executemany("INSERT INTO enseignant (id, specialite, matriculens, cours_enseignees)")
            self.cursor.executemany("VALUES (%s, %s, %s, %s)", objIns)
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_EnseignantDAO.insert() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()


    def insertList(self, objInsList) -> int:
        try:
            self.cursor.executemany("INSERT INTO enseignant (id, specialite, matriculeens, cours_enseignees)")
            self.cursor.executemany("VALUES (%s, %s, %s, %s)", objInsList)
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_EnseignantDAO.insertList() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()

    def findOne(self, findKey) -> object:
        try:
            self.cursor.execute(f"SELECT * FROM enseignant WHERE matriculeens = {findKey}")
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erreur_EnseignantDAO.findOne() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()

    def findAll(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM enseignant")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_EnseignantDAO.findAll() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()


    def findAllByOne(self, findKey) -> list:
        try:
            self.cursor.execute(f"SELECT * FROM enseignant WHERE matriculeens = {findKey}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_EnseignantDAO.findAllByOne() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()

    def findAllByLike(self, findKey) -> list:
        try:
            self.cursor.execute(f"SELECT * FROM enseignant WHERE matriculeens LIKE '%{findKey}%'")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_EnseignantDAO.findAllByLike() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()


    def update(self, cleAnc, objUpd) -> int:
        try:
            self.cursor.execute(f"UPDATE enseignant SET {objUpd} WHERE matriculeens = {cleAnc}")
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_EnseignantDAO.update() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()

    def deleteOne(self, cleSup) -> int:
        try:
            self.cursor.execute(f"DELETE FROM enseignant WHERE matriculeens = {cleSup}")
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_EnseignantDAO.deleteOne() ::: {e}")
            self.cursor.connection.rollback()
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

    