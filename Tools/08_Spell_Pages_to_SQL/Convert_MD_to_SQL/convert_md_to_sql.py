file = "/Users/jasoncameron/Desktop/py_spells/Spells/Banishing Smite.md"       # <R>  Replace
spell_id_number = "2"                                                                         # <R>  Replace

# DOC RUNNER
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

    print(spell_output)
    print(tags_output)
    print(conditions_output)
    print(damagetypes_output)
    print(classes_output)


# FUN
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
            spell["name"] = line.replace("# ", "")
        elif line.startswith("* - ("):
            spell["component_materials"] = line.replace("* - (", "").rstrip(")")
        elif line.startswith("!["):
            continue
        elif "---" in line and "|" not in line and count_three_dashes <= 3:
            count_three_dashes += 1
        elif count_three_dashes >= 4 and "|" not in line and "---" not in line:
            string_description += line.replace("**","").replace("_","") + "\n"

    spell["level"] = attributes[0]
    spell["casting_time"] = attributes[1].replace("_ritual_", "")
    spell["range_area"] = attributes[2]
    spell["component_visual"] = "v" in attributes[3]
    spell["component_semantic"] = "s" in attributes[3]
    spell["component_material"] = "m" in attributes[3]
    spell["duration"] = attributes[4].replace("_concentration_", "")
    spell["concentration"] = "_concentration_" in attributes[4]
    spell["ritual"] = "_ritual_" in attributes[1]
    spell["school"] = attributes[5]
    spell["save_type"] = attributes[6]
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
            spell["source_id"] + "')")

# <F> Tags_Output
def Tags_Output(spell_tags, spell_id_number):
    output = ""

    for tag_word in spell_tags:
        output += Get_Tag_Id_Num(tag_word, spell_id_number)

    return output.rstrip(",")

# <F> Conditions_Output
def Conditions_Output(spell_conditions, spell_id_number):
    output = ""

    for condition_word in spell_conditions:
        output += Get_Condition_Id_Num(condition_word, spell_id_number)

    return output.rstrip(",")

# <F> Damagetypes_Output
def Damagetypes_Output(spell_damagetypes, spell_id_number):
    output = ""

    for damagetype_word in spell_damagetypes:
        output += Get_Damageytpe_Id_Num(damagetype_word, spell_id_number)

    return output.rstrip(",")

# <F> Classes_Output
def Classes_Output(spell_classes, spell_id_number):
    output = ""

    for class_word in spell_classes:
        output += Get_Class_Id_Num(class_word, spell_id_number)

    return output.rstrip(",")


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
    }

    if tag_word in tag_list:
        return "("+ str(spell_id_number) + ", " + str(tag_list[tag_word]) + "),"
    else:
        return "Nothing found, <!> needs to be fixed"

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
        return "("+ str(spell_id_number) + ", " + str(condition_list[condition_word]) + "),"
    else:
        return "Nothing found, <!> needs to be fixed"

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
        return "("+ str(spell_id_number) + ", " + str(damagetype_list[damagetype_word]) + "),"
    else:
        return "Nothing found, <!> needs to be fixed"

# <f> Get_Class_Id_Num
def Get_Class_Id_Num(class_word, spell_id_number):

    class_list = {
        "rouge": 1,
        "fighter": 2,
        "cleric": 3,
        "ranger": 4,
        "druid": 5,
        "warlock": 6,
        "paladin": 7,
        "monk": 8,
        "wizard": 9,
        "barbarian": 10,
        "magician": 11,
        "artificer": 12,
        "bard": 13,
        "sourcerer": 14,
        "alchemist": 15

    }

    if class_word in class_list:
        return "("+ str(spell_id_number) + ", " + str(class_list[class_word]) + "),"
    else:
        return "\n" + class_word + "   --> Not found\n"




# RUN ====================================================
Parse_Document(file, spell_id_number)