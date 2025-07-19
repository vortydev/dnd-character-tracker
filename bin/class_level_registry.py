# class_level_registry.py
from typing import Dict, Optional, Tuple, List
from class_level import ClassLevel
from bin import ClassType, SubclassType

class ClassLevelRegistry:
    _class_levels: Dict[Tuple[ClassType, int, Optional[SubclassType]], ClassLevel] = {}

    @classmethod
    def register(cls, cl: ClassLevel):
        subclass = cl.subclass if cl.subclass else None
        print(f"[ClassLevelRegistry.register] ({cl.class_type}, {cl.level}, {repr(subclass)}), type={type(subclass)}")
        cls._class_levels[(cl.class_type, cl.level, subclass)] = cl

    @classmethod
    def get(cls, class_type: ClassType, max_level: int, subclass: SubclassType = None) -> List[ClassLevel]:
        results = []
        seen_levels = set()

        print(f"[ClassLevelRegistry.get] Requested: {class_type=} {max_level=} {subclass=}")
        print(f"[ClassLevelRegistry.get] Total keys in registry: {len(cls._class_levels)}")

        for (ct, lvl, sub), data in cls._class_levels.items():
            # Recast to unify enum identity
            try:
                ct_cast = ClassType(ct.value)
                sub_cast = SubclassType(sub.value) if sub else None
            except Exception as e:
                print(f"⛔ Failed to cast ct or sub: {e}")
                continue

            print(f"  Inspecting key: ({ct=}, {lvl=}, {sub=})")
            
            if ct_cast != class_type:
                # print(f"⛔ ClassType mismatch: {ct} != {class_type}")
                continue
            if lvl > max_level:
                # print(f"⛔ Level {lvl} > {max_level}")
                continue

            if subclass is None:
                if sub_cast is None:
                    # print(f"✅ Matched BASE level {lvl} with no subclass")
                    results.append(data)
                    seen_levels.add(lvl)
                # else:
                #     print(f"⛔ Skipped subclass level {lvl} ({sub}) since no subclass was requested")
            else:
                if sub_cast is None:
                    # print(f"✅ Matched BASE level {lvl} even though subclass={subclass}")
                    results.append(data)
                    seen_levels.add(lvl)
                elif sub_cast == subclass:
                    # print(f"✅ Matched SUBCLASS level {lvl} ({sub})")
                    results.append(data)
                    seen_levels.add(lvl)
                # else:
                #     print(f"⛔ Skipped unrelated subclass level {lvl} ({sub})")
            
            if len(seen_levels) == max_level:
                print(f"✅ Found all {max_level} levels — stopping early.")
                break

        print(f"[ClassLevelRegistry.get] → Returning {len(results)} results")
        return sorted(results, key=lambda x: x.level)

    @classmethod
    def all(cls) -> Dict[Tuple[ClassType, int, Optional[SubclassType]], ClassLevel]:
        return cls._class_levels

    @classmethod
    def clear(cls):
        cls._class_levels.clear()

    @classmethod
    def load_bulk(cls, class_levels: list[ClassLevel]):
        cls.clear()
        for cl in class_levels:
            cls.register(cl)
