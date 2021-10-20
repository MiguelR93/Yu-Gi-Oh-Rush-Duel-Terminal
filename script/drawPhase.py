import random, copy, time
import script.duel as duel

def drawACard(playerTurn):
    if len(playerTurn[1]) <= 0:
        # print(youLose)
        # return deckEmpty
        print("Se acabó todo, man")
    else:
        playerTurn[3].append(playerTurn[1][0]) # añade la carta del deck a la mano
        playerTurn[1].remove(playerTurn[1][0]) # quita del deck la carta añadida a la mano
        # activatingAnEff()
        # print(f"\n\nmano: {playerTurn[3]}\n\nCartas en mano: {len(playerTurn[3])}\n\n",sep="\n") # es necesario?


def checkingLenDeck(playerTurn):
    # global thereIsNoWinner
    if len(playerTurn[1]) <= 0:
        # print("Ya se acabó el juego, ya >>>>:C")
        playerTurn[14] = False
    else:
        if playerTurn[13] == "Jugador":
            print("Wa robar!")
        else:
            print("COM va a robar")
        drawACard(playerTurn)
        # duel.littleSleep()
    duel.littleSleep()


def drawPhase(playerTurn):
#     # activatingAnEff()
    # print(f"\nMano del jugador en turno: {playerTurn[3]}\n\n\n")
    duel.littleSleep()
    if len(playerTurn[3]) >= 5:
        checkingLenDeck(playerTurn)
    else:
        if playerTurn[13] == "Jugador":
            print("Tengo menos de 5 cartas")
        else:
            print("COM tiene menos de 5 cartas")
        while (len(playerTurn[3]) < 5) and (duel.victory() == True):
            checkingLenDeck(playerTurn)
    duel.littleSleep()



# zona de prueba ------
def run():
    print("Ore no ta-n doro!")
    # drawPhase("hola1234")


if __name__ == "__main__":
    run()