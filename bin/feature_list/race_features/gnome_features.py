# feature_list/race_features/gnome_features.py
from race_feature import RaceFeature
from race_types import RaceType

# === Gnome ===
gnome_feat_darkvision = RaceFeature(
    name="Darkvision",
    description="Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    race_type=RaceType.GNOME,
)

gnome_feat_gnome_cunning = RaceFeature(
    name="Gnome Cunning",
    description="You have advantage on all Intelligence, Wisdom, and Charisma saves against magic.",
    race_type=RaceType.GNOME,
)

# === Forest ===
forest_feat_natural_illusionist = RaceFeature(
    name="Natural Illusionist",
    description="You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it.",
    race_type=RaceType.GNOME,
)

forest_feat_speak_with_small_beasts = RaceFeature(
    name="Speak with Small Beasts",
    description="Through sound and gestures, you may communicate simple ideas with Small or smaller beasts.",
    race_type=RaceType.GNOME,
)

# === Rock ===
rock_feat_artificers_lore = RaceFeature(
    name="Artificer's Lore",
    description="Whenever you make an Intelligence (History) check related to magical, alchemical, or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus that may apply.",
    race_type=RaceType.GNOME,
)

rock_feat_tinker = RaceFeature(
    name="Tinker",
    description="You have proficiency with artisan tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. When you create a device, choose one of the following options:\
        \n- BOLD[Clockwork Toy :] This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents.\
        \n- BOLD[Fire Starter :] The device produces a miniature flame, which you can use to light a candle, torch, or campfire. Using the device requires your action.\
        \n- BOLD[Music Box :] When opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the song's end or when it is closed.\
        \nAt your DM's discretion, you may make other objects with effects similar in power to these. The Prestidigitation cantrip is a good baseline for such effects.",
    race_type=RaceType.GNOME,
)


gnome_feats = [
    gnome_feat_darkvision, gnome_feat_gnome_cunning, 
    forest_feat_natural_illusionist, forest_feat_speak_with_small_beasts,
    rock_feat_artificers_lore, rock_feat_tinker,
]