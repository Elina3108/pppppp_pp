# Задание 1
import pandas as pd 
orders = pd.read_csv('orders.csv', sep=',',encoding='utf-8')
customers = pd.read_csv('customers.csv', sep=',',encoding='utf-8')
contacts = pd.read_csv('contacts.csv', sep=',',encoding='utf-8')

merged1 = customers.merge(orders, on='customer_id', how='left')
merged_df = merged1.merge(contacts, on='customer_id', how='inner')

european_countries = ["Russia", "France", "Germany", "Spain", "Italy", "UK"]
merged_df['order_date']= pd.to_datetime(merged_df['order_date'],errors='coerce')

mask = (merged_df['country'].isin(european_countries)) & (merged_df['order_date'] >= '2023-01-01') & (merged_df['order_date'] < '2023-07-01')

filtered_sales_loc = merged_df.loc[mask, ['order_id', 'total']]
total_sales = filtered_sales_loc['total'].sum()

print(filtered_sales_loc)
print("Сумма отобранных продаж:", total_sales)

#Задание 2
merged_df['registration_date']= pd.to_datetime(merged_df['registration_date'],errors='coerce')

filtered_sales = merged_df.query('registration_date >= "2022-01-01" and order_date >= "2023-01-01" and order_date < "2024-01-01" and total > 30000')
result = filtered_sales[['first_name', 'last_name','total']]
count_sales = result.shape[0]

print(result)
print("Количество продаж:", count_sales)

# Задание 3
mask_2 =  merged_df.query('order_date >= "2022-01-01" and order_date < "2024-01-01"')
print(mask_2['gender'].value_counts(normalize=False))


