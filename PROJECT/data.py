import mysql.connector
def db_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amma@16",
    database="HOSPITALDB"
)

print("connect succesflly")

