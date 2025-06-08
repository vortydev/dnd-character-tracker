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

land_natures_wand = SubclassFeature(
    name="Nature's Wand",
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
    land_lands_stride, land_natures_wand, land_natures_sanctuary,
]
