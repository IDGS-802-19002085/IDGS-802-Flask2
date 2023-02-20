from flask import Flask, render_template, request 
from operaciones import Operaciones
from flask import request
import forms

app = Flask(__name__)

@app.route('/formulario2', methods=["GET"])
def formulario2():
    return render_template("formulario2.html")


@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    alumn_form=forms.userForm(request.form)
    mat = ''
    nom = ''
    if request.method=='POST':
        print(alumn_form.matricula.data)
        print(alumn_form.nombre.data)
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data
    return render_template('alumnos.html', form=alumn_form, mat=mat, nom=nom)


@app.route('/formularioAct', methods=['POST'])
def formularioAct():
    #num_form=forms2.UserForm(request.form)
    #if request.method=='POST':
    #print(num_form.numero.data)
    num_inputs = int(request.form['num_inputs'])
    return render_template('Actividad1-Parcial2.html',  form=num_form, num=num)



# @app.route('/forma', methods=['GET', 'POST'])
# def forma():
#     num_inputs = 0
#     # no_form = forms.userForm(request.form)
#     showForm = False
#     if (request.form.get('num_inputs')): 
#         showForm = True
#         num_inputs= int(request.form.get('num_inputs'))
#     return render_template("crear_inputs.html", showForm = showForm, num_inputs=num_inputs )


@app.route('/forma', methods=['GET', 'POST'])
def forma():
    num_inputs = 0
    showForm = False
    if (request.method=='POST') and (request.form.get('num_inputs')):
        showForm = True
        num_inputs= int(request.form.get('num_inputs'))
    return render_template("crear_inputs.html", showForm = showForm, num_inputs=num_inputs )


@app.route('/operas', methods=['POST'])
def operas():
    operaciones = Operaciones(request.form)
    return render_template('operaciones.html',
                        minimo = operaciones.minimo(),
                        maximo = operaciones.maximo(),
                        promedio = operaciones.promedio(),
                        masRep = operaciones.masRep()
                        )



@app.route('/genera', methods=[ 'POST'])
def genera():
    if request.method == 'POST':
        num_fields = int(request.form['num_fields'])
        fields = {}
        for i in range(num_fields):
            field_name = 'field{}'.format(i+1)
            fields[field_name] = request.form.get(field_name, '')
        # procesar campos adicionales
        return 'Campos adicionales: {}'.format(fields)
    else:
        return render_template('formulario.html')



if __name__ == "__main__":
    app.run(debug=True, port=3000)
