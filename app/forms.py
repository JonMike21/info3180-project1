from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import  FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()]) 
    description = TextAreaField('Description', validators=[InputRequired()])
    bedroomNum = StringField('No. of Rooms', validators=[InputRequired()])
    bathroomNum = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Type',  choices=[('apartment', 'Apartment'), ('house', 'House')])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png','jpeg'], 'Images only!')])