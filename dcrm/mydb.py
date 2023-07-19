#install mySQL
#pip install mysql
#pip install mysql connector
#pip install mysql connector_python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mAs27121995@@',
)
#prepare a cusor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE MUHAMMED")
print("All Done")