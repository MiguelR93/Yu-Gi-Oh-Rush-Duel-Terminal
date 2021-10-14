def mainPhase():
    activatingAnEff()

    while thereIsNoWinner:
        duelStatus()
        # for i in mainPhaseOptions:
        #     print(i)

        # Main Phas Opctions
        print(mainPhaseOptions[0])
        isThereMonstersInHand()
        isThereSpellTrapInHand()
        print(mainPhaseOptions[11])

        try:
            actionInMP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInMP == 1: # Invocar un monstruo de forma normal (Ataque boca arriba o Defensa boca abajo)
                normalSummon('Attack')
            elif actionInMP == 2:
                normalSummon('Defense Face-Down')
            elif actionInMP == 3:
                setSpellTrap('active')
            elif actionInMP == 4:
                pass
            elif actionInMP == 5:
                setSpellTrap('set')
            elif actionInMP == 6:
                pass
            elif actionInMP == 7:
                pass
            elif actionInMP == 8:
                pass
            elif actionInMP == 9:
                pass
            elif actionInMP == 10:
                pass
            elif actionInMP == 11:
                # endPhase()
                break
        except ValueError:
            print('Debes ingresar un número')
            time.sleep(1.5)