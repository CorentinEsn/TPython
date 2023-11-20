# This is a sample Python script.
import datetime

from Date import Date
from Etudiant import Etudiant


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def HelloWorld():
    # Use a breakpoint in the code line below to debug your script.
    print("Bonjour le monde !")  # Press Ctrl+F8 to toggle the breakpoint.


def OpenandAppendFile():
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


def NewEtudiantsFromCSV(filename):
    etudiants = []
    fic = open(filename, "r")
    for line in fic:
        line = line.strip()
        line = line.split(";")
        etudiants.append(Etudiant(line[0], line[1], Date((line[2]))))
    fic.close()
    return etudiants

# NewEtudiantsFromCSV("C:/Users/coren/OneDrive/Documents/Polytech/Cours/5a/S9/Python/fichetu.csv")


anniv1 = Date("07/06/2000")
print(anniv1)