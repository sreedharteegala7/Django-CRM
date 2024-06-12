import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="sreedhar",
    passwd="Sree!104",
)


# prepare cursor object
cursorObject = dataBase.cursor()

# create the databse
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!!")
