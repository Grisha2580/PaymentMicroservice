import requests

def post_customer():
    result = requests.post('http://localhost:5000/customers', data={'first_name': 'Daria', 'last_name': 'Zaytseva',
                                                                    'email': 'zaytseva.d@husky.neu.edu'})
    print('The customer id is {}'.format(result))

def delete_customer():
    result = requests.delete('http://localhost:5000/customers/205561079')

    print('Customer was successfully deleted {}'.format(result))


def get_customer():
    result = requests.get('http://localhost:5000/customers/628333063')

    print(result)

def subscribe():
    result = requests.post('http://localhost:5000/subscriptions', data={"token": "ghhbt7",
                                                                         'plan_id': '7zrw'})
    print('The customer has subscribed {}'.format(result))

def unsubscribe():
    result = requests.delete('http://localhost:5000/subscriptions/9yvmsg')

    print(result)



# delete_customer()
# post_customer()
# subscribe()
# unsubscribe()
get_customer()

