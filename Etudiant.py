import datetime
class Etudiant:
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def Afficher(self):
        print("Nom : {}".format(self.nom))
        print("Prénom : {}".format(self.prenom))
        print("Date de naissance : {}".format(self.date_naissance))
    def adresselec(self):
        return self.prenom + "." + self.nom + "@etu.univ-tours.fr"

    def age(self):
        return datetime.date.today().year - self.date_naissance.year
