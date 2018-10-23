from flask import Flask, request, jsonify, make_response
import datetime
import jwt
from api.models import User, Product, Sale
from functools import wraps


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    my_response = "Welcome to the store of abundance."
    return jsonify(my_response), 200


@app.route('/auth/login', methods=['POST'])
def login():
    user_data = request.get_json()
    # get login data from user
    name = user_data.get('username')
    password = user_data.get('password')
    role = user_data.get('role')

    user = User(name, password, role)
    login_result = user.login() 

    if login_result:
        return jsonify('Welcome {}'.format(login_result))
    return jsonify('No such credentials found.') 

  
@app.route('/auth/signup', methods=['POST'])
def sign_up():
    return user.sign_up()

# @app.route('/api/v1/users', methods=['GET'])
# def get_all_users():
#     return user.get_all_users()


@app.route('/api/v1/products', methods=['POST'])
def create_a_product():
    product_data = request.get_json()
    # get product data
    product_name = product_data.get('product_name')
    product_category = product_data.get('product_category')
    product_price = product_data.get('product_price')

    user = User(name, password, role)
    login_result = user.login() 

    if login_result:
        return jsonify('Welcome {}'.format(login_result))
    return jsonify('No such credentials found.') 

    
                

    # return product.create_a_product()


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    return product.get_all_products()


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_a_product(product_id):
    return product.get_a_product()


@app.route('/api/v1/sales', methods=['POST'])
def create_a_sale():
    return sale.create_a_sale()


@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    return sale.get_all_sales()

@app.route('/api/v1/users/sales/<int:sale_id>', methods=['GET'])
def get_a_sale(sale_id):
    return sale.get_a_sale(sale_id)


# @app.route('/api/v1/users/sales/<int:sale_id>', methods=['DELETE'])
# def delete_a_sale(sale_id):
#     for sale in sales:
#         if sale.sale_id == sale_id:
#     sale = [sale for sale in sales if sale["id"] == sale_id]
#     sales.remove(sale)

#     return jsonify('Sucessfully deleted'), 200
