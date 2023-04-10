"""
#     SMASH Notes
#       NAME:       Strong_App_Convert.py
#       LOCATION:   https://github.com/WebDevJasonCameron/my_python_tools/blob/main/Tools/Exercise_Conversions/Strong_App_Convert.py
#       PURPOSE:    Built to convert text files exported out of the IOS Strong App and imported into my 
#                   Obsidian Personal Management Vault
#       CREATED:    2023 04 09
#       NOTES:      This is a CLI tool that takes in two arguments.  The first param, --in-f , requires the 
#                   file path you wish to target.  The second param, --out_p , requires the path you wish to
#                   place the converted file.  The final final title is created from the second line of the 
#                   original file
"""

import argparse

from Month_Number import get_month_number

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_f", help="Targeted MD file used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="The place the new file needs to go.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
line_num = 1
file_title = ""


# (0 Day), (1 Month), (2 Day #), (3 Year), (4 "at"), (5 time), (6 "AM/PM")
def build_file_title(line):
    line_parts = line.replace(",", "").split(" ")
    day = line_parts[0]
    month_num_str = get_month_number(line_parts[1])
    day_num_str = line_parts[2]
    year_num_str = line_parts[3]
    at = line_parts[4]
    time = line_parts[5]
    am_pm = line_parts[6]
    return year_num_str + "_" + month_num_str + "_" + day_num_str + "__" + day + "__" + at + "_" + time + "_" + am_pm


def get_file_title(read_file_path):
    read_file = open(read_file_path, "r")

    line_num = 1
    out = ""

    for line in read_file:
        if line_num != 2:
            line_num += 1
        elif line == 2:
            out = build_file_title(line)

    return out


def get_ex_name(line):
    return line.replace(" ", "_")


def convert_data(read_file_path, write_file_path):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path, "r")

    line_num_mon = 0
    first_line = True

    for line in read_file:
        if first_line == True:
            first_line = False
            continue
        elif "AM" in line or "PM" in line:
            print(line)

    read_file.close()
    write_file.close()


read_file_path = args.in_f
write_file_path = args.out_p

out = get_file_title(read_file_path)
print(out)


"""
# <F> DETERMINES CARDIO, STRENGTH, BODYWEIGHT, STRETCHING   (name, ex_num)    #   After Ex name

# <F> CARDIO          id by "mi"
# EX_#: NAME
# EX_#_SET_#_DIST:    ### mi                                <- REPEAT
# EX_#_SET_#_TIME:    ### min                               <- REPEAT


# <F> STRENGTH        id by "lb"
# EX_#: NAME
# EX_#_SET_#_WEIGHT:  ### lb                                <- REPEAT
# EX_#_SET_#_REPS:    ###                                   <- REPEAT


# <F> BODYWEIGHT      id by "reps"
# EX_#: NAME
# EX_#_SET_#_REPS:    ### reps                              <- REPEAT

"""
