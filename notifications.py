from datetime import date
from plyer import notification
from db import fetch_result, create_connection
from utils.cli_styles import warning_msg, info_msg

notified_tasks = set()

def check_and_notify_tasks(silent=False):
    today = date.today().isoformat()

    query = "SELECT title, description, due_date FROM tasks WHERE due_date = %s;"
    connection = create_connection()
    try:
        result = fetch_result(connection, query, (today,))
        if result:
            for task in result:
                title, description, due_date = task
                if title not in notified_tasks:
                    notified_tasks.add(title)
                    notification.notify(
                        title=f"⏰ Reminder: {title}",
                        message=f"{description}\nDue Today: {due_date}",
                        timeout=15
                    )
                    if not silent:
                        print("\t ╭───────╮")
                        print(warning_msg(f"\t │ 🔔 Task Reminder sent: {title} "))
                        print("\t ╰───────╯")
        else:
            if not silent:
                print(info_msg("✅ No tasks due today!"))
    finally:
        connection.close()

def main(silent=False):
    check_and_notify_tasks(silent=silent)

