# scripts/import_spells_from_api.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import time

from utils.api_5e import fetch_all_resources_mt
from utils.spell_transformer import transform_api_spell
from spell_registry import SpellRegistry
from spell_io import save_spells_to_file

def import_spells(): 
    start = time.time()
    raw_spells = fetch_all_resources_mt("spells")
    spell_objects = [transform_api_spell(s) for s in raw_spells]
    SpellRegistry.load_bulk(spell_objects)

    # DEBUG
    # for idx, obj in enumerate(spell_objects):
    #     print(f"{idx}. {obj}")

    save_spells_to_file(spell_objects, api=True)
    # print(f"✅ Imported {len(spell_objects)} spells from API and saved to 'spells.json'.")

    print(f"✅ Imported {len(spell_objects)} spells in {time.time() - start:.2f} seconds.")

if __name__ == "__main__":
    try:
        import_spells()
    except KeyboardInterrupt:
        print("User aborted the program!")
