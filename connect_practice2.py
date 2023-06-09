import sqlite3
import pandas as pd

conn =sqlite3.connect('hw3.db')
query = "SELECT name FROM sqlite_master WHERE type='table'"

tables = pd.read_sql_query(query, conn)

print(tables.head(5))

def group_by_category():
    """Group games by category
    Inner join on games and gamecat by g_id 
    Inner join on games_gamecat table and categories table on c_id 
    Group combined table by category
    Print tuples of category, dataframe 

    Print categories with top 3 average scores 

    For each category, find the highest maxplayer value, 
    add category, max tuple to list, 
    Sort list by max value

    """

    query2 = "SELECT * FROM games"

    data_games = pd.read_sql_query(query2, conn)
    #print(data_games.head(5))

    query_category = "SELECT * FROM categories"
    data_category = pd.read_sql_query(query_category, conn)
    #print(data_category.head(5))

    query_gamecat = "SELECT * FROM gamecat"
    data_gamecat = pd.read_sql_query(query_gamecat, conn)
    #print(data_gamecat.head(5))

    data_games_gamecat = pd.merge(data_games, data_gamecat, on="g_id", how="inner")
    #print(data_games_gamecat.head(4))

    data_games_gamecat_category = pd.merge(data_games_gamecat, data_category, on='c_id', how='inner')
    #print(data_games_gamecat_category.head(4))

    data_groups = data_games_gamecat_category.groupby('category')
    max_player_list = []
    for category, group in data_groups:
        #print(category,group.head(5))
        max_player_list.append((group['maxplayers'].max(), category))
    sorted_list = sorted(max_player_list, reverse=True)
    print(sorted_list[0:3])


def print_table_list():
    conn= sqlite3.connect('hw3.db')
    query = ("SELECT name FROM sqlite_master where type='table'")
    tables = pd.read_sql_query(query, conn)

    print(tables.head(5))

print_table_list()