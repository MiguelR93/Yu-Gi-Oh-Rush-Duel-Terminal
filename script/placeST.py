import script.duel as duel
import script.activeEff as activeEff


def placeSTLoop(playerTurn, position, placeST):
    sTZoneCounter = 0
    for i in playerTurn[10:13]:
        if len(i) > 0:
            sTZoneCounter += 1
    if sTZoneCounter > 2:
        print("No hay zonas disponibles")
        duel.littleSleep()
    else:
        while True:
            duel.duelStatus(playerTurn)
            try:
                sTZones = ["1: zona Izquierda", "2: zona central", "3: zona derecha"]
                print('\nEn dónde quieres ponerlo?')
                for i,a in enumerate(playerTurn[10:13]):
                    if len(a) == 0:
                        print(sTZones[i])
                sTZonePosition = int(input("\nEscribe el número a la izquierda: "))
                if len(playerTurn[sTZonePosition+9]) != 0:
                    # print("Zona ocupada, elige otra")
                    # duel.littleSleep()
                    # continue
                    # else:
                    ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                    if ocupado == 1:
                        continue
                    elif ocupado == 2:
                        break
                elif (sTZonePosition + 9 > 12) or (sTZonePosition + 9 < 10):
                    print("No es una zona de magia/trampa")
                    duel.littleSleep()
                    continue
                else:
                    # playerTurn[3][placeST]['position'] = position # incluir en la clase
                    print(playerTurn[3][placeST]) # imprime el estado de la s/t
                    playerTurn[sTZonePosition + 9] = playerTurn[3][placeST] # pone la s/t
                    playerTurn[3].remove(playerTurn[3][placeST]) # quita de la mano a la s/t
                    if position == 'set':
                        # playerTurn[3][placeST]['set this turn?'] = 'yes' # incluir en la clase
                        pass
                    elif position == 'active':
                        activeEff.activeEff(playerTurn, sTZonePosition + 9)
                    break
            except IndexError:
                print('Valor equivocado')
                # input()
                duel.littleSleep()
                continue
            except ValueError:
                print('Debes ingresar un número')
                duel.littleSleep()
                continue


def setSpellTrap(playerTurn, position):
    try:
        placeST = int(input("ingresa el índice de la magia/trampa (el número a su izquierda): "))
        if 'MONSTER' in playerTurn[3][placeST].cardType: # Cuando lo que se elige es un monstruo y no debería serlo
            print('Eso no es una magia/trampa')
            duel.littleSleep()
        elif ('TRAP' in playerTurn[3][placeST].cardType) and (position == 'active'):
            print("No puedes activar una trampa desde tu mano")
            duel.littleSleep()
        else:
            placeSTLoop(playerTurn, position, placeST)
    except IndexError:
        print('Valor equivocado')
        # input()
        duel.littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        duel.littleSleep()


def isThereSpellTrapInHand(playerTurn, mainPhaseOptions):
    COUNTER = 0
    for i in playerTurn.hand:
        if ('SPELL' in i.cardType) or ('TRAP' in i.cardType):
            COUNTER += 1
    if COUNTER >= 1:
        # normalSummon()
        print(mainPhaseOptions[3], mainPhaseOptions[5],sep='\n')
    else:
        pass