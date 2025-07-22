# feature_list/subclass_features/sorcerer_origin_features.py
from class_base import ClassType
from subclass_ import SubclassType
from class_feature import SubclassFeature

# === Draconic Bloodline ===
db_dragon_ancestor = SubclassFeature(
    name="Dragon Ancestor",
    description="At 1st level, you choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later.\
        \nTABLE [Dragon,, Damage Type]: [Black,, Acid]; [Blue,, Lightning]; [Brass,, Fire]; [Bronze,, Lightning]; [Copper,, Acid]; [Gold,, Fire]; [Green,, Poison]; [Red,, Fire]; [Silver,, Cold]; [White,, Cold]\
        \nYou can speak, read, and write Draconic. Additionally, whenever you make a Charisma check when interacting with dragons, your proficiency bonus is doubled if it applies to the check.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DRACONIC_BLOODLINE
)

db_draconic_resilience = SubclassFeature(
    name="Draconic Resilience",
    description="As magic flows through your body, it causes physical traits of your dragon ancestors to emerge. At 1st level, your hit point maximum increases by 1 and increases by 1 again whenever you gain a level in this class. Additionally, parts of your skin are covered by a thin sheen of dragon-like scales. When you aren't wearing armor, your AC equals 13 + your Dexterity modifier.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DRACONIC_BLOODLINE
)

db_elemental_affinity = SubclassFeature(
    name="Elemental Affinity",
    description="Starting at 6th level, when you cast a spell that deals damage of the type associated with your draconic ancestry, you can add your Charisma modifier to one damage roll of that spell. At the same time, you can spend 1 sorcery point to gain resistance to that damage type for 1 hour.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DRACONIC_BLOODLINE
)

db_dragon_wings = SubclassFeature(
    name="Dragon Wings",
    description="At 14th level, you gain the ability to sprout a pair of dragon wings from your back, gaining a flying speed equal to your current speed. You can create these wings as a bonus action on your turn. They last until you dismiss them as a bonus action on your turn. You can't manifest your wings while wearing armor unless the armor is made to accommodate them, and clothing not made to accommodate your wings might be destroyed when you manifest them.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DRACONIC_BLOODLINE
)

db_draconic_presence = SubclassFeature(
    name="Draconic Presence",
    description="Beginning at 18th level, you can channel the dread presence of your dragon ancestor, causing those around you to become awestruck or frightened. As an action, you can spend 5 sorcery points to draw on this power and exude an aura of awe or fear (your choice) to a distance of 60 feet. For 1 minute or until you lose your concentration (as if you were casting a concentration spell), each hostile creature that starts its turn in this aura must succeed on a Wisdom saving throw or be charmed (if you chose awe) or frightened (if you chose fear) until the aura ends. A creature that succeeds on this saving throw is immune to your aura for 24 hours.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DRACONIC_BLOODLINE
)

# Array of Evocation subclass feats
draconic_bloodline = [
    db_dragon_ancestor,
    db_draconic_resilience,
    db_elemental_affinity,
    db_dragon_wings,
    db_draconic_presence
]

# === Divine Soul ===
ds_divine_magic = SubclassFeature(
    name="Divine Magic",
    description="Your link to the divine allows you to learn spells normally associated with the cleric class. When your Spellcasting feature lets you learn a sorcerer cantrip or a sorcerer spell of 1st level or higher, you can choose the new spell from the cleric spell list or the sorcerer spell list. You must otherwise obey all the restrictions for selecting the spell, and it becomes a sorcerer spell for you.\
        \nIn addition, choose an affinity for the source of your divine power: good, evil, law, chaos, or neutrality. You learn an additional spell based on that affinity, as shown below. It is a sorcerer spell for you, but it doesn't count against your number of sorcerer spells known. If you later replace this spell, you must replace it with a spell from the cleric spell list.\
        \nTABLE [Affinity,, Spell]: [Good,, Cure Wounds]; [Evil,, Inflict Wounds]; [Law,, Bless]; [Chaos,, Bane]; [Neutrality,, Protection from Evil and Good]",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DIVINE_SOUL,
    tags=["spell-table"],
)

ds_favored_by_the_gods = SubclassFeature(
    name="Favored by the Gods",
    description="Starting at 1st level, divine power guards your destiny. If you fail a saving throw or miss with an attack roll, you can roll 2d4 and add it to the total, possibly changing the outcome.\
        \nOnce you use this feature, you can't use it again until you finish a short or long rest.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DIVINE_SOUL
)

ds_empowered_healing = SubclassFeature(
    name="Empowered Healing",
    description="Starting at 6th level, the divine energy coursing through you can empower healing spells. Whenever you or an ally within 5 feet of you rolls dice to determine the number of hit points a spell restores, you can spend 1 sorcery point to reroll any number of those dice once, provided you aren't incapacitated. You can use this feature only once per turn.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DIVINE_SOUL
)

ds_angelic_form = SubclassFeature(
    name="Angelic Form",
    description="Starting at 14th level, you can use a bonus action to manifest a pair of spectral wings from your back. While the wings are present, you have a flying speed of 30 feet. The wings last until you're incapacitated, you die, or you dismiss them as a bonus action.\
        \nThe affinity you chose for your Divine Magic feature determines the appearance of the spectral wings: eagle wings for good or law, bat wings for evil or chaos, and dragonfly wings for neutrality.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DIVINE_SOUL
)

ds_unearthly_recovery = SubclassFeature(
    name="Unearthly Recovery",
    description="At 18th level, you gain the ability to overcome grievous injuries. As a bonus action when you have fewer than half of your hit points remaining, you can regain a number of hit points equal to half your hit point maximum.\
        \nOnce you use this feature, you can't use it again until you finish a long rest.",
    class_type=ClassType.SORCERER,
    subclass_type=SubclassType.DIVINE_SOUL
)

# Array of Evocation subclass feats
divine_soul = [
    ds_divine_magic,
    ds_favored_by_the_gods,
    ds_empowered_healing,
    ds_angelic_form,
    ds_unearthly_recovery,
]