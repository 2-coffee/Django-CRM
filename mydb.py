'''
script to make a database
'''

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass12345'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")