# EtudiantController.py

from model.EtudiantM import *
from dao.EtudiantDAO import *

class EtudiantController:

    @staticmethod
    def create_etudiant(id, matricule, notes):
        
        etudiant = Etudiant()
        etudiant.setId(id)
        etudiant.setMatricule(matricule)
        etudiant.setNotes(notes)

        # Sauvegarde de l'étudiant dans la base de données
        etudiantdaobackup = EtudiantDAO().insert(etudiant)
        if etudiantdaobackup != 0:
            return etudiantdaobackup
        
        else:
            return None

    @staticmethod
    def update_etudiant(id, matricule, notes):
        etudiant = Etudiant()
        etudiant.setId(id)
        etudiant.setMatricule(matricule)
        etudiant.setNotes(notes)
        # Sauvegarde de l'étudiant dans la base de données
        etudiantdaobackup = EtudiantDAO.update(etudiant)
        if etudiantdaobackup != 0:
            return etudiantdaobackup
        else:   
            return None
        

    @staticmethod
    def delete_etudiant(id):
        etudiant = Etudiant()
        etudiant.setId(id)
        # Suppression de l'étudiant dans la base de données
        etudiant = EtudiantDAO.deleteOne(etudiant)
        if etudiant != 0:
            return etudiant
        else: 
            return None
    
    @staticmethod
    def get_all_etudiants():
        etudiants = EtudiantDAO.findAll()
        return etudiants
    
    @staticmethod
    def get_etudiant_by_id(id):
        etudiant = EtudiantDAO.findById(id)
        return etudiant
    
    @staticmethod
    def get_etudiant_by_email(email):
        etudiant = EtudiantDAO.findByEmail(email)
        return etudiant
    
    @staticmethod
    def get_etudiant_by_matricule(matricule):
        etudiant = EtudiantDAO.findByMatricule(matricule)
        return etudiant