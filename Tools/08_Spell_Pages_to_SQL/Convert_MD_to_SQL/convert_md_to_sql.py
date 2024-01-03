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
    tags_output = Tags_Output(spell_tags, spell_id_number)
    conditions_output = Conditions_Output(spell_conditions, spell_id_number)
    damagetypes_output = Damagetypes_Output(spell_damagetypes, spell_id_number)
    classes_output = Classes_Output(spell_classes, spell_id_number)

    spell_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/00_insert_spells.sql", "a")
    spell_doc.writelines(spell_output)
    spell_doc.close()

    tag_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/01_insert_spell_tags.sql", "a")
    tag_doc.writelines(tags_output)
    tag_doc.close()

    conditions_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/02_insert_spell_conditions.sql", "a")
    conditions_doc.writelines(conditions_output)
    conditions_doc.close()

    damagetypes_doc = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/output/03_insert_spell_damagetypes.sql", "a")
    damagetypes_doc.writelines(damagetypes_output)
    damagetypes_doc.close()

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
            lines.append(line.strip().replace("\xa0", ""));

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
        if line.startswith("#"):
            spell["name"] = line.replace("# ", "").replace("'", "''")
        elif line.startswith("* - ("):
            spell["component_materials"] = line.replace("* - (", "").replace("'","''").rstrip(")")
        elif line.startswith("!["):
            continue
        elif "---" in line and "|" not in line and count_three_dashes <= 3:
            count_three_dashes += 1
        elif count_three_dashes >= 4 and "|" not in line and "---" not in line:
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
def Tags_Output(spell_tags, spell_id_number):
    output = ""

    for tag_word in spell_tags:
        output += Get_Tag_Id_Num(tag_word, spell_id_number)

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
def Classes_Output(spell_classes, spell_id_number):
    output = ""

    for class_word in spell_classes:
        output += Get_Class_Id_Num(class_word, spell_id_number)

    return output


