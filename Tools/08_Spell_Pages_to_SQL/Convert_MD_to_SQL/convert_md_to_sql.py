
# SPELL

# 0. Get spell_id from counting up for 0
# 1. Get Name from hash
# 2. Get level from "LEVEL"                                     => 1 in table
# 3. Get casting_time from "CASTING TIME" / cut out as needed   => 2 in table
# 4. Get range_area from "RANGE/AREA"                           => 3 in table
# 5. Get component_visual from "COMPONENTS"                     => 4 in table (true/false)
# 6. Get component_semantic from "COMPONENTS"                   => 4 in table (true/false)
# 7. Get component_material from "COMPONENTS"                   => 4 in table (true/false)
# 8. Get component_materials from "* - ("                       => near end of file
# 9. Get duration from "DURATION" / May need to cut from others => 5 in table
# 10. Get concentration if "concentration" found in "DURATION"  => 5 in table
# 11. Get ritual if "Ritual" in "CASTING TIME"                  => 2 in table
# 12. Get school from "SCHOOL"                                  => 6 in table
# 13. Get save_type from "ATTACK/SAVE"                          => 7 in table
# 14. Get descripton after forth "---" and before "* -" or "!["
# 15. image_url will be null for now
# 16. source_id will be set to ttrpg source id number for dnd 5e

# -----------------------------------------------------------------------
# SPELL TAGS

# 1. Use current spell_id number
# 2. Compile all data found in spell_tags and match it with tags table.  For each match, append to 01_ file a line
"""
    5	"Banishment"
    8	"Buff"
    9	"Charmed"
    10	"Combat"
    11	"Communication"
    12	"Compulsion"
    15	"Control"
    16	"Creation"
    18	"Damage"
    19	"Debuf"
    20	"Deception"
    21	"Detection"
    23	"Dunamancy"
    26	"Environment"
    28	"Exploration"
    33	"Foreknowledge"
    34	"Foresight"
    36	"Healing"
    44	"Movement"
    47	"Negation"
    52	"Sangromancy"
    55	"Scrying"
    57	"Shapechanging"
    58	"Social"
    59	"Special"
    61	"Summoning"
    66	"Teleportation"
"""

# -----------------------------------------------------------------------
# SPELL CONDITIONS

# 1. Use current spell_id number
# 2.a. If "DAMAGE/EFFECT" matches the conditions table, but doesn't have the "(...)", append a line to the 03_ output file.
# 2.b. IF "DAMAGE/EFFECT" has a "(...)", we need to search the description for the words found in the conditions table.  Each word found needs to be a line appended to the 03_ ouput file.
"""
    1	"Blinded"
    2	"Charmed"
    3	"Deafened"
    4	"Exhaustion"
    5	"Frightened"
    6	"Grappled"
    7	"Incapacitated"
    8	"Invisible"
    9	"Paralyzed"
    10	"Petrified"
    11	"Poisoned"
    12	"Prone"
    13	"Restrained"
    14	"Stunned"
    15	"Unconscious"
"""



# -----------------------------------------------------------------------
# SPELL DAMAGETYPE

# 1. Use current spell_id number
# 2.a. If "DAMAGE/EFFECT" matches the conditions table, but doesn't have the "(...)", append a line to the 03_ output file.
# 2.b. IF "DAMAGE/EFFECT" has a "(...)", we need to search the description for the words found in the conditions table.  Each word found needs to be a line appended to the 03_ ouput file.
"""
    1	"Acid"
    2	"Bludgeoning"
    3	"Cold"
    4	"Fire"
    5	"Force"
    6	"Lightning"
    7	"Necrotic"
    8	"Piercing"
    9	"Poison"
    10	"Psychic"
    11	"Radiant"
    12	"Slashing"
    13	"Thunder"
    14	"Shortbow"
    15	"Longbow"
    16	"One-Handed Melee Attacks"
    17	"Unarmed Attacks"
    18	"Natural Attacks"
    19	"Melee Weapon Attacks"
"""

# -----------------------------------------------------------------------
# SPELL DAMAGETYPE

# 1. Use current spell_id number
# 2. Compile all data found in available_fore and match it with rpg_classes table.  For each match, append to 04_ file a line
"""
    1	"rouge"
    2	"fighter"
    3	"cleric"
    4	"ranger"
    5	"druid"
    6	"warlock"
    7	"paladin"
    8	"monk"
    9	"wizard"
    10	"barbarian"
    11	"magician"
    12	"artificer"
    13	"bard"
"""