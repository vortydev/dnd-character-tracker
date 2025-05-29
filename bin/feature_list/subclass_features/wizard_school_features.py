# feature_list/subclass_features/wizard_school_features.py
from class_base import ClassType
from subclass_ import SubclassType
from class_feature import SubclassFeature

# === School of Evocation ===
evo_evocation_savant = SubclassFeature(
    name="Evocation Savant",
    description="Beginning when you select this school at 2nd level, the gold and time you must spend to copy an evocation spell into your spellbook is halved.",
    class_type=ClassType.WIZARD,
    subclass_type=SubclassType.EVOCATION
)

evo_sculpt_spells = SubclassFeature(
    name="Sculpt Spells",
    description="Beginning at 2nd level, you can create pockets of relative safety within the effects of your evocation spells. When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save.",
    class_type=ClassType.WIZARD,
    subclass_type=SubclassType.EVOCATION
)

evo_potent_cantrip = SubclassFeature(
    name="Potent Cantrip",
    description="Starting at 6th level, your damaging cantrips affect even creatures that avoid the brunt of the effect. When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip.",
    class_type=ClassType.WIZARD,
    subclass_type=SubclassType.EVOCATION
)

evo_empowered_evocation = SubclassFeature(
    name="Empowered Evocation",
    description="Beginning at 10th level, you can add your Intelligence modifier to one damage roll of any wizard evocation spell you cast.",
    class_type=ClassType.WIZARD,
    subclass_type=SubclassType.EVOCATION
)

evo_overchannel = SubclassFeature(
    name="Overchannel",
    description="Starting at 14th level, you can increase the power of your simpler spells. When you cast a wizard spell of 1st through 5th level that deals damage, you can deal maximum damage with that spell. The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity.",
    class_type=ClassType.WIZARD,
    subclass_type=SubclassType.EVOCATION
)

# Array of Evocation subclass feats
school_evocation = [
    evo_evocation_savant,
    evo_sculpt_spells,
    evo_potent_cantrip,
    evo_empowered_evocation,
    evo_overchannel,
]
