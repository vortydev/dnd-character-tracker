# feature_list/class_features/ranger_features.py
from class_base import ClassType
from class_feature import ClassFeature

# === Ability Score Improvement ===
ran_feat_ability_score_improvement = ClassFeature(
    name="Ability Score Improvement",
    description="When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
    class_type=ClassType.RANGER,
    tags=["asi"],
)

ran_feat_favored_enemy = ClassFeature(
    name="Favored Enemy",
    description="Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy commonly encountered in the wilds.\
        \nChoose a type of favored enemy: beasts, fey, humanoids, monstrosities, or undead. You gain a +2 bonus to damage rolls with weapon attacks against creatures of the chosen type. Additionally, you have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.\
        \nWhen you gain this feature, you also learn one language of your choice, typically one spoken by your favored enemy or creatures associated with it. However, you are free to pick any language you wish to learn.",
    class_type=ClassType.RANGER,
    tags=["new-language"],
)

ran_feat_favored_foe = ClassFeature(
    name="Favored Foe",
    description="This 1st-level feature replaces the Favored Enemy feature and works with the Foe Slayer feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.\
        \nWhen you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell).\
        \nThe first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you increase that damage by 1d4.\
        \nYou can use this feature to mark a favored enemy a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.\
        \nThis feature's extra damage increases when you reach certain levels in this class: to 1d6 at 6th level and to 1d8 at 14th level.",
    class_type=ClassType.RANGER,
    tags=["optional"],
)

ran_feat_natural_explorer = ClassFeature(
    name="Natural Explorer",
    description="Also at 1st level, you are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you're proficient in.\
        \nWhile traveling for an hour or more in your favored terrain, you gain the following benefits:\
        \n- Difficult terrain doesn't slow your group's travel.\
        \n- Your group can't become lost except by magical means.\
        \n- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\
        \n- If you are traveling alone, you can move stealthily at a normal pace.\
        \n- When you forage, you find twice as much food as you normally would.\
        \n- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.\
        \nYou choose additional favored terrain types at 6th and 10th level.",
    class_type=ClassType.RANGER,
)

ran_feat_natural_explorer_revised = ClassFeature(
    name="Natural Explorer (Revised)",
    description="You are a master of navigating the natural world, and you react with swift and decisive action when attacked. This grants you the following benefits:\
        \n- You ignore difficult terrain.\n- You have advantage on initative rolls\nOn your first turn during combat, you have advantage on attack rolls against creatures that have not yet acted.\
        \nIn addition, you are skilled at navigating the wilderness. You gain the following benefits when traveling for an hour or more:\
        \n- Difficult terrain doesn't slow your group's travel.\n- Your group can't become lost except by magical means.\
        \n- Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.\n- If you are traveling alone, you can move stealthily at a normal pace.\
        \n- When you forage, you find twice as much food as you normally would.\n- While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.",
    class_type=ClassType.RANGER,
    tags=["ua"],
)

ran_feat_deft_explorer = ClassFeature(
    name="Deft Explorer (Optional)",
    description="This 1st-level feature replaces the Natural Explorer feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.\
        \nYou are an unsurpassed explorer and survivor, both in the wilderness and in dealing with others on your travels. You gain the Canny benefit below, and you gain an additional benefit when you reach 6th level and 10th level in this class.",
    class_type=ClassType.RANGER,
    subfeatures=[
        ClassFeature(
            name="Canny (1st Level)",
            description="Choose one of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make using the chosen skill.\
                \nYou can also speak, read, and write 2 additional languages of your choice.",
            class_type=ClassType.RANGER,
            tags=["new-language"],
        ),
        ClassFeature(
            name="Roving (6th Level)",
            description="Your walking speed increases by 5, and you gain a climbing speed and a swimming speed equal to your walking speed.",
            class_type=ClassType.RANGER,
        ),
        ClassFeature(
            name="Tireless (10th Level)",
            description="As an action, you can give yourself a number of temporary hit points equal to 1d8 + your Wisdom modifier (minimum of 1 temporary hit point). You can use this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.\
                \nIn addition, whenever you finish a short rest, your exhaustion level, if any, is decreased by 1.",
            class_type=ClassType.RANGER,
        ),
    ],
    tags=["optional"],
)

# === Fighting Style ===
ran_feat_fighting_style = ClassFeature(
    name="Fighting Style",
    description="At 2nd level, you adopt a particular style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if you later get to choose again.",
    class_type=ClassType.RANGER,
    subfeatures=[
        ClassFeature(name="Archery (PHB)",
            description="You gain a +2 bonus to attack rolls you make with ranged weapons.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Blind Fighting (PHB)",
            description="You have blind sight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Defense (PHB)",
            description="While you are wearing armor, you gain a +1 bonus to AC.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Druidic Warrior (PHB)",
            description="You learn two cantrips of your choice from the Druid spell list. They count as ranger spells for you, and Wisdom is your spellcasting ability for them. Whenever you gain a level in this class, you can replace one of these cantrips with another cantrip from the Druid spell list.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Dueling (PHB)",
            description="When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Thrown Weapon Fighting (PHB)",
            description="You can draw a weapon that has the thrown property as part of the attack you make with the weapon.\
                \nIn addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Two-Weapon Fighting (PHB)",
            description="When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Close Quarters Shooter (UA)",
            description="When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Interception (TCE)",
            description="When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Mariner (UA)",
            description="As long as you are not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Tunnel Fighter (UA)",
            description="As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.",
            class_type=ClassType.RANGER),
        ClassFeature(name="Unarmed Fighting (TCE)",
            description="Your unarmed strikes can deal bludgeoning damage equal to 1d6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.\
                \nAt the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.",
            class_type=ClassType.RANGER),
    ]
)

