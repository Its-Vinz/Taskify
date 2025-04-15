#  Taskify

A powerful, lightweight, and developer-focused **command-line task manager** built in Python for busy developers and CLI Lovers.  
Designed for speed, clarity, and productivity — right from your terminal.


<br/>


##  Features at a Glance

- ✅ **Add, update, delete, and list** tasks with ease
- 🗂️ Filter by **priority, status, date, or title**
- 🕒 **Real-time system info** (time, date, day) display
- 🔔 **Smart reminders** via desktop notifications
- 💾 Uses **MySQL** for lightweight persistence
- 🎨 Terminal output with **minimal, beautiful styling**
- 🧠 Built for developers, creators, and CLI lovers


<br/>


##  Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Its-Vinz/taskify.git
   cd taskify

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt

3. **Configure Environment Create a **.env** file at the root with your DB path:**
   ```bash
   DB_PATH=taskpro.db

4. **Run the Application**
   ```bash
   python3 main.py --help


<br/>


##  Command Line Flags

| Flags           | Description                                               |
|-----------------|-----------------------------------------------------------|
| `--signup`    	| Sign up a new user                                        |
| `--login`       | Log in to Taskify                                         |
| `--logout`      | Log out from Taskify                                      |
| `-u`            | Specify username                                          |
| `-p`            | Specify password                                          |
| `--add`         | Add a new task                                            |
| `--task`        | Title of the task                                         |
| `--desc`        | Description of the task                                   |
| `--date`        | Due date in YYYY-MM-DD format                             |
| `--prio`        | Task priority (High, Medium, Low)                         |
| `--status`      | Task status (Pending or Completed)                        |
| `--display`     | Display all tasks                                         |
| `--delete`      | Delete a task by its ID                                   |
|	`--search`     | Search tasks by a keyword                                 |
| `--complete`    | Mark a task as complete by its Task ID                    |
| `--summary`     | View s summary of tasks                                   |
| `--export`      | Export all tasks to csc/pdf                               |         
| `--notify`      | Show due task notifications                               |                      
| `--silent`      | Run notifications silently (no console output)            |
| `--help` / `h`  | Display the help message and all available commands       |


<br />


## Example usage:

1. **login to taskify:**
   ```bash
   $ vinz@whithat:~/Downloads/Taskify$ python3 main.py --login -u admin
   
2. **To add new task:**
   ```bash
   $ vinz@whithat:~/Downloads/Taskify$ python3 main.py --add --title client1_Project --desc Handover_client1_project --date 2025-04-20 --prio High --status pending

3. **To display tasks:**
   ```bash
   $ vinz@whithat:~/Downloads/Taskify$ python3 main.py --display

4. **To mark as completed task (using Task ID):**
   ```bash
   $ vinz@whithat:~/Downloads/Taskify$ python3 main.py --complete 12


<br />


##  Auto Daily Reminder (Linux Cron) (Optional)

1. **Schedule daily reminders for due tasks:**
   ```bash
   $ crontab -e

2. **Add this line to notify every day at 9:00 AM:**
   ```bash
   $ 0 9 * * * python3 /absolute/path/to/main.py --notify --silent


<br />

   
## Taskify Launcher (Bonus Tip) (Optional)

1. **create a bash file **taskify.sh** and add the custom bash script as shown below:**
   ```bash
   #! /bin/bash

   #Optional: Activate virtualenv if using one
   source venv/bin/activate

   python3 main.py "$@"

2. **Make it executable:**
   ```bash
   $ chmod +x taskify.sh

3. **Run it with arguments:**
   ```bash
   $ ./taskify --login -u admin


<br />


## Folder Structure

   ```txt
   taskify/
   │
   ├── main.py                 # Entry point: handles argparse & routes commands
   ├── db.py                   # Handles DB connection and setup
   │
   ├── auth/
   │   ├── secure_auth.py      # For handling Authentication
   │   └── session.py          # For session management
   │
   ├── tasks/
   │   ├── add_task.py         # Add new task
   │   ├── view_tasks.py       # View/filter tasks
   │   ├── mark_complete.py    # Mark task as done
   │   ├── delete_task.py      # Delete task
   │   ├── search_tasks.py     # Search tasks
   │   ├── export_tasks.py     # Export to CSV/PDF
   │   └── summary.py          # Show task summary stats
   │
   ├── utils/
   │   └── cli_style.py        # Colors / ASCII / format
   │
   ├── notifications.py        # Handling notifications
   ├── .env                    # DB credentials (optional, for dotenv)
   ├── requirements.txt        # List all the Python packages
   └── README.md               # Project overview & run instructions
   ```

<br />


##  Author

**Built with precision, caffeine, and ❤️ by Vinz**

