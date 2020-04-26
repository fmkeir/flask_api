from flask import Flask, jsonify
import os
from db import db

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from controllers.product_controller import products

app.register_blueprint(products, url_prefix='/products')

@app.route('/', methods =['GET'])
def get():
    return jsonify({'msg': 'hello world!'})

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)