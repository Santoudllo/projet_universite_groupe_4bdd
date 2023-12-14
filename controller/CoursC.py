from dao.MembreDAO import *
from model.MembreM import Membre

class Membre:
    @staticmethod
    def createUser(pwd, user):
        """
        Créer un nouvel utilisateur.
        @param pwd: Mot de passe de l'utilisateur.
        @param usr: Nom d'utilisateur.
        @return: Statut de la création de l'utilisateur.
        """
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.createUser(pwd, user)
            print("sys:",sys)
            if sys==0 :
                return "ERROR"
            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"
        except Exception as e:
            print(f'Erreur_membreC.createUser() ::: {e}')
            return None
        
    @staticmethod
    def createRole(role):
        """
        Créer un nouveau rôle.
        @param role: Nom du rôle à créer.
        @return: Statut de la création du rôle.
        """
        try:
            mDAO = MembreDAO()
            sys: int = mDAO.createRole(role)
            print("sys:",sys)
            if sys==0 :
                return "ERROR"
            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"
        except Exception as e:
            print(f'Erreur_membreC.createRole() ::: {e}')
            return None
        
        @staticmethod
        def privilege_Role(privileges, tables, roles):
            """
            Attribuer des privilèges à un rôle.
            @param privileges: Liste des privilèges à attribuer.
            @param tables: Liste des tables concernées.
            @param roles: Liste des rôles auxquels attribuer les privilèges.
            @return: Statut de l'attribution des privilèges.
            """
            try:
                mDAO = MembreDAO()
                sys: int = mDAO.attribuerPriviliege(privileges, tables, roles)
                print("sys:",sys)
                if sys==0 :
                    return "ERROR"
                return "ATTRIBUTION DE(S) PRIVILEGE(S) A UN ROLE AVEC SUCCES"
            except Exception as e:
                print(f'Erreur_membreC.privilege_Role() ::: {e}')
                return None
        
        @staticmethod
        def attribution_Role(usr, roles):
            """
            Attribuer des rôles à un utilisateur.
            @param usr: Nom de l'utilisateur.
            @param roles: Liste des rôles à attribuer à l'utilisateur.
            @return: Statut de l'attribution des rôles.
            """
            try:
                mDAO = MembreDAO()
                sys: int = mDAO.attribuerRole(usr, roles)
                print("sys:",sys)
                if sys==0 :
                    return "ERROR"
                return "ATTRIBUTION DE(S) ROLE(S) A UN USER AVEC SUCCES"
            except Exception as e:
                print(f'Erreur_membreC.privilege_Role() ::: {e}')
                return None
            finally:
                mDAO.close()

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