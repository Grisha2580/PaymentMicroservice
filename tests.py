import requests

def post_customer():
    result = requests.post('http://localhost:5000/customers', data={'first_name': 'Daria', 'last_name': 'Zaytseva',
                                                                    'email': 'zaytseva.d@husky.neu.edu'})
    print('The customer id is {}'.format(result))

def delete_customer():
    result = requests.delete('http://localhost:5000/customers', data={'customer_id': 205561079})

    print('Customer was successfully deleted {}'.format(result))



delete_customer()




