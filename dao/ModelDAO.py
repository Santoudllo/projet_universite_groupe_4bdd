from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionDB

class ModelDAO(ABC):
    

    connect_object =  ConnexionDB().getConnexion()

    ### CRUD

    ## Insert

    @abstractmethod
    def insert(self, objIns) -> int:  
        pass

    @abstractmethod
    def insertList(self, objInsList) -> int:
        pass

    ## SELECT

    @abstractmethod
    def findOne(self, findKey) -> object:
        pass

    @abstractmethod
    def findAll(self) -> list:
        pass

    @abstractmethod
    def findAllByOne(self, findKey) -> list:
        pass

    @abstractmethod
    def findAllByLike(self, findKey) -> list:
        pass
    ## UPDATE

    @abstractmethod
    def update(self, cleAnc, objUpd) -> int:
        pass

    @abstractmethod
    def deleteOne(self, cleSup) -> int:
        pass


    ### 



    @abstractmethod
    def createUser(self, pwd, user) -> int:
        pass

    @abstractmethod
    def createRole(self, role) -> int:
        pass

    @abstractmethod
    def attributePrivilege(self, privileges : str, tables : str, role : str) -> int:
        pass

    @abstractmethod
    def attributeRole(self, user, role) -> int:
        pass