import random, os, time
from script import duel


def run():
    os.system("clear")
    while True:
        try:
            eleccionDelJugador = int(input(("Quieres jugar?\n1: sí\n2: no\n3: quiero irme\n")))
            if eleccionDelJugador == 1:
                # duel.
                # print('\nTodavía no sé jugar :V\n')
                duel.gameStart()
            elif eleccionDelJugador == 2:
                print('\nBueno, si no quieres, no\n')
                continue
            elif eleccionDelJugador == 3:
                print("\nAdiós!")
                break
            else:
                raise ValueError
        except ValueError:
            print("\nLas opciones son 1, 2 o 3\n")


if __name__ == '__main__':
    run()