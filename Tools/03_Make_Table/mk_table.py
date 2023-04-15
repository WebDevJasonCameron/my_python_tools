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


def fill_lines():
    read_file = open("input_text.txt", "r")
    out_lines_list = []

    for line in read_file:
        if line == "\n":
            continue
        else:
            out_lines_list.append(line.rstrip())

    read_file.close()
    return out_lines_list


def build_table(lines, rows, cols):
    write_file = open("output_table.txt", "w")
    s_num = 0
    c_num = 1
    r_num = 1
    i_num = 0
    n = 1

    while n <= len(lines):

        if r_num == 1 and c_num == 1:
            write_file.writelines("| " + lines[i_num] + " | ")
            i_num += rows
            c_num += 1

        elif r_num == 1 and c_num > 1 and c_num < cols:
            write_file.writelines(lines[i_num] + " | ")
            i_num += rows
            c_num += 1

        elif r_num == 1 and c_num == cols:
            write_file.writelines(lines[i_num] + " |\n")
            c_num = 1
            r_num += 1
            s_num += 1
            i_num = s_num

# 1ST ROW

        elif r_num == 2 and c_num == 1:
            write_file.writelines("| --- | ")
            c_num += 1

        elif r_num == 2 and c_num > 1 and c_num < cols:
            write_file.writelines("--- | ")
            c_num += 1

        elif r_num == 2 and c_num == cols:
            write_file.writelines("--- |\n")
            c_num = 1
            r_num += 1

# 2ND ROW

        elif r_num > 2 and c_num == 1:
            write_file.writelines("| " + lines[i_num] + " | ")
            i_num += rows
            c_num += 1

        elif r_num > 2 and c_num > 1 and c_num < cols:
            write_file.writelines(lines[i_num] + " | ")
            i_num += rows
            c_num += 1

        elif r_num > 2 and c_num > 1 and c_num == cols:
            write_file.writelines(lines[i_num] + " |\n")
            c_num = 1
            r_num += 1
            s_num += 1
            i_num = s_num

        else:
            write_file.writelines("\nFound an Error\n")

        n += 1
    write_file.close()


if flag:
    print("Program is running...")

    rows = int(args.row)
    cols = int(args.col)

    lines = fill_lines()
    build_table(lines, rows, cols)

    print("Program complete.")
