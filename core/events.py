import random


class EventManager:

    def __init__(self):
        pass

    def trigger_event(self, duck):

        # 25% de chance de ocorrer um evento
        if random.randint(1, 100) > 25:
            return None

        events = [

            self.find_food,

            self.find_water,

            self.bad_night,

            self.party,

            self.rain,

            self.get_sick,

            self.win_money,

            self.lonely_day
        ]

        event = random.choice(events)

        return event(duck)

    # -------------------------
    # EVENTOS
    # -------------------------

    def find_food(self, duck):

        duck.hunger = max(
            0,
            duck.hunger - 15
        )

        return "🍞 Duckinho encontrou comida na rua! (-15 fome)"

    def find_water(self, duck):

        duck.thirst = max(
            0,
            duck.thirst - 15
        )

        return "🚰 Duckinho encontrou uma poça de água. (-15 sede)"

    def bad_night(self, duck):

        duck.stress = min(
            100,
            duck.stress + 20
        )

        return "🌙 Duckinho teve uma noite ruim. (+20 estresse)"

    def party(self, duck):

        duck.stress = max(
            0,
            duck.stress - 20
        )

        duck.alcohol = min(
            100,
            duck.alcohol + 10
        )

        return "🎉 Duckinho foi para uma festa! (-20 estresse, +10 abstinência)"

    def rain(self, duck):

        duck.thirst = max(
            0,
            duck.thirst - 10
        )

        duck.stress = max(
            0,
            duck.stress - 10
        )

        return "🌧️ Um dia chuvoso deixou Duckinho relaxado."

    def get_sick(self, duck):

        if duck.hunger > 70 or duck.thirst > 70:

            duck.is_sick = True

            return "🤒 Duckinho ficou doente por falta de cuidados!"

        return None

    def win_money(self, duck):

        if hasattr(duck, "coins"):

            duck.coins += 20

        return "💰 Duckinho encontrou 20 moedas!"

    def lonely_day(self, duck):

        duck.stress = min(
            100,
            duck.stress + 15
        )

        return "😔 Duckinho passou o dia sozinho. (+15 estresse)"