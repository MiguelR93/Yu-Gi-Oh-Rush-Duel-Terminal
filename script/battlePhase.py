import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase


battlePhaseOptions = [
'\nQué quieres hacer?', 
'1: Declarar un ataque', 
'2: Ir a la End Phase'
]


def directAttack(playerTurn, chosed):
    # print(f"Esto debería ser LP rival: {playerTurn[15][0]}")
    # print(playerTurn[15][0] - int(playerTurn[chosed]['attack']))
    playerTurn[15][0] -= int(playerTurn[chosed]['attack'])


def declareAttack(playerTurn):
    # print(f"13: {playerTurn[13]}")
    # print(f"15: {playerTurn[15]}")   
    try:
        chosed = int(input("\nElige un monstruo para atacar:\n")) + 7
        # input('presiona enter')
        if 'MONSTER' not in playerTurn[chosed]['cardType']: # Cuando lo que se elige no es un monstruo
            print('Eso no es un monstruo')
            duel.littleSleep()
        elif duel.ocupiedMonsterZones(playerTurn[15]) <= 0:
            print("puedes atacar directo!")
            duel.littleSleep()
            directAttack(playerTurn, chosed)
    except IndexError:
        print('Valor equivocado')
        # input()
        duel.littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        duel.littleSleep()


def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():
        duel.duelStatus(playerTurn)
        print("\n\n\nMonstruos que pueden atacar:")        
        for i,a in enumerate(playerTurn[7:10]):            
            if (len(a) > 0) and ('Attack' in a['position']):
                print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
        

        print(battlePhaseOptions[0])
        if duel.ocupiedMonsterZones(playerTurn) > 0:
            print(battlePhaseOptions[1])
        print(battlePhaseOptions[2])

        try:
            actionInBP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInBP == 1:
                declareAttack(playerTurn)
            elif actionInBP == 2:
                # endPhase()
                break
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido')
