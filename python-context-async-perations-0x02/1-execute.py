import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=None):
        self.query = query
        self.params = params or ()
        self.conn = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")
        else:
            print("Query executed and connection closed.")

# Example usage
query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(query, params) as results:
    for row in results:
        print(row)
