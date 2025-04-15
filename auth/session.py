import json
import os

SESSION_FILE = 'auth/.session.json'

def save_session(user_id, username):
    session_data = {"user_id": user_id, "username": username}
    with open(SESSION_FILE, 'w') as file:
        json.dump(session_data, file)

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            return json.load(file)
    return None

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)