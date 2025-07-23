# feature_list/race_features/half_elf_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Half-Elf ===
half_elf_feat_darkvision = RaceFeature(
    name="Darkvision",
    description="Thanks to your elven heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    race_type=RaceType.HALF_ELF,
)

half_elf_feat_fey_ancestry = RaceFeature(
    name="Fey Ancestry",
    description="You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
    race_type=RaceType.HALF_ELF,
)

half_elf_feat_versatility = RaceFeature(
    name="Half-Elf Versatility",
    description="Choose one of the following traits:",
    race_type=RaceType.HALF_ELF,
    subfeatures=[
        RaceFeature(
            name="Skill Versatility (General)",
            description="You gain proficiency in two skills of your choice.",
            race_type=RaceType.HALF_ELF,
        ),
        RaceFeature(
            name="Elf Weapon Training (High or Wood Elf Heritage)",
            description="You have proficiency with the longsword, shortsword, shortbow, and longbow.",
            race_type=RaceType.HALF_ELF,
        ),
        RaceFeature(
            name="Cantrip (High Elf Heritage)",
            description="You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.",
            race_type=RaceType.HALF_ELF,
        ),
        RaceFeature(
            name="Fleet of Foot (Wood Elf Heritage)",
            description="Your base walking speed increases to 35 feet.",
            race_type=RaceType.HALF_ELF,
            tags=["speed-35"],
        ),
        RaceFeature(
            name="Mask of the Wild (Wood Elf Heritage)",
            description="You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.",
            race_type=RaceType.HALF_ELF,
        ),
        RaceFeature(
            name="Drow Magic (Dark Elf Heritage)",
            description="You know the Dancing Lights cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.",
            race_type=RaceType.HALF_ELF,
        ),
        RaceFeature(
            name="Swim Speed (Aquatic Elf Heritage)",
            description="You have a swimming speed of 30 feet.",
            race_type=RaceType.HALF_ELF,
            tags=["speed-swim-30"],
        ),
    ],
)

half_elf_feats = [
    half_elf_feat_darkvision, half_elf_feat_fey_ancestry, half_elf_feat_versatility,
]