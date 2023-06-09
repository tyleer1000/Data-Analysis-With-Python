import pandas as pd 

data =pd.read_csv('Sample - Superstore.csv')

#print order ID of sales > 500 

#filter_df = data[data['Sales' ] > 500 ] 
#print(filter_df[['Order ID', 'Sales']])

inner_join = pd.merge(data,data, on=['Order ID', 'Sales'], how='inner')
print(inner_join)

