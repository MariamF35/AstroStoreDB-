import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",  ##TYPE YOUR PASSWORD
        database="astrostoredb"
    )
    return conn
