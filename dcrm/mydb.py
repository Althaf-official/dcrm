#install mySQL
#pip install mysql
#pip install mysql connector
#pip install mysql connector_python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mAs27121995@@',
    database = '127.0.0.1'
)
#prepare a cusor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE mascollection")
print("Database is All Done")