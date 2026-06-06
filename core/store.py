from dataclasses import dataclass
from typing import List, Optional

from models.duck import DuckDad


@dataclass
class ShopItem:
    id: int
    name: str
    price: int
    description: str
    effect: str
    value: int = 0


class Wallet:
    def __init__(self, coins: int = 100):
        self.coins = max(0, coins)

    def can_buy(self, price: int) -> bool:
        return price <= self.coins

    def spend(self, price: int) -> bool:
        if price <= 0 or not self.can_buy(price):
            return False
        self.coins -= price
        return True

    def earn(self, amount: int) -> None:
        if amount > 0:
            self.coins += amount

    def __str__(self) -> str:
        return f"{self.coins} moedas"


class Store:
    def __init__(self, items: Optional[List[ShopItem]] = None):
        self.items = items or []

    @staticmethod
    def default() -> "Store":
        items = [
            ShopItem(
                id=1,
                name="Racao nutritiva",
                price=20,
                description="Reduz a fome e mantem o pato feliz.",
                effect="feed",
                value=30,
            ),
            ShopItem(
                id=2,
                name="Garrafa de agua",
                price=15,
                description="Acaba com a sede e recupera energia.",
                effect="drink",
                value=30,
            ),
            ShopItem(
                id=3,
                name="Brinquedo relaxante",
                price=25,
                description="O pato se diverte e o estresse diminui.",
                effect="relax",
            ),
            ShopItem(
                id=4,
                name="Cura do veterinario",
                price=40,
                description="Resolve problemas de saude e coloca o pato em forma.",
                effect="heal",
            ),
            ShopItem(
                id=5,
                name="Bebida especial",
                price=30,
                description="Alivia a abstinencia e reduz a vontade de beber.",
                effect="alcohol",
                value=20,
            ),
        ]
        return Store(items)

    def list_items(self) -> List[str]:
        lines = []
        for item in self.items:
            lines.append(
                f"{item.id}. {item.name} - {item.price} moedas\n   {item.description}"
            )
        return lines

    def find_item(self, item_id: int) -> Optional[ShopItem]:
        return next((item for item in self.items if item.id == item_id), None)

    def purchase(self, item_id: int, wallet: Wallet, duck: DuckDad) -> str:
        item = self.find_item(item_id)
        if item is None:
            return "Produto nao encontrado."

        if not wallet.can_buy(item.price):
            return "Saldo insuficiente."

        wallet.spend(item.price)
        return self.apply_item(item, duck)

    def apply_item(self, item: ShopItem, duck: DuckDad) -> str:
        if item.effect == "feed":
            return duck.feed(item.value)
        if item.effect == "drink":
            return duck.drink(item.value)
        if item.effect == "relax":
            return duck.play()
        if item.effect == "heal":
            return duck.heal()
        if item.effect == "alcohol":
            return duck.drinking_alcohol(item.value)
        return "O item foi comprado, mas nada aconteceu."
