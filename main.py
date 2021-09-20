import random, os


player1 = [ 
    8000, # 0 = "lp"
    [["011", "Monstruo", "Dragón", 2000, 4000, 8], ["012", "Monstruo", "Dragón", 4000, 3000, 5], ["013", "Monstruo", "Dragón", 3000, 4000, 4],["010", "Monstruo", "Trueno", 4000, 2000, 6], ["014", "Monstruo", "Trueno", 1000, 4000, 7], ["015", "Monstruo", "Trueno", 4000, 1000, 2],["020", "Monstruo", "Trueno", 4000, 2000, 3], ["024", "Monstruo", "Trueno", 1000, 4000, 4], ["025", "Monstruo", "Trueno", 4000, 1000, 1], ['022', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"]], # 1 = "deck"
    [], # 2 = "extraDeck"
    [], # 3 = "hand"
    [], # 4 = "gy"
    [], # 5 = "excavated"
    [], # 6 = "fieldSpellCardZone"
    [], # 7 = "leftMonsterCardZone"
    [], # 8 = "centerMonsterCardZone"
    [], # 9 = "rightMonsterCardZone"
    [], # 10 = "leftSTCardZone"
    [], # 11 = "centerleftSTCardZone"
    [] # 12 = "rightleftSTCardZone"
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

def descontadorAleatorioDeLifePoints():
    players[random.randint(0,1)][0] -= 1000

def evaluateLifePoints():
    pass

def shuffleDeck(playersDeck):
    random.shuffle(playersDeck)

def activatingAnEff():
    # si el oponente activa un efecto, resolverlo, sino, activa y resuelve uno tú
    pass

def run():
    os.system("clear")
    # Game Start
    shuffleDeck(player1[1])
    shuffleDeck(player2[1])
    print(f"Deck player1: {player1[1]}\n\n")
    print(f"Deck player2: {player2[1]}\n\n")
    # Each player draw until have 4 cards in hand
    for i in players:
        while len(i[3]) < 4:
            i[3].append(i[1][0])
            i[1].remove(i[1][0])
        print(f"\n\nmano: {i[3]}")
    TURNSCOUNTER = 0
    while thereIsNoWinner == True:
        os.system("clear")
        TURNSCOUNTER += 1
        print(f"Turn: {TURNSCOUNTER}\n")
        # player1[0] -= 1000
        descontadorAleatorioDeLifePoints()
        print(f"Tus Lp: {player1[0]}\n\nRival LP: {player2[0]}")
        if player1[0] <= 0:
            print(youLose)
            return lifePoint0
        elif player2[0] <=0:
            print(youWin)
            return lifePoint0
        # Draw Phase
        activatingAnEff()
        if len(player1[3]) >= 5:
            print("tenemos 5 o más cartas")
            if len(player1[1]) <= 0:
                print(youLose)
                return deckEmpty
            else:
                player1[3].append(player1[1][0])
                player1[1].remove(player1[1][0])
                activatingAnEff()
                print(f"\n\nmano: {player1[3]}\n\nCartas en mano: {len(player1[3])}\n\n",sep="\n")
        else:
            print("tenemos menos de 5 cartas")
            while len(player1[3]) < 5:
                if len(player1[1]) <= 0:
                    print(youLose)
                    return deckEmpty
                else:
                    player1[3].append(player1[1][0])
                    # print("aquí robamos")
                    player1[1].remove(player1[1][0])
                    # print("aquí quitamos")
                    activatingAnEff()
                    print(f"\n\nmano: {player1[3]}\n\nCartas en mano: {len(player1[3])}\n\n",sep="\n")
        # Main Phase
        activatingAnEff()
        for i,a in enumerate(player1[3]):
            if "Monstruo" in player1[3][i]:
                print("\nEs un monstruo!")
            elif "Magia" in player1[3][i]:
                print("\nEs una Magia!")
            elif "Trampa" in player1[3][i]:
                print("\nEs una Trampa!")
        # imprimiendo la mano:
        for i,a in enumerate(player1[3]):
            print(f"{i}: {player1[3][i][1:]}")
        # Acciones en Main Phase
        while True:
        # Mostrando el campo
            for i in player1[7:10]:
                print(i, end="///")
            actionInMP = int(input("\n\n\nQué quieres hacer?\n1: Invocar un monstruo\n2: Colocar un monstruo\n3: Activar una Magia de tu mano\n4: Activar una Magia del campo\n5: Colocar una Trampa de tu mano\n6: Activar una trampa del campo\n7: Ir a la Battle Phase\n"))
            if actionInMP == 1:
                summonAMonster = int(input("ingresa el índice del monstruo: "))
                monsterZonePosition = int(input("En dónde quieres ponerlo?\n1: zona Izquierda\n2: zona central\n3: zona derecha\n"))
                player1[monsterZonePosition+6] = player1[3][summonAMonster]
                player1[3].remove(player1[3][summonAMonster])
            if actionInMP == 2:
                pass
            if actionInMP == 3:
                pass
            if actionInMP == 4:
                pass
            if actionInMP == 5:
                pass
            if actionInMP == 6:
                pass
            if actionInMP == 7:
                break
        # Empieza la batalla!
        activatingAnEff()
        for i,a in enumerate(player1[7:10]):
            print(f"{i}: {a}", sep="\\")
        chosed = int(input("\nElige un monstruo para atacar:\n"))
        
        print(f"\n\nmano: {player1[3]}\n\n")


if __name__ == '__main__':
    run()