# organizar el turno :)
import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase
import script.battlePhase as battlePhase
# import drawPhase
import script.player as player
import script.endPhase as endPhase


def turn(playerTurn):
    duel.turnStarts()
    duel.duelStatus(playerTurn)
    duel.littleSleep()
    # drawPhase.drawPhase(playerTurn)
    if mainPhase.mainPhase(playerTurn) == 'End Phase':
        playerTurn.drawPhase()
    # endPhase.endPhase(playerTurn)
    duel.littleSleep()

    


# zona de prueba ------
def run():
    print("My turn!")
    # turn("hola1234")


if __name__ == "__main__":
    run()