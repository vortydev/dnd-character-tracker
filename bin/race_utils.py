# race_utils.py
from race import Race, Subrace

def create_subrace_variant(base: Race, subrace: Subrace) -> Race:
    return Race(
        name=base.name,
        subrace=subrace,
        speed=base.speed,
        size=base.size,
        ability_score_increase=combine_ability_scores(
            base.ability_score_increase,
            subrace.ability_score_increase
        ),
        feats={**subrace.feats},
        spells={**subrace.spells},
        info={**base.info, **subrace.info},
        languages=base.languages.copy()
    )

def combine_ability_scores(base: dict, bonus: dict) -> dict:
    result = base.copy()
    for k, v in bonus.items():
        result[k] = result.get(k, 0) + v
    return result
