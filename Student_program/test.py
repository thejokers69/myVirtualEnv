import pymysql

database_connection = pymysql.connect(
    host="localhost", 
    user="thejokers",
    password="sexcigareZ2",
    database="testdb"
)

mycursor = database_connection.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student1 = [("Alex", 24),("bob", 24),("hamza", 24),("dj", 24),("oumaima", 24)]
mycursor.executemany(sqlFormula, student1)

database_connection.commit()