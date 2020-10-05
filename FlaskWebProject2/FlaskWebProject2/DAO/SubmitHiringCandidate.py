import pymysql
from FlaskWebProject2 import app, mysql
from flask import render_template, redirect, flash, request
from FlaskWebProject2.Utils.RandomGeneration import get_candidate_id

conn = mysql.connect()
cursor = conn.cursor()
def submitHiringCandidate(Firstname, Lastname, EmailID, Contact_Number, Visa_Status, College_Name1, College_Name2, Technology, StartDate, EndDate, Vendor_Name, Client_Name, Job_Location, dollarRate_per_hour):
    sql = "INSERT INTO USERS (candidate_id, Firstname, Lastname, EmailID, Contact_Number, Visa_Status, College_Name1, College_Name2, Technology, StartDate, EndDate, Vendor_Name, Client_Name, Job_Location, dollarRate_per_hour)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    args = (get_candidate_id(), Firstname, Lastname, EmailID, Contact_Number, Visa_Status, College_Name1, College_Name2, Technology, StartDate, EndDate, Vendor_Name, Client_Name, Job_Location, dollarRate_per_hour)

    try:
        cursor.execute(sql, args)
    except mysql.connector.Error as err:
        print(error)
    finally:
        cursor.close()
        conn.close()
