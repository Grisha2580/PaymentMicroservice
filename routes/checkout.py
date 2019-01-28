from flask import Flask, redirect, url_for, render_template, request, flash
import sys
sys.path.append('..')
import os
from os.path import join, dirname
import braintree
from config.local_config import generate_client_token,\
    transact, find_transaction, create_payment, find_customer, cancel_subscription
from flask_restful import Resource


class Checkout(Resource):
    def get(self):
        client_token = generate_client_token()
        return render_template('checkouts/new.html', client_token=client_token)


class PaymentMethods(Resource):
    def post(self):
        customer_id = request.form['customer_id']
        payment_method_nonce = request.form['payment_method_nonce']
        result = create_payment({
            'customer_id': customer_id,
            'payment_method_nonce': payment_method_nonce
        })

        if result.is_success:
            return "Customer {} has created a new payment method".format(customer_id)
            # return redirect(url_for('show_checkout', transaction_id=customer_id))
        else:
            for x in result.errors.deep_errors:
                flash('Error: %s: %s' % (x.code, x.message))

            return redirect(url_for('payment_info'))

    def delete(self, subscription_id):
        result = cancel_subscription(subscription_id)

        if result.is_success:
            return 'Your subscription is successfully canceled'
        else:
            return 'Something went wrong canceling your subscription'
