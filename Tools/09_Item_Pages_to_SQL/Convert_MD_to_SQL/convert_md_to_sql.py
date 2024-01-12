import os
import glob

path = "/Users/jasoncameron/Desktop/dnd_items/Items"
file = "/Users/jasoncameron/Desktop/dnd_items/Items/Staff of the Woodlands.md"

item_id_number = 1


# FINAL RUNNING FUNCTION

# FUN
# <F> Parse_Document
def Pars_Document(file):
    read_file = open(file, 'r')

    lines = Capture_Lines(read_file)

    item = Fill_In_Item(lines)       # Must be completed Prior to cond & magic bonuses

    item["has_charges"] = Search_Description_For_Word("charges", item["description"])
    item["magic_bonus_plus_1"] = Search_Description_For_Bonuses("+1", item["description"])
    item["magic_bonus_plus_2"] = Search_Description_For_Bonuses("+2", item["description"])
    item["magic_bonus_plus_3"] = Search_Description_For_Bonuses("+3", item["description"])

    conditions = Capture_Condition(item["description"])
    attached_spells = Capture_Attached_Spells(item["description"])
    item_tags = Capture_Tags(lines)
    item_types = Capture_Types(lines)

    for spell in attached_spells:
        print(spell)




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
def Capture_Condition(item_description):
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

# <f> Search_Description_For_Word
def Search_Description_For_Word(searched_word, item_description):
    mod_description = item_description.lower().replace("[", " ").replace("]", " ").replace(",", "").replace(".", "")
    array_description = mod_description.split(" ")

    for word in array_description:
        if word == searched_word:
            return True
        else:
            return False

# <f> Search_Description_For_Bonuses
def Search_Description_For_Bonuses(searched_bonus, item_description):
    mod_description = item_description.lower().replace("[", " ").replace("]", " ").replace(",", "").replace(".", "")
    array_description = mod_description.split(" ")

    for word in array_description:
        if word == searched_bonus:
            index = array_description.index(word)
            next_word = array_description[index + 1]
            if next_word == "bonus":
                return True
    return False

