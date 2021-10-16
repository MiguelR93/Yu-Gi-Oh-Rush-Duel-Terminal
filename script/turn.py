# organizar el turno :)
import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase
import script.battlePhase as battlePhase
# import drawPhase

def turn(playerTurn):
    duel.duelStatus()
    duel.littleSleep()
    # print(f"Turno de: {playerTurn}")
    # print('\n\n\n:)\n\n\n')
    drawPhase.drawPhase(playerTurn)
    # print("Ahora, la Main Phase")
    mainPhase.mainPhase(playerTurn)
    battlePhase.battlePhase(playerTurn)
    duel.littleSleep()


# zona de prueba ------
def run():
    print("My turn!")
    # turn("hola1234")


if __name__ == "__main__":
    run()