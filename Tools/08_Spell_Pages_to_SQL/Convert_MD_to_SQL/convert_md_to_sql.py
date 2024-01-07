import os
import glob

path = "/Users/jasoncameron/Desktop/py_spells/Spells/"

# FINAL RUNNING FUNCTION
def Run_Parser_In_Dir(path):
    spell_id_number = 1

    files = os.listdir(path)
    for file in files:
        f = path + file
        Parse_Document(f, spell_id_number)
        spell_id_number += 1

    print("Completed")

# FUN
# <F> Parse_Document
def Parse_Document(file, spell_id_number):
    # DLVs
    input = open(file, "r")

    lines = Capture_Lines(input)
    spell_tags = Capture_Tags(lines)
    spell_classes = Capture_Classes(lines)
    attributes = Capture_Attributes(lines)
    spell = Fill_In_Spell(attributes, lines)  # Must be completed Prior to cond & DT capture

    spell_conditions = Capture_Condition(lines, spell["description"])
    spell_damagetypes = Capture_Damagetypes(lines, spell["description"])

    spell_output = Spell_Output(spell)
    tags_output = Tags_Output(spell_tags, spell_id_number, spell["name"])                       # <R>
    conditions_output = Conditions_Output(spell_conditions, spell_id_number)
    damagetypes_output = Damagetypes_Output(spell_damagetypes, spell_id_number)
    classes_output = Classes_Output(spell_classes, spell_id_number, spell["name"])              # <R>

    print(str(spell_id_number) + ". Recording Spell: " + spell["name"] + "\n")
    spell_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/00_insert_spells.sql", "a")
    spell_doc.writelines(spell_output)
    spell_doc.close()

    print(str(spell_id_number) + ". Recording Spell Tag: " + spell["name"] + "\n")
    tag_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/01_insert_spell_tags.sql", "a")
    tag_doc.writelines(tags_output)
    tag_doc.close()

    print(str(spell_id_number) + ". Recording Spell condition: " + spell["name"] + "\n")
    conditions_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/02_insert_spell_conditions.sql", "a")
    conditions_doc.writelines(conditions_output)
    conditions_doc.close()

    print(str(spell_id_number) + ". Recording damage type: " + spell["name"] + "\n")
    damagetypes_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/03_insert_spell_damagetypes.sql", "a")
    damagetypes_doc.writelines(damagetypes_output)
    damagetypes_doc.close()

    print(str(spell_id_number) + ". Recording class: " + spell["name"] + "\n")
    classes_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/04_insert_spell_classes.sql", "a")
    classes_doc.writelines(classes_output)
    classes_doc.close()

    input.close()

    print("Spell: " + str(spell_id_number) + "  Completed.  " + spell["name"] + "\n")

# <F> Capture_Lines
def Capture_Lines(input):
    lines = []
    for line in input:
        if line.strip() == "":
            continue
        else:
            lines.append(line.strip().replace("\xa0", ""))

    return lines

