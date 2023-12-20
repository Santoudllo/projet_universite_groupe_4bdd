from dao.ModelDAO import ModelDAO
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
        try:
            self.cursor.execute(f"SELECT * FROM programme_etude WHERE id = {findKey}")
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.findOne() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()


    def findAll(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM programme_etude")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.findAll() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()

    def findAllByOne(self, findKey) -> list:
        try:
            self.cursor.execute(f"SELECT * FROM programme_etude WHERE id = {findKey}")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.findAllByOne() ::: {e}")
            self.cursor.connection.rollback()
            return None
        
        finally:
            self.cursor.close()


    def findAllByLike(self, findKey) -> list:
        try:
            self.cursor.execute(f"SELECT * FROM programme_etude WHERE nom LIKE '%{findKey}%'")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.findAllByLike() ::: {e}")
            self.cursor.connection.rollback()
            return None
        finally:
            self.cursor.close()

    def update(self, cleAnc, objUpd) -> int:
        try:
            self.cursor.execute(f"UPDATE programme_etude SET {cleAnc} = %s WHERE id = %s", objUpd)
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.update() ::: {e}")
            self.cursor.connection.rollback()
            return 0
        
        finally:
            self.cursor.close()

    def deleteOne(self, cleSup) -> int:
        try :
            self.cursor.execute(f"DELETE FROM programme_etude WHERE id = {cleSup}")
            return self.cursor.rowcount
        except Exception as e:
            print(f"Erreur_ProgrammeEtudeDAO.deleteOne() ::: {e}")
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

    