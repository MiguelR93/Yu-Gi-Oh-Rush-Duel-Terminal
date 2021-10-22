import script.duel as duel


def summonLoop(playerTurn, summonAMonster, summonKind, position):
    monsterZoneCounter = 0
    for i in playerTurn[7:10]:
        if len(i) > 0:
            monsterZoneCounter += 1
    if monsterZoneCounter > 2:
        print("No hay zonas disponibles")
        duel.littleSleep()
    else:
        while True:
            duel.littleSleep()
            try:
                monstersZones = ["1: zona Izquierda", "2: zona central", "3: zona derecha"]
                print('\nEn dónde quieres ponerlo?')
                for i,a in enumerate(playerTurn[7:10]):
                    if len(a) == 0:
                        print(monstersZones[i])
                monsterZonePosition = int(input("\nEscribe el número a la izquierda: "))
                if len(playerTurn[monsterZonePosition+6]) != 0:
                    if summonKind == 'tribute Summon':
                        print("Zona ocupada, elige otra")
                        duel.littleSleep()
                        continue
                    else:
                        ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                        if ocupado == 1:
                            continue
                        elif ocupado == 2:
                            break
                elif (monsterZonePosition+6 > 9) or (monsterZonePosition+6 < 7):
                    print("No es una zona de monstruo")
                    duel.littleSleep()
                    continue
                else:
                    playerTurn[3][summonAMonster]['position'], playerTurn[3][summonAMonster]['summonKind'], playerTurn[3][summonAMonster]['summoned this turn?'], playerTurn[3][summonAMonster]['can change its position?'], playerTurn[3][summonAMonster]['attacksCounter'] = position, summonKind, 'yes', 'no', 1
                    print(playerTurn[3][summonAMonster]) # imprime el estado del monstruo
                    playerTurn[monsterZonePosition+6] = playerTurn[3][summonAMonster] # pone el monstruo de la mano en el campo
                    playerTurn[3].remove(playerTurn[3][summonAMonster]) # quita de la mano al monstruo invocado
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


def sacrifice2(playerTurn, summonAMonster, position):
    while True:
        duel.littleSleep()
        print("\nMonstruos en campo:")
        tributeAble = []
        for i,a in enumerate(playerTurn[7:10]):
            if len(a) != 0:
                print(f"{i}: {a['name']}")
                tributeAble.append(i)
        choosed = []
        tributed = int(input("Elige el primer monstruo a sacrificar: "))
        if tributed not in tributeAble:
            print("No es un valor válido")
            duel.littleSleep()
            continue
        choosed.append(tributed)
        try:
            print("Elige el segundo monstruo a sacrificar o vuelve a elegir al primero para cambiarlo: ")
            tributed2 = int(input())
            if tributed2 == choosed[0]:
                continue
            elif tributed2 not in tributeAble:
                print("No es un valor válido")
                duel.littleSleep()
            elif tributed2 != choosed[0]:
                tributeAble.append(tributed2)
                break
                duel.littleSleep()
        except IndexError:
            print('Valor equivocado')
            continue
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            continue
            duel.littleSleep()
    playerTurn[4].append(playerTurn[tributed + 7])
    playerTurn[tributed + 7] = []
    playerTurn[4].append(playerTurn[tributed2 + 7])
    playerTurn[tributed2 + 7] = []
    summonLoop(playerTurn, summonAMonster, 'tribute Summon', position)


def sacrifice1(playerTurn, summonAMonster, position):
    # debe mostras los monstruos sacrificables y sus índices. Debe dar la opción para realizar cambios o cancelar la invocación y Confirmar la invocación
    print("Monstruos en campo\n")
    # input()
    # validValues = []
    for i,a in enumerate(playerTurn[7:10]):
        if len(a) != 0:
            print(f"{i}: {a['name']}")
            # input()
            # validValues.append(a)
    try:
        choosed = int(input("Elige el monstruos a sacrificar:"))
    except IndexError:
        print('Valor equivocado')
        # input()
        duel.littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        duel.littleSleep()
    # playerTurn.remove(playerTurn[choosed + 7])
    playerTurn[4].append(playerTurn[choosed + 7])
    playerTurn[choosed + 7] = []
    summonLoop(playerTurn, summonAMonster, 'tribute Summon', position)


def normalSummon(playerTurn, position):
    try:
        summonAMonster = int(input("ingresa el índice del monstruo (el número a su izquierda): "))
        if 'MONSTER' not in playerTurn[3][summonAMonster]['cardType']: # Cuando lo que se elige no es un monstruo
            print('Eso no es un monstruo')
            duel.littleSleep()
        elif int(playerTurn[3][summonAMonster]['level']) <= 4: # Cuando lo que se elige es un monstruo nvl<=4
            # print(f"\nNivel del monstruo: {playerTurn[3][summonAMonster]['level']}\n")
            summonLoop(playerTurn, summonAMonster, 'Normal Summon', position)
        elif int(playerTurn[3][summonAMonster]['level']) <=6:
            if duel.ocupiedMonsterZones() < 1:
                print("No cuentas con monstruos suficientes")
                duel.littleSleep()
                # input()
            else:
                # mostrar los monstruos a sacrificar
                # print("entramos a sacrificar")
                # input()
                sacrifice1(playerTurn, summonAMonster, position)
        elif int(playerTurn[3][summonAMonster]['level']) >= 7:
            if duel.ocupiedMonsterZones() < 2:
                print("No cuentas con monstruos suficientes")
                duel.littleSleep()
            else:
        #         # mostrar los monstruos a sacrificar
        #         # print("entramos a sacrificar")
        #         # input()
                sacrifice1(playerTurn, summonAMonster, position)
    except IndexError:
        print('Valor equivocado')
        # input()
        duel.littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        duel.littleSleep()


def isThereMonstersInHand(playerTurn, mainPhaseOptions):
    COUNTER = 0
    for i in playerTurn[3]:
        if 'MONSTER' in i['cardType']:
            COUNTER += 1
    if COUNTER >= 1:
        # normalSummon()
        print(mainPhaseOptions[1],mainPhaseOptions[2],sep='\n')
    else:
        pass
    # else:
    #     input("No tienes monstruos para invocar [Presiona Enter para continuar]")