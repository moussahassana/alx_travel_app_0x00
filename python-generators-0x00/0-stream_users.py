from seed import connect_to_prodev
import mysql.connector

def stream_users():
    try:
        # Connect to ALX_prodev database using seed.py function
        connection = connect_to_prodev()
        if connection is None:
            print("Failed to connect to database")
            return

        cursor = connection.cursor(dictionary=True)  # Return rows as dictionaries
        cursor.execute("SELECT * FROM user_data")
        
        # Stream rows one by one with a single loop
        for row in cursor:
            yield row
            
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error streaming users: {err}")