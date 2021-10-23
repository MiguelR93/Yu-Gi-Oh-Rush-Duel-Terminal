import script.duel as duel


def activeEff(playerTurn, sTInFiel):
    # si el tipo de carta es magia/trampa normal, debe ir al GY luego de activarse, de lo contrario, permanecerá en campo
    if (playerTurn[sTInFiel]['cardType'] == 'SPELL') and (playerTurn[sTInFiel]['icon'] == 'normal'):
        # print('Es una magia normal')
        # duel.littleSleep()
        # print('¡Activa el eff de la carga (según su nombre)!')
        # duel.littleSleep()

        # print(f"Nombre de la carta: {playerTurn[sTInFiel]['name']}")

        # print('Ahora se va al GY')
        # duel.littleSleep()

        playerTurn[4].append(playerTurn[sTInFiel]) # copia del campo al GY
        playerTurn[sTInFiel] = [] # quita del campo

    elif (playerTurn[sTInFiel]['cardType'] == 'TRAP') and (playerTurn[sTInFiel]['icon'] == 'normal'):
        print('Es una trampa normal')
        duel.littleSleep()
        print('¡Activa el eff de la carga (según su nombre)!')
        duel.littleSleep()
        print('Ahora se va al GY')
        duel.littleSleep()
    elif (playerTurn[sTInFiel]['cardType'] == 'MONSTER') and ('effect' in playerTurn[sTInFiel]['frontier']):
        print('Es un monstruo de efecto')
        duel.littleSleep()
        print('¡Activa el eff de la carga (según su nombre)!')
        duel.littleSleep()
    else:
        print('no es nada de lo anterio')
        duel.littleSleep()