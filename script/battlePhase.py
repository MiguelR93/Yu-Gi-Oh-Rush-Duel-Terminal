import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase
import script.endPhase as endPhase


battlePhaseOptions = [
'\nQué quieres hacer?', 
'1: Declarar un ataque', 
'2: Ir a la End Phase'
]


def canChangeItsPosition(playerTurn):
    CHANGEABLE = 0
    for i in playerTurn[7:10]: 
        if (type(i) != list) and (i.canChangeItsPosition == 'yes'):
            CHANGEABLE += 1
    return CHANGEABLE


def changeBattlePosition(playerTurn, changePosition):
    while duel.victory():
        duel.duelStatus(playerTurn)
        CHANGEABLE = 0
        if changePosition == 'attackToDefense':
            print("\n\n\nMonstruos que pueden cambiar su posición de ataque a defensa:")        
            for i,a in enumerate(playerTurn[7:10]):            
                if (type(a) != list) and ((True in a.canChangeItsPosition) and ('Attack' in a.position)):
                    print(f"{i}: {a.name}| Nvl: {a.level} ATK/{a.attack} DEF/{a.defense} | Posición: {a.position}")
                    CHANGEABLE += 1
        elif changePosition != 'attackToDefense':
            print("\n\n\nMonstruos que pueden cambiar su posición de defensa a ataque :")        
            for i,a in enumerate(playerTurn[7:10]):            
                if (type(a) != list) and ((True in a.canChangeItsPosition) and ('Attack' not in a.position)):
                    print(f"{i}: {a.name}| Nvl: {a.level} ATK/{a.attack} DEF/{a.defense} | Posición: {a.position}")
                    CHANGEABLE += 1
        
        if CHANGEABLE == 0:
            break
        
        try:
            chosed = int(input("\nElige un monstruo para cambiar de posición:\n")) + 7
            if (len(playerTurn.playerMonsterZones[chosed]) == 0) or ('MONSTER' not in playerTurn.playerMonsterZones[chosed].cardType): # Cuando lo que se elige no es un monstruo
                raise IndexError
            else:
                if (changePosition == 'attackToDefense') and (playerTurn.playerMonsterZones[chosed].canChangeItsPosition == 'yes'):
                    playerTurn.playerMonsterZones[chosed].position = 'Defense Face-Up'
                    playerTurn.playerMonsterZones[chosed].canChangeItsPosition = 'no'
                elif (changePosition != 'attackToDefense') and (playerTurn.playerMonsterZones[chosed].canChangeItsPosition == 'yes'):
                    playerTurn.playerMonsterZones[chosed].position = 'Attack'
                    playerTurn.playerMonsterZones[chosed].canChangeItsPosition = 'no'
                break
        except IndexError:
            print('Valor equivocado')
            # input()
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            duel.littleSleep()
        except TypeError:
            print('Debes ingresar un número')
            duel.littleSleep()


def monsterCanAttack(playerTurn):
    COUNTER = 0
    for i in playerTurn.playerMonsterZones:
        if (type(i) != list) and (i.canAttackThisTurn > 0):
            COUNTER += 1
    return COUNTER 

def monsterAttacked(playerTurn, chosed):
    playerTurn.playerMonsterZones[chosed].canAttackThisTurn -= 1


def directAttack(playerTurn, chosed):
    # print(f"Esto debería ser LP rival: {playerTurn.oponent.lp}")
    # print(playerTurn.oponent.lp - int(playerTurn.playerMonsterZones[chosed].attack))
    playerTurn.oponent.lp -= int(playerTurn.playerMonsterZones[chosed].attack)
    monsterAttacked(playerTurn, chosed)
    if playerTurn.lp <= 0:
        playerTurn.victoryStatus = False
    elif playerTurn.oponent.lp <= 0:
        playerTurn.oponent.victoryStatus = False


def damage(playerTurn, chosed, target):
    print("Aquí calculamos el daño")
    if playerTurn.oponent[target].position == 'Attack':
        if int(playerTurn.playerMonsterZones[chosed].attack) == int(playerTurn.oponent[target].attack):
            print("ambos se destruyen")
            # mi monstruo se va al GY
            playerTurn[4].append(playerTurn.playerMonsterZones[chosed])
            playerTurn.playerMonsterZones[chosed] = []
            # el monstruo oponente se va al GY
            duel.fromFieldToGY(playerTurn.oponent[target], 'Destroyed by Battle')
            playerTurn.oponent.gy.append(playerTurn.oponent[target])
            playerTurn.oponent[target] = []
        elif int(playerTurn.playerMonsterZones[chosed].attack) > int(playerTurn.oponent[target].attack):
            print("Mi monstruo sigue en pie, el tuyo se va")
            lp = int(playerTurn.playerMonsterZones[chosed].attack) - int(playerTurn.oponent[target].attack)
            playerTurn.oponent.lp -= lp
            # el monstruo oponente se va al GY
            duel.fromFieldToGY(playerTurn.oponent[target], 'Destroyed by Battle')
            playerTurn.oponent.gy.append(playerTurn.oponent[target])
            playerTurn.oponent[target] = []

            monsterAttacked(playerTurn, chosed)
        elif int(playerTurn.playerMonsterZones[chosed].attack) < int(playerTurn.oponent[target].attack):
            print("Mi monstruo se va, el tuyo sigue en pie")
            lp = int(playerTurn.oponent[target].attack) - int(playerTurn.playerMonsterZones[chosed].attack)
            playerTurn.lp -= lp
            # mi monstruo se va al GY
            playerTurn[4].append(playerTurn.playerMonsterZones[chosed])
            playerTurn.playerMonsterZones[chosed] = []
    else:
        if int(playerTurn.playerMonsterZones[chosed].attack) == int(playerTurn.oponent[target].defense):
            print("ninguno se destruye")
            print("en defensa >:V")
            duel.littleSleep()
        elif int(playerTurn.playerMonsterZones[chosed].attack) > int(playerTurn.oponent[target].defense):
            print("Mi monstruo sigue en pie, el tuyo se va")
            print("en defensa >:V")
            # el monstruo oponente se va al GY
            playerTurn.oponent.gy.append(playerTurn.oponent[target])
            playerTurn.oponent[target] = []
        elif int(playerTurn.playerMonsterZones[chosed].attack) < int(playerTurn.oponent[target].defense):
            print("Mi monstruo se va, el tuyo sigue en pie")
            print("en defensa >:V")
            lp = int(playerTurn.oponent[target].defense) - int(playerTurn.playerMonsterZones[chosed].attack)
            playerTurn.lp -= lp
        monsterAttacked(playerTurn, chosed)


