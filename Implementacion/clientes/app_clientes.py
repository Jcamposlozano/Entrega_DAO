from flask import Flask, url_for, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['SECRET_KEY'] = "123"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)


class cliente(db.Model):
    id = db.Column("cliente_id", db.Integer, primary_key = True)
    cliente_nombre = db.Column(db.String(100))
    cliente_apellido = db.Column(db.String(100))
    cliente_cedula = db.Column(db.String(100))
    cliente_direccion = db.Column(db.String(100))
    cliente_telefono  = db.Column(db.String(100))

    def __init__(self, datos):
        self.cliente_nombre = datos["nombre"]
        self.cliente_apellido = datos["apellido"]
        self.cliente_cedula = datos["cedula"]
        self.cliente_direccion = datos["direccion"]
        self.cliente_telefono = datos["telefono"]

@app.route("/")
@cross_origin()
def principal():
    data = cliente.query.all()
    diccionario_clientes = {}
    for c in data:
        p = {"id": c.id,
        "nombre": c.cliente_nombre,
        "apellido": c.cliente_apellido,
        "cedula": c.cliente_cedula,
        "direccion": c.cliente_direccion,
        "telefono": c.cliente_telefono
        }
        diccionario_clientes[c.id]= p
    return diccionario_clientes

@app.route("/agregar/<nombre>/<apellido>/<cedula>/<direccion>/<telefono>")
@cross_origin()
def agregar(nombre, apellido, cedula, direccion, telefono):
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "cedula": cedula,
        "direccion": direccion,
        "telefono": telefono}
    p = cliente(datos)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/eliminar/<int:id>")
@cross_origin()
def eliminar(id):
    p = cliente.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/actualizar/<int:id>/<nombre>/<apellido>/<cedula>/<direccion>/<telefono>")
@cross_origin()
def actualizar(id, nombre, apellido, cedula, direccion, telefono):
    c = cliente.query.filter_by(id=id).first()
    c.cliente_nombre = nombre
    c.cliente_apellido= apellido
    c.cliente_cedula = cedula
    c.cliente_direccion = direccion
    c.cliente_telefono = telefono
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/buscar/<int:id>")
@cross_origin()
def buscar(id):
    d = cliente.query.filter_by(id=id).first()
    p = {"id": d.id,
        "nombre": d.cliente_nombre,
        "apellido": d.cliente_apellido,
        "cedula": d.cliente_cedula,
        "direccion": d.cliente_direccion,
        "telefono": d.cliente_telefono
        }
    return p


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)