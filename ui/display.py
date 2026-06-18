import os

LARGURA_TELA = 44




def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def _linha(caractere="="):
    return caractere * LARGURA_TELA


def _cabecalho(titulo):
    print(_linha())
    print(f"  {titulo}")
    print(_linha())



def barra_progresso(valor, maximo=100, tamanho=20):
    valor = max(0, min(valor, maximo))
    preenchido = int((valor / maximo) * tamanho)
    vazio = tamanho - preenchido
    return f"[{'█' * preenchido}{'░' * vazio}] {valor}/{maximo}"


def _linha_status(rotulo, valor):
    return f"  {rotulo:<18}{barra_progresso(valor)}"

 

_PATO_FELIZ = r"""
      __
    <(^ )_    ♪
     ( ._> /
      `---'
"""

_PATO_NORMAL = r"""
      __
    <(o )_
     ( ._> /
      `---'
"""

_PATO_COM_FOME = r"""
      __
    <(o )_    barriga roncando
     ( ._> /
      `---'
"""

_PATO_ESTRESSADO = r"""
      __
    <(>~<)__
     ( ._> /
      `---'
"""

_PATO_DOENTE = r"""
      __
    <(x )_    
     ( ._> /
      `---'
"""

_PATO_FUMANDO_BEBENDO = r"""
      __
    <(o )_    cigarro na asa
     ( ._> /  copo de bebida do lado
      `---'
"""


def desenhar_pato(duck):
    if duck.is_sick:
        return _PATO_DOENTE
    if duck.stress >= 70 and duck.alcohol >= 70:
        return _PATO_FUMANDO_BEBENDO
    if duck.stress >= 70:
        return _PATO_ESTRESSADO
    if duck.hunger >= 70 or duck.thirst >= 70:
        return _PATO_COM_FOME
    if duck.hunger <= 20 and duck.thirst <= 20 and duck.stress <= 20:
        return _PATO_FELIZ
    return _PATO_NORMAL




def exibir_status(duck, wallet, turno):
    limpar_tela()
    _cabecalho(f" TERMINAL DUCK  -  Turno {turno}")
    print(desenhar_pato(duck))
    print(f"  Nome:  {duck.name}")
    print(f"  Saldo: {wallet}")
    print()
    print(_linha_status("Fome:", duck.hunger))
    print(_linha_status("Sede:", duck.thirst))
    print(_linha_status("Estresse:", duck.stress))
    print(_linha_status("Vontade de beber:", duck.alcohol))
    print(_linha_status("Vontade de fumar:", duck.stress))
    print()
    if duck.is_sick:
        print("   O pato esta doente! Leve-o ao veterinario na loja.")
        print()
    print(_linha())


def exibir_menu_principal():
    print()
    print("  O que voce quer fazer?")
    print("  1. Ir a loja")
    print("  2. Jogar corrida de carros (ganhar moedas)")
    print("  3. Jogar dados (apostar moedas)")
    print("  4. Conversar com o pato")
    print("  5. Deixar o tempo passar")
    print("  0. Sair do jogo")
    print()
    return input("  Escolha uma opcao: ").strip()


def exibir_loja(texto_loja):
    limpar_tela()
    _cabecalho(" LOJA DO PATO")
    print()
    print(texto_loja)
    print()
    print("  0. Voltar ao menu principal")
    print()
    return input("  Digite o ID do item que deseja comprar: ").strip()


def mensagem_evento(mensagem):
    print()
    print(_linha("-"))
    for linha_texto in str(mensagem).split("\n"):
        print(f"  {linha_texto}")
    print(_linha("-"))
    input("\n  Pressione ENTER para continuar...")


def tela_game_over(duck, turno):
    limpar_tela()
    _cabecalho("GAME OVER")
    print(desenhar_pato(duck))
    print(f"  {duck.name} nao aguentou mais o descuido...")
    print(f"  O jogo durou {turno} turno(s).")
    print()
    print(_linha())
    input("\n  Pressione ENTER para sair...")
