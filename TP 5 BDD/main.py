import os
import sqlite3 as sql
import pandas as pd
from re import sub
import xml.etree.ElementTree as ET
import sqlite3 as sql


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


import os

import os

import os


import os

def sauvegardeXmlFile(fileName, table):
    mode = "a" if os.path.exists(fileName + ".xml") else "w"

    with open(fileName + ".xml", mode, encoding="utf-8") as file:
        if mode == "w":
            file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")


        connect = sql.connect(table + ".db")
        cur = connect.cursor()
        res = cur.execute(f"SELECT * FROM {table}")
        res = res.fetchall()

        # Utiliser pandas pour obtenir les noms des colonnes
        columns = [description[0] for description in cur.description]

        for row in res:
            file.write("\t<" + table + ">\n")
            for col, value in zip(columns, row):
                file.write(f"\t\t\t<{col}>{value}</{col}>\n")
            file.write("\t</" + table + ">\n")

    print("File " + fileName + ".xml updated")



def importFromXmlFile(fileName):
    tree = ET.parse(fileName + ".xml")
    root = tree.getroot()

    for table_element in root:
        table_name = table_element.tag
        table_data = []

        for record_element in table_element:
            record_data = {}
            for field_element in record_element:
                field_name = field_element.tag
                field_value = field_element.text
                record_data[field_name] = field_value

            table_data.append(record_data)

        SQLConnectAndInsert(table_name, table_data)

    print("Data imported from " + fileName + ".xml")


def totalPopulation(table):
    sum = 0
    connect = sql.connect(table+".db")
    cur = connect.cursor()
    res = cur.execute("SELECT PopulationTotale FROM "+table)
    res = res.fetchall()
    for i in res:
        pop = i[0]
        pop = pop.replace(" ", "")
        sum += int(pop)
    print(table+" total population : " + str(sum))

#totalPopulation("Departements")
#totalPopulation("Regions")
insertData()
sauvegardeXmlFile("sauvegardeDatabasesCommunes", "Communes")
sauvegardeXmlFile("sauvegardeDatabasesDepartements", "Departements")
sauvegardeXmlFile("sauvegardeDatabasesRegions", "Regions")

#importFromXmlFile("sauvegardeDatabases")
