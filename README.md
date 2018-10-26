# Store_Manager_API
[![Build Status](https://travis-ci.com/Irenyak1/Store-Manager.svg?branch=challenge_2)](https://travis-ci.com/Irenyak1/Store-Manager)
[![Coverage Status](https://coveralls.io/repos/github/Irenyak1/Store-Manager/badge.svg?branch=challenge_2)](https://coveralls.io/github/Irenyak1/Store-Manager?branch=challenge_2)
[![Maintainability](https://api.codeclimate.com/v1/badges/cec49797ac7dd6ce3290/maintainability)](https://codeclimate.com/github/Irenyak1/Store-Manager/maintainability)

This API  allows store owners or admins take proper record of the products they have in the store and what is sold out. While logged in they can be able to create accounts for store attendands, add products to the store stock, view all products in the store and sales made by the store attendants. It also allows store attendants to view products available, make sale orders and view sale orders they have made. 

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
Run  python run.py in vscode terminal
* The index  page of the app can be found on  http://127.0.0.1:5000/
* Test the end points of the app with [postman](https://www.getpostman.com/collections/b755891b1e6fe378ba0a)

## Import the unittest library in the test file
* import Unittest
* Write tests
* Run nosetests  --with-coverage --cover-package=api to see if the tests are passing. In case of any failure then refactor the code and be sure the tests run successfully

## Deployment 
* This App is hosted on [Heroku](https://the-store-manager.herokuapp.com/)


## Author 
Irene Nyakate