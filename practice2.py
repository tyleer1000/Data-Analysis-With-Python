"""
What is the average mark of kids in class 3?
Approach: 
Read in the file, filter by class 3, then get average

What is the % of males in the school? 
Approach: 
First see how many genders there are, then get count of males, then get a %

What are the names of the students with marks above 80? 
First filter df such that it only has rows where marks > 80. 
Then, create list of the names in that filtered df

What is the class with the highest average mark? 
Get list of all classes
Group students by class
Calculate average in each class 
Then, find which value in largest
Return that class 

In the original df, sort by highest mark. 

Who is the student with the second highest mark?
First, sort by highest marks descending. 
Then create sorted list of names, 
Then return second value in that list

What is the percentage of students with marks greater than or equal to 60? 
First, find total # of students with marks >= 60
Then, compare that # to the total # of students to calc. percentage

Return all the students with name Julia and Joss

exam_passing
Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15.
Filter for attempts less than 2 
Filter for score > 15 
Return that filtered result

exam_sorting
Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
Sort first by name desc
Then by score asc

exam_clean
Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.

same data
Convert null data to 0 and convert all names to lowercase. 
swap null with 0
make names lowerscase

insert_column
Write a Pandas program to insert a new column in existing DataFrame.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

group_by
Write a Pandas program to split the following dataframe into groups based on school code. Also check the type of GroupBy object.

Get the average % mark by gender
Group by gender, then calculate avg for each, then print each df

purchase_min_max
Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. 
Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) 
group by customer id (customer_id).


"""

import pandas as pd
import numpy as np

def class3_avg():
        
    data = pd.read_csv("student.csv")


    class3 = data[data['class']== 'Three'].set_index('id')

    print(class3['name'].to_list())

def get_males_avg():
    data = pd.read_csv("student.csv")
    gender_list = data.drop_duplicates('gender')
    gender_list2 = gender_list['gender'].to_list()
    #print(gender_list2)
    result = list()
    for gender in gender_list2:
        count = data[data['gender']== gender].count()
        result.append((gender, count['gender']))
    total = 0
    total_males = 0
    for value in result:
        total += value[1]
        if value[0] == 'male':
            total_males = value[1]

    percent_males = (total_males/total)*100
    print(percent_males)

def names_over_80():
    data = pd.read_csv("student.csv")
    data_over_80 = data[data['mark'] > 80]
    names_list = data_over_80['name'].to_list()

    return names_list

def highest_avg():
    data = pd.read_csv('student.csv')
    grouped_data = data.groupby('class')['mark'].mean()

    return (grouped_data.sort_values(ascending= False), grouped_data.idxmax())

def sorted_by_marks():
    data = pd.read_csv('student.csv')
    data_sorted = data.sort_values(by = 'mark', ascending=False)
    return data_sorted.head(5)

def second_highest_mark():
    data = pd.read_csv('student.csv')
    sorted_data_names = data.sort_values(by = 'mark', ascending=False)

    #returns from 1 to 2. Not inclusive of 3. 
    #return sorted_data_names.iloc[0:8]

    #return second highest value
    return sorted_data_names.iloc[1]

def percent_passed():
    data = pd.read_csv('student.csv')
    passed_data = data[data['mark'] >= 60]
    total_passed = len(passed_data)
    total = len(data)
    percentage_pass = ((total_passed/total) * 100)

    return str(round(percentage_pass, 2)) + '%'

def Julia_Joss():
    data = pd.read_csv('student.csv')
    #data_filtered = data[data['name'].isin(['Julia', 'Joss', 'John Mike'])]
    data_filtered = data[data['name'].str.contains('John')]

    return data_filtered

def exam_passing():
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b']
            
    data = pd.DataFrame(exam_data)
    data_attempts = data[(data['attempts'] < 2) & (data['score'] > 15)]
    #data_score = data_attempts[data_attempts['score'] > 15]
    print(data_attempts)
    # can use pipe | for or

def exam_sorting():

    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd']

    data = pd.DataFrame(exam_data)
    data_name_desc = data.sort_values(['name', 'score'], ascending= [False, True])
    #print(data_name_desc)

    #data_score_asc = data_name_desc.sort_values('score', ascending= True)
    print(data_name_desc)

def exam_clean():

    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e']
              
    data = pd.DataFrame(exam_data)
    data['qualify'] = data['qualify'].map({'yes': True, 'no': False})
    print(data)


def lowercase_null():

    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e']

    data = pd.DataFrame(exam_data)
    data['score'] = data['score'].fillna(0)
    data['name'] = data['name'].str.lower()
    print(data)

def insert_column():

    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    data = pd.DataFrame(exam_data)

    #data['student_id'] = [1,2,3,4,5,6,7,8,9,10]
    data.insert(0, 'student_id', [1,2,3,4,5,6,7,8,9,10])
    print(data)

def group_by_school():
    
    student_data = pd.DataFrame({
        'school_code': ['s001','s002','s003','s001','s002','s004'],
        'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
        'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
        'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
        'age': [12, 12, 13, 13, 14, 12],
        'height': [173, 192, 186, 167, 151, 159],
        'weight': [35, 32, 33, 30, 31, 32],
        'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
        index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])
    
    #creates four new dataframes, so we need for loop to print each one
    data = student_data.groupby(['school_code'])
    print(data)
    print('Grouping')
    for name, group in data:
        print (group)
        print('\n')

def avg_by_gender():
    data = pd.read_csv('student.csv')
    gender_groups = data.groupby('gender')
    for gender, groups in gender_groups:
        print(gender, groups['mark'].mean())

        

def purchase_min_max():

    orders_data = pd.DataFrame({
    'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
    'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45, 75.29,3045.6],
    'ord_date': ['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
    'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
    'salesman_id': [5002,5005,5001,5003,5002,5001,5006,5003,5002,5007,5001, 5010]})

    grouped_data = orders_data.groupby('customer_id')
    for customer, customer_data in grouped_data:
        print('customer_id ' + str(customer), 'mean ' + str(customer_data['purch_amt'].mean()), 'min ' + str(customer_data['purch_amt'].min()), 'max ' + str(customer_data['purch_amt'].max()))
        print('\n')

purchase_min_max()