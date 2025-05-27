# feature_list/subclass_features/sorcerer_origin_features.py
from class_ import ClassType
from subclass_ import SubclassType
from class_feature import SubclassFeature

# === Draconic Bloodline ===
db_dragon_ancestor = SubclassFeature(
    name="Dragon Ancestor",
    description="At 1st level, you choose one type of dragon as your ancestor. The damage type associated with each dragon is used by features you gain later.\
        \nTABLE [Dragon, Damage Type] : [Black, Acid]; [Blue, Lightning]; [Brass, Fire]; [Bronze, Lightning]; [Copper, Acid]; [Gold, Fire]; [Green, Poison]; [Red, Fire]; [Silver, Cold]; [White, Cold]\
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
