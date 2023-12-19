from Date import Date
from Etudiant import Etudiant

def HelloWorld():
    try:
        print("Bonjour le monde !")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def OpenAndAppendFile():

    try:
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

    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("Opération terminée.")


# Liste des étudiants depuis un fichier CSV
def NewEtudiantsFromCSV(filename):
    etudiants = []  # Liste d'étudiants
    try:
        with open(filename, "r") as fic:
            # Lecture du fichier ligne par ligne
            for line in fic:
                line = line.strip()
                line = line.split(";")
                assert len(line) == 3, "Format de ligne invalide"
                etudiants.append(Etudiant(line[0], line[1], Date(line[2])))
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
    except AssertionError as ae:
        print(f"Erreur de format dans le fichier CSV : {ae}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("Opération terminée.")
    return etudiants

try:
    HelloWorld()
    #OpenAndAppendFile()
    Etudiants = NewEtudiantsFromCSV("fichetu.csv")
    for etudiant in Etudiants:
        print(etudiant)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
'''
# Construction de la liste et affichage des étudiants
Etudiants = NewEtudiantsFromCSV("TP 1/fichetu.csv")
for etudiant in Etudiants:
    print(etudiant)
'''

print(Etudiant("DUPONT", 8, Date("01/01/2000")).adresselec())
print(Etudiant("DUPONT", '', Date("01/01/2000")).adresselec())

