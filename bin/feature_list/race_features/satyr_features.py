# feature_list/race_features/satyr_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Satyr ===
satyr_feat_fey = RaceFeature(
    name="Fey",
    description="Your creature type is fey, rather than humanoid.",
    race_type=RaceType.SATYR,
)

satyr_feat_ram = RaceFeature(
    name="Ram",
    description="You can use your head and horns to make unarmed strikes. If you hit with them, you deal bludgeoning damage equal to 1d4 + your Strength modifier.",
    race_type=RaceType.SATYR,
)

satyr_feat_magic_resistance = RaceFeature(
    name="Magic Resistance",
    description="You have advantage on saving throws against spells and other magical effects.",
    race_type=RaceType.SATYR,
)

satyr_feat_mirthful_leaps = RaceFeature(
    name="Mirthful Leaps",
    description="Whenever you make a long or high jump, you can roll a d8 and add the number to the number of feet you cover, even when making a standing jump. This extra distance costs movement as normal.",
    race_type=RaceType.SATYR,
)

satyr_feat_reveler = RaceFeature(
    name="Reveler",
    description="You have proficiency in the Performance and Persuasion skills, and you have proficiency with one musical instrument of your choice.",
    race_type=RaceType.SATYR,
    tags=["proficiency-performance", "proficiency-persuasion", "proficiency-musical"],
)

# Array of Satyr features
satyr_feats = [
    # Satyr
    satyr_feat_fey, satyr_feat_ram, satyr_feat_magic_resistance,
    satyr_feat_mirthful_leaps, satyr_feat_reveler
]