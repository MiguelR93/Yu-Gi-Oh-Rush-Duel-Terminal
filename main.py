import random


player1 = [ 
    8000, # "lp"
    [["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000]], # "deck"
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
    [["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["001", "Dragón", 4000, 4000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["002", "Planta", 2000, 2000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000],["003", "Trueno", 1000, 1000]], # "deck"
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
youWin = "YOU WIN!!!"
youLose = "Y O U  L O S E"

def descontadorAleatorioDeLifePoints():
    players[random.randint(0,1)][0] -= 1000

def evaluateLifePoints():
    pass

def run():
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
        # Game Start



if __name__ == '__main__':
    run()