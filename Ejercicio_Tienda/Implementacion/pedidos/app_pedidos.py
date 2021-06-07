from flask import Flask, url_for, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.db'
app.config['SECRET_KEY'] = "123"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)


class pedido(db.Model):
    id = db.Column("product_id", db.Integer, primary_key = True)
    pedido_nombre = db.Column(db.String(100))
    pedido_valor = db.Column(db.Integer)
    pedido_cantidad = db.Column(db.Integer)
    pedido_estado = db.Column(db.String(100))

    def __init__(self, datos):
        self.pedido_nombre = datos["nombrePedido"]
        self.pedido_valor = datos["cantidadPedido"]
        self.pedido_cantidad = datos["valorPedido"]
        self.pedido_estado = datos["estadoPedido"]

@app.route("/")
@cross_origin()
def principal():
    data = pedido.query.all()
    diccionario_pedidos = {}
    for d in data:
        p = {"id":d.id,
        "nombrePedido": d.pedido_nombre,
        "cantidadPedido": d.pedido_valor,
        "valorPedido": d.pedido_cantidad,
        "estadoPedido": d.pedido_estado,
            }
        diccionario_pedidos[d.id] = p
    return diccionario_pedidos


@app.route("/agregar/<nombrePedido>/<cantidadPedido>/<valorPedido>/<estadoPedido>")
@cross_origin()
def agregar(nombrePedido,cantidadPedido,valorPedido,estadoPedido):
    datos = {
        "nombrePedido": nombrePedido,
        "cantidadPedido": cantidadPedido,
        "valorPedido": valorPedido,
        "estadoPedido": estadoPedido,
    }
    p = pedido(datos)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('principal'))


@app.route("/eliminar/<int:id>")
@cross_origin()
def eliminar(id):
    p = pedido.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/actualizar/<int:id>/<nombrePedido>/<cantidadPedido>/<valorPedido>/<estadoPedido>")
@cross_origin()
def actualizar(id,nombrePedido,cantidadPedido,valorPedido,estadoPedido):
    p = pedido.query.filter_by (id = id).first()
    p.pedido_nombre = nombrePedido
    p.pedido_valor = valorPedido
    p.pedido_cantidad = cantidadPedido
    p.pedido_estado = estadoPedido
    db.session.commit()
    return redirect(url_for('principal'))

@app.route("/buscar/<int:id>")
@cross_origin()
def buscar(id):
    d = pedido.query.filter_by(id=id).first()
    p = {"id": d.id,
    "nombre": d.pedido_nombre,
    "cantidad": d.pedido_cantidad,
    "valor": d.pedido_valor,
    "estado": d.pedido_estado
    }
    return p

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)