def summonLoop(summonAMonster, summonKind, position):
    monsterZoneCounter = 0
    for i in player1[7:10]:
        if len(i) > 0:
            monsterZoneCounter += 1
    if monsterZoneCounter > 2:
        print("No hay zonas disponibles")
        littleSleep()
    else:
        while True:
            duelStatus()
            try:
                monstersZones = ["1: zona Izquierda", "2: zona central", "3: zona derecha"]
                print('\nEn dónde quieres ponerlo?')
                for i,a in enumerate(player1[7:10]):
                    if len(a) == 0:
                        print(monstersZones[i])
                monsterZonePosition = int(input("\nEscribe el número a la izquierda: "))
                if len(player1[monsterZonePosition+6]) != 0:
                    if summonKind == 'tribute Summon':
                        print("Zona ocupada, elige otra")
                        littleSleep()
                        continue
                    else:
                        ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                        if ocupado == 1:
                            continue
                        elif ocupado == 2:
                            break
                elif (monsterZonePosition+6 > 9) or (monsterZonePosition+6 < 7):
                    print("No es una zona de monstruo")
                    littleSleep()
                    continue
                else:
                    player1[3][summonAMonster]['position'], player1[3][summonAMonster]['summonKind'], player1[3][summonAMonster]['summoned this turn?'] = position, summonKind, 'yes'
                    print(player1[3][summonAMonster]) # imprime el estado del monstruo
                    player1[monsterZonePosition+6] = player1[3][summonAMonster] # pone el monstruo de la mano en el campo
                    player1[3].remove(player1[3][summonAMonster]) # quita de la mano al monstruo invocado
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


def sacrifice2(summonAMonster, position):
    while True:
        duelStatus()
        print("\nMonstruos en campo:")
        tributeAble = []
        for i,a in enumerate(player1[7:10]):
            if len(a) != 0:
                print(f"{i}: {a['name']}")
                tributeAble.append(i)
        choosed = []
        tributed = int(input("Elige el primer monstruo a sacrificar: "))
        if tributed not in tributeAble:
            print("No es un valor válido")
            littleSleep()
            continue
        choosed.append(tributed)
        try:
            print("Elige el segundo monstruo a sacrificar o vuelve a elegir al primero para cambiarlo: ")
            tributed2 = int(input())
            if tributed2 == choosed[0]:
                continue
            elif tributed2 not in tributeAble:
                print("No es un valor válido")
                littleSleep()
            elif tributed2 != choosed[0]:
                tributeAble.append(tributed2)
                break
                littleSleep()
        except IndexError:
            print('Valor equivocado')
            continue
            littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            continue
            littleSleep()
    player1[4].append(player1[tributed + 7])
    player1[tributed + 7] = []
    player1[4].append(player1[tributed2 + 7])
    player1[tributed2 + 7] = []
    summonLoop(summonAMonster, 'tribute Summon', position)


def sacrifice1(summonAMonster, position):
    # debe mostras los monstruos sacrificables y sus índices. Debe dar la opción para realizar cambios o cancelar la invocación y Confirmar la invocación
    print("Monstruos en campo\n")
    # input()
    # validValues = []
    for i,a in enumerate(player1[7:10]):
        if len(a) != 0:
            print(f"{i}: {a['name']}")
            # input()
            # validValues.append(a)
    try:
        choosed = int(input("Elige el monstruos a sacrificar:"))
    except IndexError:
        print('Valor equivocado')
        # input()
        littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        littleSleep()
    # player1.remove(player1[choosed + 7])
    player1[4].append(player1[choosed + 7])
    player1[choosed + 7] = []
    summonLoop(summonAMonster, 'tribute Summon', position)


def normalSummon(position):
    try:
        summonAMonster = int(input("ingresa el índice del monstruo (el número a su izquierda): "))
        if 'MONSTER' not in player1[3][summonAMonster]['cardType']: # Cuando lo que se elige no es un monstruo
            print('Eso no es un monstruo')
            littleSleep()
        elif int(player1[3][summonAMonster]['level']) <= 4: # Cuando lo que se elige es un monstruo nvl<=4
            # print(f"\nNivel del monstruo: {player1[3][summonAMonster]['level']}\n")
            summonLoop(summonAMonster, 'Normal Summon', position)
        elif int(player1[3][summonAMonster]['level']) <=6:
            if ocupiedMonsterZones() < 1:
                print("No cuentas con monstruos suficientes")
                littleSleep()
                # input()
            else:
                # mostrar los monstruos a sacrificar
                # print("entramos a sacrificar")
                # input()
                sacrifice1(summonAMonster, position)
        elif int(player1[3][summonAMonster]['level']) >= 7:
            if ocupiedMonsterZones() < 2:
                print("No cuentas con monstruos suficientes")
                littleSleep()
            else:
        #         # mostrar los monstruos a sacrificar
        #         # print("entramos a sacrificar")
        #         # input()
                sacrifice2(summonAMonster, position)
    except IndexError:
        print('Valor equivocado')
        # input()
        littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        littleSleep()


def isThereMonstersInHand():
    COUNTER = 0
    for i in player1[3]:
        if 'MONSTER' in i['cardType']:
            COUNTER += 1
    if COUNTER >= 1:
        # normalSummon()
        print(mainPhaseOptions[1],mainPhaseOptions[2],sep='\n')
    else:
        pass
    # else:
    #     input("No tienes monstruos para invocar [Presiona Enter para continuar]")