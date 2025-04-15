# Taskify : Get Started

**A complete developer reference for `Taskify`, your terminal-powered task manager.**

---

<br/>

## ⚙️ Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Its-Vinz/taskify.git
   cd taskify

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt

3. **Configure Environment**  
   Create a `.env` file at the root with your DB path:
   ```bash
   DB_PATH=taskpro.db

4. **Run the Application**
   ```bash
   python3 main.py --help
 
---

<br/>

## 🧾 CLI Command Flags

| Flag           | Description                                       |
|----------------|---------------------------------------------------|
| `--signup`     | Create new user account                           |
| `--login`      | Login with credentials                            |
| `--logout`     | Logout current user                               |
| `-u`           | Specify username                                  |
| `-p`           | Specify password                                  |
| `--add`        | Add a new task                                    |
| `--title`      | Task title                                        |
| `--desc`       | Task description                                  |
| `--date`       | Due date (YYYY-MM-DD)                             |
| `--prio`       | Priority (High/Medium/Low)                        |
| `--status`     | Task status (Pending/Completed)                   |
| `--display`    | View all tasks                                    |
| `--delete`     | Delete task by ID                                 |
| `--search`     | Search tasks by keyword                           |
| `--complete`   | Mark a task as complete (by ID)                   |
| `--summary`    | View task stats/summary                           |
| `--export`     | Export to PDF/CSV                                 |
| `--notify`     | Trigger notification for due tasks                |
| `--silent`     | Run notification silently (no console output)     |

---

<br/>

## 📦 Usage

1. **login to taskify:**
   ```bash
   $ python3 main.py --login -u admin
   
2. **To add new task:**
   ```bash
   $ python3 main.py --add --title client1_Project --desc Handover_client1_project --date 2025-04-20 --prio High --status pending

3. **To display tasks:**
   ```bash
   $ python3 main.py --display

4. **To mark as completed task (using Task ID):**
   ```bash
   $ python3 main.py --complete 12

5. **To delete a specific task:**
   ```bash
   $ python3 main.py --delete 12

6. **To search for task (using keyword):**
   ```bash
   $ python3 main.py --search client1

7. **To view summary:**
   ```bash
   $ python3 main.py --summary

8. **To export task in `csv` and `pdf`**
   ```bash
   $ python3 main.py --export

9. **To show notifications:**
   ```bash
   $ python3 main.py --notify

10. **For silent notifications:**
    ```bash
    $ python3 main.py --silent

---

<br/>

## 🔔 Auto Daily Reminder (Linux Cron) (Optional)

1. **Schedule daily reminders for due tasks:**
   ```bash
   $ crontab -e

2. **Add this line to notify every day at 9:00 AM:**
   ```bash
   $ 0 9 * * * python3 /absolute/path/to/main.py --notify --silent

---

<br/>

##  🚀 Taskify Launcher (Bonus Tip) (Optional)

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

---

<br/>

## ⛃ Database Schema

1. **Table for storing user credits:**   
   ```sql
   > CREATE TABLE users (
     id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(50) NOT NULL UNIQUE,
     password_hash VARCHAR(255) NOT NULL,
     approved BOOLEAN NOT NULL DEFAULT 0
   );

2. **Table for storing tasks:**
   ```sql
   > CREATE TABLE tasks (
     id INT AUTO_INCREMENT PRIMARY KEY,
     user_id INT,
     title VARCHAR(100) NOT NULL,
     description TEXT,
     due_date DATE,
     priority ENUM('Low', 'Medium', 'High') DEFAULT 'Low',
     status ENUM('pending', 'completed') DEFAULT 'pending',
     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
   );

---

<br/>


## 🗂️ Folder Structure

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

---

<br/>

##  Author

**Built with precision, caffeine, and ❤️ by Vinz**
