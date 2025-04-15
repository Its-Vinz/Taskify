import argparse, getpass
from auth.secure_auth import signup, login
from auth.session import save_session, load_session, clear_session
from tasks.add_task import add_new_task
from tasks.delete_task import delete_task
from tasks.view_task import view_my_task
from tasks.search_tasks import search_tasks
from tasks.mark_complete import mark_task_complete
from tasks.summary import show_summary
from tasks.export_tasks import export_tasks
from utils.cli_styles import header, warning_msg, error_msg, success_msg, info_msg
from notifications import main as notify_main
from datetime import datetime

def main():
    print(info_msg("\n\n\t~ WELCOME TO TASKPRO CLI — YOUR TASK, YOUR RULES! ~"))

    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d")
    current_day = now.strftime("%A")

    print("\t\t\t\t\t\t\t\t\t\t\t ╭────────────────────────────────────╮")
            
    print(header(f"\t\t\t\t\t\t\t\t\t\t\t │ {current_time} │ {current_date} │ {current_day} │"))
    print("\t\t\t\t\t\t\t\t\t\t\t ╰────────────────────────────────────╯")

    parser = argparse.ArgumentParser(description="TaskPro CLI")
    
    # Auth Options
    parser.add_argument("--signup", action="store_true", help="Signup a new user")
    parser.add_argument("--login", action="store_true", help="Login to TaskPro")
    parser.add_argument("--logout", action="store_true", help="Logout from TaskPro")
    parser.add_argument("-u", type=str, help="Username")
    parser.add_argument("-p", type=str, help="Password")
    
    # Task Actions
    parser.add_argument("--add", action="store_true", help="Add new task")
    parser.add_argument("--title", type=str, help="Task title")
    parser.add_argument("--desc", type=str, help="Task description")
    parser.add_argument("--date", type=str, help="Due date (YYYY-MM-DD)")
    parser.add_argument("--prio", type=str, help="Priority (High/Medium/Low)")
    parser.add_argument("--status", type=str, help="Task status (Pending/Completed)")

    parser.add_argument("--display", action="store_true", help="Display all your tasks")
    parser.add_argument("--delete", type=int, help="Delete task by ID")
    parser.add_argument("--search", type=str, help="Search tasks by keyword")
    parser.add_argument("--complete", type=int, help="Mark task complete by ID")
    parser.add_argument("--summary", action="store_true", help="View task summary")
    parser.add_argument("--export", action="store_true", help="Export tasks to PDF")
    parser.add_argument('--notify', action='store_true', help='Show task reminders')
    parser.add_argument('--silent', action='store_true', help='Run notify silently')

    args = parser.parse_args()

    # SIGNUP
    if args.signup:
        if not args.u or not args.p:
            print(error_msg("\t✘ Username and Password are required for signup"))
        else:
            signup(args.u, args.p)

    # LOGIN
    elif args.login:
        if not args.u:
            print(error_msg("\t✘ Username is required to login"))
        else:
            password = args.p or getpass.getpass("\t~ Enter Password: ")
            user_id = login(args.u, password)
            if user_id:
                save_session(user_id, args.u)
                print(success_msg(f"\t✔ Welcome, {args.u}! User ID: {user_id}"))
            else:
                print(error_msg("\t✘ Invalid username or password"))

    # LOGOUT
    elif args.logout:
        clear_session()
        print(warning_msg("\t✔ Logout successful!"))

    # PROTECTED TASK ROUTES — require login
    else:
        session = load_session()
        if not session:
            print(error_msg("\t✘ You must login to use TaskPro features. Use --login"))
            return
        user_id = session["user_id"]

        if args.add:
            if args.title and args.desc and args.date and args.prio and args.status:
                add_new_task(user_id, args.title, args.desc, args.date, args.prio, args.status)
            else:
                print(error_msg("\t✘ All task fields (title, desc, date, prio, status) are required."))

        elif args.display:
            view_my_task()

        elif args.delete:
            delete_task(args.delete)

        elif args.search:
            search_tasks(args.search)

        elif args.complete:
            mark_task_complete(args.complete)

        elif args.summary:
            show_summary()

        elif args.export:
            export_tasks()

        elif args.notify:
            notify_main()

        if args.notify:
            notify_main(silent=args.silent)

        else:
            print(warning_msg("\tUse --help for available options.\n"))

if __name__ == "__main__":
    main()
