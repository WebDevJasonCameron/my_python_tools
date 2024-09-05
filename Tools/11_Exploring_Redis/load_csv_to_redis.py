import os
import csv
import redis
import pandas as pd

# Establish a connection to the Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Function to upload CSV data to Redis
def upload_csv_to_redis(directory):
    # Iterate over all CSV files in the given directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            # Read the CSV file using pandas
            df = pd.read_csv(file_path)

            # Iterate over each row in the DataFrame and upload to Redis
            for index, row in df.iterrows():
                # Create a unique key for each row, for example using filename and index
                redis_key = f"{filename}_{index}"
                # Convert row to a dictionary
                row_dict = row.to_dict()
                # Upload the dictionary to Redis as a hash
                redis_client.hmset(redis_key, row_dict)

            print(f"Uploaded data from {filename} to Redis.")

# Replace 'your_directory_path' with the path to your CSV files
upload_csv_to_redis('your_directory_path')
