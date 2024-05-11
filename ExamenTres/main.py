from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/notas', methods=['GET', 'POST'])
def calculoNotas():
    if request.method == 'POST':
        try:
            numero1 = int(request.form['nota1'])
            numero2 = int(request.form['nota2'])
            numero3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            if all(10<= num <= 70 for num in [numero1, numero2, numero3]) and 0<= asistencia <= 100:
                resultado1 = round((numero1 + numero2 + numero3) / 3, 1)
                if resultado1 >= 40 and asistencia >= 75:
                    mensaje_estado = 'APROBADO'
                else:
                    mensaje_estado = 'REPROBADO'
                return render_template('notas.html', resultado1=resultado1, numero1=numero1,
                               numero2=numero2, numero3=numero3, asistencia=asistencia, mensaje_estado=mensaje_estado)
            else:
                mensaje_error = 'Ingrese números entre 10 y 70 para las notas, y entre 0 y 100 para la asistencia.'
                return render_template('notas.html', mensaje_error=mensaje_error)
        except ValueError:
            mensaje_error = 'Por favor, ingrese números válidos.'
            return render_template('notas.html', mensaje_error=mensaje_error)
    return render_template('notas.html')

@app.route('/nombres', methods=['GET', 'POST'])
def nombre():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        if len(set([nombre1, nombre2, nombre3])) != 3:
            mensaje_error = "Por favor ingrese tres nombres diferentes."
            return render_template('nombres.html', mensaje_error=mensaje_error)

        largo_nombre1 = len(nombre1)
        largo_nombre2 = len(nombre2)
        largo_nombre3 = len(nombre3)

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)
        return render_template('nombres.html', nombre1=nombre1, nombre2=nombre2,
                               nombre3=nombre3, nombre_mas_largo=nombre_mas_largo, longitud=longitud)
    return render_template('nombres.html')

if __name__ == '__main__':
    app.run(debug=True)