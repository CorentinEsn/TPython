import datetime
class Etudiant:
    def __init__(self, nom, prenom, date_naissance):    # Constructeur
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def adresselec(self):   # Adresse électronique
        mail =''

        try:
            # raise an error if the prenom is not a string
            if type(self.prenom) != str or type(self.nom) != str:
                raise TypeError("Le prénom et/ou le nom ne sont pas des chaînes de caractères")
            # raise an error if the prenom or nom is null
            if self.prenom == '' or self.nom == '':
                raise Exception("Le prénom et/ou le nom ne peuvent pas être nuls")

            mail = self.prenom + "." + self.nom + "@etu.univ-tours.fr"

        except Exception as e:
            #si le prenom est null, on affiche une erreur
            if e == TypeError:
                print("Le prénom et/ou le nom ne sont pas des chaînes de caractères")
            if e == Exception:
                print(e.__str__())
            else:
                print("Erreur lors de la création de l'adresse électronique : " + e.__str__())
        finally:
            return mail

    def age(self):  # Age de l'étudiant
        return datetime.date.today().year - self.date_naissance.year

    def __str__(self):  # Surcharge de l'opérateur print()
        return "{} {} {}".format(self.nom, self.prenom, self.date_naissance)