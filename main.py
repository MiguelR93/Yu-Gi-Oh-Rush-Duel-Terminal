import random, os


player1 = [ 
    8000, # 0 = "lp"
    [["011", "Monstruo", "Dragón", 2000, 4000, 8], ["012", "Monstruo", "Dragón", 4000, 3000, 5], ["013", "Monstruo", "Dragón", 3000, 4000, 4], ["010", "Monstruo", "Trueno", 4000, 2000, 6], ["014", "Monstruo", "Trueno", 1000, 4000, 7], ["015", "Monstruo", "Trueno", 4000, 1000, 2], ["020", "Monstruo", "Trueno", 4000, 2000, 3], ["024", "Monstruo", "Trueno", 1000, 4000, 4], ["025", "Monstruo", "Trueno", 4000, 1000, 1], ['022', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"]], # 1 = "deck"
    [], # 2 = "extraDeck"
    [], # 3 = "hand"
    [], # 4 = "gy"
    [], # 5 = "excavated"
    [], # 6 = "fieldSpellCardZone"
    [], # 7 = "leftMonsterCardZone"
    [], # 8 = "centerMonsterCardZone"
    [], # 9 = "rightMonsterCardZone"
    [], # 10 = "leftSTCardZone"
    [], # 11 = "centerSTCardZone"
    [] # 12 = "rightSTCardZone"
]    
player2 = [ 
    8000, # "lp"
    [["011", "Monstruo", "Dragón", 2000, 4000, 8], ["012", "Monstruo", "Dragón", 4000, 3000, 5], ["013", "Monstruo", "Dragón", 3000, 4000, 4],["010", "Monstruo", "Trueno", 4000, 2000, 6], ["014", "Monstruo", "Trueno", 1000, 4000, 7], ["015", "Monstruo", "Trueno", 4000, 1000, 2],["020", "Monstruo", "Trueno", 4000, 2000, 3], ["024", "Monstruo", "Trueno", 1000, 4000, 4], ["025", "Monstruo", "Trueno", 4000, 1000, 1], ['022', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"]], # "deck"
    [], # "extraDeck"
    [], # "hand"
    [], # "gy"
    [], # "excavated"
    [], # "fieldSpellCardZone"
    [], # "leftMonsterCardZone"
    [], # "centerMonsterCardZone"
    [], # "rightMonsterCardZone"
    [], # "leftSTCardZone"
    [], # "centerleftSTCardZone"
    [] # "rightleftSTCardZone"
]
players = [player1, player2]

thereIsNoWinner = True
lifePoint0 = not thereIsNoWinner
deckEmpty = not thereIsNoWinner
youWin = "YOU WIN!!!"
youLose = "Y O U  L O S E"
TURNSCOUNTER = 0


def descontadorAleatorioDeLifePoints():
    players[random.randint(0,1)][0] -= 1000


def evaluateLifePoints():
    pass


def shuffleDeck(playersDeck):
    random.shuffle(playersDeck)


def activatingAnEff():
    # si el oponente activa un efecto, resolverlo, sino, activa y resuelve uno tú
    pass


def duelStatus(): # imprime el estado del duelo: LP, deck, mano, campo, cementerio de ambos jugadores
    os.system("clear")
    print(f"Turn: {TURNSCOUNTER}")
    print(f"Rival LP: {player2[0]}")
    print(f"Deck rival: {len(player2[1])}") # deck
    print(f"Cartas en mano rival: {len(player2[3])}") # mano
    print("\nCampo oponente:")
    for i in player2[-1:-4:-1]:
        print(i,end="   ")
    print("\n")
    for i in player2[-4:-7:-1]:
        print(i,end="   ")
    print("\n\nTu campo:")
    for i in player1[7:10]:
        print(i,end="   ")
    print("\n")
    for i in player1[10:13]:
        print(i,end="   ")
    # Tu campo:
    print("\n")
    print(f"Tus Lp: {player1[0]}")
    print(f"Tu deck: {len(player1[1])}")
    # imprimiendo la mano:
    print(f"Tu mano: {len(player1[3])}")
    for i,a in enumerate(player1[3]):
        print(f"{i}: {player1[3][i][1:]}")


def gameStart():
    shuffleDeck(player1[1])
    shuffleDeck(player2[1])
    # print(f"Deck player1: {player1[1]}\n\n")
    # print(f"Deck player2: {player2[1]}\n\n")
    # Each player draw until have 4 cards in hand
    for i in players:
        while len(i[3]) < 4:
            i[3].append(i[1][0])
            i[1].remove(i[1][0])
        # print(f"\n\nmano: {i[3]}")


def checkLP():
    if player1[0] <= 0:
        print(youLose)
        return lifePoint0
    elif player2[0] <=0:
        print(youWin)
        return lifePoint0


def drawACard():
    if len(player1[1]) <= 0:
        print(youLose)
        return deckEmpty
    else:
        player1[3].append(player1[1][0]) # añade la carta del deck a la mano
        player1[1].remove(player1[1][0]) # quita del deck la carta añadida a la mano
        activatingAnEff()
        print(f"\n\nmano: {player1[3]}\n\nCartas en mano: {len(player1[3])}\n\n",sep="\n") # es necesario?


def drawPhase():
    activatingAnEff()
    if len(player1[3]) >= 5:
        # print("tenemos 5 o más cartas")
        drawACard()
    else:
        # print("tenemos menos de 5 cartas")
        while len(player1[3]) < 5:
            drawACard()


mainPhaseOptions = "\n\n\nQué quieres hacer?\n1: Invocar un monstruo\n2: Colocar un monstruo\n3: Activar una Magia de tu mano\n4: Activar una Magia del campo\n5: Colocar una Trampa de tu mano\n6: Activar una trampa del campo\n7: Cambiar la posición de ataque a defensa\n8: cambiar la posición de defensa boca-abajo a ataque\n9: Cambiar la posición de defensa boca-arriba a ataque\n10: Ir a la Battle Phase\n11: Ir a la End Phase\n"


def mainPhase():
    activatingAnEff()
    # for i,a in enumerate(player1[3]):
    #     if "Monstruo" in player1[3][i]:
    #         print("\nEs un monstruo!")
    #     elif "Magia" in player1[3][i]:
    #         print("\nEs una Magia!")
    #     elif "Trampa" in player1[3][i]:
    #         print("\nEs una Trampa!")
    # Acciones en Main Phase
    while True:
    # Mostrando el campo???
        duelStatus()
        actionInMP = int(input(mainPhaseOptions))
        if actionInMP == 1:
            summonAMonster = int(input("ingresa el índice del monstruo: "))
            while True:
                monsterZonePosition = int(input("En dónde quieres ponerlo?\n1: zona Izquierda\n2: zona central\n3: zona derecha\n"))
                if len(player1[monsterZonePosition+6]) != 0:
                    ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                    if ocupado == 1:
                        continue
                    elif ocupado == 2:
                        break
                else:
                    player1[monsterZonePosition+6] = player1[3][summonAMonster]
                    player1[3].remove(player1[3][summonAMonster])
                    break
        elif actionInMP == 2:
            pass
        elif actionInMP == 3:
            pass
        elif actionInMP == 4:
            pass
        elif actionInMP == 5:
            pass
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


def battlePhase():
    activatingAnEff()
    for i,a in enumerate(player1[7:10]):
        print(f"{i}: {a}", sep="\\")
    chosed = int(input("\nElige un monstruo para atacar:\n"))


def endPhase():
    pass


def run():
    os.system("clear")
    # Game Start
    gameStart()
    while thereIsNoWinner == True:
        global TURNSCOUNTER
        TURNSCOUNTER += 1
        gameStart()
        checkLP()
        
        duelStatus()
        # Draw Phase
        drawPhase()
        
        # Main Phase
        mainPhase()
        
        # Battle Phase: Empieza la batalla!
        # battlePhase()

        # End Phase
        endPhase()


if __name__ == '__main__':
    run()