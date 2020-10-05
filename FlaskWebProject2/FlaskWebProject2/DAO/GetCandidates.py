import pymysql
from FlaskWebProject2 import app, mysql

conn = mysql.connect()
cursor = conn.cursor()
def getCandidates():
    cursor.execute("SELECT * FROM CANDIDATES")
    return cursor.fetchall()

import pymysql
from FlaskWebProject2 import app, mysql
from flask import render_template, redirect, flash, request

conn = mysql.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)
def getCandidates():
    cursor.execute("SELECT * FROM CANDIDATES")
    return cursor.fetchall()