# item.py
from enum import Enum
from currency import Currency, CurrencyCost

class ItemType(Enum):
    """Enum of the various Item types"""
    BASE = "Base"
    TOOL = "Tool"
    WEAPON = "Weapon"
    ARMOR = "Armor"

class Item():
    """Generic item object"""
    def __init__(self, name: str, description: str = None, cost: CurrencyCost = None, weight: float = None, item_type: ItemType = ItemType.BASE):
        """
        Initialize an item.

        Parameters:
        - name: Name of the item
        - description: Item description (optional)
        - cost: CurrencyCost object or numeric value (default currency = GP)
        - weight: Item weight (optional)
        - item_type: The type of item (default = BASE)
        """
        self.name = name
        self.description = description

        if isinstance(cost, (int, float)):
            self.cost = CurrencyCost(cost, Currency.GP)
        elif isinstance(cost, CurrencyCost) or cost is None:
            self.cost = cost
        else:
            raise TypeError("cost must be an int, float, CurrencyCost, or None")

        self.weight = weight
        self.item_type = item_type

    def to_dict(self) -> dict:
        return {
            "type": self.item_type.value,
            "name": self.name,
            "description": self.description,
            "cost": self.cost.to_dict() if self.cost else None,
            "weight": self.weight,
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Item":
        return Item(
            name=data["name"],
            description=data.get("description", None),
            cost=CurrencyCost.from_dict(data["cost"]) if data.get("cost") else None,
            weight=data.get("weight", None),
        )