from dao.ModelDAO import ModelDAO
from model.MembreM import Membre


class MembreDAO(ModelDAO):

    def __init__(self) -> None:
        
        params = ModelDAO.connect_object
        self.cursor = params.cursor()

    def insert(self, objIns) -> int:
        try:
            query = "INSERT INTO Membre (id, nom, prenom, email, role) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (objIns.getId(), objIns.getNom(), objIns.getPrenom(), objIns.getEmail(), objIns.getRole())) 
            self.cursor.connection.commit()
            return self.cursor.rowcount if self.cursor.rowcount != 0 else 0

        except Exception as e:
            print(f'Erreur_MembreDAO.insert() ::: {e}')
            self.cursor.connection.rollback()
        
        finally:
            self.cursor.close()

    def insertList(self, objInsList) -> int:
        try:
            query = "INSERT INTO Membre (id, nom, prenom, email, role) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.executemany(query, [(objIns.id, objIns.nom, objIns.prenom, objIns.email, objIns.role) for objIns in objInsList])
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_MembreDAO.insertList() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()

        finally:
            self.cursor.close()
    

    def findOne(self, findKey) -> object:
        try:
            query = "SELECT * FROM Membre WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()

            if res is not None:
                membre = Membre()
                membre.setId(res[0])
                membre.setNom(res[1])
                membre.setPrenom(res[2])
                membre.setEmail(res[3])
                membre.setRole(res[4])
                return membre
            
            else:
                return None
        
        except Exception as e:
            print(f'Erreur_MembreDAO.findOne() ::: {e}')
            # if get return none
            return None

        finally:
            self.cursor.close()

    def findAll(self) -> list:
        try:
            query = "SELECT * FROM Membre"
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            list_membre = []
            if res is not None:
                
                for row in res:
                    membre = Membre()
                    membre.setId(row[0])
                    membre.setNom(row[1])
                    membre.setPrenom(row[2])
                    membre.setEmail(row[3])
                    membre.setRole(row[4])
                    list_membre.append(membre)

                return list_membre
            else:
                return None
        
        except Exception as e:
            print(f'Erreur_MembreDAO.findAll() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()


    def findAllByOne(self, findKey) -> list:
        try:
            query = "SELECT * FROM Membre WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()
        
            if res is not None:
                membre = Membre()
                membre.setId(res[0])
                membre.setNom(res[1])
                membre.setPrenom(res[2])
                membre.setEmail(res[3])
                membre.setRole(res[4])
                return [membre]
            
        except Exception as e:
            print(f'Erreur_MembreDAO.findAllByOne() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()

    def findAllByLike(self, findKey) -> list:
        try:
            query = "SELECT * FROM Membre WHERE id LIKE %s"
            self.cursor.execute(query, (findKey))
            res = self.cursor.fetchall()
            list_membre = []
            if res:
                
                for row in res:
                    membre = Membre()
                    membre.setId(row[0])
                    membre.setNom(row[1])
                    membre.setPrenom(row[2])
                    membre.setEmail(row[3])
                    membre.setRole(row[4])
                    list_membre.append(membre)
            
                return list_membre
            else:
                return None
        except Exception as e:
            print(f'Erreur_MembreDAO.findAllByLike() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()


    def update(self, cleAnc, objUpd) -> int:
        try:
            query = "UPDATE Membre SET nom = %s, prenom = %s, email = %s, role = %s WHERE id = %s"
            self.cursor.execute(query, (objUpd.nom, objUpd.prenom, objUpd.email, objUpd.role, cleAnc))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_MembreDAO.update() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
        
        finally:
            self.cursor.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = "DELETE FROM Membre WHERE id = %s"
            self.cursor.execute(query, (cleSup,))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_MembreDAO.deleteOne() ::: {e}')
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

