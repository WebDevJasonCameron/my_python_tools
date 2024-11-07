#!/usr/bin/env python3
import os
import urllib.parse
import sys
from config import file_directory  # Import the file_directory variable

print("Content-Type: application/octet-stream")

# Parse query parameters
query_string = os.environ.get('QUERY_STRING', '')
query_params = dict(urllib.parse.parse_qsl(query_string))
file_name = query_params.get("file_name")

# Construct the file path using the imported file_directory
file_path = os.path.join(file_directory, file_name) if file_name else None

# Validate file path and prevent directory traversal
if not file_name or not os.path.isfile(file_path) or not os.path.commonpath([file_directory]) == os.path.commonpath([file_directory, file_path]):
    print("\nError: Invalid file path")
    sys.exit(1)
else:
    # Set headers for download
    print(f"Content-Disposition: attachment; filename={file_name}\n")
    
    # Read and output file contents
    with open(file_path, 'rb') as file:
        print(file.read().decode('ISO-8859-1'))
