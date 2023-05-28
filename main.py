# -*- coding: utf-8 -*-
import os
from wsgiref.simple_server import make_server

import falcon

from db_connection import MongoConnect

# connect db

MongoConnect.connect_to_db()


# Define your Falcon resource
class MyResource:
    def on_get(self, req, resp):
        # Handle GET request
        resp.media = {'message': 'Hello, Falcon with Mongoengine!'}


# Create a Falcon API instance
app = falcon.App()
if __name__ == '__main__':
    with make_server('', int(os.environ['RUNNING_PORT']), app) as httpd:
        print('Serving on port' + os.environ['RUNNING_PORT'])

# Add your resource to the API
app.add_route('/', MyResource())
