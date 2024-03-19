import pandas as pd
import numpy as np


def practice():
    data = pd.read_csv("Student_Marks.csv")

    print(data.head(5))

    print(data.isnull().sum())

    #print(data.describe())
    #print(data['Marks'])

    data_table = data[['Marks']]

    print(data_table)
    print(data_table.head(4))
practice()

#Two types of data structures in Pandas. Series and Table. 
