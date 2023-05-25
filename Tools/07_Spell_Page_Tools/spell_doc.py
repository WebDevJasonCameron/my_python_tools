def get_lines():
    lines = []

    read_file = open("../input.txt", "r")

    for line in read_file:
        lines.append(line.strip())

    return lines


def get_meta(lines):
    meta_data = {"source": "", "school": "", "concentration": "",
                 "ritual": "", "spell_tags": "", "available_for": ""}

    meta_data["school"] = lines[lines.index('SCHOOL') + 1]

    if "Concentration" in lines:
        print("yes, con is here")

    for line in lines:
        if "ConcentrationRitual" in line:
            meta_data["concentration"] = "yes"
            meta_data["ritual"] = "yes"
        elif "Concentration" in line:
            meta_data["concentration"] = "yes"
        elif "Ritual" in line:
            meta_data["ritual"] = "yes"
        elif "Spell Tags:" in line:
            line_parts = line.split(": ")
            meta_data["spell_tags"] = line_parts[1].replace(" ", ", ")
        elif "Available For:" in line:
            line_parts = line.split(": ")
            meta_data["available_for"] = line_parts[1].replace(" ", ", ")
        elif "Basic Rules" in line:
            meta_data["source"] = "Basic Rules"
        elif "Player's Handbook" in line:
            meta_data["source"] = "Player's Handbook"

    return meta_data


def build_meta_block(source, school, concentration, ritual, spell_tags, available_for):
    con = ""
    rit = ""

    if concentration == "yes":
        con = " - concentration\n"

    if ritual == "yes":
        rit = " - ritual\n"

    meta_blog = "" + \
        "---\n" + \
        "ttrpg: DND5E\n" + \
        "source: " + source + "\n" + \
        "asset_type:\n" + \
        " - spells\n" + \
        " - " + school.lower() + "\n" + \
        con + rit + \
        "spell_tags: " + spell_tags.strip() + "\n" + \
        "available_for: " + available_for + "\n" + \
        "---\n"

    return meta_blog


def build_stat_block(lines):
    level = lines[lines.index('LEVEL') + 1]
    casting_time = lines[lines.index('CASTING TIME') + 1]
    range = lines[lines.index('RANGE/AREA') + 1]
    components = lines[lines.index('COMPONENTS') + 1]
    duration = lines[lines.index('DURATION') + 1]
    school = lines[lines.index('SCHOOL') + 1]
    attack_save = lines[lines.index('ATTACK/SAVE') + 1]
    damage_effect = lines[lines.index('DAMAGE/EFFECT') + 1]

    stat_block = "" + \
        "| LEVEL | CASTING TIME | RANGE/AREA | COMPONENTS | DURATION | SCHOOL | ATTACK/SAVE | DAMAGE/EFFECT | \n" + \
        "| --- | --- | --- | --- | --- | --- | --- | --- | \n" + \
        "| " + level + " | " + casting_time + " | " + range + " | " + components + " | " + \
        duration + " | " + school + " | " + attack_save + " | " + damage_effect + " | \n"

    return stat_block


def proccess_doc(lines, meta_data, meta_block, stat_block):
    write_file = open("../output.txt", "w")
    line_num = 0
    stat_line_num = 0

    write_file.writelines(meta_block)

    for line in lines:
        if stat_line_num == 0 or stat_line_num >= 16:
            if line_num == 0:
                write_file.writelines("# " + line.replace("Concentration", "").replace(
                    "Ritual", "").replace("ConcentrationRitual", "") + "\n")
                if meta_data["concentration"] == "yes":
                    write_file.writelines("_Concentration_\n")
                if meta_data["ritual"] == "yes":
                    write_file.writelines("_Ritual_\n")
                write_file.writelines("\n---\n")
                line_num += 1
            elif "LEVEL" in line:
                write_file.writelines(stat_block + "\n---\n\n")
                stat_line_num += 1
            elif "At Higher Levels." in line:
                write_file.writelines(line.replace(
                    "At Higher Levels.", "_At Higher Levels._") + "\n")
            elif "Spell Tags:" in line or "Available For:" in line or "Player's Handbook" in line:
                continue
            else:
                write_file.writelines(line + "\n")
        else:
            stat_line_num += 1

    write_file.close()


# ======== RUN
# VARS
lines = get_lines()
meta_data = get_meta(lines)
source = meta_data["source"]
school = meta_data["school"]
concentration = meta_data["concentration"]
ritual = meta_data["ritual"]
spell_tags = meta_data["spell_tags"]
available_for = meta_data["ritual"]

# FUNS
meta_block = build_meta_block(
    source, school, concentration, ritual, spell_tags, available_for)
stat_block = build_stat_block(lines)

proccess_doc(lines, meta_data, meta_block, stat_block)
