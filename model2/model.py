import mysql.connector

# Replace with your actual credentials (avoid storing sensitive information in code)
DB_NAME = "model"
HOST = "localhost"
USERNAME = "thejokers"
PASSWORD = "sexcigareZ2"

connection = mysql.connector.connect(
    host=HOST,
    user=USERNAME,
    password=PASSWORD,
    database=DB_NAME
)
