import csv



data = """
1,rouge,
2,rouge,thief
3,rouge,assassin
4,rouge,arcane trickster
5,rouge,inquisitive
6,rouge,mastermind
7,rouge,scout
8,rouge,swashbuckler
9,rouge,phantom
10,rouge,soulknife
11,fighter,
12,fighter,champion
13,fighter,battle master
14,fighter,eldritch knight
15,fighter,arcane archer
16,fighter,cavalier
17,fighter,samurai
18,fighter,psi warrior
19,fighter,rune knight
20,fighter,echo fighter
21,fighter,purple dragon knight
22,cleric,
23,cleric,knowledge domain
24,cleric,life domain
25,cleric,light domain
26,cleric,nature domain
27,cleric,tempest domain
28,cleric,trickery domain
29,cleric,war domain
30,cleric,death domain
31,cleric,twilight domain
32,cleric,order domain
33,cleric,forge domain
34,cleric,grave domain
35,cleric,peace domain
36,cleric,arcane domain
37,ranger,
38,ranger,fey wanderer
39,ranger,swarmkeeper
40,ranger,gloom stalker
41,ranger,horizon walker
42,ranger,monster slayer
43,ranger,hunter
44,ranger,beast master
45,ranger,drakewarden
46,druid,
47,druid,circle of the land
48,druid,circle of the land (arctic)
49,druid,circle of the land (coastland)
50,druid,circle of the land (desert)
51,druid,circle of the land (forest)
52,druid,circle of the land (grassland)
53,druid,circle of the land (mountains)
54,druid,circle of the land (swamps)
55,druid,circle of the land (underdark)
56,druid,circle of the moon
57,druid,circle of dreams
58,druid,circle of the shepherd
59,druid,circle of spores
60,druid,circle of stars
61,druid,circle of wildfire
62,warlock,
63,warlock,the archfey
64,warlock,the fiend
65,warlock,the great old one
66,warlock,the celestial
67,warlock,undying
68,warlock,the hexblade
69,warlock,the fathomless
70,warlock,the genie
71,warlock,the undead
72,paladin,
73,paladin,oath of devotion
74,paladin,oath of the ancients
75,paladin,oath of vengeance
76,paladin,oathbreaker
77,paladin,oath of conquest
78,paladin,oath of redemption
79,paladin,oath of glory
80,paladin,oath of the watchers
81,paladin,oath of the crown
82,paladin,oath of the open sea
83,monk,
84,monk,way of the open hand
85,monk,way of the shadow
86,monk,way of the four elements
87,monk,way of mercy
88,monk,way of the astral self
89,monk,way of the drunken master
90,monk,way of the kensei
91,monk,way of the sun soul
92,monk,way of long death
93,monk,way of the ascendant dragon
94,wizard,
95,wizard,school of abjuration
96,wizard,school of conjuration
97,wizard,school of divination
98,wizard,school of enchantment
99,wizard,school of evocation
100,wizard,school of illusion
101,wizard,school of necromancy
102,wizard,school of transmutation
103,wizard,school of graviturgy
104,wizard,school of chronurgy
105,wizard,war magic
106,wizard,bladesinging
107,wizard,order of scribes
108,barbarian,
109,barbarian,berserker
110,barbarian,totem warrior
111,barbarian,ancestral guardian
112,barbarian,storm herald
113,barbarian,zealot
114,barbarian,beast
115,barbarian,wild soul
116,barbarian,battlerager
117,artificer,
118,artificer,armorer
119,artificer,alchemist
120,artificer,artillerist
121,artificer,battle smith
122,bard,
123,bard,college of lore
124,bard,college of valor
125,bard,college of creation
126,bard,college of glamor
127,bard,college of swords
128,bard,college of whispers
129,bard,college of eloquence
130,bard,college of spirits
131,sorcerer,
132,sorcerer,aberrant mind
133,sorcerer,clockwork soul
134,sorcerer,divine soul
135,sorcerer,shadow magic
136,sorcerer,storm sorcery
137,sorcerer,draconic bloodline
138,sorcerer,wild magic
139,blood hunter,
140,blood hunter,Order of the Ghostslayer
141,blood hunter,Order of the Lycan
142,blood hunter,Order of the Mutant
143,blood hunter,Order of the Profane Soul
"""

rows = [row.split(',') for row in data.strip().split('\n')]

result_list = []

for row in rows:
    class_id = row[0]
    class_name = row[1]
    subclass_name = row[2].strip()

    if subclass_name == "":
        result_list.append(f'"{class_name}": {class_id}')
    else:
        result_list.append(f'"{subclass_name}": {class_id}')

output_file = open("/Users/jasoncameron/00_Drive/Core/Data_Engineer/my_python_tools/Tools/08_Spell_Pages_to_SQL/class_list_to_dictionary/output_file.txt", "w")

for item in result_list:
    output_file.writelines(item + "\n")

output_file.close()

