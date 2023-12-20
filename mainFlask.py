from flask import Flask, request
from flask_cors import CORS
from datetime import datetime
import json
from functools import wraps
import traceback

from controller.MembreC import MembreController
from controller.EtudiantC import EtudiantController

app = Flask(__name__)

CORS(app, resources={fr"/api/uvy/membre/*": {"origins": "*"}})

LOG_FILE_PATH = 'projet_universite_groupe_4bdd/utils/logs.json'

def log_request_info(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        try:
            start_time = datetime.now()

            # Exécuter la fonction de route
            response = route_function(*args, **kwargs)

            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()

            # Récupérer les informations de la requête
            request_info = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'route': request.path,
                'method': request.method,
                'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr),
                'execution_time': execution_time,
                'response': response
            }

            # Charger les anciens logs
            try:
                with open(LOG_FILE_PATH, 'r') as log_file:
                    logs = json.load(log_file)
            except (FileNotFoundError, json.JSONDecodeError):
                logs = []

            # Ajouter les nouveaux logs
            logs.append(request_info)

            # Enregistrer les logs dans le fichier
            with open(LOG_FILE_PATH, 'w') as log_file:
                json.dump(logs, log_file, indent=2)

            return response
        except Exception as e:
            error_message = f"Erreur lors de la journalisation de la requête : {e}"
            print(error_message)

            # Inclure les informations d'erreur dans la réponse JSON
            return {'error': 'Erreur interne du serveur', 'details': str(e), 'traceback': traceback.format_exc()}

    return wrapper

@app.route('/api/uvy/membre/create_membre', methods=['POST'])
@log_request_info
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
@log_request_info
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
@log_request_info
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
@log_request_info
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
@log_request_info
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
@log_request_info
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
@log_request_info
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
    