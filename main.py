from core.game_loop import Game


def main():
    game = Game("Duckinho", starting_coins=100)
    print("=== BEM-VINDO AO TERMINAL DUCK ===")
    print("O jogo esta iniciando\n")
    print(game.status_text())
    print("\nLoja disponivel:")
    print(game.shop_text())
    print("\nPara comprar um item, chame game.buy(item_id) no codigo ou no terminal interativo.")
    print("Para ganhar moedas jogando, chame game.play_race() no terminal interativo.")


if __name__ == "__main__":
    main()
