# feature_list/race_features/elf_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Elf ===
elf_feat_darkvision = RaceFeature(
    name="Darkvision",
    description="Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    race_type=RaceType.ELF,
)

elf_feat_fey_ancestry = RaceFeature(
    name="Fey Ancestry",
    description="You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
    race_type=RaceType.ELF,
)

elf_feat_trance = RaceFeature(
    name="Trance",
    description="Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is \"trance.\" While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.",
    race_type=RaceType.ELF,
)

elf_feat_keen_senses = RaceFeature(
    name="Keen Senses",
    description="You have proficiency in the Perception skill.",
    race_type=RaceType.ELF,
)

# === Drow ===
drow_feat_superior_darkvision = RaceFeature(
    name="Superior Darkvision",
    description="Your darkvision has a range of 120 feet, instead of 60.",
    race_type=RaceType.ELF,
)

drow_feat_sunlight_sensitivity = RaceFeature(
    name="Sunlight Sensitivity",
    description="You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight.",
    race_type=RaceType.ELF,
)

drow_feat_drow_magic = RaceFeature(
    name="Drow Magic",
    description="You know the Dancing Lights cantrip. When you reach 3rd level, you can cast the Faerie Fire spell once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the Darkness spell once and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.ELF,
)

drow_feat_drow_weapon_training = RaceFeature(
    name="Drow Weapon Training",
    description="You have proficiency with rapiers, shortswords, and hand crossbows.",
    race_type=RaceType.ELF,
)

# === High Elf ===
he_feat_cantrip = RaceFeature(
    name="Cantrip",
    description="You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.",
    race_type=RaceType.ELF,
)

he_feat_elf_weapon_training = RaceFeature(
    name="Elf Weapon Training",
    description="You have proficiency with the longsword, shortsword, shortbow, and longbow.",
    race_type=RaceType.ELF,
)

he_feat_extra_language = RaceFeature(
    name="Extra Language",
    description="You can read, speak, and write one additional language of your choice.",
    race_type=RaceType.ELF,
)

# === Wood Elf ===
we_feat_fleet_foot = RaceFeature(
    name="Fleet of Foot",
    description="Your base walking speed increases to 35 feet.",
    race_type=RaceType.ELF,
)

we_feat_mask_wild = RaceFeature(
    name="Mask of the Wild",
    description="You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.",
    race_type=RaceType.ELF,
)


elf_feats = [
    elf_feat_darkvision, elf_feat_fey_ancestry, elf_feat_trance, elf_feat_keen_senses,
    drow_feat_superior_darkvision, drow_feat_sunlight_sensitivity, drow_feat_drow_magic, drow_feat_drow_weapon_training,
    he_feat_cantrip, he_feat_elf_weapon_training, he_feat_extra_language,
    we_feat_mask_wild, we_feat_fleet_foot,
]