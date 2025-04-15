from mysql.connector import Error
from db import create_connection, fetch_result
from utils.cli_styles import success_msg, error_msg

def search_tasks(keyword):
    search_query = """
        SELECT * FROM tasks 
        WHERE title LIKE %s OR description LIKE %s OR status LIKE %s;
    """
    values = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
    connection = create_connection()

    try:
      tasks = fetch_result(connection, search_query, values)

      if tasks:
        print(success_msg(f"\t✔ Matching Tasks based on {keyword}:\n"))
        for task in tasks:
          task_type = task[5]
          task_title = task[2]
          task_desc = task[3]
          print(f"""
          📝 Task ID     : {task[0]}
          👤 User ID     : {task[1]}
          📌 Title       : {task_title}
          🧾 Description : {task_desc}
          📅 Date        : {task[4]}
          🔥 Priority    : {task_type}
          📍 Status      : {task[6]}
          ────────────────────────────────────────
          """)
      else:
          print(error_msg("\t✘ No matching tasks found."))
    except Error as e:
        print(error_msg(f"\t✘ Error: {e}"))
    finally:
        connection.close()