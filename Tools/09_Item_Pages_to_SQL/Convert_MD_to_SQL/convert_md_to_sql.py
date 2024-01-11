import os
import glob

path = "/Users/jasoncameron/Desktop/dnd_items/Items"
file = "/Users/jasoncameron/Desktop/dnd_items/Items/Arrow-Catching Shield.md"

item_id_number = 1


# FINAL RUNNING FUNCTION

# FUN
# <F> Parse_Document
def Pars_Document(file):
    read_file = open(file, 'r')

    lines = Capture_Lines(read_file)
    item_tags = Capture_Tags(lines)
    item_types = Capture_Types(lines)

    Fill_In_Item(lines)


# <F> Capture_Lines
def Capture_Lines(input):
    lines = []
    for line in input:
        if line.strip() == "":
            continue
        else:
            lines.append(line.strip().replace("\xa0", ""))

    return lines


# <F> Capture_Types
def Capture_Types(lines):
    item_types = []

    for line in lines:
        if line.startswith("- "):
            mod_line = line.replace("- ", "")
            item_types.append(mod_line.lower().strip())

    return item_types


# <F> Capture_Tags
def Capture_Tags(lines):
    item_tags = []

    for line in lines:
        if line.startswith("item_tag:"):
            mod_line = line.replace("item_tag:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                item_tags.append(l.lower().strip())

    return item_tags


# <F> Capture_Conditions
def Capture_Condition(lines, item_description):
    item_conditions = []
    condition_list = ["blinded",
                      "charmed",
                      "deafened",
                      "exhaustion",
                      "frightened",
                      "grappled",
                      "incapacitated",
                      "invisible",
                      "paralyzed",
                      "petrified",
                      "poisoned",
                      "prone",
                      "restrained",
                      "stunned",
                      "unconscious"]

    mod_description = item_description.lower().replace("[", " ").replace("]", " ").replace(",", "").replace(".", "")
    array_description = mod_description.split(" ")

    for condition_word in condition_list:
        if condition_word in array_description:
            item_conditions.append(condition_word)

    return item_conditions


# <F> Capture_Attached_Spells


# <F> Capture Effects

# <F> Fill_In_Item
def Fill_In_Item(lines):
    item = {"name": "",                                             # 1.
            "ttrpg": "DND5E",                                       # 2.
            "rarity": "",                                           # 3.
            "renowned_quality": "",                                 # 4.
            "requires_attunement": False,                           # 5.
            "has_charges": False,                                   # 6. Search Description
            "is_cursed": False,                                     # 7.
            "cost": "",                                             # 8. Blank
            "weight": "",                                           # 9. Blank
            "description": "",                                      # 10.
            "image_url": "",                                        # 11. Blank
            "source_id": 5,                                         # 12.
            "magic_bonus_plus_1": False,                            # 13. Search Description
            "magic_bonus_plus_2": False,                            # 14. Search Description
            "magic_bonus_plus_3": False,                            # 15. Search Description
            "description_notes": ""                                 # 16.
            }
    count_three_dashes = 0
    string_description = ""

    for line in lines:
        if line.startswith("# "):
            item["name"] = line.replace("#", "").replace("'", "''").strip()
        elif line.startswith("rarity:"):
            item["rarity"] = line.replace("rarity:", "").replace("'", "''").strip()
        elif line.startswith("renowned_quality:"):
            item["renowned_quality"] = line.replace("renowned_quality:", "").replace("'", "''").strip()
        elif line.startswith("req_attunement:"):
            if "yes" in line.lower():
                item["requires_attunement"] = True
        elif line.startswith("is_cursed:"):
            if "yes" in line.lower():
                item["is_cursed"] = True
        elif line.startswith("Notes:"):
            item["description_notes"] = line.replace("Notes:", "").replace("'", "''").lower().strip()
        elif line.startswith("!["):
            continue
        elif "---" in line and count_three_dashes <= 3:
            count_three_dashes += 1
            print("count: " + str(count_three_dashes))
        elif count_three_dashes >= 3:
            print("HERE!")
            string_description += line.replace("'", "''").replace("**", "").replace("_", "")

    item["description"] = string_description


    print("1. name: " + item["name"])
    print("2. ttrpg: " + item["ttrpg"])
    print("3. rarity: " + item["rarity"])
    print("4. renowned quality: " + item["renowned_quality"])
    print("5. requires attunement: " + str(item["requires_attunement"]))
    print("6. has charges: " + str(item["has_charges"]))                            # <R> Req Description
    print("7. is cursed: " + str(item["is_cursed"]))
    print("8. cost: " + str(item["cost"]))
    print("9. weight: " + str(item["weight"]))
    print("9. description: " + item["description"])
    print("10. image url: " + str(item["image_url"]))
    print("11. source id: " + str(item["source_id"]))
    print("12. magic bonus +1: " + str(item["magic_bonus_plus_1"]))
    print("13. magic bonus +2: " + str(item["magic_bonus_plus_2"]))
    print("14. magic bonus +3: " + str(item["magic_bonus_plus_3"]))
    print("15. notes: " + str(item["description_notes"]))

# RUN ====================================================
Pars_Document(file)
