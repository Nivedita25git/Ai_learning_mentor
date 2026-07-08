from database.db import connect_db


def save_chat(student_email, question, answer):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO chat_history(student_email, question, answer)
    VALUES(%s,%s,%s)
    """

    cursor.execute(
        query,
        (student_email, question, answer)
    )

    conn.commit()

    cursor.close()
    conn.close()