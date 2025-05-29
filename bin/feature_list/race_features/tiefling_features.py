# feature_list/race_features/tiefling_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Base Tiefling ===
tief_feat_darkvision = RaceFeature(
    name="Darkvision",
    description="Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    race_type=RaceType.TIEFLING
)

tief_feat_hellish_resistance = RaceFeature(
    name="Hellish Resistance",
    description="You have resistance to fire damage.",
    race_type=RaceType.TIEFLING
)


# === Bloodlines ===
bloodline_asmodeus_feat_legacy = RaceFeature(
    name="Infernal Legacy",
    description="You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_baalzebul_feat_legacy = RaceFeature(
    name="Legacy of Maladomini",
    description="You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Ray of Sickness spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Crown of Madness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_dispater_feat_legacy = RaceFeature(
    name="Legacy of Dis",
    description="You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Detect Thoughts spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_fierna_feat_legacy = RaceFeature(
    name="Legacy of Phlegethos",
    description="You know the Friends cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Suggestion spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_glasya_feat_legacy = RaceFeature(
    name="Legacy of Malbolge",
    description="You know the Minor Illusion cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Invisibility spell once as a 2nd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_levistus_feat_legacy = RaceFeature(
    name="Legacy of Stygia",
    description="You know the Ray of Frost cantrip. Once you reach 3rd level, you can cast the Armor of Agathys spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_mammon_feat_legacy = RaceFeature(
    name="Legacy of Minauros",
    description="You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Tenser's Floating Disk spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Arcane Lock spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_mephistopheles_feat_legacy = RaceFeature(
    name="Legacy of Cania",
    description="You know the Mage Hand cantrip. Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)

bloodline_zariel_feat_legacy = RaceFeature(
    name="Legacy of Avernus",
    description="You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Searing Smite spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
    race_type=RaceType.TIEFLING
)


# === Variant Tiefling ===
variant_tief_feat_feral = RaceFeature(
    name="Feral",
    description="Your Intelligence score increases by 1, and your Dexterity score increases by 2. This trait replaces the Ability Score Increase trait.",
    race_type=RaceType.VARIANT_TIEFLING
)

variant_tief_feat_devils_tongue = RaceFeature(
    name="Devil's Tongue",
    description="You know the Vicious Mockery cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Enthrall spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells. This trait replaces the Infernal Legacy trait.",
    race_type=RaceType.VARIANT_TIEFLING
)

variant_tief_feat_hellfire = RaceFeature(
    name="Hellfire",
    description="Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell. This trait replaces the Hellish Rebuke spell of the Infernal Legacy trait.",
    race_type=RaceType.VARIANT_TIEFLING
)

variant_tief_feat_winged = RaceFeature(
    name="Winged",
    description="You have bat-like wings sprouting from your shoulders. You have a flying speed of 30 feet while you aren't wearing heavy armor. This trait replaces the Infernal Legacy trait.",
    race_type=RaceType.VARIANT_TIEFLING
)


# Array of Tiefling features
tiefling_feats = [
    # Base
    tief_feat_darkvision, 
    tief_feat_hellish_resistance,
    
    # Bloodlines
    bloodline_asmodeus_feat_legacy,
    bloodline_baalzebul_feat_legacy,
    bloodline_dispater_feat_legacy,
    bloodline_fierna_feat_legacy,
    bloodline_glasya_feat_legacy,
    bloodline_levistus_feat_legacy,
    bloodline_mammon_feat_legacy,
    bloodline_mephistopheles_feat_legacy,
    bloodline_zariel_feat_legacy,

    # Variant
    variant_tief_feat_feral,
    variant_tief_feat_devils_tongue,
    variant_tief_feat_hellfire,
    variant_tief_feat_winged
]