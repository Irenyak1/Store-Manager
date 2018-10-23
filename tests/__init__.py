import unittest
from app.views import app
from app.models import User, Product, Sale, users, products, sales


class BaseTestCase(unittest.TestCase):
    "Tests base case."

    def setUp(self):
        "Sets up the application configuration"

        self.test_client = app.test_client()
        self.user_data = {
            "user_id": 1,
            "name": "Jamie Jones",
            "username": "sampthon",
            "email": "sampthon@gmail.com",
            "password": "kamukama2",
            "confirmation": "kamukama2"

        }

        self.user_login_data = {
            "username": "Tinah",
            "password": "123456"
        }


        self.product_data = {
            "product_id": 1,
            "product_name":"Sleeveless dress",
            "product_category":"Dress",
            "product_price":"20dollars"
        }

        self.sale_data = {
            "sale_id": 1,
            "attendant_name":"Jasmine",
            "product_name":"Ladies' boots",
            "product_category":"Shoes",
            "product_price":"30dollars"
        }




def tearDown(self):
    pass

if __name__ == "__main__":
    unittest.main()