# <F> Capture_Tags
def Capture_Tags(lines):
    spell_tags = []

    for line in lines:
        if line.startswith("spell_tags:"):
            mod_line = line.replace("spell_tags:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                spell_tags.append(l.lower().strip())

    return spell_tags

# <F> Capture_Conditions
def Capture_Condition(lines, spell_description):
    spell_conditions = []
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

    mod_description = spell_description.lower().replace("[", " ").replace("]", " ").replace(",", "").replace(".", "")
    array_description = mod_description.split(" ")

    for condition_word in condition_list:
        if condition_word in array_description:
            spell_conditions.append(condition_word)

    return spell_conditions

# <F> Capture_Damagetypes
def Capture_Damagetypes(lines, spell_description):
    spell_damagetypes = []
    damagetype_list = [
                        "acid",
                        "bludgeoning",
                        "cold",
                        "fire",
                        "force",
                        "lightning",
                        "necrotic",
                        "piercing",
                        "poison",
                        "psychic",
                        "radiant",
                        "slashing",
                        "thunder",
                        "shortbow",
                        "longbow",
                        "one-handed melee attacks",
                        "unarmed attacks",
                        "natural attacks",
                        "melee weapon attacks"]

    mod_damagetype = spell_description.lower().replace("[", " ").replace("]", " ").replace(",", "").replace(".", "")
    array_damagetype = mod_damagetype.split(" ")

    for damagetype_word in damagetype_list:
        if damagetype_word in array_damagetype:
            spell_damagetypes.append(damagetype_word)

    return spell_damagetypes

# <F> Capture_Classes
def Capture_Classes(lines):
    spell_classes = []

    for line in lines:
        if line.startswith("available_fore:"):
            mod_line = line.replace("available_fore:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                spell_classes.append(l.lower().strip())

    return spell_classes

# <F> Capture_Attributes
def Capture_Attributes(lines):
    attributes = []
    count_bars = 1;
    modline = ""

    for line in lines:
        if "|" in line and count_bars <= 2:
            count_bars += 1
        elif "|" in line and count_bars == 3:
            mod_line = line.strip("| ")
            array_line = mod_line.split("|")
            for l in array_line:
                attributes.append(l.lower().strip())
        else:
            continue

    return attributes

# <F> Fill_In_Spell
def Fill_In_Spell(attributes, lines):
    spell = {"name": "",
             "level": "",
             "casting_time": "",
             "range_area": "",
             "component_visual": "",
             "component_semantic": "",
             "component_material": "",
             "component_materials": "",
             "duration": "",
             "concentration": "",
             "ritual": "",
             "school": "",
             "save_type": "",
             "description": "",
             "image_url": "",
             "source_id": "5"}
    count_three_dashes = 1
    string_description = ""

    for line in lines:
        if line.startswith("# "):
            spell["name"] = line.replace("# ", "").replace("'", "''")
        elif line.startswith("* - ("):
            spell["component_materials"] = line.replace("* - (", "").replace("'","''").rstrip(")")
        elif line.startswith("!["):
            continue
        elif "---" in line and "|" not in line and count_three_dashes <= 4:
            count_three_dashes += 1
        elif count_three_dashes >= 5: # and "|" not in line and "---" not in line:
            string_description += line.replace("**","").replace("_","") + "\n"

    spell["level"] = attributes[0]
    spell["casting_time"] = attributes[1].replace("_ritual_", "").replace("'", "''")
    spell["range_area"] = attributes[2].replace("'", "''")
    spell["component_visual"] = "v" in attributes[3]
    spell["component_semantic"] = "s" in attributes[3]
    spell["component_material"] = "m" in attributes[3]
    spell["duration"] = attributes[4].replace("_concentration_", "").replace("'", "''")
    spell["concentration"] = "_concentration_" in attributes[4]
    spell["ritual"] = "_ritual_" in attributes[1]
    spell["school"] = attributes[5].replace("'", "''")
    spell["save_type"] = attributes[6].replace("'", "''")
    spell["description"] = string_description.replace("'", "''").rstrip("\n")

    return spell


# <F> Spell_Output
def Spell_Output(spell):
    return ("('" + spell["name"] + "', '" +
            spell["level"] + "', '" +
            spell["casting_time"] + "', '" +
            spell["range_area"] + "', '" +
            str(spell["component_visual"]) + "', '" +
            str(spell["component_semantic"]) + "', '" +
            str(spell["component_material"]) + "', '" +
            spell["component_materials"] + "', '" +
            spell["duration"] + "', '" +
            str(spell["concentration"]) + "', '" +
            str(spell["ritual"]) + "', '" +
            spell["school"] + "', '" +
            spell["save_type"] + "', '" +
            spell["description"] + "', '" +
            spell["image_url"] + "', '" +
            spell["source_id"] + "'),\n\t")

# <F> Tags_Output
def Tags_Output(spell_tags, spell_id_number, spell_name):                   # <R>
    output = ""

    for tag_word in spell_tags:
        output += Get_Tag_Id_Num(tag_word, spell_id_number, spell_name)     # <R>

    return output

# <F> Conditions_Output
def Conditions_Output(spell_conditions, spell_id_number):
    output = ""

    for condition_word in spell_conditions:
        output += Get_Condition_Id_Num(condition_word, spell_id_number)

    return output

# <F> Damagetypes_Output
def Damagetypes_Output(spell_damagetypes, spell_id_number):
    output = ""

    for damagetype_word in spell_damagetypes:
        output += Get_Damageytpe_Id_Num(damagetype_word, spell_id_number)

    return output

# <F> Classes_Output
def Classes_Output(spell_classes, spell_id_number, spell_name):                 # <R>
    output = ""

    for class_word in spell_classes:
        output += Get_Class_Id_Num(class_word, spell_id_number, spell_name)     # <R>

    return output


# <f> Get_Tag_Id_Num
def Get_Tag_Id_Num(tag_word, spell_id_number, spell_name):                      # <R>

    tag_list = {
        "banishment": 5,
        "buff": 8,
        "charmed": 9,
        "combat": 10,
        "communication": 11,
        "compulsion": 12,
        "control": 15,
        "creation": 16,
        "damage": 18,
        "debuff": 19,
        "deception": 20,
        "detection": 21,
        "dunamancy": 23,
        "environment": 26,
        "exploration": 28,
        "foreknowledge": 33,
        "foresight": 34,
        "healing": 36,
        "movement": 44,
        "negation": 47,
        "sangromancy": 52,
        "scrying": 55,
        "shapechanging": 57,
        "social": 58,
        "special": 59,
        "summoning": 61,
        "teleportation": 66,
        "warding": 73,
        "utility": 71
    }

    if tag_word.strip() in tag_list:
        return "(" + str(spell_id_number) + ", " + str(tag_list[tag_word]) + "),\n\t"
    elif tag_word == "teleportationcontrol":
        return "(" + str(spell_id_number) + ", 66),\n\t (" + str(spell_id_number) + ", 15),\n\t "
    elif tag_word == "teleportationbuff":
        return "(" + str(spell_id_number) + ", 66),\n\t (" + str(spell_id_number) + ", 8),\n\t "
    elif tag_word == "buffsocial":
        return "(" + str(spell_id_number) + ", 58),\n\t (" + str(spell_id_number) + ", 8),\n\t "
    elif tag_word == "buffmovement":
        return "(" + str(spell_id_number) + ", 44),\n\t (" + str(spell_id_number) + ", 8),\n\t "
    elif tag_word == "controlsocial":
        return "(" + str(spell_id_number) + ", 58),\n\t (" + str(spell_id_number) + ", 15),\n\t "
    elif tag_word == "damagecontrol":
        return "(" + str(spell_id_number) + ", 18),\n\t (" + str(spell_id_number) + ", 15),\n\t "
    else:
        return "--  " + tag_word + "   --> Not found from: "+ spell_name + "\n\t"

# <f> Get_Conditions_Id_Num
def Get_Condition_Id_Num(condition_word, spell_id_number):

    condition_list = {
        "blinded": 1,
        "charmed": 2,
        "deafened": 3,
        "exhaustion": 4,
        "frightened": 5,
        "grappled": 6,
        "incapacitated": 7,
        "invisible": 8,
        "paralyzed": 9,
        "petrified": 10,
        "poisoned": 11,
        "prone": 12,
        "restrained": 13,
        "stunned": 14,
        "unconscious": 15,
    }

    if condition_word in condition_list:
        return "("+ str(spell_id_number) + ", " + str(condition_list[condition_word]) + "),\n\t"
    else:
        return "--  " + condition_word + "   --> Not found\n\t"

# <f> Get_Damagetype_Id_Num
def Get_Damageytpe_Id_Num(damagetype_word, spell_id_number):

    damagetype_list = {
        "acid": 1,
        "bludgeoning": 2,
        "cold": 3,
        "fire": 4,
        "force": 5,
        "lightning": 6,
        "necrotic": 7,
        "piercing": 8,
        "poison": 9,
        "psychic": 10,
        "radiant": 11,
        "slashing": 12,
        "thunder": 13,
        "shortbow": 14,
        "longbow": 15,
        "one-handed melee attacks": 16,
        "unarmed attacks": 17,
        "natural attacks": 18,
        "melee weapon attacks": 19,
    }

    if damagetype_word in damagetype_list:
        return "("+ str(spell_id_number) + ", " + str(damagetype_list[damagetype_word]) + "),\n\t"
    else:
        return "--  " + damagetype_word + "   --> Not found\n\t"

# <f> Get_Class_Id_Num
def Get_Class_Id_Num(class_word, spell_id_number, spell_name):  # <R>

    class_list = {
        "rouge": 1,
        "thief": 2,
        "assassin": 3,
        "arcane trickster": 4,
        "inquisitive": 5,
        "mastermind": 6,
        "scout": 7,
        "swashbuckler": 8,
        "phantom": 9,
        "soulknife": 10,
        "fighter": 11,
        "champion": 12,
        "battle master": 13,
        "eldritch knight": 14,
        "arcane archer": 15,
        "cavalier": 16,
        "samurai": 17,
        "psi warrior": 18,
        "rune knight": 19,
        "echo fighter": 20,
        "purple dragon knight": 21,
        "cleric": 22,
        "knowledge domain": 23,
        "life domain": 24,
        "light domain": 25,
        "nature domain": 26,
        "tempest domain": 27,
        "trickery domain": 28,
        "war domain": 29,
        "death domain": 30,
        "twilight domain": 31,
        "order domain": 32,
        "forge domain": 33,
        "grave domain": 34,
        "peace domain": 35,
        "arcane domain": 36,
        "ranger": 37,
        "fey wanderer": 38,
        "swarmkeeper": 39,
        "gloom stalker": 40,
        "horizon walker": 41,
        "monster slayer": 42,
        "hunter": 43,
        "beast master": 44,
        "drakewarden": 45,
        "druid": 46,
        "circle of the land": 47,
        "circle of the land (arctic)": 48,
        "circle of the land (coast)": 49,
        "circle of the land (desert)": 50,
        "circle of the land (forest)": 51,
        "circle of the land (grassland)": 52,
        "circle of the land (mountain)": 53,
        "circle of the land (swamp)": 54,
        "circle of the land (underdark)": 55,
        "circle of the moon": 56,
        "circle of dreams": 57,
        "circle of the shepherd": 58,
        "circle of spores": 59,
        "circle of stars": 60,
        "circle of wildfire": 61,
        "warlock": 62,
        "the archfey": 63,
        "the fiend": 64,
        "the great old one": 65,
        "the celestial": 66,
        "the undying": 67,
        "the hexblade": 68,
        "the fathomless": 69,
        "the genie": 70,
        "the undead": 71,
        "paladin": 72,
        "oath of devotion": 73,
        "oath of the ancients": 74,
        "oath of vengeance": 75,
        "oathbreaker": 76,
        "oath of conquest": 77,
        "oath of redemption": 78,
        "oath of glory": 79,
        "oath of the watchers": 80,
        "oath of the crown": 81,
        "oath of the open sea": 82,
        "monk": 83,
        "way of the open hand": 84,
        "way of the shadow": 85,
        "way of the four elements": 86,
        "way of mercy": 87,
        "way of the astral self": 88,
        "way of the drunken master": 89,
        "way of the kensei": 90,
        "way of the sun soul": 91,
        "way of long death": 92,
        "way of the ascendant dragon": 93,
        "wizard": 94,
        "school of abjuration": 95,
        "school of conjuration": 96,
        "school of divination": 97,
        "school of enchantment": 98,
        "school of evocation": 99,
        "school of illusion": 100,
        "school of necromancy": 101,
        "school of transmutation": 102,
        "school of graviturgy": 103,
        "school of chronurgy": 104,
        "war magic": 105,
        "bladesinging": 106,
        "order of scribes": 107,
        "barbarian": 108,
        "berserker": 109,
        "totem warrior": 110,
        "ancestral guardian": 111,
        "storm herald": 112,
        "zealot": 113,
        "beast": 114,
        "wild soul": 115,
        "battlerager": 116,
        "artificer": 117,
        "armorer": 118,
        "alchemist": 119,
        "artillerist": 120,
        "battle smith": 121,
        "bard": 122,
        "college of lore": 123,
        "college of valor": 124,
        "college of creation": 125,
        "college of glamor": 126,
        "college of swords": 127,
        "college of whispers": 128,
        "college of eloquence": 129,
        "college of spirits": 130,
        "sorcerer": 131,
        "aberrant mind": 132,
        "clockwork soul": 133,
        "divine soul": 134,
        "shadow magic": 135,
        "storm sorcery": 136,
        "draconic bloodline": 137,
        "wild magic": 138,
        "blood hunter": 139,
        "Order of the Ghostslayer": 140,
        "Order of the Lycan": 141,
        "Order of the Mutant": 142,
        "Order of the Profane Soul": 143
    }

    if class_word.strip() in class_list:
        return "("+ str(spell_id_number) + ", " + str(class_list[class_word]) + "),\n\t"
    else:
        return "--  " + class_word + "   --> Not found in spell: "+ spell_name +"\n\t"


# RUN ====================================================
Run_Parser_In_Dir(path)
