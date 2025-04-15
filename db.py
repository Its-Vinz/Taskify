# from multiprocessing import connection
from multiprocessing import connection
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# load environment variables from .env
load_dotenv()

def create_connection():  
  "Create and return database connection"
  try: 
    connection = mysql.connector.connect(
      host = os.getenv('DB_HOST'),
      user = os.getenv('DB_USER'),
      password = os.getenv('DB_PASSWORD'),
      database = os.getenv('DB_NAME'),
      # auth_plugin="mysql_native_password"
    )

    if connection.is_connected():
      # print("connected to database") # uncomment when switching to (Debug Mode)
      return connection
  except Error as e:
    print(f"Error: {e}")
    return None

def close_connection():
  "Close the connection"
  if connection.is_connected():
    connection.close(connection)
    print("Connection closed.")

def execute_query(connection, query, values=None):
  "Execute a single (INSERT, UPDATE, DELETE, SELECT)"
  try:
      cursor = connection.cursor()
      if values:
        cursor.execute(query,values)
      else:
        cursor.execute(query)
      connection.commit()
      return cursor.rowcount # Return number of rows affected (successful insert = 1)
  except Error as e:
    print(f"Error: {e}")
  finally:
    cursor.close()

def fetch_result(connection, query, values=None):
  "Fetch results from a SELECT query"
  results = []
  try:
    cursor = connection.cursor()
    cursor.execute(query, values)
    results = cursor.fetchall()
    return results
  except Error as e:
    print(f"Error: {e}")
  finally:
    cursor.close()