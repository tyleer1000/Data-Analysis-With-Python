import sqlite3
import pandas as pd

#conn = sqlite3.connect('hw3.db')
#query = "SELECT name FROM sqlite_master WHERE type='table'"

# data = pd.read_sql_query(query, conn)
# print(data.head(5))
# query2 ="SELECT * FROM games"

datagames = pd.read_sql_query(query2, conn)
# print(datagames.head(4))

#give names of games where avgscore is higher than 7

def score_over_7():
    """
    filter games on avgscore over 7
    """
    filtered_datagames = datagames[datagames['avgscore'] >7]
    print(filtered_datagames.head(5))


def highest_designer():
    """
    What are the designers where avgscore is over 7?

    Triple inner join on games, desgame, designers 
    """
    conn = sqlite3.connect('hw3.db')
    query = ("SELECT name FROM sqlite_master WHERE type='table'")
    data_tables = pd.read_sql_query(query, conn)
    print(data_tables.head(5))
    query2 = "SELECT * FROM games"
    query3 = "SELECT * FROM desgame"
    query4 = "SELECT * FROM designers"

    data_games = pd.read_sql_query(query2, conn)
    data_desgame = pd.read_sql_query(query3, conn)
    data_designers = pd.read_sql_query(query4, conn)

    data_games_desgame = pd.merge(data_games, data_desgame, on='g_id', how='inner')
    data_games_desgame_designer = pd.merge(data_games_desgame, data_designers, on='des_id', how='inner')

    filtered_data = data_games_desgame_designer[data_games_desgame_designer['avgscore'] > 7]
    unique_designers = filtered_data.drop_duplicates('designer')
    print(unique_designers['designer'])

highest_designer()