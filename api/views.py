from flask import Flask, request, jsonify, make_response
from api.models import User, Product, Sale


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ Endpoint to get the index page """
    my_response = "Welcome to the store of abundance."
    return jsonify(my_response), 200


@app.route('/auth/login', methods=['POST'])
def login():
    """ Endpoint for a user to login """
    user_data = request.get_json()
    # get login data from user
    name = user_data.get('username')
    password = user_data.get('password')
    role = user_data.get('role')

    user = User(name, password, role)
    login_result = user.login()

    if login_result:
        return jsonify('Welcome {}'.format(login_result)), 200
    return jsonify('No such credentials found.'), 400


@app.route('/api/v1/products', methods=['POST'])
def create_a_product():
    """ Endpoint for the admin to create a product """
    response = {'message': ''}
    if User.user_role == 'admin':
        product_data = request.get_json()
        # get product data
        product_name = product_data.get('product_name')
        product_category = product_data.get('product_category')
        product_price = product_data.get('product_price')
        # validate product data
        if not product_data:
            return jsonify({'message': 'Please all fields should be filled'}), 400

        if product_name == "":
            return jsonify({'message': 'Please the name is required'}), 400

        if product_category == "":
            return jsonify({'message': 'Please fill in the category'}), 400

        if product_price == "":
            return jsonify({'message': 'Please the price is required'}), 400

        new_product = Product(product_name, product_category, product_price)
        result_create_a_product = new_product.create_a_product()

        if result_create_a_product:
            return jsonify({'message': 'Product succesfully created.'}), 201

    return jsonify({"message": "You have no rights to create a product"}), 400


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    """ Endpoint to get all products created by the admin """
    return jsonify(Product.PRODUCTS), 200


@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def get_a_product(product_id):
    """ Endpoint to fetch a single product """
    for product_list in Product.PRODUCTS:
        if product_list['product_id'] == product_id:
            return jsonify(product_list), 200
    return jsonify('There is no such product in the list'), 400


@app.route('/api/v1/sales', methods=['POST'])
def create_a_sale():
    """ Endpoint to create a sale order by the attendant """
    if User.user_role == 'attendant':
        sale_data = request.get_json()
        # get sale data
        attendant_name = sale_data.get('attendant_name')
        product_name = sale_data.get('product_name')
        product_category = sale_data.get('product_category')
        product_price = sale_data.get('product_price')

        # validate sale data
        if not sale_data:
            return jsonify({'message': 'Please all fields should be filled'}), 400

        if attendant_name == "":
            return jsonify({'message': 'Please attendant name is required'}), 400

        if product_name == "":
            return jsonify({'message': 'Please product name is required'}), 400

        if product_category == "":
            return jsonify({'message': 'Please fill in the product category'}), 400

        if product_price == "":
            return jsonify({'message': 'Please the price is required'}), 400

        new_sale = Sale(attendant_name, product_name,
                        product_category, product_price)
        result_create_a_sale = new_sale.create_a_sale()

        if result_create_a_sale:
            return jsonify(result_create_a_sale), 201

        return jsonify({"message": "You have no rights to create a sale order"}), 400


@app.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    """ Endpoint for the admin to get all sale orders entered by the attendants """
    if User.user_role == 'admin':
        return jsonify(Sale.SALES), 200
    return jsonify({"message": "You have no rights to access sales"}), 400


@app.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_a_sale(sale_id):
    """ Endpoint to fetch a single sale order """
    for sale_list in Sale.SALES:
        if sale_list['sale_id'] == sale_id:
            return jsonify(sale_list), 200
    return jsonify('There is no such sale order made'), 400
