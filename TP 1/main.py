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
        with open(filename, "at") as fic:
            # Ajout du texte
            print("Texte à ajouter :")
            text = input("> ")
            fic.write(text + "/n")

        # Affichage du contenu du fichier
        print("Le fichier contient le texte suivant :")
        with open(filename, "r") as fic:
            print(fic.read())

        # Vider le fichier
        with open(filename, "wt"):
            pass

    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("Opération terminée.")

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
