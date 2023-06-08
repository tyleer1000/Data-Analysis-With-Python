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


"""

import pandas as pd
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

print(Julia_Joss())
