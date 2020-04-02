import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart= pd.merge(visits, cart, how = 'left')
print(len(visits_cart))
print(visits_cart)

null_cart_time = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_cart_time)


checkout_cart = pd.merge(cart,checkout, how='left')
print(checkout_cart)
checkout_cart_rows = len(checkout_cart)
null_checkout_cart = len(checkout_cart[checkout_cart.checkout_time.isnull()])
print(float(null_checkout_cart) / checkout_cart_rows)

all_data = visits.merge(cart, how='left')
                 .merge(check_out, how='left')
                 .merge(purchase,how= 'left')
print(all_data.head())
