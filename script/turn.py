# organizar el turno :)
import script.drawPhase as drawPhase
# import drawPhase

def turn(playerTurn):
    # print(f"Turno de: {playerTurn}")
    # print('\n\n\n:)\n\n\n')
    drawPhase.drawPhase(playerTurn)


# zona de prueba ------
def run():
    print("My turn!")
    # turn("hola1234")


if __name__ == "__main__":
    run()