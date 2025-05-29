# currency.py
from enum import Enum

class Currency(Enum):
    """
    Enum representing the different coin types in D&D.
    Each value represents a different type of currency.
    """
    CP = "Copper"
    SP = "Silver"
    EP = "Electrum"
    GP = "Gold"
    PP = "Platinum"

    def __str__(self):
        return self.name.lower()
    
    def to_gp_value(self) -> float:
        """Returns the value of 1 unit of this currency in gold pieces (GP)."""
        conversion_table = {
            Currency.CP: 0.01,
            Currency.SP: 0.1,
            Currency.EP: 0.5,
            Currency.GP: 1.0,
            Currency.PP: 10.0,
        }
        return conversion_table[self]


class CurrencyCost:
    """
    Represents a cost using a specific currency and amount.
    """
    def __init__(self, amount: int, currency: Currency = Currency.GP):
        """
        Initialize a CurrencyCost with a given amount and currency type.
        Defaults to gold pieces (GP).
        """
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return self.formatted()
    
    def formatted(self) -> str:
        """Returns a nicely formatted string like '5 gp' or '20 sp'."""
        return f"{self.amount} {str(self.currency)}"

    def to_dict(self):
        """Serialize the CurrencyCost to a dictionary."""
        return {
            "amount": self.amount,
            "currency": self.currency.name  # Save as enum name
        }
    
    def to_gp(self) -> float:
        return self.amount * self.currency.to_gp_value()

    @staticmethod
    def from_dict(data: dict) -> "CurrencyCost":
        """Deserialize a dictionary into a CurrencyCost object."""
        return CurrencyCost(
            amount=data["amount"],
            currency=Currency[data["currency"]]  # Load enum from name
        )
    
    @staticmethod
    def convert(amount: int, from_currency: Currency, to_currency: Currency) -> float:
        """
        Convert an amount from one currency to another.
        Returns a float representing the amount in the target currency.
        """
        gold_value = amount * from_currency.to_gp_value()
        return gold_value / to_currency.to_gp_value()