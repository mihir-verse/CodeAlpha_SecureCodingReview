# CodeAlpha Secure Coding Review
# Example: SQL Injection vulnerability
# Educational demonstration only.

def get_user_query(username):
    # INSECURE: User input is directly joined to the SQL query.
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query


if __name__ == "__main__":
    username = input("Enter username: ")
    query = get_user_query(username)

    print("\nGenerated SQL query:")
    print(query)