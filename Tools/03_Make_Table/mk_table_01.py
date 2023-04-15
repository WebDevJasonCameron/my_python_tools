import argparse

parser = argparse.ArgumentParser(
    description='Create markdown table from text and prompts.')

parser.add_argument(
    "--c", help="How many columns in the table.", default="No Arguments provided.")

args = parser.parse_args()
flag = True

if args.c == "No column Arguments provided.":
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


def build_table(lines, cols):
    write_file = open("output_table.txt", "w")
    rows = len(lines) / cols
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

    cols = int(args.c)

    lines = fill_lines()
    build_table(lines, cols)

    for line in lines:
        print(line)

    print("Program complete.")
