#!/usr/bin/env python3

# list_files.py
# Place in the /cgi-bin/ directory

import os
import json

print("Content-Type: application/json\n")

dir_path = "/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Explore/02_Web_FTP/directory_to_manage"  # Directory to manage
files = os.listdir(dir_path)
print(json.dumps(files))