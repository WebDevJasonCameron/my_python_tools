import re


def get_meta():
    meta_data = {"source": "", "cost": "", "item_tag": ""}
    read_file = open("../input.txt", "r")
    tag_flag = False
    tag_list = []

    for line in read_file:
        if tag_flag == False:
            if "Cost:" in line and "Weight:" in line:
                pattern = r'Cost:(.*?)Weight:'
                match = re.search(pattern, line)
                meta_data["cost"] = match.group(1).strip()
            if "Tags:" in line:
                tag_flag = True
        elif tag_flag and line != "\n":
            if "Basic Rules" in line or "Player's Handbook" in line:
                meta_data["source"] = line
            else:
                tag_list.append(line.rstrip())
                print(line)

    meta_data["item_tag"] = (", ").join(tag_list)

    read_file.close()

    print(meta_data)

    return meta_data


def build_meta_block(source, cost, item_tag):
    meta_block = "---\n" + \
        "ttrpg: DND5E \n" + \
        "source: " + source + "\n" + \
        "asset_type:\n" + \
        " - item\n" + \
        " - gear and equipment\n" + \
        " - \n" + \
        "rarity: " + "\n" + \
        "renowned_quality: \n" + \
        "req_attunement: \n" + \
        "is_cursed: \n" + \
        "cost: " + cost + "\n" + \
        "item_tag: " + item_tag + "\n" + \
        "---\n"
    return meta_block


def doc_processing(meta_block):
    read_file = open("../input.txt", "r")
    write_file = open("../output.txt", "w")
    line_num = 0
    end_flag = False

    write_file.writelines(meta_block)

    for line in read_file:
        if end_flag == False:
            if line_num == 0:
                write_file.writelines("# " + line + "\n")
                line_num += 1
            elif "Tags:" in line:
                end_flag = True
            else:
                write_file.writelines(line + "\n")
        elif end_flag == True:
            continue

    read_file.close()
    write_file.close()


# START PROGRAM

# Vars
meta_data = {}
meta_data = get_meta()
source = meta_data.get("source")
cost = meta_data.get("cost")
item_tag = meta_data.get("item_tag")

# Blocks
meta_block = build_meta_block(source, cost, item_tag)

# Doc
doc_processing(meta_block)
