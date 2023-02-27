from flask import Flask, render_template, request 
from operaciones import Operaciones
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms

app = Flask(__name__)

app.config['SECRET_KEY']="Esta es una clave de encriptacion"
csrf=CSRFProtect()


@app.route("/cookies", methods=["GET","POST"])
def cookies():
    reg_user=forms.LoginForm(request.form)
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data 
        passw=reg_user.password.data
        datos=user+'@'+passw
        response.set_cookies('datos_user', datos)


    response=make_response(render_template('cookies.html',form=reg_user))
    return render_template('cookies.html', form=reg_user)



@app.route('/formulario2', methods=["GET"])
def formulario2():
    return render_template("formulario2.html")



@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    alumn_form=forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method=='POST' and alumn_form.validate():
        mat=alumn_form.matricula.data
        nom=alumn_form.nombre.data
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data
    return render_template('alumnos.html', forms=alumn_form, mat=mat, nom=nom)


# @app.route('/formularioAct', methods=['POST'])
# def formularioAct():
#     #num_form=forms2.UserForm(request.form)
#     #if request.method=='POST':
#     #print(num_form.numero.data)
#     num_inputs = int(request.form['num_inputs'])
#     return render_template('Actividad1-Parcial2.html',  form=num_form, num=num)


@app.route('/forma', methods=['GET', 'POST'])
def forma():
    num_inputs = 0
    VerFormulario = False
    if (request.method=='POST') and (request.form.get('num_inputs')):
        VerFormulario = True
        num_inputs= int(request.form.get('num_inputs'))
    return render_template("crear_inputs.html", VerFormulario = VerFormulario, num_inputs=num_inputs )

@app.route('/operas', methods=['POST'])
def operas():
    operaciones = Operaciones(request.form)
    return render_template('operaciones.html',
                        minimo = operaciones.minimo(),
                        maximo = operaciones.maximo(),
                        promedio = operaciones.promedio(),
                        masRep = operaciones.masRep()
                        )

@app.route('/traducir', methods=['GET'])
def traducir():
    valor_input = ""
    # valor_input= request.form.get('pingles')
    valor_input = request.args.get('pingles')
    return render_template('resultado.html', valor_input=valor_input)

    return render_template("traductor.html")








@app.route('/consultar', methods=['GET','POST'])
def consultar():
    #tomar le valor de un radiobuton 
    word=request.form['pingles']
    radio=request.form['palabra']
    if request.method == 'POST': 
        if radio == 'espanol':
            with open('diccionario.txt') as f:
                for line in f:
                    parts = line.strip().split('=')
                    if parts[0] == word:
                        translation = parts[1]
                        print("No selecciono el correcto")
                        return render_template('traductor.html', translation=translation)
                #     return render_template('translate.html', error='No se encontró la traducción para la palabra "{}".'.format(word))  
                # return render_template('translate.html')
        elif radio == 'ingles':
            with open('diccionario.txt', 'r') as archivo:
                contenido = archivo.read()
            lineas = contenido.splitlines()
            indice_renglon = -1
                #translation = []
            for i, linea in enumerate(lineas):
                if word in linea:
                    indice_renglon = i
                    break
            if indice_renglon != -1:
                translation = lineas[indice_renglon].split("=")[0].strip()
                #translation.append(palabra)

        #             #palabra = linea.split("=")[0].strip() 
        #             #translation.append(palabra)
            return render_template('Actividad2.html', translation=translation)






@app.route('/guardars', methods=['GET', 'POST'])
def guardars():
    datos = {}
    base = request.form['base']       
    basen = request.form['basen']
    if request.method == 'POST':
        
        datos[basen] = {'basen': basen, 'base': base}
        # Aquí se guarda el diccionario en un archivo txt
        with open('diccionario.txt', 'a') as archivo:
            archivo.write(basen + '=' + base + '\n')

    return render_template('exito.html')
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)
