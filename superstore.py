import pandas as pd 
import sqlite3 as sql

data =pd.read_csv('Sample - Superstore.csv')

return_data = pd.read_csv('returns.csv')

#Show customer names that are not in Second, First, or Standard Class
def exclude_shipping():
    exclusions = ['Second Class', 'First Class', 'Standard Class']
    data_class_filter = data[~data['Ship Mode'].isin(exclusions)]
    print(data_class_filter['Ship Mode'].drop_duplicates())

#show customer names not in california
def exclude_ca():
    exclusions = ['California']
    ca_filter = data[~data['State'].isin(exclusions)]
    print(ca_filter.describe())

#show orderID where Row ID is even. 
def even_orderid():
    data_even = data[data['Row ID'] % 2 ==0]
    print(data_even)

even_orderid()






# data_merged = pd.merge(data, return_data, on=['Order ID'], how ='inner')
# print(data_merged['Sales'].median())



#print order ID of sales > 500 

#filter_df = data[data['Sales' ] > 500 ] 
#print(filter_df[['Order ID', 'Sales']])

#inner_join = pd.merge(data,data, on=['Order ID', 'Sales'], how='inner')
#print(inner_join)

