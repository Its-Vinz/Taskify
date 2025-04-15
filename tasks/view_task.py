from mysql.connector import Error
from auth.session import load_session
from db import create_connection, fetch_result
from utils.cli_styles import error_msg, success_msg

def view_my_task():
  session = load_session()
  if not session:
    print(error_msg("✘ Please login to view your tasks!"))
    return
  user_id = session["user_id"]

  try:

    connection = create_connection()

    fetching_data = """
      SELECT * FROM tasks WHERE user_id = %s;
    """

    username_query = "SELECT username FROM users WHERE id = %s;"
    username_result = fetch_result(connection, username_query, (user_id,))
    username = username_result[0][0] if username_result else "Unknown"
    
    displaying_data = fetch_result(connection, fetching_data, (user_id,))
    if displaying_data:
      print(success_msg("\t~ Here are you tasks:"))
      for task in displaying_data:
        print(f"""
          ╭────────────────────────╮
          │ 📝  Task ID     :  {task[0]}  │
          ╰────────────────────────╯
          ╭────╮
          │ 👤 │  User          : {username} (ID: {task[1]})
          │    │
          │ 📌 │  Title         : {task[2]}
          │    │ 
          │ 🧾 │  Description   : {task[3]}
          │    │
          │ 📅 │  Date          : {task[4]}
          │    │
          │ 🔥 │  Priority      : {task[5]}
          │    │
          │ 📍 │  Status        : {task[6]}
          ╰────╯ 
          """)
        {'─' * 40}
    else:
      print(error_msg("\t✘ No task found!"))

  except Error as e:
    print(error_msg(f'\t✘ Error: {e}'))
  finally:
    connection.close()