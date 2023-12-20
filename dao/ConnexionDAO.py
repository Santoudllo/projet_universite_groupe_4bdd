import psycopg2  # pip install psycopg2-binary
import yaml # pip install PyYAML

class ConnexionDB:

    def __init__(self):
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("- class connexionBD() is running ... \n\n")
            print("- config/Config.yml is loading ...")

            #get file and data
            with open("./config/Config.yaml", "r") as fic :
                donnees = yaml.safe_load(fic)
            db = donnees["database_name"]
            host = donnees["host"]
            port = donnees["port"]
            usr = donnees["user"]
            pwd = donnees["pwd"]

            self.cnx = psycopg2.connect(dbname=db,
                                    host=host,
                                    port=port,
                                    user=usr,
                                    password=pwd
                                    )
            return self.cnx
        except Exception as e:
            print(f"Erreur-CONNECTION ::: {e}")
        return self.cnx

