import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase

def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():
        for i,a in enumerate(playerTurn[7:10]):
            print(f"{i}: {a}", sep="\\")
        chosed = int(input("\nElige un monstruo para atacar:\n"))