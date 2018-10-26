import unittest
from api.views import app
from flask import json
from api.models import User


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        "Sets up the application configuration"

        self.test_client = app.test_client()

    def test_if_product_data_is_empty(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.post('/api/v1/products', content_type='application/json',
                                             data=json.dumps(dict()))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please all fields should be filled',
                          responseJson['message'])

    def test_if_product_name_is_empty(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.post('/api/v1/products', content_type='application/json',
                                             data=json.dumps(dict(product_name="",
                                                                  product_category="Dress",
                                                                  product_price="25dollars")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please the name is required',
                          responseJson['message'])

    def test_if_product_category_is_empty(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.post('/api/v1/products', content_type='application/json',
                                             data=json.dumps(dict(product_name="Short sleeved dress",
                                                                  product_category="",
                                                                  product_price="25dollars")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please fill in the category',
                          responseJson['message'])

    def test_if_product_price_is_empty(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.post('/api/v1/products', content_type='application/json',
                                             data=json.dumps(dict(product_name="Short sleeved dress",
                                                                  product_category="Dress",
                                                                  product_price="")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please the price is required',
                          responseJson['message'])

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

    def test_create_a_sale_method_requires_attendant_role(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict(attendant_name="Jamie",
                                                                  product_name="Jungle boots",
                                                                  product_category="shoes",
                                                                  product_price="50dollars")))
            self.assertEqual(response.status_code, 201)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Sale order created successfully.',
                          responseJson['message'])

    def test_get_all_sales_requires_admin_role(self):
        with self.test_client:
            User.user_role = 'admin'
            response = self.test_client.get('/api/v1/sales', content_type='application/json',
                                            data=json.dumps(dict(attendant_name="Jamie",
                                                                 product_name="Jungle boots",
                                                                 product_category="shoes",
                                                                 product_price="50dollars")))
            self.assertEqual(response.status_code, 200)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Jamie', responseJson[0]['attendant_name'])

    def test_get_a_sale(self):
        with self.test_client:
            response = self.test_client.get('/api/v1/sales/1', content_type='application/json',
                                            data=json.dumps(dict(attendant_name="Jamie",
                                                                 product_name="Jungle boots",
                                                                 product_category="shoes",
                                                                 product_price="50dollars")))
            self.assertEqual(response.status_code, 200)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Jamie', responseJson['attendant_name'])

    def test_if_sale_data_is_empty(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict()))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please all fields should be filled',
                          responseJson['message'])

    def test_if_attendant_name_is_empty(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict(attendant_name="",
                                                                  product_name="Jungle boots",
                                                                  product_category="shoes",
                                                                  product_price="50dollars")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please attendant name is required',
                          responseJson['message'])

    def test_if_product_sales_name_is_empty(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict(attendant_name="Jamie",
                                                                  product_name="",
                                                                  product_category="shoes",
                                                                  product_price="50dollars")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please product name is required',
                          responseJson['message'])

    def test_if_product_sales_category_is_empty(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict(attendant_name="Jamie",
                                                                  product_name="Jungle boots",
                                                                  product_category="",
                                                                  product_price="50dollars")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please fill in the product category',
                          responseJson['message'])

    def test_if_product_sales_price_is_empty(self):
        with self.test_client:
            User.user_role = 'attendant'
            response = self.test_client.post('/api/v1/sales', content_type='application/json',
                                             data=json.dumps(dict(attendant_name="Jamie",
                                                                  product_name="Jungle boots",
                                                                  product_category="Shoes",
                                                                  product_price="")))
            self.assertEqual(response.status_code, 400)
            responseJson = json.loads(response.data.decode())
            self.assertIn('Please the price is required',
                          responseJson['message'])

    def tearDown(self):
        pass
