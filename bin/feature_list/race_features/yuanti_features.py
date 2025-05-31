# feature_list/race_features/yuanti_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Yuan-Ti Pureblood ===
ytp_feat_darkvision = RaceFeature(
    name="Darkvision",
    description="You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    race_type=RaceType.YUANTI_PUREBLOOD,
)

ytp_feat_innate_spellcasting = RaceFeature(
    name="Innate Spellcasting",
    description="You know the Poison Spray cantrip. You can cast Animal Friendship an unlimited number of times with this trait, but you can target only snakes with it. Starting at 3rd level, you can also cast Suggestion with this trait. Once you cast it, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.YUANTI_PUREBLOOD,
)

ytp_feat_magic_resistance = RaceFeature(
    name="Magic Resistance",
    description="You have advantage on saving throws against spells and other magical effects.",
    race_type=RaceType.YUANTI_PUREBLOOD,
)

ytp_feat_poison_immunity = RaceFeature(
    name="Poison Immunity",
    description="You are immune to poison damage and the poisoned condition.",
    race_type=RaceType.YUANTI_PUREBLOOD,
)


# Array of Tiefling features
yuanti_feats = [
    # Yuan-Ti Pureblood
    ytp_feat_darkvision, ytp_feat_innate_spellcasting, ytp_feat_magic_resistance, ytp_feat_poison_immunity,
]