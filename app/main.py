import os
import mysql.connector

MARIADB_DATABASE = os.getenv('MARIADB_DATABASE')
MARIADB_USER = os.getenv('MARIADB_USER')
MARIADB_PASSWORD = os.getenv('MARIADB_PASSWORD')
MARIADB_ROOT_PASSWORD = os.getenv('MARIADB_ROOT_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


cnx = mysql.connector.connect(user=MARIADB_USER, password=MARIADB_PASSWORD,
                              host=DB_HOST, database=MARIADB_DATABASE, port=3306)


cursor = cnx.cursor()

query = ("SELECT * FROM tasks")

cursor.execute(query)

for task in cursor:
    print(task)

cursor.close()
cnx.close()
