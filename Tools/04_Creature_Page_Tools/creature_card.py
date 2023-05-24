def other_titles_by_period(line):
    line_parts = line.split(".")

    if len(line_parts[0].split()) < 3:
        line_parts[0] = "**" + line_parts[0] + "**"

    return " ".join(line_parts)


def other_titles_by_recharge(line):
    line_parts = line.split("(")

    line_parts[0] = "**" + line_parts[0].rstrip() + "**"
    line_parts[1] = "(" + line_parts[1]

    return " ".join(line_parts)


def create_stat_block():
    read_file = open("../input.txt", "r")
    stat_parts = []
    line_num = 0

    for line in read_file:

        if line_num <= 12:
            if line.startswith("STR"):
                stat_parts.append(line.rstrip())
                line_num += 1
            elif line_num > 0:
                stat_parts.append(line.rstrip())
                line_num += 1
            else:
                continue

    read_file.close()

    stat_block = " | " + stat_parts[0] + " | " + stat_parts[2] + " | " + stat_parts[4] + " | " + stat_parts[6] + " | " + stat_parts[8] + " | " + stat_parts[10] + " |\n | --- | --- | --- | --- | --- | --- |\n | " + stat_parts[1] + " | " + stat_parts[3] + " | " + stat_parts[5] + " | " + stat_parts[7] + \
        " | " + stat_parts[9] + " | " + stat_parts[11] + " |\n "

    return stat_block


def card_proccess(stat_block):
    read_file = open("../input.txt", "r")
    write_file = open("../output.txt", "w")
    line_num = 1
    stat_block_num = 0

    for line in read_file:

        if stat_block_num == 0 or stat_block_num >= 12:
            if line_num == 1:
                write_file.writelines(
                    "## [[" + line.upper().rstrip() + "]]\n\n")
                line_num += 1
            elif line.startswith("STR"):
                write_file.writelines(stat_block + "\n")
                stat_block_num += 1
            elif line.startswith("Armor Class"):
                write_file.writelines(line.replace(
                    "Armor Class", "**Armor Class**"))
            elif line.startswith("Hit Points"):
                write_file.writelines(line.replace(
                    "Hit Points", "**Hit Points**"))
            elif line.startswith("Speed"):
                write_file.writelines(line.replace(
                    "Speed", "**Speed**").rstrip())
            elif line.startswith("Skills"):
                write_file.writelines(line.replace("Skills", "\n**Skills**"))
            elif line.startswith("Saving Throws"):
                write_file.writelines(line.replace(
                    "Saving Throws", "**Saving Throws**"))
            elif line.startswith("Damage Resistances"):
                write_file.writelines(line.replace(
                    "Damage Resistances", "**Damage Resistances**"))
            elif line.startswith("Damage Immunities"):
                write_file.writelines(line.replace(
                    "Damage Immunities", "**Damage Immunities**"))
            elif line.startswith("Condition Immunitie"):
                write_file.writelines(line.replace(
                    "Condition Immunitie", "**Condition Immunitie**"))
            elif line.startswith("Senses"):
                write_file.writelines(line.replace("Senses", "**Senses**"))
            elif line.startswith("Languages"):
                write_file.writelines(line.replace(
                    "Languages", "**Languages**"))
            elif line.startswith("Multiattack"):
                write_file.writelines(line.replace(
                    "Multiattack", "***Multiattack**"))
            elif line.startswith("Actions"):
                write_file.writelines("##### " + line)
            elif line.startswith("Bonus Action"):
                write_file.writelines("##### " + line)
            elif line.startswith("Reaction"):
                write_file.writelines("##### " + line)
            elif line.startswith("Legendary Actions"):
                write_file.writelines("##### " + line)
            elif "." in line and not "(Recharge" in line:
                output = other_titles_by_period(line)
                write_file.writelines(output)
            elif "(Recharge" in line:
                output = other_titles_by_recharge(line)
                write_file.writelines(output)
            else:
                write_file.writelines(line)
        else:
            stat_block_num += 1

    write_file.writelines("\n\n---\n---\n\n")
    read_file.close()
    write_file.close()


stat_block = create_stat_block()
card_proccess(stat_block)
