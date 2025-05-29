# item_registry.py
from typing import Dict, List, Optional, Tuple, Union
from items.item import Item, ItemType
from items.tool_item import ToolItem, ToolType

class ItemRegistry:
    _registry: Dict[Tuple[str, ItemType], Item] = {}

    @classmethod
    def register(cls, item: Item):
        cls._registry[item.name.lower(), item.item_type] = item

    @classmethod
    def get(cls, name: str, item_type: ItemType = ItemType.BASE) -> Item:
        return cls._registry[name.lower(), item_type]

    @classmethod
    def all(cls) -> Dict[Tuple[str, ItemType], Item]:
        return cls._registry

    @classmethod
    def clear(cls):
        cls._registry.clear()

    @classmethod
    def load_bulk(cls, items: list[Item]):
        cls.clear()
        for i in items:
            cls.register(i)
