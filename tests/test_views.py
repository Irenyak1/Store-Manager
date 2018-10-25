import unittest
from api.views import app
from flask import json
from api.models import User


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        "Sets up the application configuration"

        self.test_client = app.test_client()

    # def test_if_product_data_is_empty(self):
    #     with self.test_client:
    #         User.user_role = 'admin'
    #         response = self.test_client.post('/api/v1/products', content_type='application/json',
    #                             data=json.dumps(dict(product_name= "",
    #                                                 product_category= "",
    #                                                 product_price= "")))
    #         self.assertEqual(response.status_code, 400)
    #         responseJson = json.loads(response.data.decode())
    #         self.assertIn('Please all fields should be filled', responseJson['message'])

    def test_create_a_product_method_requires_admin_role(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.post('/api/v1/products', content_type='application/json',
                                             data=json.dumps(dict(product_name="sleevless dress",
                                                                  product_category="dress",
                                                                  product_price="30dollars")))
            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Product succesfully created.',
                          responseJson['message'])

    def test_get_all_products(self):
        with self.test_client:
            response = self.test_client.get('/api/v1/products', content_type='application/json',
                                            data=json.dumps(dict(product_name="sleevless dress",
                                                                 product_category="dress",
                                                                 product_price="30dollars")))
            self.assertEqual(response.status_code, 200)
            responseJson = json.loads(response.data.decode())
            self.assertIn('sleevless dress', responseJson[0]['product_name'])
    
    def test_get_a_product_by_id(self):
        with self.test_client:
            response = self.test_client.get('/api/v1/products/1', content_type='application/json',
                                            data=json.dumps(dict(product_name="sleevless dress",
                                                                 product_category="dress",
                                                                 product_price="30dollars")))
            self.assertEqual(response.status_code, 200)
            responseJson = json.loads(response.data.decode())
            self.assertIn('sleevless dress', responseJson['product_name'])
    
    

    def tearDown(self):
        pass
