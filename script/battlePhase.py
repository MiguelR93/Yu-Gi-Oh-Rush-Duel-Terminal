import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase

def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():        
        for a,i in enumerate(playerTurn[7:10]):
            if len(i) > 0:
                print(f"{a + 7}: {i['name']} | Posición: {i['position']}| Nivel: {i['level']} ATK/{i['attack']} DEF/{i['defense']}",sep="//", end="   ")

        chosed = int(input("\nElige un monstruo para atacar:\n"))