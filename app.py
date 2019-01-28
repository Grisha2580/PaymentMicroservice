from flask import Flask
from flask_restful import Api
import sys
sys.path.append('..')
from routes.checkout import Checkout, PaymentMethods
from routes.subscriptions import Subscriptions
from routes.customers import Customers



app = Flask(__name__)



api = Api(app)

def add_payments_api():
    api.add_resource(Checkout, '/payment_info')
    api.add_resource(PaymentMethods, '/payment_methods')

def add_cusotmers_api():
    api.add_resource(Customers, '/customers')


def add_subscriptions_api():
    api.add_resource(Subscriptions, '/subscriptions')

def add_apis():
    add_payments_api()
    add_cusotmers_api()
    add_subscriptions_api()


if __name__ == '__main__':
    add_apis()
    app.run(debug=True)
