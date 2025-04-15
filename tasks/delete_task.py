from mysql.connector import Error
from db import create_connection, execute_query
from utils.cli_styles import success_msg, warning_msg, error_msg
import logging

def delete_task(id):
  confirm = input(warning_msg(f'Are you sure you want to delete Task? Id:{id} (yes/no): '))
  if confirm.strip().lower() != "yes":
    print(warning_msg("\t✘ Deletion cancelled!"))
    return
  delete_query = """
    DELETE FROM tasks WHERE id = %s;
  """
  values = (id,)
  connection = create_connection()
  try:
    cursor = execute_query(connection, delete_query, values)
    if cursor > 0:
      print(success_msg("\t✔ Task deleted!"))
      logging.basicConfig(filename='taskpro.log', level=logging.INFO, format='%(asctime)s - %(message)s')
      logging.info(f"\t✔ Task deleted | Task ID: {id} ")
    else:
      print(error_msg("\t✘ Task not found or you don't have permission!"))
  except Error as e:
    print(error_msg(f"\t✘ Error: {e}"))
  finally:
    connection.close()