# === Spellcasting ===
ran_feat_spellcasting = ClassFeature(
    name="Spellcasting",
    description="By the time you reach 2nd level, you have learned to use the magical essence of nature to cast spells, much as a druid does.",
    class_type=ClassType.RANGER,
    subfeatures=[
        ClassFeature(
            name="Spell Slots",
            description="The Ranger table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.\
                \nFor example, if you know the 1st-level spell Animal Friendship and have a 1st-level and a 2nd-level spell slot available, you can cast Animal Friendship using either slot.",
            class_type=ClassType.RANGER,
        ),
        ClassFeature(
            name="Spells Known of 1st Level and Higher",
            description="You know two 1st-level spells of your choice from the ranger spell list. The Spells Known column of the Ranger table shows when you learn more ranger spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 5th level in this class, you can learn one new spell of 1st or 2nd level.\
                \nAdditionally, when you gain a level in this class, you can choose one of the ranger spells you know and replace it with another spell from the ranger spell list, which also must be of a level for which you have spell slots.",
            class_type=ClassType.RANGER,
        ),
        ClassFeature(
            name="Spellcasting Ability",
            description="Wisdom is your spellcasting ability for your ranger spells, since your magic draws on your attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a ranger spell you cast and when making an attack roll with one.\
                \nTABLE [Condition,, Result] : [Spell save DC,, 8 + your proficiency bonus + your Wisdom modifier]; [Spell attack modifier,, your proficiency bonus + your Wisdom modifier]",
            class_type=ClassType.RANGER,
        ),
        ClassFeature(
            name="Spellcasting Focus (Optional)",
            description="At 2nd level, you can use a druidic focus as a spellcasting focus for your ranger spells. A druidic focus might be a sprig of mistletoe or holly, a wand or rod made of yew or another special wood, a staff drawn whole from a living tree, or an object incorporating feathers, fur, bones, and teeth from sacred animals.",
            class_type=ClassType.RANGER,
            tags=["optional"],
        ),
    ]
)

# === Primeval Awareness ===
ran_feat_primeval_awareness = ClassFeature(
    name="Primeval Awareness",
    description="Beginning at 3rd level, you can use your action and expend one ranger spell slot to focus your awareness on the region around you. For 1 minute per level of the spell slot you expend, you can sense whether the following types of creatures are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain): aberrations, celestials, dragons, elementals, fey, fiends, and undead. This feature doesn't reveal the creatures' location or number.",
    class_type=ClassType.RANGER,
)

ran_feat_primeval_awareness_optional = ClassFeature(
    name="Primeval Awareness (Optional)",
    description="This 3rd-level feature replaces the Primeval Awareness feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.\
        \nYou can focus your awareness through the interconnections of nature: you learn additional spells when you reach certain levels in this class if you don't already know them, as shown in the Primal Awareness Spells table. These spells don't count against the number of ranger spells you know.\
        \nTABLE [[Primal Awareness Spells]] [Ranger Level,, Spell] : [3rd,, Speak with Animals]; [5th,, Beast Sense]; [9th,, Speak with Plants]; [13th,, Locate Creature]; [17th,, Commune with Nature]\
        \nYou can cast each of these spells once without expending a spell slot. Once you cast a spell in this way, you can't do so again until you finish a long rest.",
    class_type=ClassType.RANGER,
)

ran_feat_primeval_awareness_revised = ClassFeature(
    name="Primeval Awareness (Revised)",
    description="Beginning at 3rd level, your mastery of ranger lore allows you to establish a powerful link to beasts and to the land around you.\
        \nYou have an innate ability to communicate with beasts, and they recognize you as a kindred spirit. Through sounds and gestures, you can communicate simple ideas to a beast as an action, and can read its basic mood and intent. You learn its emotional state, whether it is affected by magic of any sort, its short-term needs (such as food or safety), and actions you can take (if any) to persuade it to not attack.\
        \nYou cannot use this ability against a creature that you have attacked within the past 10 minutes.\
        \nAdditionally, you can attune your senses to determine if any of your favored enemies lurk nearby. By spending 1 uninterrupted minute in concentration (as if you were concentrating on a spell), you can sense whether any of your favored enemies are present within 5 miles of you. This feature reveals which of your favored enemies are present, their numbers, and the creatures' general direction and distance (in miles) from you.\
        \nIf there are multiple groups of your favored enemies within range, you learn this information for each group.",
    class_type=ClassType.RANGER,
    tags=["ua"],
)

