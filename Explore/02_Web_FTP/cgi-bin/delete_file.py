#!/usr/bin/env python3
import cgi
import os

print("Content-Type: text/plain\n")

form = cgi.FieldStorage()
file_name = form.getvalue("file_name")
dir_path = "/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Explore/02_Web_FTP/directory_to_manage"
file_path = f"{dir_path}/{file_name}"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Success: {file_name} has been deleted.")
else:
    print(f"Error: {file_name} does not exist.")
