import codecademylib
import pandas as pd
#load the data
inventory = pd.read_csv('inventory.csv')

#inspect the first 10 rows
print(inventory.head(10))

#The first 10 rows represent data from your Staten Island location. Select these rows and save them to staten_island.
staten_island = inventory.head(10)

#A customer just emailed you asking what products are sold at your Staten Island location. Select the column product_description from staten_island and save it to the variable product_request.
product_request = staten_island.product_description

 #Another customer emails to ask what types of seeds are sold at the Brooklyn location.Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request.

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

 #Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
inventory['in_stock'] = inventory.apply(lambda row : True if row.quantity > 0 else False, axis=1)

 #Petal Power wants to know how valuable their current inventory is.Create a column called total_value that is equal to price multiplied by quantity.
inventory['total_value'] = inventory.price * inventory.quantity 

#Using combine_lambda, create a new column in inventory called full_description that has the complete description of each product.
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1)                     

