def get_meta():
    read_file = open("input.txt", "r")
    meta_data = {"size": "", "alignment": "", "challenge_num": "",
                 "xp_num": "", "monster_tag": "", "enviornment": ""}

    for line in read_file:
        if line.startswith("Tiny") or line.startswith("Small") or line.startswith("Medium") or line.startswith("Large") or line.startswith("Huge") or line.startswith("Gargantuan"):
            line_parts_1 = line.split(" ")
            meta_data["size"] = line_parts_1[0]
            line_parts_2 = line.split(", ")
            meta_data["alignment"] = line_parts_2[1].rsplit()

    read_file.close()
    return meta_data


def build_meta_block(size, alignment, challenge_num, xp_num, monster_tag, enviornment):
    output = "---\n" + \
        "ttrpg: DND5E \n" + \
        "asset_type:\n" + \
        "- species\n" + \
        "- non_playable\n" + \
        "- \n" + \
        "size: " + size + "\n" + \
        "alignment: " + alignment + "\n" + \
        "challenge: " + challenge_num + "\n" + \
        "xp: " + xp_num + "\n" + \
        "monster_tag: " + monster_tag + "\n" + \
        "enviornment: " + enviornment + "\n" + \
        " ---\n"


def doc_processing(stat_block):
    read_file = open("input.txt", "r")
    write_file = open("output.txt", "w")
    line_num = 1
    stat_block_num = 0

    for line in read_file:
        if line_num == 1:
            if stat_block_num == 0 or stat_block_num >= 12:
                if line_num == 1:
                    write_file.writelines(
                        "# " + line.upper() + "\n\n")

    read_file.close()
    write_file.close()
