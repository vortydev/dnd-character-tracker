# feature_list/race_features/human_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Human Variant ===
hv_feat_asi = RaceFeature(
    name="Ability Score Increase",
    description="Two different ability scores of your choice increase by 1.",
    race_type=RaceType.VARIANT_HUMAN,
)

hv_feat_skills = RaceFeature(
    name="Skills",
    description="You gain proficiency in one skill of your choice.",
    race_type=RaceType.VARIANT_HUMAN,
)

hv_feat_feat = RaceFeature(
    name="Feat",
    description="You gain one Feat of your choice.",
    race_type=RaceType.VARIANT_HUMAN,
)

human_variant_feats = [hv_feat_asi, hv_feat_skills, hv_feat_feat]