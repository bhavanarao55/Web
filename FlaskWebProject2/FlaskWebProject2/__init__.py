"""
The flask application package.
"""

from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bunny55'
app.config['MYSQL_DATABASE_DB'] = 'PROJECT'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

import FlaskWebProject2.views

if __name__ == "__main__":
    app.run()