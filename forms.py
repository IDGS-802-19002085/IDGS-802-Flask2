from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField,SubmitField, FieldList, FormField, SelectField, RadioField, SearchField
from wtforms.fields import EmailField, TextAreaField, PasswordField 
from wtforms import validators 
from wtforms.validators import DataRequired

class UserForm(Form):
  matricula=StringField('matricula', [validators.DataRequired(message='La matricula es obligatoria.')])
  nombre=StringField('nombre')
  apaterno=StringField('apaterno')
  email=EmailField('correo')


class numForm(Form):
    numero=StringField('numero')
    num_inputs = IntegerField('Número de campos')
