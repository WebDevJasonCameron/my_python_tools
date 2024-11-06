#!/usr/bin/env python3
import cgi
import os

# Set the path to your files directory
file_directory = "/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Explore/02_Web_FTP/directory_to_manage"  # Update with your actual directory

print("Content-Type: application/octet-stream")

# Get the filename from the query parameters
form = cgi.FieldStorage()
file_name = form.getvalue("file_name")

# Validate the file path to avoid directory traversal attacks
file_path = os.path.join(file_directory, file_name)
if not os.path.isfile(file_path) or not os.path.commonpath([file_directory]) == os.path.commonpath([file_directory, file_path]):
    print("\nError: Invalid file path")
else:
    # Set headers for file download
    print(f"Content-Disposition: attachment; filename={file_name}\n")
    
    # Read and output the file contents
    with open(file_path, 'rb') as file:
        print(file.read().decode('ISO-8859-1'))  # Decoding as ISO-8859-1 for CGI compatibility with binary data
