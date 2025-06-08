# feature_list/class_features/druid_features.py
from class_base import ClassType
from class_feature import ClassFeature

# === Druidic ===
druid_feat_druidic = ClassFeature(
    name="Druidic",
    description="You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic.",
    class_type=ClassType.DRUID
)

# === Spellcasting ===
druid_subfeat_cantrips = ClassFeature(
    name="Cantrips",
    description="At 1st level, you know two cantrips of your choice from the druid spell list. You learn additional druid cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Druid table.",
    class_type=ClassType.DRUID
)

druid_subfeat_prepare = ClassFeature(
    name="Preparing and Casting Spells",
    description="The Druid table shows how many spell slots you have to cast your druid spells of 1st level and higher. To cast one of these druid spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.\
        \nYou prepare the list of druid spells that are available for you to cast, choosing from the druid spell list. When you do so, choose a number of druid spells equal to your Wisdom modifier + your Druid level (minimum of one spell). The spells must be of a level for which you have spell slots.\
        \nFor example, if you are a 3rd-level druid, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.\
        \nYou can also change your list of prepared spells when you finish a long rest. Preparing a new list of druid spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.",
    class_type=ClassType.DRUID
)

druid_subfeat_spellcasting_ability = ClassFeature(
    name="Spellcasting Ability",
    description="Wisdom is your spellcasting ability for your druid spells, since your magic draws upon your devotion and attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a druid spell you cast and when making an attack roll with one.",
    class_type=ClassType.DRUID,
    subfeatures=[
        ClassFeature(
            name="Spell save DC",
            description="8 + your proficiency bonus + your Wisdom modifier",
            class_type=ClassType.DRUID
        ),
        ClassFeature(
            name="Spell attack modifier",
            description="your proficiency bonus + your Wisdom modifier",
            class_type=ClassType.DRUID
        )
    ]
)

druid_subfeat_ritual_casting = ClassFeature(
    name="Ritual Casting",
    description="You can cast a druid spell as a ritual if that spell has the ritual tag and you have the spell prepared.",
    class_type=ClassType.DRUID
)

druid_subfeat_spellcasting_focus = ClassFeature(
    name="Spellcasting Focus",
    description="You can use a druidic focus as a spellcasting focus for your druid spells.",
    class_type=ClassType.DRUID
)

druid_feat_spellcasting = ClassFeature(
    name="Spellcasting",
    description="Drawing on the divine essence of nature itself, you can cast spells to shape that essence to your will.",
    class_type=ClassType.DRUID,
    subfeatures=[
        druid_subfeat_cantrips,
        druid_subfeat_prepare,
        druid_subfeat_spellcasting_ability,
        druid_subfeat_ritual_casting,
        druid_subfeat_spellcasting_focus,
    ]
)

# === Wild Shape ===
druid_feat_wild_shape = ClassFeature(
    name="Wild Shape",
    description="Starting at 2nd level, you can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.\
        \nYour druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed.\
        \nTABLE [[Beat Shapes]] [Level,, Max. CR,, Limitations,, Example] : [2nd,, 1/4,, No flying or swimming speed,, Wolf]; [4th,, 1/2,, No flying speed,, Crocodile]; [8th,, 1,, ,, Giant eagle]\
        \nYou can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.\
        \nWhile you are transformed, the following rules apply :\
        \n- Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.\
        \n- When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.\
        \n- You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.\
        \n- You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.\
        \n- You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.",
    class_type=ClassType.DRUID,
)

# === Druid Circle ===
druid_feat_druid_circle = ClassFeature(
    name="Druid Circle",
    description="At 2nd level, you choose to identify with a circle of druids. Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level.\
        \nTABLE[Circle,, Source]: [Dreams,, Xanathar's Guide to Everything]; [Land,, Player's Handbook]; [Moon,, Player's Handbook]; [Sheperd,, Xanathar's Guide to Everything; [Spores,, Tasha's Cauldron of Everything]; [Stars,, Tasha's Cauldron of Everything]; [Wildlife,, Tasha's Cauldron of Everything]",
    class_type=ClassType.DRUID
)

# === Wild Companion ===
druid_feat_wild_companion = ClassFeature(
    name="Wild Companion (Optional)",
    description="At 2nd level, you gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the Find Familiar spell, without material components.\
        \nWhen you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your druid level.",
    class_type=ClassType.DRUID
)

# === Ability Score Improvement ===
druid_feat_asi = ClassFeature(
    name="Ability Score Improvement",
    description="When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
    class_type=ClassType.DRUID
)

# === Cantrip Versatility ===
druid_feat_cantrip_vers = ClassFeature(
    name="Cantrip Versatility (Optional)",
    description="Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the druid spell list.",
    class_type=ClassType.DRUID
)

# === Cantrip Versatility ===
druid_feat_timeless_body = ClassFeature(
    name="Timeless Body",
    description="Starting at 18th level, the primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.",
    class_type=ClassType.DRUID
)

# === Beast Spells ===
druid_feat_beast_spells = ClassFeature(
    name="Beast Spells",
    description="Beginning at 18th level, you can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components.",
    class_type=ClassType.DRUID
)

# === Archdruid ===
druid_feat_archdruid = ClassFeature(
    name="Archdruid",
    description="At 20th level, you can use your Wild Shape an unlimited number of times.\
        \nAdditionally, you can ignore the verbal and somatic components of your druid spells, as well as any material components that lack a cost and aren't consumed by a spell. You gain this benefit in both your normal shape and your beast shape from Wild Shape.",
    class_type=ClassType.DRUID
)


# === Array of DRUID class features
druid_feats: list[ClassFeature] = [
    druid_feat_druidic,
    druid_feat_spellcasting,
    druid_feat_wild_shape,
    druid_feat_druid_circle,
    druid_feat_wild_companion,
    druid_feat_asi,
    druid_feat_cantrip_vers,
    druid_feat_timeless_body,
    druid_feat_beast_spells,
    druid_feat_archdruid,
]
