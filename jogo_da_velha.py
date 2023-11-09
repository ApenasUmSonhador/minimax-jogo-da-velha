"""Módulo responsável por me permitir saber a versão do Sistema Operacional (Windows ou não)
e agir de maneira correta utilizando o console a partir desse conhecimento"""
from os import system, name


def clear():
    """Função responsável por limpar o terminal"""
    # Windows
    if name == "nt":
        system("cls")

    # Outros
    else:
        system("clear")


def mostrar_tabuleiro(tab):
    """Função reponsável por apresentar estado atual do tabuleiro ao usuário"""
    clear()
    interface = "------------ \n"
    for i, _ in enumerate(tab):
        for j, _ in enumerate(tab):
            if tab[i][j] == "X":
                interface += "X"
            elif tab[i][j] == "O":
                interface += "O"
            else:
                interface += " "
            interface += " | "
        interface += "\n------------ \n"
    print(interface)


def movimento(tab, player):
    """Função responsável por computar o movimento do jogador"""
    mostrar_tabuleiro(tab)
    move = int(input(f"Digite onde quer colocar o {player}: "))
    move -= 1
    linha = move // len(tab)
    coluna = move % len(tab)
    tab[linha][coluna] = player
