import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase


def declareAttack(playerTurn):
    pass

    

    
    chosed = int(input("\nElige un monstruo para atacar:\n"))


def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():        
        for i,a in enumerate(playerTurn[7:10]):            
            if (len(a) > 0) and ('Attack' in a['position']):
                print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
        
        declareAttack(playerTurn)
