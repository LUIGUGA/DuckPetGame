# DuckPetGame

Jogo de terminal com pato virtual, loja de itens e minigame de corrida.

## Como jogar

1. Execute o jogo:

```bash
python main.py
```

2. No terminal interativo, crie o jogo e confira o status:

```python
from core.game_loop import Game

game = Game("Duckinho", starting_coins=100)
print(game.status_text())
```

3. Ver a loja disponível:

```python
print(game.shop_text())
```

4. Comprar um item:

```python
print(game.buy(1))  # compra o item de ID 1
print(game.status_text())
```

5. Jogar a corrida para ganhar moedas:

```python
print(game.play_race())
print(game.status_text())
```

## Itens da loja

- Racao nutritiva: reduz fome e deixa o pato mais feliz.
- Garrafa de agua: reduz sede.
- Brinquedo relaxante: diminui estresse.
- Cura do veterinario: cura o pato quando ele fica doente.
- Bebida especial: reduz a vontade de beber.

## Economia

- O jogador começa com moedas no `Wallet`.
- Cada compra gasta moedas.
- O minigame de corrida recompensa moedas conforme o desempenho.

## Arquivos importantes

- `main.py` – ponto de entrada do jogo.
- `core/store.py` – loja, itens e carteira.
- `core/game_loop.py` – lógica principal do jogo.
- `models/duck.py` – modelo de status do pato.
- `minigames/car_racing.py` – minigame que gera moedas.