# <F> Capture_Attached_Spells
def Capture_Attached_Spells(item_description):
    attached_spells = []
    spells = [
        "Druidcraft",
        "Regenerate",
        "Locate Creature",
        "Spare the Dying",
        "Circle of Power",
        "Power Word Kill",
        "Bless",
        "Harm",
        "Counterspell",
        "Polymorph",
        "Mage Armor",
        "Gentle Repose",
        "Fabricate",
        "Raise Dead",
        "Call Lightning",
        "Gate",
        "Mordenkainen’s Private Sanctum",
        "Phantasmal Force",
        "Beacon of Hope",
        "Produce Flame",
        "Transport via Plants",
        "Glyph of Warding",
        "Swift Quiver",
        "Fly",
        "Nondetection",
        "Sleep",
        "Sanctuary",
        "Speak with Plants",
        "Bestow Curse",
        "Reincarnate",
        "Hunter's Mark",
        "Misty Step",
        "Evard’s Black Tentacles",
        "Etherealness",
        "Flaming Sphere",
        "Plant Growth",
        "Arcane Eye",
        "Antipathy/Sympathy",
        "Conjure Fey",
        "Modify Memory",
        "Entangle",
        "Mass Suggestion",
        "Detect Evil and Good",
        "Dominate Beast",
        "Enhance Ability",
        "Blur",
        "Dispel Magic",
        "BLIGHT",
        "Eyebite",
        "Zone of Truth",
        "Poison Spray",
        "Hex",
        "Wall of Thorns",
        "Awaken",
        "True Polymorph",
        "Slow",
        "Hail of Thorns",
        "Hypnotic Pattern",
        "Banishing Smite",
        "Conjure Volley",
        "Guards and Wards",
        "Augury",
        "Animal Friendship",
        "Feeblemind",
        "Stone Shape",
        "Chill Touch",
        "Phantasmal Killer",
        "Mirror Image",
        "Detect Magic",
        "Dominate Monster",
        "Find Steed",
        "Holy Aura",
        "Maze",
        "Arcane Lock",
        "Divination",
        "Conjure Celestial",
        "Barkskin",
        "Arcane Gate",
        "Conjure Elemental",
        "Seeming",
        "Antimagic Field",
        "Animal Shapes",
        "Wind Walk",
        "Color Spray",
        "Pass without Trace",
        "Thorn Whip",
        "Prestidigitation",
        "Find Traps",
        "Globe of Invulnerability",
        "Magic Circle",
        "Dissonant Whispers",
        "Rary's Telepathic Bond",
        "Crown of Madness",
        "Leomund’s Secret Chest",
        "Finger of Death",
        "Resurrection",
        "Ray of Enfeeblement",
        "Banishment",
        "Teleportation Circle",
        "Create or Destroy Water",
        "Confusion",
        "Charm Person",
        "Grasping Vine",
        "Blade Ward",
        "Elemental Weapon",
        "Animate Objects",
        "Guidance",
        "Levitate",
        "Arms of Hadar",
        "Clone",
        "Feign Death",
        "Create Food and Water",
        "Shillelagh",
        "Calm Emotions",
        "Inflict Wounds",
        "Mending",
        "Illusory Script",
        "Control Water",
        "Cloudkill",
        "Meld into Stone",
        "Sleet Storm",
        "Comprehend Languages",
        "Word of Recall",
        "Imprisonment",
        "True Seeing",
        "Stinking Cloud",
        "Enthrall",
        "Fog Cloud",
        "Mirage Arcane",
        "Greater Restoration",
        "Protection from Energy",
        "Contagion",
        "Remove Curse",
        "Commune with Nature",
        "Nystul’s Magic Aura",
        "Minor Illusion",
        "Mind Blank",
        "Conjure Woodland Beings",
        "Weird",
        "Drawmij's Instant Summons",
        "Sequester",
        "Demiplane",
        "Grease",
        "Identify",
        "Haste",
        "Blindness/Deafness",
        "Aid",
        "Cordon of Arrows",
        "Storm of Vengeance",
        "Disguise Self",
        "Foresight",
        "Mage Hand",
        "Protection from Evil and Good",
        "True Strike",
        "Guardian of Faith",
        "Cloud of Daggers",
        "Silvery Barbs",
        "Tasha’s Hideous Laughter",
        "Locate Object",
        "Scrying",
        "Shield of Faith",
        "Magic Weapon",
        "Heroes' Feast",
        "Knock",
        "Command",
        "Friends",
        "Commune",
        "Animal Messenger",
        "Tree Stride",
        "Clairvoyance",
        "Contact Other Plane",
        "Locate Animals or Plants",
        "Bane",
        "Otto's Irresistible Dance",
        "Spirit Guardians",
        "Protection from Poison",
        "Time Stop",
        "Mislead",
        "Incendiary Cloud",
        "Mordenkainen’s Faithful Hound",
        "Legend Lore",
        "Creation",
        "Simulacrum",
        "Suggestion",
        "Wish",
        "Move Earth",
        "Teleport",
        "Animate Dead",
        "Death Ward",
        "Circle of Death",
        "Silent Image",
        "Dimension Door",
        "Zephyr Strike",
        "Find Familiar",
        "Planar Ally",
        "Ray of Sickness",
        "Vampiric Touch",
        "Hold Person",
        "Conjure Minor Elementals",
        "Silence",
        "Dominate Person",
        "Dispel Evil and Good",
        "Heat Metal",
        "Invisibility",
        "Freedom of Movement",
        "Web",
        "Magic Jar",
        "Programmed Illusion",
        "Rope Trick",
        "Thaumaturgy",
        "Speak with Dead",
        "Feather Fall",
        "Telekinesis",
        "Insect Plague",
        "Detect Poison and Disease",
        "Fear",
        "True Resurrection",
        "Flesh to Stone",
        "Armor of Agathys",
        "Phantom Steed",
        "Gaseous Form",
        "Vicious Mockery",
        "Speak with Animals",
        "Resistance",
        "Mordenkainen’s Magnificent Mansion",
        "Message",
        "Greater Invisibility",
        "Magic Mouth",
        "Spike Growth",
        "Enlarge/Reduce",
        "Darkvision",
        "Beast Sense",
        "Find the Path",
        "Symbol",
        "Stoneskin",
        "Dream",
        "Lesser Restoration",
        "Prismatic Wall",
        "Giant Insect",
        "Project Image",
        "Aura of Life",
        "Plane Shift",
        "Jump",
        "Astral Projection",
        "Blink",
        "Major Image",
        "Forbiddance",
        "Hallucinatory Terrain",
        "Reverse Gravity",
        "Acid Splash",
        "Goodberry",
        "Revivify",
        "Geas",
        "Create Undead",
        "Planar Binding",
        "Disintegrate",
        "Water Breathing",
        "Control Weather",
        "Detect Thoughts",
        "Ensnaring Strike",
        "Expeditious Retreat",
        "Tongues",
        "Tsunami",
        "Compelled Duel",
        "Shapechange",
        "Hold Monster",
        "Warding Bond",
        "Conjure Barrage",
        "Longstrider",
        "Shield",
        "Antilife Shell",
        "Alter Self",
        "See Invisibility",
        "Tenser’s Floating Disk",
        "Spider Climb",
        "Water Walk",
        "Compulsion",
        "Alarm",
        "Unseen Servant",
        "Lightning Arrow",
        "Glibness",
        "Heroism",
        "False Life",
        "Passwall",
        "Purify Food and Drink",
        "Power Word Stun",
        "Aura of Purity",
        "Conjure Animals"
    ]

    for spell in spells:
        if spell.lower() in item_description.replace("\n", "").replace(",", " ").replace("-", " ").replace("(", " ").lower():
            attached_spells.append(spell)

    if "Friends" in attached_spells and "Animal Friendship" in attached_spells:
        attached_spells.remove("Friends")

    if "Command" in attached_spells:
        array_description = item_description.lower().split(" ")
        index = array_description.index("command")
        next_word = array_description[index + 1].replace(",", "").replace("-", "").replace(".", "")
        if next_word == "word":
            attached_spells.remove("Command")

    return attached_spells

# <F> Capture Effects

# <F> Fill_In_Item
def Fill_In_Item(lines):
    item = {"name": "",
            "ttrpg": "DND5E",
            "rarity": "",
            "renowned_quality": "",
            "requires_attunement": False,
            "has_charges": False,
            "is_cursed": False,
            "cost": "",
            "weight": "",
            "description": "",
            "image_url": "",
            "source_id": 5,
            "magic_bonus_plus_1": False,
            "magic_bonus_plus_2": False,
            "magic_bonus_plus_3": False,
            "description_notes": ""
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
        elif count_three_dashes >= 3:
            string_description += line.replace("'", "''").replace("**", "").replace("_", "").replace("[[", "").replace("]]", "") + "\n"

    item["description"] = string_description.rstrip("\n")

    return item

# RUN ====================================================
Pars_Document(file)

