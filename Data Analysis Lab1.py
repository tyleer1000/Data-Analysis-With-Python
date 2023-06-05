import pandas as pd
import numpy as np 

data = pd.read_csv('imports-85.data')

print(data.head(6))

print(data.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

data.columns = headers
print(data.head(10))

data1=data.replace('?',np.NaN)

data=data1.dropna(subset=["price"], axis=0)
print(data.head(20))

print(data.describe(include = "all"))

print(data[['length', 'compression-ratio']].describe())

print(data.info)