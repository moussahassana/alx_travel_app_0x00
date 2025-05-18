from seed import connect_to_prodev
import mysql.connector

def stream_users_in_batches(batch_size):
    try:
        connection = connect_to_prodev()
        if connection is None:
            print("Failed to connect to database")
            return

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        batch = []
        # Loop 1: Fetch rows and group into batches
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        
        # Yield any remaining rows
        if batch:
            yield batch
            
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error streaming batches: {err}")

def batch_processing(batch_size):
    try:
        # Loop 2: Iterate over batches
        for batch in stream_users_in_batches(batch_size):
            # Loop 3: Filter users over 25
            filtered_batch = [user for user in batch if user['age'] > 25]
            if filtered_batch:
                # Yield each user individually
                for user in filtered_batch:
                    yield user
    except Exception as err:
        print(f"Error processing batches: {err}")