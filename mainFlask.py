from flask import Flask, request

from controller.MembreC import MembreController
from controller.EtudiantC import EtudiantController

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
    

@app.route('/api/uvy/membre/create_membre_list', methods=['POST'])
def _insert_list():
    # récupérer les values de la requêtes
    # exemple : id = request.json.get('id')
    listouille = request.json.get('liste')
    var = MembreController.insertList(listouille)
    if var != 'Error':
        return {'response' : 'LIST ADDED'}
    else:
        return {'response' : 'LIST NOT ADDED'}
    

@app.route('/api/uvy/membre/update_membre', methods=['POST'])
def _update_membre():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        id = request.json.get('id')
        nom = request.json.get('nom')
        prenom = request.json.get('prenom')
        email = request.json.get('email')
        role = request.json.get('role')

        eC = MembreController().update(id, nom, prenom, email, role)
        print(eC)
        return {'response' : 'True'}
    except Exception as e:
        print(f"Erreur lors de la recherche d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}
    
@app.route('/api/uvy/membre/delete_one', methods=['POST'])
def _delete_membre_one():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        id = request.json.get('id')
        eC = MembreController().deleteOne(id)
        print(eC)
        return {'response' : 'True'}
    except Exception as e:
        print(f"Erreur lors de la suppression d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}
    
@app.route('/api/uvy/membre/find_one', methods=['POST'])
def _find_one_membre():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        id = request.json.get('id')
        eC = MembreController().findOne(id)
        print(eC)
        if eC:
            res = {
                'id' : eC.getId(),
                'nom' : eC.getNom(),
                'prenom' : eC.getPrenom(),
                'email' : eC.getEmail(),
                'role' : eC.getRole()
            }
            return {'response' : res}
        else:
            res = {'response' : 'Error'}
    except Exception as e:
        print(f"Erreur lors de la recherche d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}

@app.route('/api/uvy/membre/find_all', methods=['POST'])
def _find_all_membre():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        eC = MembreController().findAll()
        print(eC)
        if eC:
            res = []
            for e in eC:
                res.append({
                    'id' : e.getId(),
                    'nom' : e.getNom(),
                    'prenom' : e.getPrenom(),
                    'email' : e.getEmail(),
                    'role' : e.getRole()
                })
            return {'response' : res}
        else:
            res = {'response' : 'Error'}
    except Exception as e:
        print(f"Erreur lors de la recherche d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}
    

@app.route('/api/uvy/membre/create_etudiant', methods=['POST'])
def _insert_etudiant():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        id = request.json.get('id')
        matriculeetu = request.json.get('matriculeetu')
        notes = request.json.get('notes')

        eC = EtudiantController().create_etudiant(id, matriculeetu, notes)
        print(eC)
        return {'response' : 'True'}
    except Exception as e:
        print(f"Erreur lors de l'ajout d'un etudiant ::: {e}")
        return {'response': 'Internal Server Error'}
    