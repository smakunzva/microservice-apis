from flask import Flask
from flask_restx import Api

app = Flask('orders')

app.config['ERROR_INCLUDE_MESSAGE'] = False

api = Api(
    app, version='1.0', title='Orders API',
    description='API for the orders microservice',
)

namespace = api.namespace(
    '', description='Orders operations interface'
)


from app.views.views import *
