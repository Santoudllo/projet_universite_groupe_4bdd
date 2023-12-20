from flask import Flask, request

from controller.MembreC import MembreController

app = Flask(__name__)

@app.route('/api/uvy/membre/create_membre', methods=['POST'])
def _insert_membre():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')

        id = request.json.get('id')
        nom = request.json.get('nom')
        prenom = request.json.get('prenom')
        email = request.json.get('email')
        role = request.json.get('role')

        eC = MembreController().insert(id, nom, prenom, email, role)

        print(eC)
        return {'response' : 'True'}
    except Exception as e:
        print(f"Erreur lors de l'ajout d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}