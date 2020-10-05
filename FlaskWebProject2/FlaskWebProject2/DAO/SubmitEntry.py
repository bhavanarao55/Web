import pymysql
from FlaskWebProject2 import app, mysql
from flask import render_template, redirect, flash, request
from FlaskWebProject2.Utils.RandomGeneration import get_task_id

conn = mysql.connect()
cursor = conn.cursor()
def submitEntry(name, task, details, technology, source, link, time, notes):
    sql = "INSERT INTO TASKS (task_id, name, task, details, technology, source, link, time, notes)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = (get_task_id(), name, task, details, technology, source, link, time, notes)

    try:
        cursor.execute(sql, args)
    except mysql.connector.Error as err:
        print(error)
    finally:
        cursor.close()
        conn.close()
