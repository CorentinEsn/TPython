import sqlite3 as sql
import pandas as pd

# Create a SQL connection to our SQLite database
def SQLConnect():
    sql.connect()

def readTable(path): #reads a .csv file using pandas and returns the table
