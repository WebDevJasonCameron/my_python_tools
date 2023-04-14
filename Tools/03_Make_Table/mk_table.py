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


if flag:
    print("Program is running...")

    write_file = open("table_text.txt", "r")

    write_file.close()
    print("Program complete.")
