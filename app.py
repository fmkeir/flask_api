from flask import Flask, request, jsonify
from db import db
from flask_marshmallow import Marshmallow
import os

from models.product import Product

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ma = Marshmallow(app)

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name, description, price, quantity)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

@app.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    return products_schema.jsonify(all_products)

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()

    return product_schema.jsonify(product)

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

@app.route('/', methods =['GET'])
def get():
    return jsonify({'msg': 'hello world!'})

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)