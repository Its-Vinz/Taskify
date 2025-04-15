from mysql.connector import Error
from db import create_connection, execute_query
from utils.cli_styles import success_msg, error_msg
import logging


def add_new_task(user_id, title, description, due_date, priority, status):
  insert_query = """
    INSERT INTO tasks (user_id, title, description, due_date, priority, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
  values = (user_id, title, description, due_date, priority, status)
  connection = create_connection()

  try:
    cursor = execute_query(connection, insert_query, values)
    if cursor > 0:
      print(success_msg("\t✔ Task added!"))
      logging.basicConfig(filename='taskpro.log', level=logging.INFO, format='%(asctime)s - %(message)s')
      logging.info(f"\t✔ Task added | User ID: {user_id} | Title: {title}")
    else:
      print(error_msg("\t✘ Task could not be added!"))
  except Error as e:
    print(f"\t✘ Error {e}")
  finally:
    connection.close()