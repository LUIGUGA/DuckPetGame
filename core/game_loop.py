from core.store import Store, Wallet
from minigames.car_racing import CarRacing
from models.duck import DuckDad


class Game:
    def __init__(self, duck_name: str = "Pato", starting_coins: int = 100):
        self.duck = DuckDad(duck_name)
        self.wallet = Wallet(starting_coins)
        self.store = Store.default()

    def status_text(self) -> str:
        return (
            f"=== Status do jogo ===\n"
            f"Nome: {self.duck.name}\n"
            f"Saldo: {self.wallet}\n"
            f"Fome: {self.duck.hunger}\n"
            f"Sede: {self.duck.thirst}\n"
            f"Estresse: {self.duck.stress}\n"
            f"Vontade de beber: {self.duck.alcohol}\n"
            f"Doente: {'Sim' if self.duck.is_sick else 'Nao'}"
        )

    def shop_text(self) -> str:
        items = self.store.list_items()
        return "\n".join(items)

    def buy(self, item_id: int) -> str:
        return self.store.purchase(item_id, self.wallet, self.duck)

    def play_race(self) -> str:
        message, reward = CarRacing().play()
        self.wallet.earn(reward)
        self.duck.pass_time()
        return (
            f"{message}\n"
            f"Voce ganhou {reward} moedas e agora tem {self.wallet}."
        )
