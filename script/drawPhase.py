# def drawACard():
#     if len(player1[1]) <= 0:
#         print(youLose)
#         return deckEmpty
#     else:
#         player1[3].append(player1[1][0]) # añade la carta del deck a la mano
#         player1[1].remove(player1[1][0]) # quita del deck la carta añadida a la mano
#         activatingAnEff()
#         print(f"\n\nmano: {player1[3]}\n\nCartas en mano: {len(player1[3])}\n\n",sep="\n") # es necesario?


# def checkingLenDeck():
#     global thereIsNoWinner
#     if len(player1[1]) <= 0:
#         thereIsNoWinner = not thereIsNoWinner
#     else:
#         drawACard()


def drawPhase(playerTurn):
#     # activatingAnEff()
    print(f"Mano del jugador: {playerTurn[3]}")
#     if len(playerTurn[3]) >= 5:
#         print("doro!!!")
# #         # print("tenemos 5 o más cartas")
# #         # checkingLenDeck()
#     else:
#         print("tenemos menos de 5 cartas")
# #         # while len(player1[3]) < 5:
# #         #     checkingLenDeck()



# zona de prueba ------
def run():
    print("Ore no ta-n doro!")
    drawPhase("hola1234")


if __name__ == "__main__":
    run()