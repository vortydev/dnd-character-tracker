# feature_list/class_features/sorcerer_features.py
from class_ import ClassType
from class_feature import ClassFeature

# === Spellcasting ===
sorc_subfeat_cantrips = ClassFeature(
    name="Cantrips",
    description="At 1st level, you know four cantrips of your choice from the sorcerer spell list. You learn additional sorcerer cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Sorcerer table.",
    class_type=ClassType.SORCERER
)

sorc_subfeat_spell_slots = ClassFeature(
    name="Spell Slots",
    description="The Sorcerer table shows how many spell slots you have to cast your sorcerer spells of 1st level and higher. To cast one of these sorcerer spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finisha long rest. For example, if you know the 1st-level spell burning hands and have a 1st-level and a 2nd-level spell slot available, you can cast burning hands using either slot.",
    class_type=ClassType.SORCERER
)

sorc_subfeat_spells_known = ClassFeature(
    name="Spells Known of 1st Level and Higher",
    description="You know two 1st-level spells of your choice from the sorcerer spell list. The Spells Known column of the Sorcerer table shows when you learn more sorcerer spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level. Additionally, when you gain a level in this class, you can choose one of the sorcerer spells you know and replace it with another spell from the sorcerer spell list, which also must be of a level for which you have spell slots.",
    class_type=ClassType.SORCERER
)

sorc_subfeat_spellcasting_ability = ClassFeature(
    name="Spellcasting Ability",
    description="Charisma is your spellcasting ability for your sorcerer spells, since the power of your magic relies on your ability to project your will into the world. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a sorcerer spell you cast and when making an attack roll with one.",
    class_type=ClassType.SORCERER,
    subfeatures=[
        ClassFeature(
            name="Spell save DC",
            description="8 + your proficiency bonus + your Charisma modifier",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Spell attack modifier",
            description="your proficiency bonus + your Charisma modifier",
            class_type=ClassType.SORCERER
        )
    ]
)

sorc_subfeat_spellcasting_focus = ClassFeature(
    name="Spellcasting Focus",
    description="You can use an arcane focus (see the Adventuring Gear section) as a spellcasting focus for your sorcererz spells.",
    class_type=ClassType.SORCERER
)

sorc_feat_spellcasting = ClassFeature(
    name="Spellcasting",
    description="An event in your past, or in the life of a parent or ancestor, left an indelible mark on you, infusing you with arcane magic. This font of magic, whatever its origin, fuels your spells. See Spells Rules for the general rules of spellcasting and the Spells Listing for the sorcerer spell list.",
    class_type=ClassType.SORCERER,
    subfeatures=[
        sorc_subfeat_cantrips,
        sorc_subfeat_spell_slots,
        sorc_subfeat_spells_known,
        sorc_subfeat_spellcasting_ability,
        sorc_subfeat_spellcasting_focus,
    ]
)

# === Sorcerous Origin ===
sorc_feat_sorcerous_origin = ClassFeature(
    name="Sorcerous Origin",
    description="Choose a sorcerous origin, which describes the source of your innate magical power: Draconic Bloodline, detailed at the end of the class description, or one from another source. Your choice grants you features when you choose it at 1st level and again at 6th, 14th, and 18th level.",
    class_type=ClassType.SORCERER
)

# === Font of Magic ===
sorc_feat_font_magic = ClassFeature(
    name="Font of Magic",
    description="At 2nd level, you tap into a deep wellspring of magic within yourself. This wellspring is represented by sorcery points, which allow you to create a variety of magical effects.",
    class_type=ClassType.SORCERER,
    subfeatures=[
        ClassFeature(
            name="Sorcery Points",
            description="You have 2 sorcery points, and you gain more as you reach higher levels, as shown in the Sorcery Points column of the Sorcerer table. You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Flexible Casting",
            description="You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels. Any spell slot you create with this feature vanishes when you finish a long rest.",
            class_type=ClassType.SORCERER,
            subfeatures=[
                ClassFeature(
                    name="Creating Spell Slots",
                    description="You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. Any spell slot you create with this feature vanishes when you finish a long rest.\
                        \nTABLE [Spell Slot level, Sorcery Point Cost] : [1, 2]; [2, 3]; [3, 5]; [4, 6]; [5, 7]",
                    class_type=ClassType.SORCERER
                ),
                ClassFeature(
                    name="Converting a Spell Slot to Sorcery Points",
                    description="As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level.",
                    class_type=ClassType.SORCERER
                )
            ]
        )
    ]
)

# === Metamagic ===
# LATER At some point this could be a Sorcerer feature
sorc_feat_metamagic = ClassFeature(
    name="Metamagic",
    description="At 3rd level, you gain the ability to twist your spells to suit your needs. You gain two of the following Metamagic options of your choice. You gain another one at 10th and 17th level. You can use only one Metamagic option on a spell when you cast it, unless otherwise noted.",
    class_type=ClassType.SORCERER,
    subfeatures=[
        ClassFeature(
            name="Careful Spell",
            description="When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell's full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your Charisma modifier (minimum of one creature). A chosen creature automatically succeeds on its saving throw against the spell.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Distant Spell",
            description="When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the range of the spell. When you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Empowered Spell",
            description="When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls. You can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Extended Spell",
            description="When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Heightened Spell",
            description="When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Quickened Spell",
            description="When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Subtle Spell",
            description="When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components.",
            class_type=ClassType.SORCERER
        ),
        ClassFeature(
            name="Twinned Spell",
            description="When you cast a spell that targets only one creature and doesn't have a range of self, you can spend a number of sorcery points equal to the spell's level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).\
                \nTo be eligible, a spell must be incapable of targeting more than one creature at the spell's current level. For example, magic missile and scorching ray aren't eligible, but ray of frost and chromatic orb are.",
            class_type=ClassType.SORCERER
        ),
    ]
)

# === Ability Score Improvement ===
sorc_feat_ability_score_improvement = ClassFeature(
    name="Ability Score Improvement",
    description="When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
    class_type=ClassType.SORCERER
)

# === Sorcerous Restoration ===
sorc_feat_sorcerous_restoration = ClassFeature(
    name="Sorcerous Restoration",
    description="At 20th level, you regain 4 expended sorcery points whenever you finish a short rest.",
    class_type=ClassType.SORCERER
)


# === Array of SORCERER class features
sorc_feats: list[ClassFeature] = [
    sorc_feat_spellcasting,
    sorc_feat_sorcerous_origin,
    sorc_feat_font_magic,
    sorc_feat_metamagic,
    sorc_feat_ability_score_improvement,
    sorc_feat_sorcerous_restoration,
]
