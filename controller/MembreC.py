from dao.MembreDAO import MembreDAO
from model import MembreM

class MembreController:

    @staticmethod
    def insert(id_membre, nom, prenom, email, role) -> object:
        try:
            mM = MembreM.Membre()
            mM.setId(id_membre)
            mM.setNom(nom)
            mM.setPrenom(prenom)
            mM.setEmail(email)
            mM.setRole(role)
            res_m = MembreDAO().insert(mM)
            if res_m!= 0:
                return "AJOUT DU MEMBRE REUSSI"
            return 'ERROR'
        except Exception as e:
            print(f"Erreur_membreC.insertOne() ::: {e}")
        return None
    

    @staticmethod
    def findOne(findKey) -> object:
        try:
            mDAO = MembreDAO()
            sys: object = mDAO.findOne(findKey)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.findOne() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def findAll() -> list:
        try:
            mDAO = MembreDAO()
            sys: list = mDAO.findAll()
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.findAll() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def findAllByOne(findKey) -> list:
        try:
            mDAO = MembreDAO()
            sys: list = mDAO.findAllByOne(findKey)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.findAllByOne() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def findAllByLike(findKey) -> list:
        try:
            mDAO = MembreDAO()
            sys: list = mDAO.findAllByLike(findKey)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.findAllByLike() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def update(cleAnc, objUpd) -> int:
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.update(cleAnc, objUpd)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.update() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def deleteOne(cleSup) -> int:
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.deleteOne(cleSup)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.deleteOne() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def attributePrivilege(privileges : str, tables : str, role : str) -> int:
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.attribuerPriviliege(privileges, tables, role)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.attributePrivilege() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def attributeRole(usr : str, roles : str) -> int:
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.attribuerRole(usr, roles)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.attributeRole() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    @staticmethod
    def attributeUser(usr : str, roles : str) -> int:
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.attribuerRole(usr, roles)
            print("sys:",sys)
            return sys
        except Exception as e:
            print(f'Erreur_membreC.attributeRole() ::: {e}')
            return None
        finally:
            mDAO.close()
    
    