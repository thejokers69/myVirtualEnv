from peewee import *
sqlite_db = SqliteDatabase('/path/to/my_db')

mysql_db = MySQLDatabase('my_db', user='thejokers', password='sexcigagreZ2', host='localhost', port ='3306')

pg_db = PostgresqlDatabase('my_db', user='thejokers', password='sexcigagre', host='localhost', port ='5443')