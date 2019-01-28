from flask import Flask
from flask_restful import Api
import sys
sys.path.append('..')
from routes.checkout import Checkout, PaymentMethod, PaymentMethodsList
from routes.subscriptions import Subscription, SubscriptionList
from routes.customers import Customer, CustomersList



app = Flask(__name__, template_folder='templates')
api = Api(app)

def add_payments_api():
    api.add_resource(Checkout, '/checkouts/new')
    api.add_resource(PaymentMethod, '/payment_methods/<payment_token>')
    api.add_resource(PaymentMethodsList, '/payment_methods/')

def add_customers_api():
    api.add_resource(Customer, '/customers/<customer_id>')
    api.add_resource(CustomersList, '/customers')


def add_subscriptions_api():
    api.add_resource(Subscription, '/subscriptions/<subscription_id>')
    api.add_resource(SubscriptionList, '/subscriptions')

def add_apis():
    add_payments_api()
    add_customers_api()
    add_subscriptions_api()


if __name__ == '__main__':
    add_apis()
    app.run(debug=True)
