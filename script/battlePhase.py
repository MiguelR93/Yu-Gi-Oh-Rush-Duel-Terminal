import script.drawPhase as drawPhase
import script.duel as duel
import script.mainPhase as mainPhase


battlePhaseOptions = [
'\nQué quieres hacer?', 
'1: Declarar un ataque', 
'2: Ir a la End Phase'
]


def canChangeItsPosition(playerTurn):
    CHANGEABLE = 0
    for i in playerTurn[7:10]: 
        if (len(i) > 0) and (i['can change its position?'] == 'yes'):
            CHANGEABLE += 1
    return CHANGEABLE


def changeBattlePosition(playerTurn, changePosition):
    while duel.victory():
        duel.duelStatus(playerTurn)
        CHANGEABLE = 0
        if changePosition == 'attackToDefense':
            print("\n\n\nMonstruos que pueden cambiar su posición de ataque a defensa:")        
            for i,a in enumerate(playerTurn[7:10]):            
                if (len(a) > 0) and (('yes' in a['can change its position?']) and ('Attack' in a['position'])):
                    print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
                    CHANGEABLE += 1
        elif changePosition != 'attackToDefense':
            print("\n\n\nMonstruos que pueden cambiar su posición de defensa a ataque :")        
            for i,a in enumerate(playerTurn[7:10]):            
                if (len(a) > 0) and (('yes' in a['can change its position?']) and ('Attack' not in a['position'])):
                    print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
                    CHANGEABLE += 1
        
        if CHANGEABLE == 0:
            break
        
        try:
            chosed = int(input("\nElige un monstruo para cambiar de posición:\n")) + 7
            if (len(playerTurn[chosed]) == 0) or ('MONSTER' not in playerTurn[chosed]['cardType']): # Cuando lo que se elige no es un monstruo
                raise IndexError
            else:
                if (changePosition == 'attackToDefense') and (playerTurn[chosed]['can change its position?'] == 'yes'):
                    playerTurn[chosed]['position'] = 'Defense Face-Up'
                    playerTurn[chosed]['can change its position?'] = 'no'
                elif (changePosition != 'attackToDefense') and (playerTurn[chosed]['can change its position?'] == 'yes'):
                    playerTurn[chosed]['position'] = 'Attack'
                    playerTurn[chosed]['can change its position?'] = 'no'
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
    for i in playerTurn[7:10]:
        if (len(i) > 0) and (i['attacksCounter'] > 0):
            COUNTER += 1
    return COUNTER 

def monsterAttacked(playerTurn, chosed):
    playerTurn[chosed]['attacksCounter'] -= 1


def directAttack(playerTurn, chosed):
    # print(f"Esto debería ser LP rival: {playerTurn[15][0]}")
    # print(playerTurn[15][0] - int(playerTurn[chosed]['attack']))
    playerTurn[15][0] -= int(playerTurn[chosed]['attack'])
    monsterAttacked(playerTurn, chosed)
    if playerTurn[0] <= 0:
        playerTurn[14] = False
    elif playerTurn[15][0] <= 0:
        playerTurn[15][14] = False


