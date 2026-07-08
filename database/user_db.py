from database.db import connect_db
from utils.auth import hash_password, verify_password


def register_user(full_name, email, password, course, year):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE email=%s",
        (email,)
    )

    if cursor.fetchone():
        conn.close()
        return False, "Email already exists."

    hashed = hash_password(password)

    cursor.execute(
        """
        INSERT INTO students
        (full_name, email, password, course, year)
        VALUES (%s,%s,%s,%s,%s)
        """,
        (full_name, email, hashed, course, year)
    )

    conn.commit()
    conn.close()

    return True, "Registration Successful."


def login_user(email, password):

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE email=%s",
        (email,)
    )

    student = cursor.fetchone()

    conn.close()

    if student is None:
        return False, None

    if verify_password(password, student["password"]):
        return True, student

    return False, None