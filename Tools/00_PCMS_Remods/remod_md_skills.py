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
                meta_data["skill_name"] = line.removeprefix(
                    "# ").rstrip()
                first_hash = False
        elif line.startswith("Abillity: "):
            meta_data["ability_score"] = line.replace(
                "Abillity: ", "").rstrip()
        elif line.startswith("Skill Catagory: "):
            meta_data["skill_cat"] = line.replace(
                "Skill Catagory: ", "").rstrip()
        elif line.startswith("Skill Type: "):
            meta_data["skill_type"] = line.replace("Skill Type: ", "").rstrip()
        else:
            continue

    read_file.close()
    return meta_data


def buil_body_block():
    output = " |    | Situation | Task | Action | Result | \n" + \
        " | --- | --- | --- | --- | --- | \n" + \
        " | Explination | Think of a specific time or circumstance when you used this skill; define the general context of that situation. |  Name the key objective you were responsible for in that situation or the challenges/ obstacles you had to overcome. | Describe what you did to complete the assigned task; emphasize the skills you used, and the resources involved. | Summarize the outcome and how you specifically contributed to that outcome; describe the improvements and/or benefits that were observed. | \n" + \
        " | Example | My department received new portable generators that had to be installed, operated, and maintained after my company lost power. | I was tasked with ensuring my team members were able to install, operate, and follow new maintenance procedures for the new portable generators. | I designed and conducted training for a team of 16 people to properly install, operate, and maintain the new generators. | The team members received a 95% pass rate on their first proficiency test and a 100% satisfaction rate from corporate managers. | \n" + \
        " |     |     |     |     |     | \n\n"

    return output


def write_final_file(read_file_path, write_file_path, meta_data):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + meta_data["file_name"], "w")

    # META BLOCK
    write_file.writelines("---\n" +
                          "file_name: " + meta_data["file_name"] + "\n" +
                          "skill_name: " + meta_data["skill_name"] + "\n" +
                          "ability_score: " + meta_data["ability_score"] + "\n" +
                          "skill_cat: " + meta_data["skill_cat"] + "\n" +
                          "skill_type: " + meta_data["skill_type"] + "\n" +
                          "---\n")

    write_file.writelines("# " + meta_data["skill_name"] + "\n\n")

    write_file.writelines(buil_body_block())

    # WRITE BODY

    read_file.close()
    write_file.close()


def remod_all_in_file_list(read_file_list, out_dir):
    write_file_path = out_dir

    for read_file in read_file_list:
        meta_data = get_meta_data(read_file)
        write_final_file(read_file, write_file_path, meta_data)


if flag:
    print("Program is running...")

    read_file_list = get_file_list(args.in_dir)
    remod_all_in_file_list(read_file_list, args.out_dir)

print("\nCompleted")