# <f> Get_Tag_Id_Num
def Get_Tag_Id_Num(tag_word, spell_id_number):

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
        "debuf": 19,
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
        return "--  " + tag_word + "   --> Not found\n\t"

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
def Get_Class_Id_Num(class_word, spell_id_number):

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
        "circle of the moon": 48,
        "circle of dreams": 49,
        "circle of the shepherd": 50,
        "circle of spores": 51,
        "circle of stars": 52,
        "circle of wildfire": 53,
        "warlock": 54,
        "the archfey": 55,
        "the fiend": 56,
        "the great old one": 57,
        "the celestial": 58,
        "undying": 59,
        "the hexblade": 60,
        "the fathomless": 61,
        "the genie": 62,
        "the undead": 63,
        "paladin": 64,
        "oath of devotion": 65,
        "oath of the ancients": 66,
        "oath of vengeance": 67,
        "oathbreaker": 68,
        "oath of conquest": 69,
        "oath of redemption": 70,
        "oath of glory": 71,
        "oath of the watchers": 72,
        "oath of the crown": 73,
        "monk": 74,
        "way of the open hand": 75,
        "way of the shadow": 76,
        "way of the four elements": 77,
        "way of mercy": 78,
        "way of the astral self": 79,
        "way of the drunken master": 80,
        "way of the kensei": 81,
        "way of the sun soul": 82,
        "way of long death": 83,
        "way of the ascendant dragon": 84,
        "wizard": 85,
        "school of abjuration": 86,
        "school of conjuration": 87,
        "school of divination": 88,
        "school of enchantment": 89,
        "school of evocation": 90,
        "school of illusion": 91,
        "school of necromancy": 92,
        "school of transmutation": 93,
        "school of graviturgy": 94,
        "school of chronurgy": 95,
        "war magic": 96,
        "bladesinging": 97,
        "order of scribes": 98,
        "barbarian": 99,
        "berserker": 100,
        "totem warrior": 101,
        "ancestral guardian": 102,
        "storm herald": 103,
        "zealot": 104,
        "beast": 105,
        "wild soul": 106,
        "battlerager": 107,
        "artificer": 108,
        "armorer": 109,
        "alchemist": 110,
        "artillerist": 111,
        "battle smith": 112,
        "bard": 113,
        "college of lore": 114,
        "college of valor": 115,
        "college of creation": 116,
        "college of glamor": 117,
        "college of swords": 118,
        "college of whispers": 119,
        "college of eloquence": 120,
        "college of spirits": 121,
        "sorcerer": 122,
        "aberrant mind": 123,
        "clockwork soul": 124,
        "divine soul": 125,
        "shadow magic": 126,
        "storm sorcery": 127,
        "draconic bloodline": 128,
        "wild magic": 129,
        "blood hunter": 130,
        "Order of the Ghostslayer": 131,
        "Order of the Lycan": 132,
        "Order of the Mutant": 133,
        "Order of the Profane Soul": 134,
    }

    if class_word in class_list:
        return "("+ str(spell_id_number) + ", " + str(class_list[class_word]) + "),\n\t"
    elif (class_word == "circle of the land (forest)" or
          class_word == "circle of the land (swamp)" or
          class_word == "circle of the land (mountain)" or
          class_word == "circle of the land (desert)" or
          class_word == "circle of the land (grassland)" or
          class_word == "circle of the land (coast)" or
          class_word == "domaincircle of the land (grassland)" or
          class_word == "domaincircle of the land (coast)" or
          class_word == "domaincircle of the land (arctic)" or
          class_word == "domaincircle of the land (underdark)" or
          class_word == "circle of the land (underdark)"):
        return "("+ str(spell_id_number) + ", 47),\n\t"
    elif class_word == "the archfeythe great old one":
        return "(" + str(spell_id_number) + ", 57),\n\t ( " + str(spell_id_number) + ", 55),\n\t"
    elif class_word == "warlock.wizard":
        return "(" + str(spell_id_number) + ", 54),\n\t ( " + str(spell_id_number) + ", 85),\n\t"
    elif class_word == "arcana domain" or class_word == "arcana":
        return "(" + str(spell_id_number) + ", 36),\n\t"
    elif class_word == "nature":
        return "(" + str(spell_id_number) + ", 26),\n\t"
    elif class_word == "trickery":
        return "(" + str(spell_id_number) + ", 100),\n\t"
    elif class_word == "domainoath of the watchers":
        return "(" + str(spell_id_number) + ", 72),\n\t"
    elif class_word == "forge":
        return "(" + str(spell_id_number) + ", 33),\n\t"
    elif class_word == "tempest":
        return "(" + str(spell_id_number) + ", 27),\n\t"
    elif class_word == "death":
        return "(" + str(spell_id_number) + ", 30),\n\t"
    elif class_word == "domainthe genie":
        return "(" + str(spell_id_number) + ", 62),\n\t"
    elif class_word == "domainoath of vengeance":
        return "(" + str(spell_id_number) + ", 67),\n\t"
    elif class_word == "the undying":
        return "(" + str(spell_id_number) + ", 59),\n\t"
    elif class_word == "domainoath of the ancients":
        return "(" + str(spell_id_number) + ", 66),\n\t"
    elif class_word == "twilight":
        return "(" + str(spell_id_number) + ", 31),\n\t"
    elif class_word == "oath of the open sea":
        return "(" + str(spell_id_number) + ", 135),\n\t"
    elif class_word == "clericdruid":
        return "(" + str(spell_id_number) + ", 22),\n\t ( " + str(spell_id_number) + ", 46),\n\t"
    elif class_word == "knowledge domainlight":
        return "(" + str(spell_id_number) + ", 23),\n\t ( " + str(spell_id_number) + ", 25),\n\t"
    elif class_word == "paladin.war domain":
        return "(" + str(spell_id_number) + ", 64),\n\t ( " + str(spell_id_number) + ", 29),\n\t"
    elif class_word == "the undyingthe fathomless":
        return "(" + str(spell_id_number) + ", 59),\n\t ( " + str(spell_id_number) + ", 61),\n\t"
    elif class_word == "circle of sporesalchemist":
        return "(" + str(spell_id_number) + "51, ),\n\t ( " + str(spell_id_number) + ", 110),\n\t"
    elif class_word == "artificer≤circle of the land (grassland)":
        return "(" + str(spell_id_number) + ", 108),\n\t ( " + str(spell_id_number) + ", 47),\n\t"
    elif class_word == "sorcererwarlockwizard":
        return ("(" + str(spell_id_number) + ", 122),\n\t ( "
                + str(spell_id_number) + ", 54),\n\t ("
                + str(spell_id_number) + ", 85),\n\t ")
    elif class_word == "the archfeythe hexblade":
        return ("(" + str(spell_id_number) + ", 55),\n\t ( "
                + str(spell_id_number) + ", 60),\n\t")
    elif class_word == "bardsorcererwizardartificer":
        return ("(" + str(spell_id_number) + ", 113),\n\t ( "
                + str(spell_id_number) + ", 122),\n\t ("
                + str(spell_id_number) + ", 85),\n\t "
                + str(spell_id_number) + ", 108),\n\t ")
    elif class_word == "bardclericdruidartificerpeace domainthe celestial":
        return ("(" + str(spell_id_number) + ", 133),\n\t ( "
                + str(spell_id_number) + ", 22),\n\t ("
                + str(spell_id_number) + ", 46),\n\t ("
                + str(spell_id_number) + ", 108\n\t ("
                + str(spell_id_number) + ", 35\n\t ("
                + str(spell_id_number) + ", 58\n\t (")
    elif class_word == "domain":
        print("skipped")
    else:
        return "--  " + class_word + "   --> Not found\n\t"


# RUN ====================================================
Run_Parser_In_Dir(path)
