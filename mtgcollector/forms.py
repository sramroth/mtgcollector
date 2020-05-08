#####################################################################################
# Name: Scott Ramroth
# Class: CS3080 Python Programming
# 
# Description: MTGCollector is a web-based card collection application that utlizes
# open source card pricing data to help collectors keep track of the value of their
# collection. The application is build in Flask and uses SQLAlchemy to manage a
# database.
#####################################################################################

import csv

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, Length

#######################################################
# Forms
#######################################################
class CardForm(FlaskForm):
    search = StringField('Enter the card name exactly as it appears:', validators=[DataRequired(), Length(min=2, max=50)])
    is_foil = RadioField('', choices=[('paper', 'Not Foil'), ('paperFoil', 'Foil')])
    add = SubmitField('Add')

