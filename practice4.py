import pandas as pd 
import psycopg2


try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host="::1",
        port="5432",
        database="postgres",
        user="postgres",
        password="PGEvan444!"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM practice")

    # Fetch the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except Exception as e:
    print("An error occurred:", e)

# Close the cursor and the connection
#cursor.close()
#connection.close()