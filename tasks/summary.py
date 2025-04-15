from mysql.connector import Error
from db import create_connection, fetch_result
from utils.cli_styles import success_msg, error_msg

def show_summary():
    try:
        connection = create_connection()
        total_query = "SELECT COUNT(*) FROM tasks"
        completed_query = "SELECT COUNT(*) FROM tasks WHERE status = 'completed'"
        pending_query = "SELECT COUNT(*) FROM tasks WHERE status = 'pending'"
        priority_query = """
            SELECT 
              SUM(CASE WHEN priority = 'High' THEN 1 ELSE 0 END) AS high,
              SUM(CASE WHEN priority = 'Medium' THEN 1 ELSE 0 END) AS medium,
              SUM(CASE WHEN priority = 'Low' THEN 1 ELSE 0 END) AS low
            FROM tasks
        """

        total = fetch_result(connection, total_query)[0][0]
        completed = fetch_result(connection, completed_query)[0][0]
        pending = fetch_result(connection, pending_query)[0][0]
        prio_result = fetch_result(connection, priority_query)[0]
        
        print(success_msg("\t~ Task Summary:"))
        print(f"""
          ╭────╮
          │ 📦 │  Total Tasks        :  {total}
          │    │
          │ ✅ │  Completed Tasks    :  {completed}
          │    │ 
          │ ⏳ │  Pending Tasks      :  {pending}
          ╰────╯
          ────────────────────────────
          ╭────╮
          │ 🔥 │  High Priority      :  {prio_result[0]}
          │    │
          │ ⚖️  │  Medium Priority    :  {prio_result[1]}
          │    │
          │ 🧊 │  low Priority       :  {prio_result[2]}
          ╰────╯
        """)

    except Error as e:
        print(error_msg(f"\t✘ Error: {e}"))
    finally:
        connection.close()