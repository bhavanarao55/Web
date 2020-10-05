import pymysql
from FlaskWebProject2 import app, mysql

conn = mysql.connect()
cursor = conn.cursor()
def getTasks(user_id):
    cursor.execute("SELECT * FROM TASKS where user_id='"+user_id+"';")
    return cursor.fetchall()