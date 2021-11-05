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
                    # playerTurn.hand[summonAMonster]['position'], playerTurn.hand[summonAMonster]['summonKind'], playerTurn.hand[summonAMonster]['summoned this turn?'], playerTurn.hand[summonAMonster]['can change its position?'], playerTurn.hand[summonAMonster]['attacksCounter'] = position, summonKind, 'yes', 'no', 1 # incluir esto en la clase monster.py
                    print(playerTurn.hand[summonAMonster]) # imprime el estado del monstruo
                    playerTurn[monsterZonePosition+6] = playerTurn.hand[summonAMonster] # pone el monstruo de la mano en el campo
                    playerTurn.hand.remove(playerTurn.hand[summonAMonster]) # quita de la mano al monstruo invocado
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
                print(f"{i}: {a.name}")
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
            print(f"{i}: {a.name}")
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
        if 'MONSTER' not in playerTurn.hand[summonAMonster].cardType: # Cuando lo que se elige no es un monstruo
            print('Eso no es un monstruo')
            duel.littleSleep()
        elif int(playerTurn.hand[summonAMonster].level) <= 4: # Cuando lo que se elige es un monstruo nvl<=4
            # print(f"\nNivel del monstruo: {playerTurn.hand[summonAMonster].level}\n")
            summonLoop(playerTurn, summonAMonster, 'Normal Summon', position)
        elif int(playerTurn.hand[summonAMonster].level) <=6:
            if duel.ocupiedMonsterZones() < 1:
                print("No cuentas con monstruos suficientes")
                duel.littleSleep()
                # input()
            else:
                # mostrar los monstruos a sacrificar
                # print("entramos a sacrificar")
                # input()
                sacrifice1(playerTurn, summonAMonster, position)
        elif int(playerTurn.hand[summonAMonster].level) >= 7:
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
    for i in playerTurn.hand:
        if 'MONSTER' in i.cardType:
            COUNTER += 1
    if COUNTER >= 1:
        # normalSummon()
        print(mainPhaseOptions[1],mainPhaseOptions[2],sep='\n')
    else:
        pass
    # else:
    #     input("No tienes monstruos para invocar [Presiona Enter para continuar]")


class Summon():

    def __init__(self):
        pass
    
    def normalSummon(self, monster):
        # Recuerda indicar la posición de invocación
        if int(monster['level']) <= 4:
            self._summonLoop()
        elif (int(monster['level']) > 4) and (int(monster['level']) < 7):
            self._sacrifice1()
        elif (int(monster['level']) >= 7):
            self._sacrifice2()
        
        # 1. Elegir al monstruo
        # 2. Si nvl monstruo <= 4 ir a (7)
        # 3. Si nvl monstruo == 5 o 6 ir a (5)
        # 4. Si nvl monstruo >= 7 ir a (6)
        # 5. Tributar un monstruo, luego ir a (7)
        # 6. Tributar dos monstruos, luego ir a (7)
        # 7. Invoca al monstruo (añadiéndole los atributos: invocación normal, invocado este turno, cantidad de ataques posibles, no puede cambiar de posición este turno
    
    def normalSummonFaceDown(self, monster):
        # 1. Elegir al monstruo
        # 2. Si nvl monstruo <= 4 ir a (7)
        # 3. Si nvl monstruo == 5 o 6 ir a (5)
        # 4. Si nvl monstruo >= 7 ir a (6)
        # 5. Tributar un monstruo, luego ir a (7)
        # 6. Tributar dos monstruos, luego ir a (7)
        # 7. Invoca al monstruo (añadiéndole los atributos: invocación normal boca abajo, invocado este turno, cantidad de ataques posibles, no puede cambiar de posición este turno
        pass
    

    def specialSummon(self):
        # Recuerda indicar la posición de invocación
        self._summonLoop()
    

    def maximumSummon(self):
        # si hay monstruos en el campos, se van al GY
        # la pieza derecha del maximum debe ir en la zona de monstruo respectiva
        self._summonLoop()
        self._summonLoop()
        self._summonLoop()        


    def fusionSummon(self):
        # envía materiales del campo al cementerio
        self._summonLoop()

    def _sacrifice1(self):
        print('Safrifica un monstruo')
        self._summonLoop()
    
    def _sacrifice2(self):
        print('Sacrifica dos monstruos')
        self._summonLoop()
    
    def _summonLoop(self):
        print('Elige donde irá el monstruo')
        print('El monstruo se invocó!')
        

# Zona de prueba
if __name__ == '__main__':
    summon = Summon()
    summon.normalSummon({'id': '2', 'name': 'Gravity Press Dragon', 'cardType': 'MONSTER', 'text': '[Requirement] You can send 1 card from your hand to the GY.\n[Effect] Choose 1 face-up monster your opponent controls. It loses 700 ATK/DEF until the end of this turn.', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '6', 'attack': '1500', 'defense': '1000', 'frontier': '[effect]', 'effect': 'none'})