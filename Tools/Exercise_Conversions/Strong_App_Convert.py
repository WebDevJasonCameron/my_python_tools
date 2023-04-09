import argparse
import glob

from Month_Number import get_month_number

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_f", help="Targeted MD file used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="The place the new file needs to go.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
line_num = 0
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


checks = build_file_title("Friday, December 10, 2021 at 9:41 AM")

print(checks)
