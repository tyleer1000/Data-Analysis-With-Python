import pandas as pd
import numpy as np

data = pd.read_csv("2.1 2.csv")

data = data.dropna()

#print(data.head(5))

def practice():

    print(data.head(5))

    #print(data.isnull.sum())

    #What Origin has the most number of cars? 

    #print(data['Origin'].value_counts())
    print(data['Origin'].describe())
#practice()

"""
Analyze cars in the Origin of Asia
"""
def only_asia():

    data_asia = data[data['Origin']=='Asia']

    #print(data[data['Origin']=='Asia'].describe())

    print(data_asia['Origin'].value_counts())
    
#only_asia()
    
"""
Cars with Engsize >2.3
"""
def big_cylinders():
    data_eng = data[data['EngineSize'] >2.3]
    print(data_eng.value_counts())
    print(data_eng['EngineSize'].min())
    print(data_eng.describe())

#big_cylinders()

#print(data.iloc[:9,-9:])
#print(data.loc[:,['Make', 'Origin']])

#Two types of data structures in Pandas. Series and Table. 
#to get rid of null values, could use dropna, notnull. 
    
'''Remove commas from invoice and convert to a float so you can perform operations on it. '''

def clean_invoice():

    data['Invoice'] = data['Invoice'].str.replace(",", "")
    data['Invoice'] = data['Invoice'].str.replace("$", "")
    data['Invoice'] = data['Invoice'].astype(float)
    #data['Invoice'] = data['Invoice'] * 2
    data['High Invoice'] = data['Invoice'] > 30000
    filter_data = data[data['Invoice'] > 30000]

    filter_data2 = data[(data['Invoice'] > 30000) & (data['Cylinders'] > 4)]
    #print(data.dtypes)
    #print(data.head(5))
    print(filter_data2.head())

clean_invoice()

