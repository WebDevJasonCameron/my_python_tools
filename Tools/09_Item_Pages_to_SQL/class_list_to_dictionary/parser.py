import csv
data = """
1,Ammunition,
2,Armor,
3,Artificer,
4,Bane,
5,Banishment,
6,Bard,
7,Belt,
8,Buff,
10,Combat,
11,Communication,
13,Consumable,
14,Container,
15,Control,
16,Creation,
17,Cursed,
18,Damage,
19,Debuff,
20,Deception,
21,Detection,
22,Divination,
24,Eldritch Machine,
25,Enchantment,
27,Evocation,
28,Exploration,
29,Eyewear,
30,Finesse,
31,Focus,
32,Footwear,
33,Foreknowledge,
35,Handwear,
36,Healing,
37,Held,
38,Headwear,
39,Heavy,
40,Instrument,
41,Jewelry,
42,Magical,
43,Melee,
44,Movement,
45,Necklace,
46,Negates Difficult Terrain,
47,Negation,
48,Outerwear,
49,Ranged,
50,Ring,
51,Rod,
53,Sentient,
54,Scroll,
55,Scrying,
56,Shield,
57,Shapechanging,
58,Social,
60,Subclass Feature,
61,Summoning,
62,Symbiotic,
63,Staff,
64,Tag,
65,Tags,
66,Teleportation,
67,Thrown,
68,Transmutation,
69,Versatile,
70,Vestige of divergence,
71,Utility,
72,Wand,
73,Warding,
74,Warm,
75,Wondrous Item,
76,Wristwear,
"""

rows = [row.split(',') for row in data.strip().split('\n')]

result_list = []

for row in rows:
    class_id = row[0].lower()
    class_name = row[1].lower()
    subclass_name = row[2].strip().lower()

    if subclass_name == "":
        result_list.append(f'"{class_name}": {class_id},')
    else:
        result_list.append(f'"{subclass_name}": {class_id},')

output_file = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/09_Item_Pages_to_SQL/class_list_to_dictionary/output_file.txt", "w")

for item in result_list:
    output_file.writelines(item + "\n")

output_file.close()

