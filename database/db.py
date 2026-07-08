import mysql.connector


def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Nivedita@123",
            database="ai_learning_mentor"
        )

        return connection

    except mysql.connector.Error as err:
        print("Database Error:", err)
        return None