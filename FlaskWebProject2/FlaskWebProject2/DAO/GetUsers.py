import pymysql
from FlaskWebProject2 import app, mysql

conn = mysql.connect()
cursor = conn.cursor()
def getUsers():
    cursor.execute("SELECT * FROM USERS")
    return cursor.fetchall()