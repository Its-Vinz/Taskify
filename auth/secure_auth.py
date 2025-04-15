import bcrypt
from mysql.connector import Error
from db import create_connection, fetch_result, execute_query
from utils.cli_styles import success_msg, error_msg
from auth.session import save_session

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

def signup(username, password):
    hashed = hash_password(password)
    query = "INSERT INTO users (username, password_hash) VALUES (%s, %s);"
    values = (username, hashed.decode('utf-8'))
    result = []
    try:
        connection = create_connection()
        execute_query(connection, query, values)
        print(success_msg("\t✔ Signup successful! You can now login."))
        if result and verify_password(password, result[0][2]):
            user_id = result[0][0]
            save_session(user_id, username)
            print(success_msg("\t✔ Login successful!"))
            return user_id
    except Error as e:
        if "Duplicate entry" in str(e):
            print(error_msg("\t✘ Username already exists! Try logging in."))
        else:
            print(error_msg(f"\t✘ Signup failed: {e}"))
    finally:
        connection.close()

def login(username, password):
    query = "SELECT * FROM users WHERE username = %s;"
    try:
        connection = create_connection()
        result = fetch_result(connection, query, (username,))

        user_id, username, hashed_password, approved = result[0]

        if not verify_password(password, hashed_password):
            print(error_msg("\t✘ Invalid username or password."))
            return None

        if not approved:
            print(error_msg("\t✘ Account not approved yet. Please wait for admin approval."))
            return None

        print(success_msg("\t✔ Login successful!"))
        return user_id  # Only if everything passes

    except Error as e:
        print(error_msg(f"\t✘ Login failed: {e}"))
        return None
    finally:
        connection.close()