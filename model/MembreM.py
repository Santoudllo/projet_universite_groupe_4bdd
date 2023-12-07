class Membre:

    def __init__(self) -> None:
        
        self.__id : int = None
        self.__nom : str = None
        self.__prenom : str = None
        self.__email : str = None
        self.__role : str = None

    def setId(self, id) -> int:

        self.__id = id

    def getId(self) -> int:

        return self.__id
    
    def setNom(self, nom) -> str:

        self.__nom = nom

    def getNom(self) -> str:

        return self.__nom
    
    def setPrenom(self, prenom) -> str:

        self.__prenom = prenom

    def getPrenom(self) -> str:

        return self.__prenom
    
    def setEmail(self, email) -> str:

        self.__email = email

    def getEmail(self) -> str:

        return self.__email
    
    def setRole(self, role) -> str:

        self.__role = role

    def getRole(self) -> str:

        return self.__role
    
