import os
import braintree
import sys
sys.path.append('..')


gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        environment='sandbox',
        merchant_id='',
        public_key='',
        private_key=''
    )
)

def generate_client_token():
    return gateway.client_token.generate()

def transact(options):
    return gateway.transaction.sale(options)

def find_transaction(id):
    return gateway.transaction.find(id)

def find_customer(id):
    return gateway.customer.find(id)

def create_subscripton(options):
    return gateway.subscription.create(options)

def cancel_subscription(id):
    return gateway.subscription.cancel(id)

def create_payment(options):
    return gateway.payment_method.create(options)

def create_customer(options):
    return gateway.customer.create(options)

def search_customers(options):
    return gateway.customer.search(options)

def delete_customer(customer_id):
    return gateway.customer.delete()



# from app import app
#
# app.secret_key = os.environ.get('APP_SECRET_KEY')