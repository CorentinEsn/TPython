import datetime
class Etudiant:
    def __init__(self, nom, prenom, date_naissance):    # Constructeur
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def adresselec(self):   # Adresse électronique
        return self.prenom + "." + self.nom + "@etu.univ-tours.fr"

    def age(self):  # Age de l'étudiant
        return datetime.date.today().year - self.date_naissance.year

    def __str__(self):  # Surcharge de l'opérateur print()
        return "{} {} {}".format(self.nom, self.prenom, self.date_naissance)