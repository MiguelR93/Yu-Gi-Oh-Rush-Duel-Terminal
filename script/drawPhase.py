import random, copy, time
import script.duel as duel

def drawACard(playerTurn):
    if len(playerTurn.deck) <= 0:
        # print(youLose)
        # return deckEmpty
        print("Se acabó todo, man")
    else:
        playerTurn.hand.append(playerTurn.deck[0]) # añade la carta del deck a la mano
        playerTurn.deck.remove(playerTurn.deck[0]) # quita del deck la carta añadida a la mano
        # activatingAnEff()
        # print(f"\n\nmano: {playerTurn.hand}\n\nCartas en mano: {len(playerTurn.hand)}\n\n",sep="\n") # es necesario?


def checkingLenDeck(playerTurn):
    # global thereIsNoWinner
    if len(playerTurn.deck) <= 0:
        # print("Ya se acabó el juego, ya >>>>:C")
        playerTurn[14] = False
    else:
        if playerTurn.name == "Jugador":
            print("Wa robar!")
        else:
            print("COM va a robar")
        drawACard(playerTurn)
        # duel.littleSleep()
    duel.littleSleep()


def drawPhase(playerTurn):
#     # activatingAnEff()
    # print(f"\nMano del jugador en turno: {playerTurn.hand}\n\n\n")
    duel.littleSleep()
    if len(playerTurn.hand) >= 5:
        checkingLenDeck(playerTurn)
    else:
        if playerTurn.name == "Jugador":
            print("Tengo menos de 5 cartas")
        else:
            print("COM tiene menos de 5 cartas")
        while (len(playerTurn.hand) < 5) and (duel.victory() == True):
            checkingLenDeck(playerTurn)
    duel.littleSleep()



# zona de prueba ------
def run():
    print("Ore no ta-n doro!")
    # drawPhase("hola1234")


if __name__ == "__main__":
    run()