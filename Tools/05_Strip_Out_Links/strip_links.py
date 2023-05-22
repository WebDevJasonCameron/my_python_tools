import re


def strip_file_contents(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    stripped_lines = []

    for line in lines:
        if "[]" in line and "!" not in line:
            pattern = r'\[\]\([^)]+\)'
            stripped_line = re.sub(pattern, '', line)
            print(stripped_line)
            stripped_lines.append(stripped_line)
        else:
            stripped_lines.append(line)

    return stripped_lines


# Usage example
filename = 'input.txt'  # Replace with your file name
stripped_lines = strip_file_contents(filename)

output_file = open("output.txt", "w")

for line in stripped_lines:
    output_file.writelines(line)

output_file.close()
