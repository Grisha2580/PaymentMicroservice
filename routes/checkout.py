from flask import Flask, redirect, url_for, render_template, request, flash, make_response
import sys
sys.path.append('..')

from config.local_config import generate_client_token, create_payment, delete_payment_method
from flask_restful import Resource


class Checkout(Resource):
    def get(self):
        client_token = generate_client_token()
        headers = {'Content-type':'text/html'}
        return make_response(render_template('checkouts/new.html', client_token=client_token), 200, headers)


class PaymentMethodsList(Resource):
    def post(self):
        customer_id = request.form['customer_id']
        payment_method_nonce = request.form['payment_method_nonce']
        result = create_payment({
            'customer_id': customer_id,
            'payment_method_nonce': payment_method_nonce
        })

        if result.is_success:
            return "Customer {} has created a new payment method".format(customer_id)
        else:
            for x in result.errors.deep_errors:
                flash('Error: %s: %s' % (x.code, x.message))

            return redirect(url_for('payment_info'))


class PaymentMethod(Resource):
    def delete(self, payment_token):
        result = delete_payment_method(payment_token)

        if result.is_success:
            return 'Your subscription is successfully canceled'
        else:
            return 'Something went wrong canceling your subscription'
