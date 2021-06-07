from flask import Flask, url_for, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domiciliarios.db'
app.config['SECRET_KEY'] = "123"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)


class domiciliarios(db.Model):
    id = db.Column("domiciliario_id", db.Integer, primary_key = True)
    domiciliario_nombre = db.Column(db.String(100))
    domiciliario_apellido = db.Column(db.String(100))
    domiciliario_cedula = db.Column(db.String(100))
    domiciliario_placa = db.Column(db.String(100))
    domiciliario_vehiculo  = db.Column(db.String(100))

    def __init__(self, datos):
        self.domiciliario_nombre = datos["nombre"]
        self.domiciliario_apellido = datos["apellido"]
        self.domiciliario_cedula = datos["cedula"]
        self.domiciliario_placa = datos["placa"]
        self.domiciliario_vehiculo = datos["vehiculo"]

@app.route("/")
@cross_origin()
def principal():
    data = domiciliarios.query.all()
    diccionario_domiciliarios = {}
    for c in data:
        p = {"id": c.id,
        "nombre": c.domiciliario_nombre,
        "apellido": c.domiciliario_apellido,
        "cedula": c.domiciliario_cedula,
        "placa": c.domiciliario_placa,
        "vehiculo": c.domiciliario_vehiculo
        }
        diccionario_domiciliarios[c.id]= p
    return diccionario_domiciliarios

@app.route("/agregar/<nombre>/<apellido>/<cedula>/<placa>/<vehiculo>")
@cross_origin()
def agregar(nombre, apellido, cedula, placa, vehiculo):
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "placa": placa,
        "vehiculo": vehiculo}
    p = domiciliarios(datos)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/eliminar/<int:id>")
@cross_origin()
def eliminar(id):
    p = domiciliarios.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/actualizar/<int:id>/<nombre>/<apellido>/<cedula>/<placa>/<vehiculo>")
@cross_origin()
def actualizar(id, nombre, apellido, cedula, placa, vehiculo):
    c = domiciliarios.query.filter_by(id=id).first()
    c.domiciliario_nombre = nombre
    c.domiciliario_apellido= apellido
    c.domiciliario_cedula = cedula
    c.domiciliario_placa = placa
    c.domiciliario_vehiculo = vehiculo
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/buscar/<int:id>")
@cross_origin()
def buscar(id):
    d = domiciliarios.query.filter_by(id=id).first()
    p = {"id": d.id,
        "nombre": d.domiciliario_nombre,
        "apellido": d.domiciliario_apellido,
        "cedula": d.domiciliario_cedula,
        "placa": d.domiciliario_placa,
        "vehiculo": d.domiciliario_vehiculo
        }
    return p


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)