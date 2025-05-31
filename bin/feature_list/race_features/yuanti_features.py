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


# === Yuan-Ti Gorgon (Homebrew) ===
ytg_feat_main_snake = RaceFeature(
    name="Main Snake Heads",
    description="The ITALIC[Main Snake] heads are sentient and distinct entities with their own personalities.\
        A Yuan-Ti Gorgon starts with 2 ITALIC[Main Snake] heads at birth.",
    race_type=RaceType.YUANTI_PUREBLOOD,
    subfeatures=[
        RaceFeature(
            name="Sneaky Snake Hand Action",
            description="You may do a hand action using a ITALIC[Main Snake] as a bonus action.",
            race_type=RaceType.YUANTI_PUREBLOOD
        ),
        RaceFeature(
            name="Main Snake Bite",
            description="Once per combat, you may use an action to bite a target in melee range using the ITALIC[Main Snake] heads. The bites inflict 1d4 piercing damage per head.",
            race_type=RaceType.YUANTI_PUREBLOOD
        ),
        RaceFeature(
            name="Reptilian Growth",
            description="At each level where you gain an Ability Score Increase, choose one of the following:\
                \n- A new ITALIC[Main Snake] head grows on your head, for a maximum of 4.\
                \n- Add 1d4 piercing or 1d4 poison damage to the BOLD[Main Snake Bite] feature.",
            race_type=RaceType.YUANTI_PUREBLOOD
        ),
    ]
)

ytg_feat_poisonous_bite = RaceFeature(
    name="Poisonous Bite",
    description="Starting at level 12, choose a type of poison (approved by your DM). Once per long rest, you may inflict the chosen poison to a target within melee range.",
    race_type=RaceType.YUANTI_PUREBLOOD
)


# Array of Tiefling features
yuanti_feats = [
    # Yuan-Ti Pureblood
    ytp_feat_darkvision, ytp_feat_innate_spellcasting, ytp_feat_magic_resistance, ytp_feat_poison_immunity,

    # Yuan-Ti Gorgon
    ytg_feat_main_snake, ytg_feat_poisonous_bite,
]