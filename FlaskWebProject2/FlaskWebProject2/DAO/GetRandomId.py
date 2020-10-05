import pymysql
from FlaskWebProject2 import app, mysql

conn = mysql.connect()
cursor = conn.cursor()
def getRandomId(str,id):
    print("SELECT " + str + "_id from " + str + "s where " + str + "_id='" + id + "';")
    cursor.execute("SELECT " + str + "_id from " + str + "s where " + str + "_id='" + id + "';")
    return cursor.fetchall()
