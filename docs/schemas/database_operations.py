import os
import pandas as pd
import psycopg2
from psycopg2 import OperationalError
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NewsData(Base):
    __tablename__ = 'news_data'

    source_id = Column(String, primary_key=True)
    title = Column(String)
    published_at = Column(DateTime)
    content = Column(String)
    category = Column(String)
    source_name = Column(String)
    topic = Column(Integer)
    tags = Column(String)
    cluster = Column(Integer)
    event = Column(String)


def create_connection():
    connection = None

    # Database connection parameters
    dbname = 'postgres'
    user = 'news_admin'
    password = 'pass123'
    host = 'localhost'

    try:
        # Establishing the connection
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def save_to_db(data, table_name):
    # Create the connection
    engine = create_engine(connection_string)

    print("CONNECTION TO ENGINE CREATED!")

    # Save the data to the database
    data.to_sql(table_name, engine, if_exists='replace', index=False)

    # Close the connection
    engine.dispose()


def save_to_csv(data, file_path):
    # Save the data to a CSV file
    data.to_csv(file_path, index=False)


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def fetch_query_results(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


if __name__ == '__main__':
    # Create the database connection
    connection = create_connection()

    # Create the table if it doesn't exist
    NewsData.metadata.create_all(connection)

    # Load data into a DataFrame (assuming the data is available in a pandas DataFrame called 'data')
    data = pd.DataFrame()

    # Save data to the database
    save_to_db(data, 'news_data')

    # Save data to a CSV file
    save_to_csv(data, 'data.csv')

    # Execute a query
    query = "SELECT * FROM news_data"
    execute_query(connection, query)

    # Fetch query results
    results = fetch_query_results(connection, query)

    # Print the results
    print(results)

    # Close the connection
    connection.close()