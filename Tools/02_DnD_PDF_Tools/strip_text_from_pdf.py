import argparse
import glob
from pdfminer.high_level import extract_text

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument(
    "--in_f", help="Targeted PDF file  used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="Text placed in this file.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True

if args.in_f == "No Input Directory Arguments provided." or args.out_p == "No Output Directory Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    target_file = glob.glob(args.in_f)

    write_file = open(
        args.out_p + "/replace_title_with_book_and_chapter_title.txt", "a")

    for f in target_file:
        text = extract_text(f)
        write_file.writelines(text)

    write_file.close()
    print("Program is done.")

else:
    print("Unable to run Program with out correct arguments.")
