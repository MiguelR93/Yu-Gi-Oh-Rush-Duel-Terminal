import random


player1 = [ 
    8000, # "lp"
    [["011", "Monstruo", "Dragón", 4000, 4000], ["011", "Monstruo", "Dragón", 4000, 4000], ["011", "Monstruo", "Dragón", 4000, 4000],["010", "Monstruo", "Trueno", 4000, 4000], ["010", "Monstruo", "Trueno", 4000, 4000], ["010", "Monstruo", "Trueno", 4000, 4000], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"]], # "deck"
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
player2 = [ 
    8000, # "lp"
    [["011", "Monstruo", "Dragón", 4000, 4000], ["011", "Monstruo", "Dragón", 4000, 4000], ["011", "Monstruo", "Dragón", 4000, 4000],["010", "Monstruo", "Trueno", 4000, 4000], ["010", "Monstruo", "Trueno", 4000, 4000], ["010", "Monstruo", "Trueno", 4000, 4000], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['002', "Magia"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"], ['001', "Trampa"]], # "deck"
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
    # Game Start
    shuffleDeck(player1[1])
    shuffleDeck(player2[1])
    print(player1[1])
    print(player2[1])
    # Each player draw until have 4 cards in hand
    for i in players:
        while len(i[3]) < 4:
            i[3].append(i[1][0])
            i[1].remove(i[1][0])
        print(f"\n\nmano: {i[3]}")
    while thereIsNoWinner == True:
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
            if len(player1[1]) <= 0:
                print(youLose)
                return deckEmpty
            else:
                player1[3].append(player1[1][0])
                player1[1].remove(player1[1][0])
                activatingAnEff()
                print(f"\n\nmano: {player1[3]}")
        else:
            while len(player1[3]) < 5:
                if len(player1[1]) <= 0:
                    print(youLose)
                    return deckEmpty
                else:
                    player1[3].append(player1[1][0])
                    player1[1].remove(player1[1][0])
                    activatingAnEff()
                    print(f"\n\nmano: {player1[3]}")
        # Main Phase
        activatingAnEff()
        # for i in player1[3]:
        #     if "Monstruo" in player1[3]
        
        
        print(f"\n\nmano: {player1[3]}")


if __name__ == '__main__':
    run()