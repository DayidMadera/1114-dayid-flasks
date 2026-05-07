
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

if __name__ == "__main__":

    app.run(debug=True)