# === Ranger Conclave ===
ran_feat_ranger_conclave = ClassFeature(
    name="Ranger Conclave",
    description="At 3rd level, you choose to emulate the ideals and training of a ranger conclave. Your choice grants you features at 3rd level and again at 7th, 11th, and 15th level.\
        \nTABLE [Conclave,, Source]: [Beast Master,, Player's Handbook]; [Hunter,, Player's Handbook];\
        [Gloom Stalker,, Xanathar's Guide to Everything]; [Horizon Walker,, Xanathar's Guide to Everything]; [Monster Slayer,, Xanathar's Guide to Everything];\
        [Fey Wanderer,, Tasha's Cauldron of Everything]; [Swarmkeeper,, Tasha's Cauldron of Everything]; [Drakewarden,, Fizban's Treasury of Dragons]",
    class_type=ClassType.RANGER,
    tags=["choice-subclass"],
)

# === Martial Versatility (Optional) ===
ran_feat_martial_versatility = ClassFeature(
    name="Martial Versatility (Optional)",
    description="Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, as you shift the focus of your martial practice:\
        \n- Replace a fighting style you know with another fighting style available to fighters.\
        \n- If you know any maneuvers from the Battle Master archetype, you can replace one maneuver you know with a different maneuver.",
    class_type=ClassType.RANGER,
    tags=["optional"],
)

# === Extra Attack ===
ran_feat_extra_attack = ClassFeature(
    name="Extra Attack",
    description="Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.",
    class_type=ClassType.RANGER,
    tags=["extra-attack"],
)

# === Land's Stride ===
ran_feat_lands_stride = ClassFeature(
    name="Land's Stride",
    description="Starting at 8th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.\
        \nIn addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.",
    class_type=ClassType.RANGER,
)

# === Hide in Plain Sight ===
ran_feat_hide_in_plain_sight = ClassFeature(
    name="Hide in Plain Sight",
    description="Starting at 10th level, you can spend 1 minute creating camouflage for yourself. You must have access to fresh mud, dirt, plants, soot, and other naturally occurring materials with which to create your camouflage.\
        \nOnce you are camouflaged in this way, you can try to hide by pressing yourself up against a solid surface, such as a tree or wall, that is at least as tall and wide as you are. You gain a +10 bonus to Dexterity (Stealth) checks as long as you remain there without moving or taking actions. Once you move or take an action or a reaction, you must camouflage yourself again to gain this benefit.",
    class_type=ClassType.RANGER,
)

# === Nature's Veil ===
ran_feat_natures_veil = ClassFeature(
    name="Nature's Veil (Optional)",
    description="This 10th-level feature replaces the Hide in Plain Sight feature. You gain no benefit from the replaced feature and don't qualify for anything in the game that requires it.\
        \nYou draw on the powers of nature to hide yourself from view briefly. As a bonus action, you can magically become invisible, along with any equipment you are wearing or carrying, until the start of your next turn.\
        \nYou can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
    class_type=ClassType.RANGER,
    tags=["optional"],
)

# === Vanish ===
ran_feat_vanish = ClassFeature(
    name="Vanish",
    description="Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail.",
    class_type=ClassType.RANGER,
)

# === Vanish ===
ran_feat_vanish = ClassFeature(
    name="Vanish",
    description="Starting at 14th level, you can use the Hide action as a bonus action on your turn. Also, you can't be tracked by nonmagical means, unless you choose to leave a trail.",
    class_type=ClassType.RANGER,
)

# === Feral Senses ===
ran_feat_feral_senses = ClassFeature(
    name="Feral Senses",
    description="At 18th level, you gain preternatural senses that help you fight creatures you can't see. When you attack a creature you can't see, your inability to see it doesn't impose disadvantage on your attack rolls against it.\
    \nYou are also aware of the location of any invisible creature within 30 feet of you, provided that the creature isn't hidden from you and you aren't blinded or deafened.",
    class_type=ClassType.RANGER,
)

# === Foe Slayer ===
ran_feat_foe_slayer = ClassFeature(
    name="Foe Slayer",
    description="At 20th level, you become an unparalleled hunter of your enemies. Once on each of your turns, you can add your Wisdom modifier to the attack roll or the damage roll of an attack you make against one of your favored enemies. You can choose to use this feature before or after the roll, but before any effects of the roll are applied.",
    class_type=ClassType.RANGER,
)


# === Array of Fighter class features
ran_feats: list[ClassFeature] = [
    ran_feat_ability_score_improvement,
    ran_feat_favored_foe, ran_feat_favored_enemy, ran_feat_deft_explorer, 
    ran_feat_natural_explorer, ran_feat_natural_explorer_revised,
    ran_feat_primeval_awareness, ran_feat_primeval_awareness_optional, ran_feat_primeval_awareness_revised,
    ran_feat_fighting_style, ran_feat_spellcasting,
    ran_feat_ranger_conclave, ran_feat_martial_versatility, ran_feat_extra_attack,
    ran_feat_lands_stride, ran_feat_hide_in_plain_sight,
    ran_feat_natures_veil, ran_feat_vanish, 
    ran_feat_feral_senses, ran_feat_foe_slayer,
]
