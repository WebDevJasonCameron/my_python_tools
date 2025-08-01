import random

rpgClasses = ['barbarian',
              'bard',
              'cleric',
              'druid',
              'fighter',
              'monk',
              'paladin',
              'ranger',
              'rogue',
              'sorcerer',
              'warlock',
              'wizard',
              'artificer',
              'gunslinger',
              'blood hunter'
              ]

rpgSpecies = [
    'aarakocra',
    'aasimar',
    'air genasi',
    'ashborn',
    'astral elf',
    'auto gnome',
    'azureborn',
    'bearfolk',
    'bogborn',
    'bugbear',
    'dragonborn',
    'centaur',
    'cervan',
    'changeling',
    'corvum',
    'cnidaran',
    'curseborn',
    'cyclopian',
    'dara',
    'darakhul',
    'deepborn',
    'deep gnome',
    'the disembodied',
    'dwarf',
    'duergar',
    'earth genasi',
    'eladrin',
    'elf',
    'erina',
    'etherean',
    'fairy',
    'feral tiefling',
    'firbolg',
    'fire genasi',
    'gallus',
    'geleton',
    'geppettin',
    'giff',
    'githyanki',
    'githzerai',
    'gnarlborn',
    'gnome',
    'gobboc',
    'golynn',
    'goblin',
    'goliath',
    'graveborn',
    'grung',
    'habozee',
    'harengon',
    'halfling',
    'harvestborn',
    'hedge',
    'hobgoblin',
    'human',
    'jerbeen',
    'kalashtar',
    'kender',
    'kenku',
    'kobold',
    'leonin',
    'locathah',
    'loxodon',
    'lizardfolk',
    'luma',
    'mandrake',
    'mapach',
    'minotaur',
    'nakudama',
    'orc',
    'owlin',
    'plagueborn',
    'plasmoid',
    'quickstep',
    'raptor',
    'ratatosk',
    'relicborn',
    'ravenfolk',
    'rakin',
    'satarre',
    'satyr',
    'sea elf',
    'shade',
    'shadar-kai',
    'shadow goblin',
    'shifter',
    'silkborn',
    'simic hybrid',
    'stoneborn',
    'strig',
    'tabaxi',
    'threadborn',
    'thri-kreen',
    'tortle',
    'triton',
    'tiefling',
    'umbral human',
    'verdan',
    'vedalkin',
    'vulpin',
    'warforged',
    'water genasi',
    'wechselkind',
    'yuan-ti',
    'yuan-ti pureblood'
]

rpgBackgrounds = [
    'Acolyte',
    'Anthropologist',
    'Archaeologist',
    'Artisan',
    'Astral Drifter',
    'Athlete',
    'Azorius Functionary',
    'Boros Legionnaire',
    'Celebrity Adventurer’s Scion',
    'Charlatan',
    'City Watch / Investigator',
    'Clan Crafter',
    'Cloistered Scholar',
    'Courtier',
    'Criminal / Spy',
    'Dimir Operative',
    'Entertainer',
    'Faceless',
    'Faction Agent',
    'Failed Merchant',
    'Far Traveler',
    'Farmer',
    'Feylost',
    'Fisher',
    'Folk Hero',
    'Gambler',
    'Gate Warden',
    'Giant Foundling',
    'Gladiator',
    'Golgari Agent',
    'Gruul Anarch',
    'Guard',
    'Guide',
    'Haunted One',
    'Hermit',
    'House Agent (Cannith)',
    'House Agent (Deneith)',
    'House Agent (Ghallanda)',
    'House Agent (Jorasco)',
    'House Agent (Kundarak)',
    'House Agent (Lyrandar)',
    'House Agent (Medani)',
    'House Agent (Orien)',
    'House Agent (Phiarlan)',
    'House Agent (Sivis)',
    'House Agent (Tharashk)',
    'House Agent (Thuranni)',
    'House Agent (Vadalis)',
    'Inheritor',
    'Investigator',
    'Izzet Engineer',
    'Knight',
    'Knight of Solamnia',
    'Knight of the Order',
    'Lorehold Student',
    'Mage of High Sorcery',
    'Marine',
    'Mercenary Veteran',
    'Merchant',
    'Noble',
    'Orzhov Representative',
    'Outlander',
    'Pirate',
    'Plaintiff',
    'Planar Philosopher',
    'Prismari Student',
    'Quandrix Student',
    'Rakdos Cultist',
    'Rewarded',
    'Rival Intern',
    'Ruined',
    'Rune Carver',
    'Sage',
    'Sailor',
    'Scribe',
    'Selesnya Initiate',
    'Shipwright',
    'Silverquill Student',
    'Simic Scientist',
    'Smuggler',
    'Soldier',
    'Urban Bounty Hunter',
    'Urchin',
    'Uthgardt Tribe Member'
    'Waterdhavian Noble',
    'Wayfarer',
    'Wildspacer',
    'Witchlight Hand',
    'Witherbloom Student'
]

colors = [
    "Red",
    "Blue",
    "Yellow",
    "Green",
    "Orange",
    "Purple",
    "Pink",
    "Brown",
    "Black",
    "White",
    "Gray",
    "Baby Blue",
    "Mint Green",
    "Lavender",
    "Peach",
    "Powder Pink",
    "Sky Blue",
    "Pale Yellow",
    "Lilac",
    "Crimson",
    "Electric Blue",
    "Lime Green",
    "Magenta",
    "Tangerine",
    "Fuchsia",
    "Neon Green",
    "Cobalt",
    "Terracotta",
    "Olive",
    "Sand",
    "Mocha",
    "Forest Green",
    "Rust",
    "Clay",
    "Charcoal",
    "Rose Gold",
    "Midnight Blue",
    "Teal",
    "Coral",
    "Mustard",
    "Sage",
    "Aubergine",
    "Ice Blue"
]

gender = [
    "Male",
    "Female"
]

# Randomly select one from each array
selected_class = random.choice(rpgClasses)
selected_species = random.choice(rpgSpecies)
selected_background = random.choice(rpgBackgrounds)
selected_color = random.choice(colors)
selected_gender = random.choice(gender)

# Output result
print("Character Generator Output:")
print(f"Class: {selected_class}")
print(f"Species: {selected_species}")
print(f"Background: {selected_background}")
print(f"Favorite Color: {selected_color}")
print(f"Gender: {selected_gender}")