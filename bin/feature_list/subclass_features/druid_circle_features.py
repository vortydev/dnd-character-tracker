# feature_list/subclass_features/druid_circle_features.py
from class_base import ClassType
from subclass_ import SubclassType
from class_feature import SubclassFeature

# === Circle of the Land ===
land_bonus_cantrip = SubclassFeature(
    name="Bonus Cantrip",
    description="When you choose this circle at 2nd level, you learn one additional druid cantrip of your choice. This cantrip doesn't count against the number of druid cantrips you know.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

land_natural_recovery = SubclassFeature(
    name="Natural Recovery",
    description="Starting at 2nd level, you can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest.\
        \nFor example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

land_circle_spells = SubclassFeature(
    name="Circle Spells",
    description="Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Choose that land – arctic, coast, desert, forest, grassland, mountain, swamp, or Underdark – and consult the associated list of spells.\
        \nOnce you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.\
        \nTABLE [[Artic]] [Druid Level,, Circle Spells]: [3rd,, Hold Person, Spike Growth]; [5th,, Sleet Storm, Slow]; [7th,, Freedom of Movement, Ice Storm]; [9th,, Commune with Nature, Cone of Cold]\
        \nTABLE [[Coast]] [Druid Level,, Circle Spells]: [3rd,, Mirror Image, Misty Step]; [5th,, Water Breathing, Water Walk]; [7th,, Control Water, Freedom of Movement]; [9th,, Conjure Elemental, Scrying]\
        \nTABLE [[Desert]] [Druid Level,, Circle Spells]: [3rd,, Barkskin, Spider Climb]; [5th,, Call Lightning, Plant Growth]; [7th,, Divination, Freedom of Movement]; [9th,, Commune with Nature, Tree Stride]\
        \nTABLE [[Grassland]] [Druid Level,, Circle Spells]: [3rd,, Invisibility, Pass Without Trace]; [5th,, Daylight, Haste]; [7th,, Divination, Freedom of Movement]; [9th,, Dream, Insect Plague]\
        \nTABLE [[Mountain]] [Druid Level,, Circle Spells]: [3rd,, Spider Climb, Spike Growth]; [5th,, Lightning Bolt, Meld into Stone]; [7th,, Stone Shape, Stoneskin]; [9th,, Passwall, Wall of Stone]\
        \nTABLE [[Swamp]] [Druid Level,, Circle Spells]: [3rd,, Darkness, Melf's Acid Arrow]; [5th,, Water Walk, Stinking Cloud]; [7th,, Freedom of Movement, Locate Creature]; [9th,, Insect Plague, Scrying]\
        \nTABLE [[Underdark]] [Druid Level,, Circle Spells]: [3rd,, Spider Climb, Web]; [5th,, Gaseous Form, Stinking Cloud]; [7th,, Greater Invisibility, Stone Shape]; [9th,, Cloudkill, Insect Plague]",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

land_lands_stride = SubclassFeature(
    name="Land's Stride",
    description="Starting at 6th level, moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.\
        \nIn addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

land_natures_ward = SubclassFeature(
    name="Nature's Ward",
    description="When you reach 10th level, you can't be charmed or frightened by elementals or fey, and you are immune to poison and disease.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

land_natures_sanctuary = SubclassFeature(
    name="Nature's Sanctuary",
    description="When you reach 14th level, creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours.\
        \nThe creature is aware of this effect before it makes its attack against you.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_LAND
)

# Array of Evocation subclass feats
circle_of_the_land = [
    land_bonus_cantrip, land_natural_recovery, land_circle_spells,
    land_lands_stride, land_natures_ward, land_natures_sanctuary,
]


# === Circle of Stars ===
stars_star_map = SubclassFeature(
    name="Star Map",
    description="You've created a star chart as part of your heavenly studies. It is a Tiny object and can server as a spellcasting focus for your druid spells. You determine its form by rolling the Star Map table or by choosing one.\
        \nWhile holding this map, you have these benefits:\
        \n- You know the ITALIC[guidance] cantrip.\
        \n- You have the ITALIC[guiding bolt] spell prepared. It counts as a druid spell for you, and it doesn't count against the number of spells you can have prepared.\
        \n- You can cast ITALIC[guiding bolt] without expending a spell slot. You can do so a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.\
        \nIf you lose the map, you can perform a 1-hour ceremony to magically create a replacement. This ceremony can be performed during a short or long rest, and it destroys the previous map.\
        \nTABLE [[Star Map]] [d6,, Map Form]: [1,, A scroll covered with depictions of constellations]; [2,, A stone tablet with fine holes drilled through it]; [3,, A speckled owlbear hide, tooled with raised marks]; [4,, A collection of maps bound in an ebony cover]; [5,, A crystal that projects starry patterns when placed before a light]; [6,, Glass disks that depict constellations]",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_STARS
)

stars_starry_form = SubclassFeature(
    name="Starry Form",
    description="As a bonus action, you can expend a use of your Wild Shape feature to take on a starry form, rather than transforming into a beast.\
        \nWhile in your starry form, you retain your game statistics, but your body becomes luminous; your joints glimmer like stars, and glowing lines connect them as on a star chart. This form lasts for 10 minutes. It ends early if you dismiss it (no action required), are incapacitated, die, or use this feature again.\
        \nWhenever you assume your starry form, choose which of the following constellations glimmers on your body; your choice gives certain benefits while in the form:\
        \nBOLD[Archer :] A constellation of an archer appears on you. When you activate this form, and as a bonus action on your subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one creature within 60 feet of you. On a hit, the attack deals radiant damage equal to 1d8 + your Wisdom modifier.\
        \nBOLD[Chalice :] A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that restores hit points to a creature, you or another creature within 30 feet of you can regain hit points equal to 1d8 + your Wisdom modifier.\
        \nBOLD[Dragon :] A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a Constitution saving throw to maintain concentration on a spell, you can treat a roll of 9 or lower on the d20 as a 10.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_STARS
)

stars_cosmic_omen = SubclassFeature(
    name="Cosmic Omen",
    description="Whenever you finish a long rest, you can consult your Star Map for omens. When you do so, roll a die. Until you finish your next long rest, you gain access to a special reaction based on wether you rolled an even or an odd number on the die:\
        \nBOLD[Weal (even) :] Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use yout reaction to roll a d6 and add the number rolled to the total.\
        \nBOLD[Woe (odd) :] Whenever a creature you can see within 30 feet of you is about to make an attack roll, a saving throw, or an ability check, you can use your reaction to roll a d6 and subtract the number rolled from the total.\
        \nYou can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_STARS
)

stars_twinkling_constellations = SubclassFeature(
    name="Twinkling Constellations",
    description="The constellations of your Starry Form improve. The 1d8 of the Archer and the Chalice becomes 2d8, and while the Dragon is active, you have a flying speed of 20 feet and can hover.\
        \nMoreover, at the start of each of your turns while in your Starry Form, you can change which constellation glimmers on your body.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_STARS
)

stars_full_of_stars = SubclassFeature(
    name="Full of Stars",
    description="While in your Starry Form, you become partially incorporeal, giving you resistance to bludgeoning, piercing, and slashing damage.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_STARS
)

circle_of_stars = [
    stars_star_map, stars_starry_form,
    stars_cosmic_omen, stars_twinkling_constellations, stars_full_of_stars,
]


# === Circle of Dreams ===
dreams_balm_of_the_summer_court = SubclassFeature(
    name="Balm of the Summer Court",
    description="At 2nd level, you become imbued with the blessings of the Summer Court. You are a font of energy that offers respite from injuries. You have a pool of fey energy represented by a number of d6s equal to your druid level.\
        \nAs a bonus action, you can choose an ally you can see within 120 feet of you and spend a number of those dice equal to half your druid level or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent.\
        \nYou regain the expended dice when you finish a long rest.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_DREAMS
)

dreams_heart_of_moonlight_and_shadow = SubclassFeature(
    name="Hearth of Moonlight and Shadow",
    description="At 6th level, home can be wherever you are. During a short or long rest, you can invoke the shadowy power of the Gloaming Court to help guard your respite. At the start of the rest, you touch a point in space, and an invisible, 30-foot-radius sphere of magic appears, centered on that point. Total cover blocks the sphere.\
        \nWhile within the sphere, you and your allies gain a +5 bonus to Dexterity (Stealth) and Wisdom (Perception) checks, and any light from open flames in the sphere (a campfire, torches, or the like) isn't visible outside it.\
        \nThe sphere vanishes at the end of the rest or when you leave the sphere.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_DREAMS
)

dreams_hidden_paths  = SubclassFeature(
    name="Hidden Paths",
    description="Starting at 10th level, you can use the hidden, magical pathways that some fey use to traverse space in a blink of an eye. As a bonus action on your turn, you can teleport up to 60 feet to an unoccupied space you can see. Alternatively, you can use your action to teleport one willing creature you touch up to 30 feet to an unoccupied space you can see.\
        \nYou can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_DREAMS
)

dreams_walker_in_dreams = SubclassFeature(
    name="Walker in Dreams",
    description="At 14th level, the magic of the Feywild grants you the ability to travel mentally or physically through dreamlands.\
        \nWhen you finish a short rest, you can cast one of the following spells, without expending a spell slot or requiring material components: Dream (with you as the messenger), Scrying, or Teleportation Circle.\
        \nThis use of Teleportation Circle is special. Rather than opening a portal to a permanent teleportation circle, it opens a portal to the last location where you finished a long rest on your current plane of existence. If you haven't taken a long rest on your current plane, the spell fails but isn't wasted.\
        \nOnce you use this feature, you can't use it again until you finish a long rest.",
    class_type=ClassType.DRUID, subclass_type=SubclassType.CIRCLE_DREAMS
)

circle_of_dreams  = [
    dreams_balm_of_the_summer_court,
    dreams_heart_of_moonlight_and_shadow,
    dreams_hidden_paths,
    dreams_walker_in_dreams,
]