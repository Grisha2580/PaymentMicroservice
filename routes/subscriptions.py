import sys
sys.path.append('..')
from flask import request
from config.local_config import create_subscripton, cancel_subscription
from flask_restful import Resource, reqparse


subscription_args_parser = reqparse.RequestParser()

subscription_args_parser.add_argument('token')
subscription_args_parser.add_argument('plan_id')


class SubscriptionList(Resource):
    def post(self):
        args = subscription_args_parser.parse_args()
        result = create_subscripton({
            'payment_method_token': args['token'],
            'plan_id': args['plan_id']
        })

        if result.is_success:
            return 'Your subscription was successfully created {}'.format(result)
        else:
            return "Something went wrong, the payment method or the subscription id are invalid"

class Subscription(Resource):
    def delete(self, subscription_id):
        result = cancel_subscription(subscription_id)

        if result.is_success:
            return "Your subscription was successfully canceled"
        else:
            return 'Unable to delete your subscription'




