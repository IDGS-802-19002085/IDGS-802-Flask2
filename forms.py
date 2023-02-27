from wtforms import Form 
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField,SubmitField, FieldList, FormField, SelectField, RadioField, SearchField
from wtforms.fields import EmailField, TextAreaField, PasswordField 
from wtforms import validators 
from wtforms.validators import DataRequired

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
  matricula=StringField('matricula', [validators.DataRequired(message='La matricula es obligatoria.')])
  nombre=StringField('nombre', [validators.DataRequired(message='el campo es requerido')])
  apaterno=StringField('apaterno')
  email=EmailField('correo')


class numForm(Form):
    numero=StringField('numero')
    num_inputs = IntegerField('Número de campos')




class LoginForm(Form):
    username=StringField('matricula', [validators.DataRequired(message='La matricula es obligatoria.')])
    password=StringField('contrasenña', [validators.DataRequired(message='La matricula es obligatoria.')] )
