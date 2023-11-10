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


def movimento(tab, n, player):
    """Função responsável por computar o movimento do jogador"""
    mostrar_tabuleiro(tab)
    move = int(input(f"Digite onde quer colocar o {player}: "))
    move -= 1
    linha = move // len(tab)
    coluna = move % len(tab)
    tab[linha][coluna] = player
    n += 1
    return n


def confere_vitoria(tab, player):
    """Confere se o jogador ganhou"""

    def confere_vertical(tab, player):
        """Confere se o jogador ganhou via conexão em vertical"""
        for i, _ in enumerate(tab):
            venceu = True
            for j, _ in enumerate(tab):
                if tab[j][i] != player:
                    venceu = False
                    break
            if venceu:
                return True
        return False

    def confere_horizontal(tab, player):
        """Confere se o jogador ganhou via conexão em horizontal"""
        for i, _ in enumerate(tab):
            venceu = True
            for j, _ in enumerate(tab):
                if tab[i][j] != player:
                    venceu = False
                    break
            if venceu:
                return True
        return False

    def confere_diagonal(tab, player):
        """Confere se o jogador ganhou via conexão em diagonal"""
        venceu = True
        for i, _ in enumerate(tab):
            if tab[i][i] != player:
                venceu = False
                break
        if venceu:
            return True
        n = len(tab) - 1
        for i, _ in enumerate(tab):
            if tab[n - i][i] != player:
                return False
        return True

    vitoria = (
        confere_horizontal(tab, player)
        or confere_vertical(tab, player)
        or confere_diagonal(tab, player)
    )
    return vitoria


def confere_empate(tab, n):
    """Confere se o jogo acabou em empate 'velha'"""
    if n >= len(tab) ** 2:
        return True
    return False


def main():
    """Função que define o jogo em si e seu funcionamento."""
    tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
    vitoria = empate = False
    i = 0
    while not vitoria or not empate:
        i = movimento(tabuleiro, i, "X")
        empate = confere_empate(tabuleiro, i)
        vitoria = confere_vitoria(tabuleiro, "X")

        if empate or vitoria:
            break

        i = movimento(tabuleiro, i, "O")
        empate = confere_empate(tabuleiro, i)
        vitoria = confere_vitoria(tabuleiro, "X")
        if empate or vitoria:
            break

    mostrar_tabuleiro(tabuleiro)
    print("Fim de jogo!")


main()
