from mysql.connector import Error
from db import create_connection, execute_query
from utils.cli_styles import success_msg, error_msg

def mark_task_complete(task_id):
    try:
        update_query = """
            UPDATE tasks SET status = 'completed' WHERE id = %s;
        """
        connection = create_connection()
        cursor = execute_query(connection, update_query, (task_id,))
        if cursor > 0:
          print(success_msg(f"\t✔ Task ID {task_id} marked as completed."))
        else:
          print(error_msg(f"\t✘ Task ID {task_id} Already marked as completed!"))
    except Error as e:
        print(error_msg(f"\t✘ Error: {e}"))
    finally:
        connection.close()