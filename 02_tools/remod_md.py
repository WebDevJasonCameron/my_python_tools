import argparse
import glob

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_f", help="Targeted MD file  used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="The place the new file needs to go.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
line_num = 0
file_title = ""

if args.in_f == "No Input Directory Arguments provided." or args.out_p == "No Output Directory Arguments provided.":
    flag = False


def build_file_name(read_file):
    read_file = open(read_file, "r")
    first_hash = True
    out_title = ""

    for line in read_file:
        if "#" in line:
            if first_hash:
                out_title = line.removeprefix("# ").replace(" ", "_").rstrip()
                first_hash = False
            else:
                continue
        elif "Start Time:" in line:
            broken_line = line.split(":")
            out_title = out_title + "__" + \
                better_date_output(broken_line[1]) + ".md"

    read_file.close()
    return out_title


def better_date_output(line):
    no_coma_line = line.replace(",", "")
    parts = no_coma_line.split(" ")
    day = int(parts[2].rstrip())
    return parts[3].rstrip() + get_month_number(parts[1]).rstrip() + str("{:02d}".format(day))


def get_month_number(month):

    if month == "January":
        return "_01_"
    elif month == "February":
        return "_02_"
    elif month == "March":
        return "_03_"
    elif month == "April":
        return "_04_"
    elif month == "May":
        return "_05_"
    elif month == "June":
        return "_06_"
    elif month == "July":
        return "_07_"
    elif month == "August":
        return "_08_"
    elif month == "September":
        return "_09_"
    elif month == "October":
        return "_10_"
    elif month == "November":
        return "_11_"
    elif month == "December":
        return "_12_"
    else:
        return "_Missing_"


def reconstruct_line(line):
    part_01 = ""
    part_02 = ""
    if ":" in line:
        line_parts = line.split(":")
        part_01 = line_parts[0].replace(" ", "_") + ":"

        if "_/" in part_01:
            part_01 = part_01.replace("_/", "")

        if "POC_3_1:" in part_01:
            part_01 = "POC_3_Number"

        part_02 = line_parts[1]
    return part_01 + part_02


def hash_title(file_title):
    file_title_split = file_title.split("__")
    out_title = file_title_split[0].replace("_", " ")
    return out_title


def write_final_file(read_file_path, write_file_path, file_title):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + file_title, "w")
    heading_line = True
    first_blank_line = True

    write_file.writelines("---\n")

    for line in read_file:
        if "[" in line or "---" in line or "#" in line:
            continue
        elif ":" in line:
            write_file.writelines(reconstruct_line(line))
        elif line == "\n" and first_blank_line:
            first_blank_line = False
            continue
        else:
            if heading_line:
                write_file.writelines("\n---\n")
                write_file.writelines("# " + hash_title(file_title) + "\n\n")
                write_file.writelines("### Job Duties\n")
                heading_line = False
            else:
                write_file.writelines(line)

    read_file.close()
    write_file.close()


if flag:
    print("Program is running...")

    read_file_path = args.in_f
    write_file_path = args.out_p

    file_title = build_file_name(read_file_path)
    write_final_file(read_file_path, write_file_path, file_title)

print("\nCompleted")
