import argparse
import glob

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_dir", help="Targeted dir to get the md files.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_dir", help="Ouput dir for mod md files.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
file_list = ()

if args.in_dir == "No Input Directory Arguments provided." or args.out_dir == "No Output Directory Arguments provided.":
    flag = False


def get_file_list(in_dir_path):
    return glob.glob(in_dir_path + '/*.md', recursive=True)


def get_meta_data(read_file):
    read_file = open(read_file, "r")
    first_hash = True
    meta_data = {"file_name": "", "skill_name": "",
                 "ability_score": "", "skill_cat": "", "skill_type": ""}

    for line in read_file:
        if "#" in line:
            if first_hash:
                meta_data["file_name"] = line.removeprefix(
                    "# ").replace(" ", "_").rstrip() + ".md"
                meta_data["skill_name"] = line
                first_hash = False
        elif line.startswith("Abillity: "):
            meta_data["ability_score"] = line.replace("Abillity: ", "")
        elif line.startswith("Skill Catagory: "):
            meta_data["skill_cat"] = line.replace("Skill Catagory: ", "")
        elif line.startswith("Skill Type: "):
            meta_data["skill_type"] = line.replace("Skill Type: ", "")
        else:
            continue

    read_file.close()
    return meta_data


def buil_body_block():
    return "# Situation \n" + \
        ""


def write_final_file(read_file_path, write_file_path, meta_data):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + meta_data["file_name"], "w")

    # META BLOCK
    write_file.writelines("---\n" +
                          "file_name: " + meta_data["file_name"] + "\n" +
                          "skill_name: " + meta_data["skill_name"] + "\n" +
                          "ability_score: " + meta_data["ability_score"] + "\n" +
                          "skill_cat: " + meta_data["skill_cat"] + "\n" +
                          "skill_type" + meta_data["skill_type"] + "\n" +
                          "---\n")

    write_file.writelines("# " + meta_data["file_name"])

    # WRITE BODY

    read_file.close()
    write_file.close()


def remod_all_in_file_list(file_list, out_dir):
    write_file_path = out_dir

    for file in file_list:
        read_file_path = file

        file_title = build_file_name(read_file_path)
        write_final_file(read_file_path, write_file_path, file_title)


if flag:
    print("Program is running...")

    file_list = get_file_list(args.in_dir)
    remod_all_in_file_list(file_list, args.out_dir)

print("\nCompleted")
