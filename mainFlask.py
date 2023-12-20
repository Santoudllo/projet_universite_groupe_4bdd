from flask import Flask, requets

app = Flask(__name__)

@app.route('/api/amz/membre/insert_membre', methods=['POST'])
def _insert_membre():
    try:
        # récupérer les values de la requêtes
        # exemple : id = request.json.get('id')
        pass
    except Exception as e:
        print(f"Erreur lors de l'ajout d'un membre ::: {e}")
        return {'response': 'Internal Server Error'}