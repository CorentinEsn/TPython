import sqlite3 as sql
import pandas as pd
from re import sub


def camel(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


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
            print(str(table[0])[1:-1])
            cur.execute("CREATE TABLE " + name + "(" + camel(attributes) + ")")
        else:
            return -1
    # insert the data
    for line in table[1:]:
        print(str(line)[1:-1])
        cur.execute("INSERT INTO " + name + " VALUES (" + str(line)[1:-1] + ")")
    connect.commit()
    connect.close()


# reads an Excel table and returns a list of lists (table of data)
def readTable(path):
    try:
        # Essayez avec l'encodage latin-1
        df_csv = pd.read_csv(path, sep=';', encoding='latin-1', header=None, skiprows=0)

        # Remplacer les valeurs vides par "/"
        df_csv.fillna("", inplace=True)

        # Convertir le DataFrame en une liste de listes
        tableau_de_tableaux = df_csv.values.tolist() if not df_csv.empty else None
        return tableau_de_tableaux
    except pd.errors.EmptyDataError:
        # Le fichier est vide
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")
        return None


# insert the data into the database
def insertData():
    SQLConnectAndInsert("Communes", readTable("data_Base_de_données/communes.csv"))
    SQLConnectAndInsert("Departements", readTable("data_Base_de_données/departements.csv"))
    SQLConnectAndInsert("Regions", readTable("data_Base_de_données/regions.csv"))


# return the total population of a table
def totalPopulation(table):
    sum = 0
    connect = sql.connect(table + ".db")
    cur = connect.cursor()
    res = cur.execute("SELECT PopulationTotale FROM " + table)
    res = res.fetchall()
    for i in res:
        pop = i[0]
        pop = pop.replace(" ", "")
        sum += int(pop)
    print(table + " total population : " + str(sum))


# Returns list of communes with the same name but different departements
def sameNameDifferentDepartement():
    communes = []
    connect = sql.connect("Communes.db")
    cur = connect.cursor()
    res = cur.execute("SELECT NomDeLaCommune FROM Communes GROUP BY NomDeLaCommune HAVING COUNT(*) > 1")
    res = res.fetchall()
    for i in res:
        communes.append(i[0])
    return communes


# returns commune by name with list of departements of homonyms
def getCommuneByName(name):
    homonymes = []
    connect = sql.connect("Communes.db")
    cur = connect.cursor()
    if "'" in name:
        name = name.replace("'", "''")
    res = cur.execute("SELECT NomDeLaCommune, CodeDépartement FROM Communes WHERE NomDeLaCommune = '" + name + "'")
    res = res.fetchall()
    homonymes.append(res[0][1])
    for i in res:
        if i[1] not in homonymes:
            homonymes.append(i[1])
    print("Homonymes de " + name + " : " + str(homonymes))
    connect.close()


#returns name and departement of homonyms
def getHomonyms():
    list = sameNameDifferentDepartement()
    for i in list:
        getCommuneByName(i)


getHomonyms()
