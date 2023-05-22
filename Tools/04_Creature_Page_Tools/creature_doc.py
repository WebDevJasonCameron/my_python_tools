def other_titles_by_period(line):
    line_parts = line.split(".")

    if len(line_parts[0].split()) < 3:
        line_parts[0] = "**" + line_parts[0] + "**"

    return " ".join(line_parts)


def create_stat_block():
    read_file = open("input.txt", "r")
    stat_parts = []
    line_num = 0

    for line in read_file:

        if line_num <= 12 and line != "\n":
            if line.startswith("STR"):
                stat_parts.append(line.rstrip())
                line_num += 1
            elif line_num > 0:
                stat_parts.append(line.rstrip())
                line_num += 1
            else:
                continue

    read_file.close()

    stat_block = " | " + stat_parts[0] + " | " + stat_parts[2] + " | " + stat_parts[4] + " | " + stat_parts[6] + " | " + stat_parts[8] + " | " + stat_parts[10] + " |\n | --- | --- | --- | --- | --- | --- |\n | " + stat_parts[1] + " | " + stat_parts[3] + " | " + stat_parts[5] + " | " + stat_parts[7] + \
        " | " + stat_parts[9] + " | " + stat_parts[11] + " |\n "

    return stat_block


def get_meta():
    read_file = open("input.txt", "r")
    meta_data = {"size": "", "alignment": "", "challenge_num": "",
                 "xp_num": "", "monster_tag": "", "enviornment": ""}

    for line in read_file:
        if line.startswith("Tiny") or line.startswith("Small") or line.startswith("Medium") or line.startswith("Large") or line.startswith("Huge") or line.startswith("Gargantuan"):
            line_1 = line
            line_2 = line
            line_parts_1 = line_1.split(" ")
            meta_data["size"] = line_parts_1[0]
            line_parts_2 = line_2.split(", ")
            meta_data["alignment"] = line_parts_2[1].strip()
        elif line.startswith("Challenge"):
            line = line.replace("Challenge", "").strip()
            line_parts = line.split(" ")
            meta_data["challenge_num"] = line_parts[0].strip()
            meta_data["xp_num"] = line_parts[1].replace(
                "(", "").replace(",", "").strip()
        elif line.startswith("Monster Tags:"):
            line_parts = line.split(":")
            meta_data["monster_tag"] = line_parts[1].replace(
                " ", ", ").replace("\\xa0", "").strip()
        elif line.startswith("Environment:"):
            line_parts = line.split(":")
            meta_data["enviornment"] = line_parts[1].replace(
                " ", ", ").rstrip()

    read_file.close()
    return meta_data


def build_meta_block(size, alignment, challenge_num, xp_num, monster_tag, enviornment):
    meta_block = "---\n" + \
        "ttrpg: DND5E \n" + \
        "asset_type:\n" + \
        " - species\n" + \
        " - non_playable\n" + \
        " - \n" + \
        "size: " + size + "\n" + \
        "alignment: " + alignment + "\n" + \
        "challenge: " + challenge_num + "\n" + \
        "xp: " + xp_num + "\n" + \
        "monster_tag: " + monster_tag + "\n" + \
        "enviornment: " + enviornment + "\n" + \
        "---\n"
    return meta_block


def doc_processing(stat_block, meta_block):
    read_file = open("input.txt", "r")
    write_file = open("output.txt", "w")
    line_num = 1
    stat_block_num = 0

    write_file.writelines(meta_block)

    for line in read_file:
        if stat_block_num == 0 or stat_block_num >= 24:
            if line_num == 1:
                write_file.writelines(
                    "# " + line.upper())
                line_num += 1
            elif line == "\n":
                write_file.writelines(line)
                line_num += 1
            elif line_num == 3:
                write_file.writelines(line.lower())
                line_num += 1
            elif line.startswith("STR"):
                write_file.writelines(stat_block)
                stat_block_num += 1
            elif line.startswith("Armor Class"):
                write_file.writelines(line.replace(
                    "Armor Class", "**Armor Class**"))
            elif line.startswith("Hit Points"):
                write_file.writelines(line.replace(
                    "Hit Points", "**Hit Points**"))
            elif line.startswith("Speed"):
                write_file.writelines(line.replace(
                    "Speed", "**Speed**"))
            elif line.startswith("Saving Throws"):
                write_file.writelines(line.replace(
                    "Saving Throws", "**Saving Throws**"))
            elif line.startswith("Skills"):
                write_file.writelines(line.replace(
                    "Skills", "**Skills**"))
            elif line.startswith("Damage Resistances"):
                write_file.writelines(line.replace(
                    "Damage Resistances", "**Damage Resistances**"))
            elif line.startswith("Damage Immunities"):
                write_file.writelines(line.replace(
                    "Damage Immunities", "**Damage Immunities**"))
            elif line.startswith("Condition Immunities"):
                write_file.writelines(line.replace(
                    "Condition Immunities", "**Condition Immunities**"))
            elif line.startswith("Senses"):
                write_file.writelines(line.replace(
                    "Senses", "**Senses**"))
            elif line.startswith("Languages"):
                write_file.writelines(line.replace(
                    "Languages", "**Languages**").rstrip())
            elif line.startswith("Proficiency Bonus"):
                write_file.writelines(line.replace(
                    "Proficiency Bonus", "**Proficiency Bonus**"))
            elif line.startswith("Actions"):
                write_file.writelines("## " + line + "---")
            elif line.startswith("Bonus Action"):
                write_file.writelines("## " + line + "---")
            elif line.startswith("Reaction"):
                write_file.writelines("## " + line + "---")
            elif line.startswith("Legendary Actions"):
                write_file.writelines("## " + line + "---")
            elif line.startswith("### Description"):
                write_file.writelines(line.replace("###", "##") + "---")
            elif "." in line and not "!" in line and not "_" in line:
                output = other_titles_by_period(line)
                write_file.writelines(output)
            elif line.startswith("Monster Tags:") or line.startswith("Environment:") or line.startswith("Challenge"):
                continue
            else:
                write_file.writelines(line)
        else:
            stat_block_num += 1

    read_file.close()
    write_file.close()


# START PROGRAM

# Vars
meta_data = {}
stat_block = create_stat_block()
meta_data = get_meta()
size = meta_data.get("size")
alignment = meta_data.get("alignment")
challenge_num = meta_data.get("challenge_num")
xp_num = meta_data.get("xp_num")
monster_tag = meta_data.get("monster_tag")
enviornment = meta_data.get("enviornment")

# Blocks
meta_block = build_meta_block(
    size, alignment, challenge_num, xp_num, monster_tag, enviornment)


# Doc
doc_processing(stat_block, meta_block)
