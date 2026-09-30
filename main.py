import csv
import sqlite3
import pandas as pd

db_name = "shipment_database.db"

df = pd.read_csv('data/shipping_data_0.csv')
# print(df.head())

with sqlite3.connect(db_name) as con:
    df.to_sql('shipping_data', con, if_exists="replace")


df_1 = pd.read_csv('data/shipping_data_1.csv')
df_1_grouped = df_1.groupby(['shipment_identifier', 'product', 'on_time']).size().reset_index(name='quantity')
# print(df_1_grouped.head())
df_2 = pd.read_csv('data/shipping_data_2.csv')
# print(df_2.head())

final = pd.merge(df_1_grouped,df_2,on = "shipment_identifier", how = "inner")
with sqlite3.connect(db_name) as con:
    df.to_sql('shipment_products', con, if_exists="replace", index = False)