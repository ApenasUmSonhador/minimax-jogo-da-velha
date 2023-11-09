from os import system, name


def clear():
    # Windows
    if name == "nt":
        system("cls")

    # Outros
    else:
        system("clear")


def mostrar_tabuleiro(tab):
    clear()
    interface = "------------ \n"
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == "X":
                interface += "X"
            elif tab[i][j] == "O":
                interface += "O"
            else:
                interface += " "
            interface += " | "
        interface += "\n------------ \n"
    print(interface)