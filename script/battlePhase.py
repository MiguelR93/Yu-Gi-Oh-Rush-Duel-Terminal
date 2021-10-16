import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase


def declareAttack(playerTurn):
    print(f"13: {playerTurn[13]}")
    print(f"15: {playerTurn[15]}")   
    # chosed = int(input("\nElige un monstruo para atacar:\n"))
    input('presiona enter')

    # if duel.ocupiedMonsterZones(playerTurn[15]) <= 0:
    #     # directAttack(playerTurn)
    #     print("puedes atacar directo!")
    #     littleSleep()


def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():        
        for i,a in enumerate(playerTurn[7:10]):            
            if (len(a) > 0) and ('Attack' in a['position']):
                print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
        
        declareAttack(playerTurn)
        break
