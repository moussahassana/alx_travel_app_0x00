from itertools import islice
import importlib
stream_users = importlib.import_module('0-stream_users').stream_users

# Iterate over the generator function and print only the first 6 rows
try:
    for user in islice(stream_users(), 6):
        print(user)
except Exception as e:
    print(f"Error streaming users: {e}")