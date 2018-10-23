# Store_Manager_API


This API  allows admins to create accounts, login, create products and view all products and sales made by the store attendants. It also allows store attendants to login their accounts and view products available, make sale orders and view sale orders they have made. 

##  Features or Endpoints required 
       
Endpoint | Functionality
-------- | -------------
GET /products | Fetch all products
GET /products/<productId> | Fetch a single product record
GET /sales | Fetch all sale records
GET /sales/<saleId> | Fetch a single sale record
POST /products | Create a product
POST /sales | Create a sale order

##  Prerequisites
* Flask framework

##  Technologies 
* Python 3.6.0

##  Requirements
* Setup a virtual environment (venv)
* `pip install -r requirements.txt`

##  Run the application
Run python app.py in vscode terminal
* The index  page of the app can be found on  http://127.0.0.1:5000/
* Test the end points of the app with postman

## Import the unittest library in the test file
* import Unittest
* write tests
* Run pytest on command prompt to see if the tests are passing. In case of any failure then refactor the code and be sure the tests run successfully
