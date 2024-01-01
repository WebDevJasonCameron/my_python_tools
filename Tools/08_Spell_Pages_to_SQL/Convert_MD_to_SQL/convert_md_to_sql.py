# DLVs
spell = { "name" : "",
          "level" : "",
          "casting_time" : "",
          "range_area" : "",
          "component_visual" : "",
          "component_semantic" : "",
          "component_material" : "",
          "component_materials" : "",
          "duration" : "",
          "concentration" : "",
          "ritual" : "",
          "school" : "",
          "save_type" : "",
          "description" : "",
          "image_url" : "",
          "source_id" : 5}

lines = []
spell_tags = []
spell_conditions = []
spell_damagetypes = []
spell_classes = []
attributes = []

file_input = open("/Users/jasoncameron/Desktop/py_spells/Spells/acid arrow.md", "r")


# FUN
# <F> Capture_Lines
def Capture_Lines(input):
    for line in input:
        if line.strip() == "":
            continue
        else:
            lines.append(line.strip().replace("\xa0", ""));

# <F> Capture_Conditions

# <F> Capture_Damagetypes

# <F> Capture_Tags
def Capture_Tags(lines):
    for line in lines:
        if line.startswith("spell_tags:"):
            mod_line = line.replace("spell_tags:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                spell_tags.append(l.lower().strip())

# <F> Capture_Classes
def Capture_Classes(lines):
    for line in lines:
        if line.startswith("available_fore:"):
            mod_line = line.replace("available_fore:", "")
            array_line = mod_line.split(",")
            for l in array_line:
                spell_classes.append(l.lower().strip())

# <F> Capture_Attributes
def Capture_Attributes(lines):
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

#<F> Fill_In_Dictionary
def Fill_In_Spell(attributes, lines):
    count_three_dashes = 1
    string_description = ""

    for line in lines:
        if line.startswith("#"):
            spell["name"] = line.replace("# ", "")
        elif line.startswith("* - ("):
            spell["component_materials"] = line.replace("* - (", "").rstrip(")")
        elif line.startswith("!["):
            continue
        elif "---" in line and count_three_dashes <= 3:
            count_three_dashes += 1
        elif count_three_dashes == 4:
            string_description += line.replace("**","").replace("_","") + "\n"

    spell["level"] = attributes[0]
    spell["casting_time"] = attributes[1].replace("_ritual_", "")
    spell["range_area"] = attributes[2]
    spell["component_visual"] = "v" in attributes[3]
    spell["component_semantic"] = "s" in attributes[3]
    spell["component_material"] = "m" in attributes[3]
    spell["duration"] = attributes[4].replace("_concentration_", "")
    spell["school"] = attributes[5]

    spell["description"] = string_description.rstrip("\n")

# RUN ====================================================
Capture_Lines(file_input)
Capture_Tags(lines)
Capture_Classes(lines)
Capture_Attributes(lines)
Fill_In_Spell(attributes, lines)

print("name: " + spell["name"])
print("level: " + spell["level"])
print("casting time: " + spell["casting_time"])
print("range / area: " + spell["range_area"])
print("requires visual component: " + str(spell["component_visual"]))
print("requires semantic component: " + str(spell["component_semantic"]))
print("requires material component: " + str(spell["component_material"]))
print("material components: " + spell["component_materials"])
print("duration: " + spell["duration"])
print("school: " + spell["school"])
print("description: " + spell["description"])