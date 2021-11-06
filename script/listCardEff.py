def counterMonsterInField(playerTurn):

    return playerTurn.typeCardInPlayerArea(playerTurn.playerMonsterZones, 'MONSTER') + playerTurn.typeCardInPlayerArea(playerTurn.oponent.playerMonsterZones, 'MONSTER')


def counterDragonInHand(playerTurn):
    return playerTurn.typeMonsterInPlayerArea(playerTurn.hand, 'Dragon')


def sendDragonInHandToGY(playerTurn):
    for a,i in enumerate(playerTurn.hand):
        if (i.cardType == 'MONSTER') and (i.typeMonster == 'Dragon'):
            print(f"{a}: {i.name}")
    
    choosed = []
    while len(choosed) < 3:
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
            if (i.cardType == 'MONSTER') and ((i.typeMonster == 'Dragon') and (int(i.level) <= 4):
                COUNTER += 1
    return COUNTER


def specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn):
    print('Invocando desde el GY')
    # hace una invocación especial en posición de defensa
    if len(playerTurn.gy) > 0:
        for a,i in enumerate(playerTurn.gy):
            if (i.cardType == 'MONSTER') and ((i.typeMonster == 'Dragon') and (int(i.level) <= 4):
                print(f"{a}: {i.name}")
    
    while True:
        try:
            summonAMonster = int(input("Elige el monstruo a invocar:\n"))
            if 'MONSTER' not in playerTurn.gy[chosenMonster].cardType: # Cuando lo que se elige no es un monstruo
                    print('Eso no es un monstruo')
            elif int(playerTurn.hand[summonAMonster].level) <= 4:
                playerTurn.summonLoop('specialSummon',  'defense face-up', summonAMonster)
                break
        except IndexError:
            print('Valor equivocado')
        except ValueError:
            print('Debes ingresar un número')
        duel.littleSleep()


# Card's Effects -------
def DragonicPressure(playerTurn):
# TEXT: 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'

# 1. CONDICIÓN: A) Debe evaluar si hay monstruos en el campo; B) Debe evaluar si el jugador tiene al menos 3 dragones en mano; RESULTADO: Debe destruir los monstruos del campo (si es que hay alguno) y contar si destruyó alguno
# 2 CONDICIÓN: A) haber destruido al menos un monstruo con este efecto; B) ver si hay algún monstruo de nvl <= 4 en GY del jugador; RESULTADO: el jugador elige un monstruo nvl <= 4 de su GY y lo invoca en posición de defensa boca arriba

    counterMonsterInField(playerTurn)
    counterDragonInHand(playerTurn)
    if (counterMonsterInField(playerTurn) > 0) and (counterDragonInHand(playerTurn) >= 3):
        sendDragonInHandToGY(playerTurn)
        # destroyAllMonsterInField()
        counterMonsterDestroyed(playerTurn)
    if (counterMonsterDestroyed(playerTurn) > 0) and (counterMonsterDragonNvlFourOrLessInGY(playerTurn) >= 1):
        specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn)
