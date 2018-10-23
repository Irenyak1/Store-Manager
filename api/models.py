from flask import Flask, request, jsonify, make_response
import datetime
import jwt
from functools import wraps

USERS = [{"username": "admin", "password": "admin", "role": "admin"},
         {"username": "wango", "password": "kabula1", "role": "attendant"}]
           

class User:

    user_role = ""

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def login(self):  
    # validate login data
        for user in USERS:
            if user['username'] == self.username and user['password'] == self.password and user['role'] == self.role:
                User.user_role = self.role
        return self.user_role
       

    def sign_up(self):
        user_data = request.get_json()
        name = str(user_data.get('name')).strip()
        username = str(user_data.get('username')).strip()
        email = user_data.get('email')
        password = user_data.get('password')
        confirmation = user_data.get('confirmation')

        if not user_data:
            return jsonify("Please fill all fields."), 400
        if name == "":
            return jsonify("Please fill this field."), 400
        if username == "":
            return jsonify("Please this field is required."), 400
        if email == "":
            return jsonify("This field can't be empty."), 400
        if password == "":
            return jsonify("Please fill password."), 400
        if confirmation == "":
            return jsonify("Fill password confirmation."), 400
        if len(password) <= 5:
            return jsonify("Password too short."), 400
        for user in users:
            if user['username'] == username and user['password'] == password:
                return jsonify("User already exists."), 400
        user_data['id'] = len(users) + 1
        # store your data to your database
        users.append(user_data)
        return jsonify({"message": f"Hello '{username}' has been signed up"}), 201

    
    def get_all_users(self):
        if len(users) >= 1:
            return jsonify({'users': users}), 200
        else:
            return jsonify({
                "Status": "Failure",
                "Message": "There are no users"}), 404

    # def token_required(self, func):
    #     @wraps(func)
    #     def decorated(*args, **kwargs):
    #         token = None
    #         if "Authorization" in request.headers:
    #             token = request.headers['Authorization']
    #         else:
    #             return jsonify({'message': 'No token'}), 401
    #         try:
    #             data = jwt.decode(token, self.key)
    #             # current_user = self.search_list(data['user']['username'])
    #         except:
    #             return jsonify({'message': 'Access denied'}), 401
    #         return func(current_user, *args, **kwargs)
    #     return decorated


class Product:
    def __init__(self, product_name, product_category, product_price, product_id):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
        self.product_id = product_id

    def create_a_product(self):
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

        #     product_data['id'] = len(products) + 1
        #     # store your data to your database
        #     products.append(product_data)

        #     return jsonify({"message": "Hello you have created a product!"}), 201
        # else:
        #     return jsonify ({"message": "You have no rights to access this section"})

    def get_all_products(self):
        if len(products) >= 1:
            return jsonify({'products': products}), 200
        else:
            return jsonify({
                "Status": "Failure",
                "Message": "There are no products in the store"}), 404

    def get_a_product(self, product_id):
        for each_product in products:
            if each_product.get('id') == product_id:
                return jsonify({'product': each_product})
        return jsonify({'error': 'There is no such product in the store'}), 404


products = []


class Sale:
    # def __init__(self, attendant_name, product_name, product_category, product_price, sale_id):
    #     self.attendant_name = attendant_name
    #     self.product_name = product_name
    #     self.product_category = product_category
    #     self.product_price = product_price
    #     self.sale_id = sale_id

    def create_a_sale(self):
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

        sale_data['id'] = len(sales) + 1
        # store your data to your database
        sales.append(sale_data)

        return jsonify({"message": f"Hey '{attendant_name}' it's a sale!"}), 201

    def get_all_sales(self):
        if len(sales) >= 1:
            return jsonify({'sales': sales}), 200
        else:
            return jsonify({
                "Status": "Failure",
                "Message": "You have no sales yet"}), 404

    def get_a_sale(self, sale_id):
        for each_sale in sales:
            if each_sale.get('id') == sale_id:
                return jsonify({'sale': each_sale})

        return jsonify({'error': 'Sale Not Found'}), 404


sales = []
