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

def readTable(path):  # reads a .csv file using pandas and returns the table
    return
