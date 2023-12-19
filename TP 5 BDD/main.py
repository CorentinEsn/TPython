import sqlite3 as sql
import pandas as pd

# Create a SQL connection to our SQLite database
def SQLConnect():
    sql.connect()


def readTable(path):
    try:
        # Essayez avec l'encodage latin-1
        df_csv = pd.read_csv(path, sep=';', encoding='latin-1', header=None, skiprows=0)

        # Convertir le DataFrame en une liste de listes
        tableau_de_tableaux = df_csv.values.tolist() if not df_csv.empty else None
        return tableau_de_tableaux
    except pd.errors.EmptyDataError:
        # Le fichier est vide
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        return None

# Exemple d'utilisation
file = readTable("data_Base_de_données/regions.csv")
