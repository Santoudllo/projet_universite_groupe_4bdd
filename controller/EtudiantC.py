# EtudiantController.py

from model.EtudiantM import *
from dao.EtudiantDAO import *

class EtudiantController:

    @staticmethod
    def create_etudiant(id, nom, prenom, email, role, matricule, notes):
        
        etudiant = Etudiant()
        etudiant.setId(id)
        etudiant.setNom(nom)
        etudiant.setPrenom(prenom)
        etudiant.setEmail(email)
        etudiant.setRole(role)
        etudiant.setMatricule(matricule)
        etudiant.setNotes(notes)

        # Sauvegarde de l'étudiant dans la base de données
        EtudiantDAO.save(etudiant)

        return etudiant

    @staticmethod
    def get_etudiant(matricule):
        # Chargement de l'étudiant à partir de la base de données en utilisant le matricule
        etudiant_data = EtudiantDAO.load(matricule)

        if etudiant_data:
            etudiant = Etudiant()
            etudiant.setId(etudiant_data['id'])
            etudiant.setNom(etudiant_data['nom'])
            etudiant.setPrenom(etudiant_data['prenom'])
            etudiant.setEmail(etudiant_data['email'])
            etudiant.setRole(etudiant_data['role'])
            etudiant.setMatricule(etudiant_data['matricule'])
            etudiant.setNotes(etudiant_data['notes'])
            return etudiant
        else:
            return None
