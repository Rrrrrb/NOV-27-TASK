import mysql.connector
from mysql.connector import error
try:
    connection=mysql.connector.connect(        #cursor=mysql.connector.connect().cursor()
        host="local host",
        database="database name",
        user="user name",
        password="pasword"
    )
    if connection.is_connected():
        print("connected to database, successfully")
        cursor=connection.cursor()
        result=cursor.execute("SQL command")
        print(result)
except error as e:
    print("error! while fetching database")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("database connection is closed.")




    