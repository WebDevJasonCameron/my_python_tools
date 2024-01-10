import os
import glob

path = "/Users/jasoncameron/Desktop/dnd_items/Items"


# FINAL RUNNING FUNCTION

# FUN
# <F> Parse Document


# <F> Capture Lines
def Capture_Lines(input):
    lines = []
    for line in input:
        if line.strip() == "":
            continue
        else:
            lines.append(line.strip().replace("\xa0", ""))

    return lines

# <F> Capture Types

# <F> Capture Tags
def Capture_Tags(lines):
    item_tags = []

    for line in lines:
        if line.startswith("item_tag:"):
            mod_line = line.replace("item_tag:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                item_tags.append(l.lower().strip())

    return item_tags

# <F> Capture Notes

# <F> Capture Conditions
def Capture_Condition(lines, item_description):
    item_conditions = []
    condition_list = [ "blinded",
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

# <F> Capture Attached Spells

# <F> Capture Effects
