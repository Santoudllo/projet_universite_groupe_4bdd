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
        
        except Exception as e:
            print(f'Erreur_CoursDAO.insert() ::: {e}')
            self.cnx.rollback()
            
            return 0
        
        finally:
            self.cursor.close()

    def insertList(self, objInsList) -> int:
        try:
            query = "INSERT INTO cours VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.executemany(query, [(objIns.idCours, objIns.titre, objIns.description, objIns.dateDebut, objIns.dateFin, objIns.idProgramme) for objIns in objInsList])
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_CoursDAO.insertList() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
            
            return 0
        
        finally:
            self.cursor.close()


    def findOne(self, findKey) -> object:
        try:
            query = "SELECT * FROM cours WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()
            
            if res is not None:
                cours = Cours()
                cours.setIdCours(res[0])
                cours.setTitre(res[1])
                cours.setDescription(res[2])
                cours.setDateDebut(res[3])
                cours.setDateFin(res[4])
                cours.setIdProgramme(res[5])
                return cours
            
            else:
                return None
            
        except Exception as e:
            print(f'Erreur_CoursDAO.findOne() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()

    def findAll(self) -> list:
        try:
            query = "SELECT * FROM cours"
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            list_cours = []
            if res is not None:
                
                for row in res:
                    cours = Cours()
                    cours.setIdCours(row[0])
                    cours.setTitre(row[1])
                    cours.setDescription(row[2])
                    cours.setDateDebut(row[3])
                    cours.setDateFin(row[4])
                    cours.setIdProgramme(row[5])
                    list_cours.append(cours)
            
                return list_cours
            
            else:
                return None
            
        except Exception as e:
            print(f'Erreur_CoursDAO.findAll() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()
            

    def findAllByOne(self, findKey) -> list:
        try:
            query = "SELECT * FROM cours WHERE id = %s"
            self.cursor.execute(query, (findKey,))
            res = self.cursor.fetchone()
        
            if res is not None:
                cours = Cours()
                cours.setIdCours(res[0])
                cours.setTitre(res[1])
                cours.setDescription(res[2])
                cours.setDateDebut(res[3])
                cours.setDateFin(res[4])
                cours.setIdProgramme(res[5])
                return [cours]
            
        except Exception as e:
            print(f'Erreur_CoursDAO.findAllByOne() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()


    def findAllByLike(self, findKey) -> list:
        try:
            query = "SELECT * FROM cours WHERE id LIKE %s"
            self.cursor.execute(query, (findKey))
            res = self.cursor.fetchall()
            list_cours = []
            if res is not None:
                
                for row in res:
                    cours = Cours()
                    cours.setIdCours(row[0])
                    cours.setTitre(row[1])
                    cours.setDescription(row[2])
                    cours.setDateDebut(row[3])
                    cours.setDateFin(row[4])
                    cours.setIdProgramme(row[5])
                    list_cours.append(cours)
            
                return list_cours
            
            else:
                return None
        
        except Exception as e:
            print(f'Erreur_CoursDAO.findAllByLike() ::: {e}')
            # if get return none
            return None
        
        finally:
            self.cursor.close()


    def update(self, cleAnc, objUpd) -> int:
        try:
            query = "UPDATE cours SET titre = %s, description = %s, dateDebut = %s, dateFin = %s, idProgramme = %s WHERE id = %s"
            self.cursor.execute(query, (objUpd.titre, objUpd.description, objUpd.dateDebut, objUpd.dateFin, objUpd.idProgramme, cleAnc))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_CoursDAO.update() ::: {e}')
            # if commit return rollback
            self.cursor.connection.rollback()
            
            return 0
        
        finally:
            self.cursor.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = "DELETE FROM cours WHERE id = %s"
            self.cursor.execute(query, (cleSup,))
            self.cursor.commit()
            return self.cursor.rowcount if self.cursor.rowcount!= 0 else 0
        
        except Exception as e:
            print(f'Erreur_CoursDAO.deleteOne() ::: {e}')
            # if commit return rollback
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

    