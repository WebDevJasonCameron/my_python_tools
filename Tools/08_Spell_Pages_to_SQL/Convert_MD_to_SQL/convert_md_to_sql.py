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

file_input = open("/Users/jasoncameron/Desktop/py_spells/Spells/acid arrow.md", "r");
count_three_dashes = 0;


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





# RUN ====================================================
Capture_Lines(file_input)
Capture_Tags(lines)
Capture_Classes(lines)
Capture_Attributes(lines)

for line in attributes:
    print(line)
