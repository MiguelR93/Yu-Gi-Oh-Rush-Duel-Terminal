import random, copy, time
import script.duel as duel
import script.summon as summon
import script.placeST as placeST
import script.battlePhase as battlePhase


mainPhaseOptions = [
'\nQué quieres hacer?', 
'1: Invocar un monstruo', 
'2: Colocar un monstruo', 
'3: Activar una Magia de tu mano', 
'4: Activar una Magia del campo', 
'5: Colocar una Trampa o Magia de tu mano', 
'6: Activar una trampa del campo', 
'7: Cambiar la posición de ataque a defensa', 
'8: Cambiar la posición de defensa boca-abajo a ataque', 
'9: Cambiar la posición de defensa boca-arriba a ataque', 
'10: Ir a la Battle Phase', 
'11: Ir a la End Phase'
]


def mainPhase(playerTurn):
    # activatingAnEff()

    while duel.victory():
        duel.duelStatus(playerTurn)
        # for i in mainPhaseOptions:
        #     print(i)

        # Main Phas Opctions
        print(mainPhaseOptions[0])
        summon.isThereMonstersInHand(playerTurn, mainPhaseOptions)
        placeST.isThereSpellTrapInHand(playerTurn, mainPhaseOptions)
        print(mainPhaseOptions[10])
        print(mainPhaseOptions[11])

        try:
            actionInMP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInMP == 1: # Invocar un monstruo de forma normal (Ataque boca arriba o Defensa boca abajo)
                summon.normalSummon(playerTurn, 'Attack')
            elif actionInMP == 2:
                summon.normalSummon(playerTurn, 'Defense Face-Down')
            elif actionInMP == 3:
                placeST.setSpellTrap(playerTurn, 'active')
                pass
            elif actionInMP == 4:
                pass
            elif actionInMP == 5:
                placeST.setSpellTrap(playerTurn, 'set')
                pass
            elif actionInMP == 6:
                pass
            elif actionInMP == 7:
                pass
            elif actionInMP == 8:
                pass
            elif actionInMP == 9:
                pass
            elif actionInMP == 10:
                battlePhase.battlePhase(playerTurn)
            elif actionInMP == 11:
                # endPhase()
                break
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido')
            time.sleep(1.5)