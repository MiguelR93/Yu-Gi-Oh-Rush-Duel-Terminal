import script.duel as duel

def counterMonsterInField(playerTurn):
    print("Contando monstruos en campo")
    counter =  playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') + playerTurn.typeCardInPlayerArea(playerTurn.oponent.playerMonsterZones, 'MONSTER')
    print(f"Hay: {counter} monstruos en campo")
    return counter

def counterDragonInHand(playerTurn):
    return playerTurn.typeMonsterInPlayerArea(playerTurn.hand, 'Dragon')


def sendDragonInHandToGY(playerTurn):
    for a,i in enumerate(playerTurn.hand):
        if (i.cardType == 'MONSTER') and (i.typeMonster == 'Dragon'):
            print(f"{a}: {i.name}")
    
    choosed = []
    while len(choosed) < 3:
        print(f"{choosed}, {len(choosed)}")
        try:
            monster = int(input("Escribe el número a la izquierda: "))
            if monster not in choosed:
                choosed.append(monster)
            elif monster in choosed:
                choosed.remove(monster)
            else:
                raise IndexError
        except IndexError:
            print('Valor equivocado')
            continue
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            continue
    
    for i in choosed:
        playerTurn.gy.append(i)
        playerTurn.hand.remove(i)


def counterMonsterDestroyed(playerTurn):
    print('Contando a los monstruos destruidos por este efecto')
    # cada ciclo debe ver si hay un monstruo en la zona de monstruo respectiva, luego debe añadirlo al GY, removerlo del campo, y añadir 1 al contador de monstruos destruidos
    COUNTER = 0
    for i in playerTurn.oponent.playerMonsterZones:
        if (len(i) > 0) and (i.cardType == 'MONSTER'):
            playerTurn.oponent.gy.append(i)
            i = []
            COUNTER += 1
    for i in playerTurn.playerMonsterZones:
        if (len(i) > 0) and (i.cardType == 'MONSTER'):
            playerTurn.gy.append(i)
            i = []
            COUNTER += 1
    return COUNTER


def counterMonsterDragonNvlFourOrLessInGY(playerTurn):
    print('Contando monstruos de nvl <= 4 en GY')
    COUNTER = 0
    if len(playerTurn.gy) > 0:
        for i in playerTurn.gy:
            if (i.cardType == 'MONSTER') and (i.typeMonster == 'Dragon') and (int(i.level) <= 4):
                COUNTER += 1
    return COUNTER


def specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn):
    print('Invocando desde el GY')
    # hace una invocación especial en posición de defensa
    if len(playerTurn.gy) > 0:
        for a,i in enumerate(playerTurn.gy):
            if (i.cardType == 'MONSTER') and (i.typeMonster == 'Dragon') and (int(i.level) <= 4):
                print(f"{a}: {i.name}")
    
    while True:
        try:
            summonAMonster = int(input("Elige el monstruo a invocar:\n"))
            if 'MONSTER' not in playerTurn.gy[summonAMonster].cardType: # Cuando lo que se elige no es un monstruo
                    print('Eso no es un monstruo')
            elif int(playerTurn.hand[summonAMonster].level) <= 4:
                playerTurn.summonLoop('specialSummon',  'defense face-up', summonAMonster)
                break
        except IndexError:
            print('Valor equivocado')
        except ValueError:
            print('Debes ingresar un número')
        duel.littleSleep()