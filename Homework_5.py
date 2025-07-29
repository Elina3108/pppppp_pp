
import pandas as pd 

# Задание 1
orders = pd.read_csv('orders_new.csv', sep=',',encoding='utf-8')
users = pd.read_csv('users_new.csv', sep=',',encoding='utf-8')
merged1 = users.merge(orders, on='user_id', how='left')
mask = (merged1['region'] == 'North') & (merged1['age'] < 30)
filtered_orders_loc = merged1.loc[mask]
print(filtered_orders_loc.groupby('name')['quantity'].sum())

# Задание 2
orders['total'] = orders['quantity'] *  orders['price']
filted_orders = orders.query('product == "C" and total > 250' )
print(filted_orders)

# Задание 3
print(orders['product'].value_counts())

# Задание 4
merged1['total'] = merged1['quantity'] *  merged1['price']
data_pivot = merged1.pivot_table(index= 'region', columns= 'product', values = 'total')
print(data_pivot)

# Задание 5

rouped_by_name =merged1.groupby("name")["order_id"].count().reset_index(name='orders_count')
mask_1 = (rouped_by_name['orders_count'] > 1)
filtered_orders_loc_1 = rouped_by_name.loc[mask_1]
print(filtered_orders_loc_1)