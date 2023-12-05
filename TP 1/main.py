from Date import Date
from Etudiant import Etudiant


def HelloWorld():
    print("Bonjour le monde !")


def OpenAndAppendFile():

    # Choix du fichier à ouvrir
    print("Choisissez un fichier à ouvrir :")
    filename = input("> ")
    fic = open(filename, "at")

    # Ajout du texte
    print("Texte à ajouter :")
    text = input("> ")
    fic.write(text + "/n")
    fic.close()

    # Affichage du contenu du fichier
    print("Le fichier contient le texte suivant :")
    fic = open(filename, "r")
    print(fic.read())
    fic.close()

    # Vider le fichier
    fic = open(filename, "wt")
    fic.close()


# Liste des étudiants depuis un fichier CSV
def NewEtudiantsFromCSV(filename):
    etudiants = []  # Liste d'étudiants
    fic = open(filename, "r")   # Ouverture du fichier
    for line in fic:    # Lecture du fichier ligne par ligne
        line = line.strip()
        line = line.split(";")
        etudiants.append(Etudiant(line[0], line[1], Date((line[2]))))
    fic.close()
    return etudiants


# Construction de la liste et affichage des étudiants
Etudiants = NewEtudiantsFromCSV("TP 1/fichetu.csv")
for etudiant in Etudiants:
    print(etudiant)

