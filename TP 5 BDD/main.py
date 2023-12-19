import sqlite3 as sql
import pandas as pd

# Create a SQL connection to our SQLite database
def SQLConnectAndInsert(name, table):
    connect = sql.connect(name + ".db")
    cur = connect.cursor()

    # check if table already exists, else create it
    res = cur.execute("SELECT name FROM sqlite_master WHERE name='" + name + "'")
    res = res.fetchone()
    if res is None:
        print(name + " table does not exist")
        create = input("Do you want to create it ? Y/N : ")
        if create == "Y" or create == "y":
            attributes = str(table[0])[1:-1]  # return list content without []
            cur.execute("CREATE TABLE " + name + "(" + attributes + ")")
        else:
            return -1
    # insert the data
    for line in table[1:]:
        cur.execute("INSERT INTO " +name+" VALUES ("+str(line)[1:-1]+")")
    cur.commit()

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
