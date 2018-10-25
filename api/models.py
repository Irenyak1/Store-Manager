from flask import Flask, request, jsonify, make_response

""" A global variable called USERS """
USERS = [{"username": "admin", "password": "admin", "role": "admin"},
         {"username": "irynah", "password": "goose", "role": "attendant"}]


class User:
    """
    This class defines the user in terms of
    the username, password and role.
    """

    user_role = ""

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def login(self):
        """ This method allows the user to login after cross checking their 
        username, password and role
        """
        for user in USERS:
            if user['username'] == self.username and user['password'] == self.password and user['role'] == self.role:
                User.user_role = self.role
        return self.user_role


class Product:
    
    """
    This class defines the product in terms of its
    name, category and price.
    """

    PRODUCTS = []
    """
    This is a list that will store all the products 
    that will be  created.
    """
    

    def __init__(self, product_name, product_category, product_price):
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price

    def create_a_product(self):
        """ This method allows the admin to create a product. 
        It also generates the Id of the product automatically 
        """
        if User.user_role == 'admin':
            my_products = dict
            if not Product.PRODUCTS:
                product_id = 1
        else:
            product_id = Product.PRODUCTS[-1].get('product_id') + 1

        self.my_products = {
            'product_id': product_id,
            'product_name': self.product_name,
            'product_category': self.product_category,
            'product_price': self.product_price
        }
        """ The created product is appended to the dictionary """
        Product.PRODUCTS.append(self.my_products)

        return 'Product successfully created.'

    def get_all_products(self):
        """ This method is used to fetch all created products in the dictionary """ 
        if len(Products.PRODUCTS) >= 1:
            return (Products.PRODUCTS)

        return 'There are no products in the store'

    def get_a_product(self, product_id):
        """ This method is used to fetch a single product from the 
        dictionary using the id of the product
        """
        for my_product in Product.PRODUCTS:
            if my_product.get('id') == product_id:
                return my_product

        return 'There is no such product in the store.'


class Sale:
    """
    This class defines a sale order in terms of
    attendant_name, product_name, product_category, product_price.
    """
    

    SALES = []
    """
    This is a list that will store all the sales 
    that will be  created.
    """

    def __init__(self, attendant_name, product_name, product_category, product_price):
        self.attendant_name = attendant_name
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price

    def create_a_sale(self):
        """ This method allows the attendant to create a sale. 
            It also generates the Id of the sale automatically 
        """
        if User.user_role == 'attendant':
            my_sales = dict
            if not Sale.SALES:
                sale_id = 1
        else:
            sale_id = Sale.SALES[-1].get('sale_id') + 1

        self.my_sales = {
            'sale_id': sale_id,
            'attendant_name': self.attendant_name,
            'product_name': self.product_name,
            'product_category': self.product_category,
            'product_price': self.product_price
        }

        Sale.SALES.append(self.my_sales)

        return 'Sale order created successfully.'

    def get_all_sales(self):
        """ This method is used to fetch all created sales in the dictionary """ 
        if len(Sale.SALES) >= 1:
            return (Sale.SALES)

        return 'There are no sale orders yet'

    def get_a_sale(self, sale_id):
        """ This method is used to fetch a single sale from the 
            dictionary using the id of the sale
        """
        for my_sale in Sale.SALES:
            if my_sale.get('sale_id') == sale_id:
                return my_sale

        return 'Sale Not Found.'