def damage(playerTurn, chosed, target):
    print("Aquí calculamos el daño")
    if playerTurn[15][target]['position'] == 'Attack':
        if int(playerTurn[chosed]['attack']) == int(playerTurn[15][target]['attack']):
            print("ambos se destruyen")
            # mi monstruo se va al GY
            playerTurn[4].append(playerTurn[chosed])
            playerTurn[chosed] = []
            # el monstruo oponente se va al GY
            playerTurn[15][4].append(playerTurn[15][target])
            playerTurn[15][target] = []
        elif int(playerTurn[chosed]['attack']) > int(playerTurn[15][target]['attack']):
            print("Mi monstruo sigue en pie, el tuyo se va")
            lp = int(playerTurn[chosed]['attack']) - int(playerTurn[15][target]['attack'])
            playerTurn[15][0] -= lp
            # el monstruo oponente se va al GY
            playerTurn[15][4].append(playerTurn[15][target])
            playerTurn[15][target] = []

            monsterAttacked(playerTurn, chosed)
        elif int(playerTurn[chosed]['attack']) < int(playerTurn[15][target]['attack']):
            print("Mi monstruo se va, el tuyo sigue en pie")
            lp = int(playerTurn[15][target]['attack']) - int(playerTurn[chosed]['attack'])
            playerTurn[0] -= lp
            # mi monstruo se va al GY
            playerTurn[4].append(playerTurn[chosed])
            playerTurn[chosed] = []
    else:
        if int(playerTurn[chosed]['attack']) == int(playerTurn[15][target]['defense']):
            print("ninguno se destruye")
            print("en defensa >:V")
            duel.littleSleep()
        elif int(playerTurn[chosed]['attack']) > int(playerTurn[15][target]['defense']):
            print("Mi monstruo sigue en pie, el tuyo se va")
            print("en defensa >:V")
            # el monstruo oponente se va al GY
            playerTurn[15][4].append(playerTurn[15][target])
            playerTurn[15][target] = []
        elif int(playerTurn[chosed]['attack']) < int(playerTurn[15][target]['defense']):
            print("Mi monstruo se va, el tuyo sigue en pie")
            print("en defensa >:V")
            lp = int(playerTurn[15][target]['defense']) - int(playerTurn[chosed]['attack'])
            playerTurn[0] -= lp
        monsterAttacked(playerTurn, chosed)


def attackOnMonster(playerTurn, chosed):
    # debe permitir escoger un monstruo oponente como objetivo. Si lo que se escoge no es un monstruo, debe dar la opción de volver a escoger. También debe dar la opción de cancelar la declaración de ataque
    while True:
        print("Debería imprimir monstruos oponentes")
        for a,i in enumerate(playerTurn[15][7:10]):
            if len(i) > 0:
                print(f"{a}: {i['name']} | Posición: {i['position']}| Nivel: {i['level']} ATK/{i['attack']} DEF/{i['defense']}", end="\n")
            # else:
            #     print(i, end="   ")
            # print(i,end="\n")
        # duel.littleSleep()
        # input()
        try:
            target = int(input("Elige un objetivo:\n")) + 7
            if (len(playerTurn[15][target]) == 0) or ('MONSTER' not in playerTurn[15][target]['cardType']):
                # raise IndexError
                print("no hay un monstruo aquí")
                duel.littleSleep()
            elif playerTurn[15][target]['position'] == 'Defense Face-Down':
                print("El monstruo en defensa se voltea")
                playerTurn[15][target]['position'] = 'Defense Face-Up'
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
    # print(f"15: {playerTurn[15]}")   
    try:
        chosed = int(input("\nElige un monstruo para atacar:\n")) + 7
        # print(playerTurn[chosed]['cardType'])
        # print(len(playerTurn[chosed]), playerTurn[chosed])
        # duel.littleSleep()
        if (len(playerTurn[chosed]) == 0) or ('MONSTER' not in playerTurn[chosed]['cardType']): # Cuando lo que se elige no es un monstruo
            raise IndexError
            duel.littleSleep()
        elif playerTurn[chosed]['attacksCounter'] < 1:
            print("Este monstruo no puede atacar")
        elif duel.ocupiedMonsterZones(playerTurn[15]) <= 0:
            print("puedes atacar directo!")
            duel.littleSleep()
            directAttack(playerTurn, chosed)
        else:
            attackOnMonster(playerTurn, chosed)


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
        for i,a in enumerate(playerTurn[7:10]):            
            if (len(a) > 0) and (('Attack' in a['position']) and (a['attacksCounter'] > 0)):
                print(f"{i}: {a['name']}| Nvl: {a['level']} ATK/{a['attack']} DEF/{a['defense']} | Posición: {a['position']}")
        

        print(battlePhaseOptions[0])
        if (duel.ocupiedMonsterZones(playerTurn) > 0) and (monsterCanAttack(playerTurn) > 0):
            print(battlePhaseOptions[1])
        print(battlePhaseOptions[2])

        try:
            actionInBP = int(input("\nEscribe el número a la izquierda de la acción que quieres realizar: "))

            if actionInBP == 1 and duel.ocupiedMonsterZones(playerTurn) > 0:
                declareAttack(playerTurn)
            elif actionInBP == 2:
                # endPhase()
                break
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido')
