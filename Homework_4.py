# Задание 1
import pandas as pd 
df = pd.read_csv('group_orders.csv', sep=',', encoding='utf-8')
group_city = df.groupby('city')['order_id'].count()
print(group_city)

# Задание 2
group_city_1 = df.groupby('city')['total'].mean()
print(group_city_1)

# Задание 3
top_product = df.groupby('product')['quantity'].sum()
print(top_product.sort_values( ascending = False).head(1))

# Задание 4
df['order_date'] = pd.to_datetime(df['order_date'])
df['order_mounth'] = df['order_date'].dt.month
month_group =  df.groupby('order_mounth')['total'].sum()
print(month_group)

# Задание 5
group_city_2 = df.groupby('city')['total'].mean().sort_values(ascending = False)
print((group_city_2).head(3))