#install mySQL
#pip install mysql
#pip install mysql connector
#pip install mysql connector_python

import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mAs27121995@@'
)
#prepare a cusor object
cursorObject = dataBase.cursor()