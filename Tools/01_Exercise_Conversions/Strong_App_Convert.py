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


# (0 Day), (1 Month), (2 Day #), (3 Year), (4 "at"), (5 time), (6 "AM/PM")
def build_file_title(line):
    line_parts = line.replace(",", "").split(" ")
    day = line_parts[0]
    month_num_str = get_month_number(line_parts[1])
    day_num_str = line_parts[2].zfill(2)
    year_num_str = line_parts[3]
    at = line_parts[4]
    time = line_parts[5]
    am_pm = line_parts[6]
    return year_num_str + "_" + month_num_str + "_" + day_num_str + "__" + day + "__" + at + "_" + time + "_" + am_pm


def get_file_title(read_file_path):
    read_file = open(read_file_path, "r")

    line_num = 1

    for line in read_file:
        if line_num != 2:
            line_num += 1
        else:
            return build_file_title(line).rstrip() + ".md"


def get_ex_name(line, ex_num):
    return (("Ex_" + str(ex_num) + ": " + line), line.replace(" ", "_").replace("(", "").replace(")", ""))


def build_plank_sets(line, ex_name):
    line_parts = line.split(":")
    set = ex_name + "_" + line_parts[0].replace(" ", "_") + ":: "
    min = line_parts[1].rstrip()
    sec = line_parts[2].rstrip()
    return set + min + " min " + sec + " sec\n"


def build_rep_only_sets(line, ex_name):
    line_parts = line.split(":")
    set = ex_name + "_" + line_parts[0].replace(" ", "_") + ":: "
    reps = line_parts[1]
    return set + reps


def build_weight_sets(line, ex_name):
    line_parts = line.split(":")
    part_01 = line_parts[0].replace(" ", "_")
    part_02 = line_parts[1].split(" × ")

    sets = ex_name + "_" + part_01
    weights = sets + "_weight:: " + part_02[0]
    reps = sets + "_reps:: " + part_02[1]
    return weights + "\n" + reps


def build_cardio_sets(line, ex_name):
    line_parts = line.split(":")
    part_01 = line_parts[0].replace(" ", "_")
    part_02 = line_parts[1].split(" | ")

    sets = ex_name + "_" + part_01
    distance = sets + "_distance:: " + part_02[0]
    reps = sets + "_time:: " + part_02[1]
    return distance + "\n" + reps + "\n"


def convert_data(read_file_path, write_file_path, file_title):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + file_title, "w")

    parts = file_title.split("__")
    date = parts[0].replace("_", " ")
    day = parts[1].replace("_", " ")
    pre_time = parts[2].replace("_", " ")
    time = pre_time[3: (len(pre_time) - 3)]

    header_count = 1
    ex_num = 1
    ex_name = ""

    write_file.writelines("---\n")
    write_file.writelines("workout_date: " + date + "\n")
    write_file.writelines("workout_day: " + day + "\n")
    write_file.writelines("workout_time: " + time + "\n")
    write_file.writelines("workout_quality: \n")
    write_file.writelines("---\n")

    write_file.writelines("# Workout Log: " + date + "\n")

    for line in read_file:
        if header_count < 3:
            header_count += 1
            continue

        elif "http" in line:
            continue

        elif line == "\n":
            write_file.writelines(line)

        elif "Set" not in line and header_count >= 3:
            ex_name_list = get_ex_name(line, ex_num)
            ex_name = ex_name_list[1].rstrip()
            ex_num += 1
            write_file.writelines(ex_name_list[0])

        elif "Set" in line and "mi" in line:
            write_file.writelines(build_cardio_sets(line, ex_name))

        elif "Set" in line and "lb" in line:
            write_file.writelines(build_weight_sets(line, ex_name))

        elif "Set" in line and "reps" in line:
            write_file.writelines(build_rep_only_sets(line, ex_name))

        elif "Set" in line:
            write_file.writelines(build_plank_sets(line, ex_name))

        else:
            write_file.writelines("Error Here\n")

    read_file.close()
    write_file.close()


print("Running\n\n")

read_file_path = args.in_f
write_file_path = args.out_p
file_title = ""

file_title = get_file_title(read_file_path)
convert_data(read_file_path, write_file_path, file_title)

print("\n\nCompleted")
