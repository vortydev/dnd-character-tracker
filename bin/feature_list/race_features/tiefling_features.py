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


# === Abyssal Tiefling ===
ua_feat_abyssal_arcana = RaceFeature(
    name="Abyssal Arcana",
    description="Each time you finish a long rest, you gain the ability to cast cantrips and spells randomly determined from a short list. At 1st level, you can cast a cantrip. When you reach 3rd level, you can also cast a 1st-level spell. At 5th level, you can cast a 2nd-level spell.\
        \n- You can cast a spell gained from this trait only once until you complete your next long rest. You can cast a cantrip gained from this trait at will, as normal. For 1st-level spells whose effect changes if cast using a spell slot of 2nd level or higher, you cast the spell as if using a 2nd-level slot. Spells of 2nd level are cast as if using a 2nd-level slot.\
        \n- At the end of each long rest, you lose the cantrips and spells previously granted by this feature, even if you did not cast them. You replace those cantrips and spells by rolling for new ones on the Abyssal Arcana Spells table. Roll separately for each cantrip and spell. If you roll the same spell or cantrip you gained at the end of your previous long rest, roll again until you get a different result.",
    race_type=RaceType.TIEFLING,
    subfeatures=[
        RaceFeature(
            name="Abyssal Arcana Spells",
            description="TABLE [d6, 1st Level, 3rd Level, 5th Level] :\
                [1, Dancing Ligths, Burning Hands, Alter Self];\
                [2, True Strike, Charm Person, Darkness];\
                [3, Light, Magic Missile, Invisibility];\
                [4, Message, Cure Wounds, Levitate];\
                [5, Spare the Dying, Tasha's Hideous Laughter, Mirror Image];\
                [6, Prestidigitation, Thunderwave, Spider Climb]",
            race_type=RaceType.TIEFLING
        )
    ]
)

ua_feat_abyssal_fortitude = RaceFeature(
    name="Abyssal Fortitude",
    description="Your hit point maximum increases by half your level (minimum 1).",
    race_type=RaceType.TIEFLING
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
    variant_tief_feat_winged,

    # UA - Abyssal
    ua_feat_abyssal_arcana,
    ua_feat_abyssal_fortitude,
]