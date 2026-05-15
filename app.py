
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/chao")
def chao(): 
    return render_template("chao.html")


@app.route("/hola")
def hola(): 
    return render_template("hola.html")


@app.route("/css")
def css():
    return render_template("css.html")

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/recursos')
def recursos():

    recursos = ["Documentación oficial de Flask","Curso de Python","Repositorio de GitHub","Tutorial de HTML y CSS"]
    return render_template(
        'recursos.html',
        recursos=recursos
    )


if __name__ == "__main__":

    app.run(debug=True)
