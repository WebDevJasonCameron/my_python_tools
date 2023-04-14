import argparse

parser = argparse.ArgumentParser(description='Removing Parts of a txt doc.')

parser.add_argument(
    "--file", help="The file you wish to mod.", default="No Arguments provided.")

args = parser.parse_args()

flag = True
num_count = 0


def possible_title(line):
    checker = line.split(" ")
    if len(checker) <= 4 and len(checker) > 0:
        return True
    else:
        return False


if args.file == "No Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    with open(args.file, "r") as f:
        lines = f.readlines()

    with open(args.file, "w") as f:
        for line in lines:
            if len(line) > 1:
                if line.startswith("#"):
                    f.write(line + " \n")
                elif possible_title(line):
                    f.write(line + "\n")
                elif line.endswith("."):
                    f.write(line + "  \n")
                else:
                    f.write((" " + line).rstrip())
            else:
                continue
