# feature_list/race_features/halfling_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Halfling ===
halfling_feat_lucky = RaceFeature(
    name="Lucky",
    description="When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.",
    race_type=RaceType.HALFLING,
)

halfling_feat_brave = RaceFeature(
    name="Brave",
    description="You have advantage on saving throws against being frightened.",
    race_type=RaceType.HALFLING,
)

halfling_feat_nimble = RaceFeature(
    name="Nimble",
    description="You can move through the space of any creature that is of a size larger than yours.",
    race_type=RaceType.HALFLING,
)

# === Lightfoot ===
lightfoot_feat_naturally_stealthy = RaceFeature(
    name="Naturally Stealthy",
    description="You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you.",
    race_type=RaceType.HALFLING,
)

# === Stout ===
stout_feat_stout_resilience = RaceFeature(
    name="Stout Resilience",
    description="You have advantage on saving throws against poison, and you have resistance to poison damage.",
    race_type=RaceType.HALFLING,
)


halfling_feats = [
    halfling_feat_lucky, halfling_feat_brave, halfling_feat_nimble,
    lightfoot_feat_naturally_stealthy,
    stout_feat_stout_resilience,
]