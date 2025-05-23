# feature_list/subclass_features/fighter_martial_archetype_features.py
from class_ import ClassType
from subclass_ import SubclassType
from class_feature import SubclassFeature

# === Champion ===
chmp_improved_critical = SubclassFeature(
    name="Improved Critical",
    description="Beginning when you choose this archetype at 3rd level, your weapon attacks score a critical hit on a roll of 19 or 20.",
    class_type=ClassType.FIGHTER,
    subclass_type=SubclassType.CHAMPION
)

chmp_remarkable_athlete = SubclassFeature(
    name="Remarkable Athlete",
    description="Starting at 7th level, you can add half your proficiency bonus (round up) to any Strength, Dexterity, or Constitution check you make that doesn't already use your proficiency bonus. In addition, when you make a running long jump, the distance you can cover increases by a number of feet equal to your Strength modifier.",
    class_type=ClassType.FIGHTER,
    subclass_type=SubclassType.CHAMPION
)

chmp_additonal_fighting_style = SubclassFeature(
    name="Additional Fighting Style",
    description="At 10th level, you can choose a second option from the Fighting Style class feature.",
    class_type=ClassType.FIGHTER,
    subclass_type=SubclassType.CHAMPION
)

chmp_superior_critical = SubclassFeature(
    name="Superior Critical",
    description="Starting at 15th level, your weapon attacks score a critical hit on a roll of 18-20.",
    class_type=ClassType.FIGHTER,
    subclass_type=SubclassType.CHAMPION
)

chmp_survivor = SubclassFeature(
    name="Survivor",
    description="At 18th level, you attain the pinnacle of resilience in battle. At the start of each of your turns, you regain hit points equal to 5 + your Constitution modifier if you have no more than half of your hit points left. You don't gain this benefit if you have 0 hit points.",
    class_type=ClassType.FIGHTER,
    subclass_type=SubclassType.CHAMPION
)

# Array of Champion subclass feats
ma_champion = [
    chmp_improved_critical,
    chmp_remarkable_athlete,
    chmp_additonal_fighting_style,
    chmp_superior_critical,
    chmp_survivor
]
