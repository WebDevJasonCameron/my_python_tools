#!/usr/bin/env python3
import cgi
import os

print("Content-Type: text/plain\n")

form = cgi.FieldStorage()
file_name = form.getvalue("file_name")
dir_path = "/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Explore/02_Web_FTP/directory_to_manage"   
file_path = f"{dir_path}/{file_name}" 

with open(file_path, 'w') as file:
    file.write(content)
print(f"Success: {file_name} has been written.")
