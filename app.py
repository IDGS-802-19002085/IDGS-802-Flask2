from flask import Flask, render_template, request
import forms as form
from calcular import Calcular

app = Flask(__name__)

@app.route('/formulario2', methods=['GET'])
def formulario2():
  return render_template('formulario2.html')

@app.route('/alumnos', methods=['GET', 'POST'])
def alumno():
  alumn_form=form.UserForm(request.form)
  mat = ''
  nom = ''
  if request.method == 'POST':
    mat=alumn_form.matricula.data
    nom=alumn_form.nombre.data
  return render_template('alumnos.html', form = alumn_form, mat = mat, nom = nom)

@app.route('/multinputs', methods=['GET', 'POST'])
def multinputs():
  showForm = False
  nInputs = 0
  
  if (request.form.get('numero')):
    showForm = True
    nInputs = int(request.form.get('numero'))

  return render_template('multinputs.jinja', showForm = showForm, nInputs = nInputs)

@app.route('/calcular', methods=['POST'])
def calcular():
  calc = Calcular(request.form)
  return render_template('calcular.jinja',
                        minimo = calc.minimo(),
                        maximo = calc.maximo(),
                        promedio = calc.promedio(),
                        masRep = calc.masRep()
                        )


if __name__ == '__main__':
  app.run(debug=True, port=8000)