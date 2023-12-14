from dao import ModelDAO
from model.EnseignantM import Enseignant


class EnseignantDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            query = "INSERT INTO Enseignant (id, nom, prenom, email, role)"
            self.cursor.execute(query, (objIns.id, objIns.nom, objIns.prenom, objIns.email, objIns.role))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.insert() ::: {e}')
            self.cursor.connection.rollback()
        
        finally:
            self.cursor.close()


    def insertList(self, objInsList) -> int:
        try:
            query = "INSERT INTO Enseignant (id, nom, prenom, email, role) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.executemany(query, [(objIns.id, objIns.nom, objIns.prenom, objIns.email, objIns.role) for objIns in objInsList])
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.insertList() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
        
        finally:
            self.cursor.close()


    def findOne(self, findKey) -> object:
        try:
            query = "SELECT * FROM Enseignant WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()
            
            if res is not None:
                ens = Enseignant()
                ens.setId(res[0])
                ens.setNom(res[1])
                ens.setPrenom(res[2])
                ens.setEmail(res[3])
                ens.setRole(res[4])
                return ens
            
            else:
                return None
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.findOne() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()
    

    def findAll(self) -> list:
        try:
            query = "SELECT * FROM Enseignant"
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            list_ens = []
            if res is not None:
                
                for row in res:
                    ens = Enseignant()
                    ens.setId(row[0])
                    ens.setNom(row[1])
                    ens.setPrenom(row[2])
                    ens.setEmail(row[3])
                    ens.setRole(row[4])
                    list_ens.append(ens)
            
                return list_ens
            else:
                return None
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.findAll() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()


    def findAllByOne(self, findKey) -> list:
        try:
            query = "SELECT * FROM Enseignant WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()
        
            if res is not None:
                ens = Enseignant()
                ens.setId(res[0])
                ens.setNom(res[1])
                ens.setPrenom(res[2])
                ens.setEmail(res[3])
                ens.setRole(res[4])
                return [ens]
            
        except Exception as e:
            print(f'Erreur_EnseignantDAO.findAllByOne() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()

    def findAllByLike(self, findKey) -> list:
        try:
            query = "SELECT * FROM Enseignant WHERE id LIKE %s"
            self.cursor.execute(query, (findKey))
            res = self.cursor.fetchall()
            list_ens = []
            if res is not None:
                
                for row in res:
                    ens = Enseignant()
                    ens.setId(row[0])
                    ens.setNom(row[1])
                    ens.setPrenom(row[2])
                    ens.setEmail(row[3])
                    ens.setRole(row[4])
                    list_ens.append(ens)
            
                return list_ens
            
        except Exception as e:
            print(f'Erreur_EnseignantDAO.findAllByLike() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()

    def update(self, cleAnc, objUpd) -> int:
        try:
            query = "UPDATE Enseignant SET nom = %s, prenom = %s, email = %s, role = %s WHERE id = %s"
            self.cursor.execute(query, (objUpd.nom, objUpd.prenom, objUpd.email, objUpd.role, cleAnc))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.update() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
        
        finally:
            self.cursor.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = "DELETE FROM Enseignant WHERE id = %s"
            self.cursor.execute(query, (cleSup,))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_EnseignantDAO.deleteOne() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
        
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

    