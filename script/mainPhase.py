import random, copy, time
import script.duel as duel
import script.summon as summon
import script.placeST as placeST
import script.battlePhase as battlePhase
import script.endPhase as endPhase


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
        # if (playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') >= 1) and (battlePhase.canChangeItsPosition(playerTurn) >= 1):
        if (playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') >= 1) and (battlePhase.canChangeItsPosition(playerTurn) >= 1):
            for i in mainPhaseOptions[7:10]:
                print(i)
        if duel.currentlyTurn() > 1:
            print(mainPhaseOptions[10])
        if playerTurn.typeCardInPlayerArea(playerTurn.hand, "SPELL") > 0:
            print("Activar un efecto de magia en mano? [escribe 12]")
        print(mainPhaseOptions[11])

        try:
            actionInMP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInMP == 1: # Invocar un monstruo de forma normal (Ataque boca arriba o Defensa boca abajo)
                # summon.normalSummon(playerTurn, 'Attack')
                playerTurn.normalSummon('attackPosition')
                duel.littleSleep()
            elif actionInMP == 2:
                playerTurn.normalSummon('Defense Face-Down')
            elif actionInMP == 3:
                playerTurn.placeSpellTrap('active')
            elif actionInMP == 4:
                pass
            elif actionInMP == 5:
                playerTurn.placeSpellTrap('set')
            elif actionInMP == 6:
                pass
            elif actionInMP == 7:
                if playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') < 1:
                    raise ValueError
                else:
                    battlePhase.changeBattlePosition(playerTurn, 'attackToDefense')
            elif actionInMP == 8:
                if playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') < 1:
                    raise ValueError
                else:
                    battlePhase.changeBattlePosition(playerTurn, 'defenseFDToAttack')
            elif actionInMP == 9:
                if playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') < 1:
                    raise ValueError
                else:
                    battlePhase.changeBattlePosition(playerTurn, 'defenseFDToAttack')
            elif actionInMP == 10:
                if duel.currentlyTurn() <= 1:
                    raise ValueError
                else:
                    battlePhase.battlePhase(playerTurn)
                    break
            elif actionInMP == 11:
                # print("Fin del turno")
                # duel.littleSleep()
                playerTurn.endPhase()
                # return 'End Phase'
                # print("seguimos en MP?")
                # duel.littleSleep()
                break
            elif actionInMP == 12:
                print("Debería mostar una lista de cartas en mano que sean magias")
                for a,i in enumerate(playerTurn.hand):
                    print(f"{a}: {i.name}")
                try:
                    activa = int(input("escribe el número de la carta"))
                    playerTurn.hand[activa].cardEffect(playerTurn)
                except AttributeError:
                    print(f"Elegiste: {activa.name} ")
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido')
            duel.littleSleep()