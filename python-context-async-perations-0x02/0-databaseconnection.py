import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

def get_users_info(db_file):
    with DatabaseConnection(db_file) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

# Test the context manager
get_users_info("users.db")
