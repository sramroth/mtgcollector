#####################################################################################
# Name: Scott Ramroth
# Class: CS3080 Python Programming
# 
# Description: MTGCollector is a web-based card collection application that utlizes
# open source card pricing data to help collectors keep track of the value of their
# collection. The application is build in Flask and uses SQLAlchemy to manage a
# database.
#####################################################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app and identify the database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'its a secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from mtgcollector import views