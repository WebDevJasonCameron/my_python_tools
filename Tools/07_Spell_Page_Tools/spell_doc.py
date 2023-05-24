def get_lines():
    lines = []

    read_file = open("../input.txt", "r")

    for line in read_file:
        lines.append(line.strip())

    return lines


def get_meta(lines):
    meta_data = {"source": "", "school": "", "concentration": "",
                 "ritual": "", "spell_tag": "", "available_for": ""}

    meta_data["school"] = lines[lines.index('SCHOOL') + 1]

    if "Concentration" in lines:
        print("yes, con is here")

    for n in lines:
        if "ConcentrationRitual" in n:
            meta_data["concentration"] = "yes"
            meta_data["ritual"] = "yes"
        elif "Concentration" in n:
            meta_data["concentration"] = "yes"
        elif "Ritual" in n:
            meta_data["ritual"] = "yes"

    if "Basic Rules" in lines:
        meta_data["source"] = "Basic Rules"
    elif "Player's Handbook" in lines:
        meta_data["source"] = "Player's Handbook"


"""
---
ttrpg: DND5E
source: Player's Handbook
asset_type:
 - spells
 - 
COMBAT, WARDING
 BARD, SORCERER, WARLOCK, WIZARD
---
  """


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
        school + \
        con + rit + " - \n" + \
        "spell_tags: " + spell_tags + "\n" + \
        "available_for: " + available_for + "\n" + \
        "---"

    return meta_blog

    # RUN
lines = get_lines()
meta_data = get_meta(lines)
source = meta_data["source"]
school = meta_data["school"]
concentration = meta_data["concentration"]
ritual = meta_data["ritual"]
spell_tags = ""
available_for = ""


meta_block = build_meta_block(
    source, school, concentration, ritual, spell_tags, available_for)

print(meta_block)
