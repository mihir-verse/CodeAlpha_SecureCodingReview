# CodeAlpha Secure Coding Review
# Secure example: Parameterized SQL query
# Educational demonstration only.

import sqlite3


def create_database():
    connection = sqlite3.connect(":memory:")

    connection.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    """)

    connection.execute(
        "INSERT INTO users (username) VALUES (?)",
        ("mihir",)
    )

    return connection


def get_user(connection, username):
    # SECURE: Parameterized query keeps input separate from SQL code.
    query = "SELECT id, username FROM users WHERE username = ?"

    cursor = connection.execute(query, (username,))
    return cursor.fetchall()


if __name__ == "__main__":
    connection = create_database()

    username = input("Enter username to search: ")
    results = get_user(connection, username)

    if results:
        print("User found:", results)
    else:
        print("No matching user found.")

    connection.close()