def attackOnMonster(playerTurn, chosed):
    # debe permitir escoger un monstruo oponente como objetivo. Si lo que se escoge no es un monstruo, debe dar la opción de volver a escoger. También debe dar la opción de cancelar la declaración de ataque
    while True:
        print("Debería imprimir monstruos oponentes")
        for a,i in enumerate(playerTurn.oponent[7:10]):
            if type(i) != list:
                print(f"{a}: {i.name} | Posición: {i.position}| Nivel: {i.level} ATK/{i.attack} DEF/{i.defense}", end="\n")
            # else:
            #     print(i, end="   ")
            # print(i,end="\n")
        # duel.littleSleep()
        # input()
        try:
            target = int(input("Elige un objetivo:\n")) + 7
            if (len(playerTurn.oponent[target]) == 0) or ('MONSTER' not in playerTurn.oponent[target].cardType):
                # raise IndexError
                print("no hay un monstruo aquí")
                duel.littleSleep()
            elif playerTurn.oponent[target].position == 'Defense Face-Down':
                print("El monstruo en defensa se voltea")
                playerTurn.oponent[target].position = 'Defense Face-Up'
                damage(playerTurn, chosed, target)
                break
            else:
                damage(playerTurn, chosed, target)
                break
        except IndexError:
            print('Valor equivocado')
            # input()
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            duel.littleSleep()
        except TypeError:
            print('Debes ingresar un número')
            duel.littleSleep()


def declareAttack(playerTurn):
    # print(f"13: {playerTurn[13]}")
    # print(f"15: {playerTurn.oponent}")   
    try:
        chosed = int(input("\nElige un monstruo para atacar:\n"))
        # print(playerTurn.playerMonsterZones[chosed].cardType)
        # print(len(playerTurn.playerMonsterZones[chosed]), playerTurn.playerMonsterZones[chosed])
        # duel.littleSleep()
        if (type(playerTurn.playerMonsterZones[chosed]) == list) or ('MONSTER' not in playerTurn.playerMonsterZones[chosed].cardType): # Cuando lo que se elige no es un monstruo
            print("Error")
            raise IndexError
            duel.littleSleep()
        elif playerTurn.playerMonsterZones[chosed].canAttackThisTurn < 1:
            print("Este monstruo no puede atacar")
        elif playerTurn.playerMonsterZones[chosed].position != 'attackPosition':
            print("Este monstruo no puede atacar")
        elif duel.ocupiedMonsterZones(playerTurn.oponent) <= 0:
            print("puedes atacar directo!")
            # duel.littleSleep()
            directAttack(playerTurn, chosed)
        else:
            attackOnMonster(playerTurn, chosed)
            print("ahora, atacaremos a un monstruo!")
            duel.littleSleep()


    except IndexError:
        print('Valor equivocado')
        # input()
        duel.littleSleep()
    except ValueError:
        print('Debes ingresar un número')
        duel.littleSleep()


def battlePhase(playerTurn):
    # activatingAnEff()
    while duel.victory():
        duel.duelStatus(playerTurn)
        print("\n\n\nMonstruos que pueden atacar:")   
        COUNTER_MONSTER_CAN_ATTACK = 0     
        for i,a in enumerate(playerTurn.playerMonsterZones):            
            if (type(a) != list) and (('attackPosition' in a.position) and (a.canAttackThisTurn > 0)):
                print(f"{i}: {a.name}| Nvl: {a.level} ATK/{a.attack} DEF/{a.defense} | Posición: {a.position}")
                COUNTER_MONSTER_CAN_ATTACK += 1
        

        print(battlePhaseOptions[0])
        if (playerTurn.counterMonsterInMyField() > 0) and (monsterCanAttack(playerTurn) > 0):
            print(battlePhaseOptions[1])
        print(battlePhaseOptions[2])

        try:
            actionInBP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInBP == 1 and COUNTER_MONSTER_CAN_ATTACK > 0:
                declareAttack(playerTurn)
            elif actionInBP == 1 and COUNTER_MONSTER_CAN_ATTACK <= 0:
                print("No cuentas con monstruos para atacar")
            elif actionInBP == 2:
                # endPhase.endPhase(playerTurn)
                playerTurn.endPhase()
                break
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido')
