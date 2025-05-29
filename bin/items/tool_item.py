# tool_item.py
from enum import Enum
from currency import CurrencyCost
from items.item import Item, ItemType

class ToolType(Enum):
    ARTISAN = "Artisan's tools"
    GAMING = "Gaming set"
    MUSICAL = "Musical instrument"
    MISC = "Miscellaneous"

class ToolItem(Item):
    """Tool item object"""
    def __init__(self, name: str, tool_type: ToolType, description: str = None, cost: CurrencyCost = None, weight: float = None):
        super().__init__(name, description, cost, weight, item_type=ItemType.TOOL)
        self.tool_type = tool_type
    
    def to_dict(self) -> dict:
        item = super().to_dict()
        item["tool_type"] = self.tool_type.value
        return item
    
    @staticmethod
    def from_dict(data: dict) -> "ToolItem":
        item = Item.from_dict(data)
        return ToolItem(
            name=item.name,
            tool_type=ToolType(data["tool_type"]),
            description=item.description,
            cost=item.cost,
            weight=item.weight,
        )