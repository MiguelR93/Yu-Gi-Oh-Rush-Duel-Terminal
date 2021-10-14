def placeSTLoop(position, placeST):
    sTZoneCounter = 0
    for i in player1[10:13]:
        if len(i) > 0:
            sTZoneCounter += 1
    if sTZoneCounter > 2:
        print("No hay zonas disponibles")
        littleSleep()
    else:
        while True:
            duelStatus()
            try:
                sTZones = ["1: zona Izquierda", "2: zona central", "3: zona derecha"]
                print('\nEn dónde quieres ponerlo?')
                for i,a in enumerate(player1[10:13]):
                    if len(a) == 0:
                        print(sTZones[i])
                sTZonePosition = int(input("\nEscribe el número a la izquierda: "))
                if len(player1[sTZonePosition+9]) != 0:
                    # print("Zona ocupada, elige otra")
                    # littleSleep()
                    # continue
                    # else:
                    ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                    if ocupado == 1:
                        continue
                    elif ocupado == 2:
                        break
                elif (sTZonePosition + 9 > 12) or (sTZonePosition + 9 < 10):
                    print("No es una zona de magia/trampa")
                    littleSleep()
                    continue
                else:
                    player1[3][placeST]['position'] = position
                    print(player1[3][placeST]) # imprime el estado de la s/t
                    player1[sTZonePosition + 9] = player1[3][placeST] # pone la s/t
                    player1[3].remove(player1[3][placeST]) # quita de la mano a la s/t
                    break
            except IndexError:
                print('Valor equivocado')
                # input()
                littleSleep()
                continue
            except ValueError:
                print('Debes ingresar un número')
                littleSleep()
                continue


def setSpellTrap(position):
    try:
        placeST = int(input("ingresa el índice de la magia/trampa (el número a su izquierda): "))
        if 'MONSTER' in player1[3][placeST]['cardType']: # Cuando lo que se elige es un monstruo y no debería serlo
            print('Eso no es una magia/trampa')
            littleSleep()
        else:
            placeSTLoop(position, placeST)
    except IndexError:
        print('Valor equivocado')
        # input()
        littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        littleSleep()


def isThereSpellTrapInHand():
    COUNTER = 0
    for i in player1[3]:
        if ('SPELL' in i['cardType']) or ('TRAP' in i['cardType']):
            COUNTER += 1
    if COUNTER >= 1:
        # normalSummon()
        print(mainPhaseOptions[3], mainPhaseOptions[5],sep='\n')
    else:
        pass