"""
What is the average mark of students in Class 3?
"""

import pandas as pd

data = pd.read_csv("student.csv")

#question: do I need to worry about standardized format? Capitalization? 
#print(data.head(5))

#filter rows to only class Three
#data2 = data[data['class'].str.lower().str.contains('three')]

#print(data2.describe())

#print((data2['mark'].mean().round(2)))

print(data.describe())
#Print unique values (set) under gender. Count by gender, then filter by male, then filter by female, see if that adds up, then calc %. 
#35 total. 

genders = data.drop_duplicates(subset='gender')
print(genders)

#females =data[data['gender'].str.lower().str.contains('female')]
#print(females.describe())

#print(genders.head(10))

genders_list = genders['gender'].to_list()
data['gender'].isin(genders_list)
print(data['gender'].isin(genders_list))


totalbygender = dict()
for gender in genders_list:
    print(gender, data['gender'].isin([gender]))
    totalbygender[gender] = data['gender'].isin([gender]).drop_duplicates(subset='True')

print(totalbygender)