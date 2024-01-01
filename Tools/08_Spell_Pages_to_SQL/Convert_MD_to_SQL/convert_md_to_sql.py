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


# FUN
# <F> Capture_Lines
def Capture_Lines(input):
    for line in input:
        if line.strip() == "":
            continue
        else:
            lines.append(line.strip());



# RUN ====================================================
Capture_Lines(file_input);
