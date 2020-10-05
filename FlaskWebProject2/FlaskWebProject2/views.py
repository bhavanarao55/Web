"""
Routes and views for the flask application.
"""
import pymysql
from FlaskWebProject2 import app, mysql
from FlaskWebProject2.ModelBuilders.UsersMB import UsersMB
from FlaskWebProject2.ModelBuilders.TasksMB import TasksMB
from FlaskWebProject2.ModelBuilders.CandidatesMB import CandidatesMB
from FlaskWebProject2.DAO.SubmitEntry import submitEntry
from FlaskWebProject2.DAO.SubmitPlacedCandidate import submitPlacedCandidate
from FlaskWebProject2.DAO.SubmitHiringCandidate import submitHiringCandidate
from flask import render_template, redirect, flash, request


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/hiring', methods=['GET'])
def hiring():
    return render_template('hiring.html')

@app.route('/marketing', methods=['GET'])
def marketing():
    return render_template('marketing.html', users=UsersMB().getUsersModel())

@app.route('/onboarding1', methods=['GET'])
def onboarding():
    return render_template('onboarding.html', users=UsersMB().getUsersModel())

@app.route('/task', methods=['GET'])
def task():
    user_id = request.args.get('userid')
    return render_template('task.html', tasks=TasksMB().getTasksModel(user_id))

@app.route('/candidate', methods=['GET'])
def candidate():
    return render_template('placedCandidates.html', candidates=CandidatesMB().getCandidatesModel())

@app.route('/submitEntry', methods=['POST'])
def Entry():
    submitEntry(task_id = request.form['task_id'],
                name =  request.form['name'],
                task = request.form['task'],
                details = request.form['task'],
                technology = request.form['technology'],
                source = request.form['source'],
                link = request.form['link'],
                time = request.form['time'],
                notes = request.form['notes'])
    return "success"

@app.route('/submitPlacedCandidate', methods=['GET'])
def Placed():
    submitPlacedCandidate(Firstname = request.args.get('Firstname'),
                Lastname = request.args.get('Lastname'),
                EmailID = request.args.get('EmailID'),
                Contact_Number = request.args.get('Contact_Number'),
                Visa_Status = request.args.get('Visa_Status'),
                College_Name1 = request.args.get('College_Name1'),
                College_Name2 = request.args.get('College_Name2'),
                Technology = request.args.get('Technology'),
                StartDate = request.args.get('StartDate'),
                EndDate = request.args.get('EndDate'),
                Vendor_Name = request.args.get('Vendor_Name'),
                Client_Name = request.args.get('Client_Name'),
                Job_Location = request.args.get('Job_Location'),
                dollarRate_per_hour = request.args.get('dollarRate_per_hour'))
    return "success"

@app.route('/submitHiringCandidate', methods=['GET'])
def Hiring():
    submitHiringCandidate(Firstname =  request.form['Firstname'],
                Lastname = request.form['Lastname'],
                EmailID = request.form['EmailID'],
                Contact_Number = request.form['Contact_Number'],
                Visa_Status = request.form['Visa_Status'],
                College_Name1 = request.form['College_Name1'],
                College_Name2 = request.form['College_Name2'],
                Technology = request.form['Technology'],
                StartDate = request.form['StartDate'],
                EndDate = request.form['EndDate'],
                Vendor_Name = request.form['Vendor_Name'],
                Client_Name = request.form['Client_Name'],
                Job_Location = request.form['Job_Location'],
                dollarRate_per_hour = request.form['dollarRate_per_hour'])
    return "success"
