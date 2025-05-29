# feature_list/class_features/wizard_features.py
from class_base import ClassType
from class_feature import ClassFeature

# === Spellcasting ===
wiz_subfeat_cantrips = ClassFeature(
    name="Cantrips",
    description="At 1st level, you know three cantrips of your choice from the wizard spell list. You learn additional wizard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Wizard table.",
    class_type=ClassType.WIZARD
)

wiz_subfeat_spellbook = ClassFeature(
    name="Spellbook",
    description="At 1st level, you have a spellbook containing six 1st-level wizard spells of your choice. Your spellbook is the repository of the wizard spells you know, except your cantrips, which are fixed in your mind.",
    class_type=ClassType.WIZARD
)

wiz_subfeat_preparing_and_casting_spells = ClassFeature(
    name="Preparing and Casting Spells",
    description="The Wizard table shows how many spell slots you have to cast your wizard spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.\
        \nYou prepare the list of wizard spells that are available for you to cast. To do so, choose a number of wizard spells from your spellbook equal to your Intelligence modifier + your wizard level (minimum of one spell). The spells must be of a level for which you have spell slots. For example, if you're a 3rd-level wizard, you have four 1st-level and two 2nd-level spell slots. With an Intelligence of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination, chosen from your spellbook. If you prepare the 1st-level spell magic missile, you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.\
        \nYou can change your list of prepared spells when you finish a long rest. Preparing a new list of wizard spells requires time spent studying your spellbook and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list.",
    class_type=ClassType.WIZARD
)

wiz_subsubfeat_spell_save_dc = ClassFeature(
    name="Spell save DC",
    description="8 + your proficiency bonus + your Intelligence modifier",
    class_type=ClassType.WIZARD
)
wiz_subsubfeat_spell_attack_mod = ClassFeature(
    name="Spell attack modifier",
    description="your proficiency bonus + your Intelligence modifier",
    class_type=ClassType.WIZARD
)

wiz_subfeat_spellcasting_ability = ClassFeature(
    name="Spellcasting Ability",
    description="Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.",
    class_type=ClassType.WIZARD,
    subfeatures=[
        wiz_subsubfeat_spell_save_dc,
        wiz_subsubfeat_spell_attack_mod
    ]
)

wiz_subfeat_ritual_casting = ClassFeature(
    name="Ritual Casting",
    description="You can cast a wizard spell as a ritual if that spell has the ritual tag and you have the spell in your spellbook. You don't need to have the spell prepared.",
    class_type=ClassType.WIZARD
)

wiz_subfeat_spellcasting_focus = ClassFeature(
    name="Spellcasting Focus",
    description="You can use an arcane focus (see the Adventuring Gear section) as a spellcasting focus for your wizard spells.",
    class_type=ClassType.WIZARD
)

wiz_subfeat_learning_spells = ClassFeature(
    name="Learning Spells of 1st Level and Higher",
    description="Each time you gain a wizard level, you can add two wizard spells of your choice to your spellbook for free. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook (see \"Your Spellbook\").",
    class_type=ClassType.WIZARD
)

wiz_feat_spellcasting = ClassFeature(
    name="Spellcasting",
    description="As a student of arcane magic, you have a spellbook containing spells that show the first glimmerings of your true power. See Spells Rules for the general rules of spellcasting and the Spells Listing for the wizard spell list.",
    class_type=ClassType.WIZARD,
    subfeatures=[
        wiz_subfeat_cantrips,
        wiz_subfeat_spellbook,
        wiz_subfeat_preparing_and_casting_spells,
        wiz_subfeat_spellcasting_ability,
        wiz_subfeat_ritual_casting,
        wiz_subfeat_spellcasting_focus,
        wiz_subfeat_learning_spells,
    ]
)

# === Your Spellbook ===
wiz_subfeat_copy_spell = ClassFeature(
    name="Copying a Spell into the Book",
    description="When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a spell level you can prepare and if you can spare the time to decipher and copy it. Copying that spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation. For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.",
    class_type=ClassType.WIZARD,
)

wiz_subfeat_replace_spellbook = ClassFeature(
    name="Replacing the Book",
    description="You can copy a spell from your own spellbook into another book—for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell. If you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place.",
    class_type=ClassType.WIZARD,
)

wiz_subfeat_appearance_spellbook = ClassFeature(
    name="The Book's Appearance",
    description="Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library, or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap.",
    class_type=ClassType.WIZARD,
)

wiz_feat_your_spellbook = ClassFeature(
    name="Your Spellbook",
    description="The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard's chest, for example, or in a dusty tome in an ancient library.",
    class_type=ClassType.WIZARD,
    subfeatures=[
        wiz_subfeat_copy_spell,
        wiz_subfeat_replace_spellbook,
        wiz_subfeat_appearance_spellbook
    ]
)

# === Arcane Recovery ===
wiz_feat_arcane_recovery = ClassFeature(
    name="Arcane Recovery",
    description="You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher. For example, if you're a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots.",
    class_type=ClassType.WIZARD
)

# === Arcane Tradition ===
wiz_feat_arcane_tradition = ClassFeature(
    name="Arcane Tradition",
    description="When you reach 2nd level, you choose an arcane tradition, shaping your practice of magic through one of eight schools: Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, or Transmutation. The School of Evocation is detailed at the end of the class description, and more choices are available in other sources. Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level.",
    class_type=ClassType.WIZARD
)

# === Ability Score Improvement ===
wiz_feat_ability_score_improvement = ClassFeature(
    name="Ability Score Improvement",
    description="When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.",
    class_type=ClassType.WIZARD
)

# === Spell Mastery ===
wiz_feat_spell_mastery = ClassFeature(
    name="Spell Mastery",
    description="At 18th level, you have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal. By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.",
    class_type=ClassType.WIZARD
)

# === Signature Spells ===
wiz_feat_signature_spells = ClassFeature(
    name="Signature Spells",
    description="When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don't count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or long rest. If you want to cast either spell at a higher level, you must expend a spell slot as normal.",
    class_type=ClassType.WIZARD
)


# === Array of Wizard class features
wiz_feats: list[ClassFeature] = [
    wiz_feat_spellcasting,
    wiz_feat_your_spellbook,
    wiz_feat_arcane_recovery,
    wiz_feat_arcane_tradition,
    wiz_feat_ability_score_improvement,
    wiz_feat_spell_mastery,
    wiz_feat_signature_spells
]
