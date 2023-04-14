import argparse

parser = argparse.ArgumentParser(
    description='Create markdown table from text and prompts.')

parser.add_argument(
    "--col", help="How many columns in the table.", default="No Arguments provided.")

parser.add_argument(
    "--row", help="How many rows in the table.", default="No Arguments provided.")

args = parser.parse_args()
flag = True

if args.col == "No column Arguments provided." or args.row == "No Row Arguments provided.":
    flag = False


def dash_counter(line):
    output = ""
    for d in line.rstrip():
        output += "-"
    return output


def build_col(row, start_num, col_num):
    read_file = open("table_text.txt", "r")
    write_file = open("output_table.txt", "a")

    line_num = start_num

    for line in read_file:
        if line_count == 1:
            write_file.writelines("| " + line.rstrip() + " |\n")
            write_file.writelines("| " + dash_counter(line) + " |\n")
            line_count += 1
        elif line_count == row * col_num:
            write_file.writelines("| " + line.rstrip() + " |\n")

    read_file.close()
    write_file.close()


if flag:
    print("Program is running...")

    print("Program complete.")
