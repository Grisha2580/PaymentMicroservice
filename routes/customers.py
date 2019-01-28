import sys

sys.path.append('..')

from flask_restful import Resource, reqparse
from config.local_config import create_customer, delete_customer, find_customer

customer_args_parser = reqparse.RequestParser()
customer_args_parser.add_argument('first_name')
customer_args_parser.add_argument('last_name')
customer_args_parser.add_argument('email')
customer_args_parser.add_argument('customer_id')


class CustomersList(Resource):
    def post(self):
        args = customer_args_parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']
        email = args['email']
        result = create_customer({
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        })

        if result.is_success:
            return {'customer_id': result.customer.id,
                    'last_name': result.customer.last_name,
                    'first_name': result.customer.first_name}
        else:
            return "Failed to create customer due to {}".format(result.error)



class Customer(Resource):
    def get(self, customer_id):
        customer = find_customer(customer_id)

        customer_payment_methods = customer.payment_methods

        info = {
            'subscription': False,
            'payment_methods': []
        }

        for payment_method in customer_payment_methods:
            info['payment_methods'].append(payment_method.payment_method_token())
            paym_subscriptions = payment_method.subscriptions

            for subscription in paym_subscriptions:
                if subscription.status == 'Active':
                    print('here')
                    info['subscription'] = True

        return info


    def delete(self, customer_id):
        delete_customer(customer_id)





