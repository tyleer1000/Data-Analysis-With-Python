"""
Find the orders between Feb 2014 and Feb 2016
First, access data column and covert to_datetime
Then create start and end dates
Then filter for between those dates

Give all orders (just order ID) where the ship date is less than 3 days of the order date 
First, convert order date and ship date to_datetime 
then filter for ship date minus order date is between 2 and 0
return order ID

Find total profit
Sum column profit 

Which state had the least profit? 
Group rows by state
Find sum of each state's profit
Find min value of profit in the list of state's profits

What are the top three states by profit? 
group rows by state
find sum of each state's profit
sort states by profit descending
return top 3

Which state had the most orders returned?
read in both csvs. 
Make a new df with an inner join on both csvs. 
Then group by state
Then return group with most rows 

Return all states with no returns
Make a list of all states in data 
Inner join csvs
Make list of states in inner join 
Return states in first list not in second list 

Or: do left join with returns as left data

What is the avg difference between ship date and order date on items that were returned? 
Inner join both sets 
Convert ship date and order date into dt
Find days between ship date and order date for all orders
Add days between to list, 
Get average of list

"""

import pandas as pd
from datetime import datetime

data = pd.read_csv('Sample - Superstore.csv')
data_returns = pd.read_csv('returns.csv')

def feb_data_filter():
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    start_date = '2014-02-01'
    end_date = '2016-02-01'
    feb_data = data[(data['Order Date'] >= start_date) & (data['Order Date'] <= end_date)]
    print(feb_data)

def three_day_shipping():
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    data['Ship Date'] = pd.to_datetime(data['Ship Date'])
    three_day_data = data[(data['Ship Date'] - data['Order Date']).dt.days < 3]
    print(three_day_data)

def total_profit():
    print(data['Profit'].sum())

def worst_state():
    #returns a tuple. First item is State (name we're filtering on), 2nd item is new dataframe
    #unpacking in python
    grouped_data = data.groupby('State')
    min = 900000000
    lowest_state = ''
    for state, group in grouped_data:
        state_profits = group['Profit'].sum()
        if state_profits < min:
            min = state_profits
            lowest_state = state

    return lowest_state

def top_three_state_profits():


    #create list of tuples (Profit, State)
    state_profit_list = []
    grouped_states = data.groupby('State')
    for state, group in grouped_states:
        state_profit = group['Profit'].sum()
        state_profit_list.append((state_profit, state))
    sorted_state_profit_list = sorted(state_profit_list, reverse=True)
    print(sorted_state_profit_list[48])

def most_state_returns():
    #length, state
    state_length_list = []
    data_with_returns = pd.merge(data, data_returns, on='Order ID', how="inner")
    grouped_states = data_with_returns.groupby('State')
    for state, group in grouped_states:
        state_length_list.append((len(group), state))
    sorted_state_list = sorted(state_length_list, reverse=True)
    for count, state in sorted_state_list [0:3]:
        print(state)

def states_no_returns():
    state_return_data = pd.merge(data_returns, data, on='Order ID', how='right')
    states_without_returns = state_return_data[state_return_data['Returned'].isna()]
    print(states_without_returns.head(5))

def avg_ship_after_order():
    days_between = []
    merged_data = pd.merge(data, data_returns, on="Order ID", how='inner')
    merged_data['Order Date'] = pd.to_datetime(merged_data['Order Date'])
    merged_data['Ship Date'] = pd.to_datetime(merged_data['Ship Date'])
    for order in merged_data:
        day_dif = (merged_data['Ship Date'] - merged_data['Order Date']).dt.days
        days_between= day_dif.tolist()
    avg = sum(days_between)/len(days_between)
    print(avg)

avg_ship_after_order()

