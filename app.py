from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "clave-secreta-super-segura-1114"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    programa = db.Column(db.String(50), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<Estudiante {self.nombre}>'

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

@app.route("/inscripcion", methods=["GET", "POST"])
def inscripcion():
    mensaje = None
    
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        programa = request.form.get("programa")
        
        # Validacion
        if not nombre or not email or not programa:
            mensaje = "Por favor completa todos los campos."
        else:
            try:
                # Crear nuevo estudiante
                nuevo_estudiante = Estudiante(
                    nombre=nombre,
                    email=email,
                    programa=programa
                )
                
                # Guardar en BD
                db.session.add(nuevo_estudiante)
                db.session.commit()
                
                mensaje = f"Bienvenido {nombre}! Te hemos registrado."
            except Exception as e:
                db.session.rollback()
                mensaje = f"Error: Este email ya esta registrado."
    
    return render_template("inscripcion.html", mensaje=mensaje)


@app.route("/login", methods=["GET", "POST"])
def login():

    mensaje = None

    if request.method == "POST":

        usuario = request.form.get("usuario")
        contraseña = request.form.get("contraseña")

        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and user.verificar_contraseña(contraseña):

            session['usuario_id'] = user.id
            session['usuario_nombre'] = user.usuario
            session['rol'] = user.rol

            if user.rol == "profesor":
                return redirect(url_for("panel_profesor"))

            else:
                return redirect(url_for("panel_estudiante"))

        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template("login.html", mensaje=mensaje)

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("inicio"))

@app.route("/estudiantes")
def estudiantes():

    if 'rol' not in session or session['rol'] != 'profesor':
        return redirect(url_for("login"))

    lista_estudiantes = Estudiante.query.all()

    return render_template(
        "estudiantes.html",
        estudiantes=lista_estudiantes
    )

@app.route("/panel-profesor")
def panel_profesor():

    if 'usuario_id' not in session or session['rol'] != 'profesor':
        return redirect(url_for("login"))

    return render_template(
        "panel_profesor.html",
        usuario=session['usuario_nombre']
    )

@app.route("/panel_estudiante")
def panel_estudiante():

    if 'usuario_id' not in session or session['rol'] != 'estudiante':
        return redirect(url_for("login"))

    return render_template(
        "panel_estudiante.html",
        usuario=session['usuario_nombre']
    )

from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # "profesor" o "estudiante"

    def establecer_contraseña(self, contraseña):
        self.contraseña = generate_password_hash(contraseña)

    def verificar_contraseña(self, contraseña):
        return check_password_hash(self.contraseña, contraseña)

    def __repr__(self):
        return f'<Usuario {self.usuario}>'



if __name__ == "__main__":

    app.run(debug=True)
