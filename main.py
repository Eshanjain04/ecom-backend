# -*- coding: utf-8 -*-
import os
from wsgiref.simple_server import make_server

import falcon

from db_connection import MongoConnect
from email_generator.email_generator import EMAILService
from Product.view.category import CategoryManager
from Product.view.product import ProductManager
from User.views.login import Login
from User.views.register_user import RegisterUser

# connect db

MongoConnect.connect_to_db()

# Create a Falcon API instance
app = falcon.App()
if __name__ == '__main__':
    with make_server('', int(os.environ['RUNNING_PORT']), app) as httpd:
        print('Serving on port' + os.environ['RUNNING_PORT'])

# Add your resource to the API
app.add_route('/user/register/', RegisterUser())
app.add_route('/user/login/', Login())
app.add_route('/category/add/', CategoryManager())
app.add_route('/category/list/', CategoryManager())
app.add_route('/product/add/', ProductManager())
app.add_route('/product/list/', ProductManager())
app.add_route('/generate-email/', EMAILService())
