import random, copy, time, os
import script.turn as turn
# contiene los elementos del juego: jugadores, turnos, contador de LP y condiciones de victoria

# Variables ----------------
player = [ 
    8000, # 0 = "lp"
    [
        # {'id': '1', 'name': 'Rush Dragon Dragears', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send the top card of your Deck to the GY.\n[Effect]: This turn, this card can make a second attack during the Battle Phase it destroyed a monster by battle.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '7', 'attack': '2500', 'defense': '1500', 'frontier': '[effect]', 'effect': 'none'},
        # {'id': '1', 'name': 'Rush Dragon Dragears', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send the top card of your Deck to the GY.\n[Effect]: This turn, this card can make a second attack during the Battle Phase it destroyed a monster by battle.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '7', 'attack': '2500', 'defense': '1500', 'frontier': '[effect]', 'effect': 'none'},
        # {'id': '1', 'name': 'Rush Dragon Dragears', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send the top card of your Deck to the GY.\n[Effect]: This turn, this card can make a second attack during the Battle Phase it destroyed a monster by battle.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '7', 'attack': '2500', 'defense': '1500', 'frontier': '[effect]', 'effect': 'none'},
        
        # {'id': '2', 'name': 'Gravity Press Dragon', 'cardType': 'MONSTER', 'text': '[Requirement] You can send 1 card from your hand to the GY.\n[Effect] Choose 1 face-up monster your opponent controls. It loses 700 ATK/DEF until the end of this turn.', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '6', 'attack': '1500', 'defense': '1000', 'frontier': '[effect]', 'effect': 'none'},
        # {'id': '3', 'name': 'Fire Guardian', 'cardType': 'MONSTER', 'text': 'The gatekeeper guarding the path to the Fire Dragon Kingdom. Those who cannot withstand its blazing breath are not qualified to go any further.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '6', 'attack': '2100', 'defense': '400', 'frontier': '[normal]'},
        # {'id': '4', 'name': 'Dragon Knight of Darkness', 'cardType': 'MONSTER', 'text': 'A dragon knight who leads the dark army. His merciless strikes are without equal. The evil sword he wields consumes the souls of his enemies, continuing to grow.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '5', 'attack': '1600', 'defense': '1100', 'frontier': '[normal]'},
        
        {'id': '5', 'name': 'Dragolite', 'cardType': 'MONSTER', 'text': 'It came from an underground mineral vein. It keeps fighting using the energy of an unknown ore as a power source. Its super hard hitting blows are simply outstanding!', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '4', 'attack': '1500', 'defense': '0', 'frontier': '[normal]'},
        {'id': '6', 'name': 'Twin-Edge Dragon', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: This card can make a second attack this turn.', 'attribute': 'LIGHT', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '0', 'frontier': '[effect]', 'effect': 'none'},
        {'id': '7', 'name': "Dragon's Priestess", 'cardType': 'MONSTER', 'text': "A young priestess from the bloodline of an ancient dragon. She offers her prayers daily for the peace of her tribe. It's said that her clear eyes can change the future of those they lay upon.", 'attribute': 'WATER', 'type': 'Dragon', 'level': '3', 'attack': '1100', 'defense': '100', 'frontier': '[normal]'},
        # {'id': '8', 'name': 'Dragon Bat', 'cardType': 'MONSTER', 'text': "A mysterious organism, researchers are still split over whether it's a bird or a beast. A flock of these flying together appears sort of draconian, so maybe it's a dragon.", 'attribute': 'DARK', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '400', 'frontier': '[normal]'},
        # {'id': '9', 'name': 'Phoenix Dragon', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: Add 1 monster (Level 5 or higher Dragon) from your GY to your hand.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '2', 'attack': '500', 'defense': '500', 'frontier': '[effect]', 'effect': 'none'},
        {'id': '10', 'name': 'Palm-Sized Drago', 'cardType': 'MONSTER', 'text': "A tiny dragon that loves peace. It's very used to people and will come close if you toss it some nuts. Apparently the ring hanging on its neck has some amazing secret.", 'attribute': 'WIND', 'type': 'Dragon', 'level': '1', 'attack': '0', 'defense': '1400', 'frontier': '[normal]'},

        {'id': '5', 'name': 'Dragolite', 'cardType': 'MONSTER', 'text': 'It came from an underground mineral vein. It keeps fighting using the energy of an unknown ore as a power source. Its super hard hitting blows are simply outstanding!', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '4', 'attack': '1500', 'defense': '0', 'frontier': '[normal]'},
        {'id': '6', 'name': 'Twin-Edge Dragon', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: This card can make a second attack this turn.', 'attribute': 'LIGHT', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '0', 'frontier': '[effect]', 'effect': 'none'},
        {'id': '7', 'name': "Dragon's Priestess", 'cardType': 'MONSTER', 'text': "A young priestess from the bloodline of an ancient dragon. She offers her prayers daily for the peace of her tribe. It's said that her clear eyes can change the future of those they lay upon.", 'attribute': 'WATER', 'type': 'Dragon', 'level': '3', 'attack': '1100', 'defense': '100', 'frontier': '[normal]'},
        {'id': '8', 'name': 'Dragon Bat', 'cardType': 'MONSTER', 'text': "A mysterious organism, researchers are still split over whether it's a bird or a beast. A flock of these flying together appears sort of draconian, so maybe it's a dragon.", 'attribute': 'DARK', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '400', 'frontier': '[normal]'},
        {'id': '9', 'name': 'Phoenix Dragon', 'cardType': 'MONSTER', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: Add 1 monster (Level 5 or higher Dragon) from your GY to your hand.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '2', 'attack': '500', 'defense': '500', 'frontier': '[effect]', 'effect': 'none'},
        {'id': '10', 'name': 'Palm-Sized Drago', 'cardType': 'MONSTER', 'text': "A tiny dragon that loves peace. It's very used to people and will come close if you toss it some nuts. Apparently the ring hanging on its neck has some amazing secret.", 'attribute': 'WIND', 'type': 'Dragon', 'level': '1', 'attack': '0', 'defense': '1400', 'frontier': '[normal]'},

        # {'id': '11', 'name': 'Dragonic Pressure', 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'},
        # {'id': '12', 'name': "Fire Dragon's Heatflash", 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: If you control a face-up monster (Dragon).\n[Effect]: Destroy 1 Spell/Trap your opponent controls.'},
        # {'id': '13', 'name': 'Dragon Encounter', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement] When your opponent Normal or Special Summons a monster(s).\n[Effect] Special Summon 1 monster (Dragon) from your hand.'},
        # {'id': '14', 'name': 'Counteroffensive Dragonstrike', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': "[Requirement] When a monster (Dragon) you control is destroyed by battle with an opponent's attacking monster, send 1 card from your hand to the GY.\n[Effect] Destroy 1 monster your opponent controls."},


        # # {'id': '11', 'name': 'Dragonic Pressure', 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'},
        # # {'id': '12', 'name': "Fire Dragon's Heatflash", 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: If you control a face-up monster (Dragon).\n[Effect]: Destroy 1 Spell/Trap your opponent controls.'},
        # # {'id': '13', 'name': 'Dragon Encounter', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement] When your opponent Normal or Special Summons a monster(s).\n[Effect] Special Summon 1 monster (Dragon) from your hand.'},
        # # {'id': '14', 'name': 'Counteroffensive Dragonstrike', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': "[Requirement] When a monster (Dragon) you control is destroyed by battle with an opponent's attacking monster, send 1 card from your hand to the GY.\n[Effect] Destroy 1 monster your opponent controls."},


        # # {'id': '11', 'name': 'Dragonic Pressure', 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'},
        # # {'id': '12', 'name': "Fire Dragon's Heatflash", 'cardType': 'SPELL', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement]: If you control a face-up monster (Dragon).\n[Effect]: Destroy 1 Spell/Trap your opponent controls.'},
        # # {'id': '13', 'name': 'Dragon Encounter', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': '[Requirement] When your opponent Normal or Special Summons a monster(s).\n[Effect] Special Summon 1 monster (Dragon) from your hand.'},
        # # {'id': '14', 'name': 'Counteroffensive Dragonstrike', 'cardType': 'TRAP', 'text': 'none', 'icon': 'normal', 'effect': "[Requirement] When a monster (Dragon) you control is destroyed by battle with an opponent's attacking monster, send 1 card from your hand to the GY.\n[Effect] Destroy 1 monster your opponent controls."},


       ], # 1 = "deck"
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
    [], # 12 = "rightSTCardZone"
    [], # 13 = "player's name"
    True, # 14 = "victory condition" both True == There's no winner; both False == DRAW; one False, that player lose
    None, # 15 = "oponent" for "Jugador" == "COM" and vice versa
]    


players = {'p1': copy.deepcopy(player), # el jugador
        'p2': copy.deepcopy(player)} # la computadora

TURNSCOUNTER = 0

# Duel tools ----------------
def shuffleDeck(playerDeck):
    random.shuffle(playerDeck)


def turnStarts():
    global TURNSCOUNTER
    TURNSCOUNTER += 1


def currentlyTurn():
    return TURNSCOUNTER

def victory():
    if players['p1'][14] == False:
        return False
    elif players['p2'][14] == False:
        return False
    else:
        return True


def ocupiedMonsterZones(playerTurn): # convertir en anónima
    COUNTER = 0
    for i in playerTurn[7:10]:
        if len(i) > 0:
            COUNTER += 1
    return COUNTER


def duelStatus(playerTurn): # imprime el estado del duelo: LP, deck, mano, campo, cementerio de ambos jugadores
    os.system("clear")
    print(f"Turn: {TURNSCOUNTER}")
    print(f"Turno de: {playerTurn[13]}\n\n")
    # print(f"Zonas de Monstruo ocupadas: {ocupiedMonsterZones(playerTurn)}") # esta cambia en función del jugador en turno
    print(f"Rival LP: {max(players['p2'][0],0)}")
    print(f"Deck rival: {len(players['p2'][1])}") # deck
    print(f"Cartas en mano rival: {len(players['p2'][3])}") # mano
    # ----v OPONENT'S HAND
    for i,a in enumerate(players['p2'][3]):
        if 'level' in players['p2'][3][i]:
            print(f"{i}: {players['p2'][3][i]['name']}| Nvl: {players['p2'][3][i]['level']} ATK/{players['p2'][3][i]['attack']} DEF/{players['p2'][3][i]['defense']}")
        else:
            print(f"{i}: {players['p2'][3][i]['name']} | {players['p2'][3][i]['cardType']} | {players['p2'][3][i]['icon']}")
    # ----^ OPONENT'S HAND
    print(f"Cartas en GY rival: {len(players['p2'][4])}")
    print("\nCampo oponente:")
    # s/t
    for i in players['p2'][12:9:-1]:
        if len(i) > 0:
            print(f"{i['name']} | {i['cardType']} | Posición: {i['position']}",sep="//", end="   ")
        else:
            print(i,end="   ")
    print("\n")
    # monstruos
    for i in players['p2'][9:6:-1]:
        if len(i) > 0:
            print(f"{i['name']} | Posición: {i['position']}| Nivel: {i['level']} ATK/{i['attack']} DEF/{i['defense']}",sep="//", end="   ")
        else:
            print(i, end="   ")
    print("\n\nTu campo:")
    # monstruos
    for i in players['p1'][7:10]:
        # if type(i) == dict:
        #     print(i['name'], end="   ")
        if len(i) > 0:
            print(f"{i['name']} | Posición: {i['position']}| Nivel: {i['level']} ATK/{i['attack']} DEF/{i['defense']} | puede cambiar de posición {i['can change its position?']}",sep="//", end="   ")
        else:
            print(i, end="   ")
    print("\n")
    # s/t
    for i in players['p1'][10:13]:
        if len(i) > 0:
            print(f"{i['name']} | {i['cardType']} | Posición: {i['position']}",sep="//", end="   ")
        else:
            print(i,end="   ")
    # Tu campo:
    print("\n")
    print(f"Tus Lp: {players['p1'][0]}")
    print(f"Tu deck: {len(players['p1'][1])}")
    print(f"Tu GY: {len(players['p1'][4])}")
    # imprimiendo la mano:
    print(f"Tu mano: {len(players['p1'][3])}")
    for i,a in enumerate(players['p1'][3]):
        if 'level' in players['p1'][3][i]:
            print(f"{i}: {players['p1'][3][i]['name']}| Nvl: {players['p1'][3][i]['level']} ATK/{players['p1'][3][i]['attack']} DEF/{players['p1'][3][i]['defense']}")
        else:
            print(f"{i}: {players['p1'][3][i]['name']} | {players['p1'][3][i]['cardType']} | {players['p1'][3][i]['icon']}")


def littleSleep(): time.sleep(0)


def printHandAndDeckCards():
    for i in players:
        print(f"\n\n\n{i}'s mano: {players[i][3]}\n\n\n")
        print(f"\n\n\n{i}'s Deck: {players[i][1]}", end="\n\n\n")
    

# Game start! ----------------
def gameStart():
    print('\nBienvenido a gameStart\n') # borrar :)
    # # print both deck status
    # printHandAndDeckCards()
    # global players

    players['p1'][13], players['p2'][13] = "Jugador", "COM"
    players['p2'][15], players['p1'][15] = players['p1'], players['p2']

    # Game start ------
    # shuffle both players' deck
    shuffleDeck(players['p1'][1])
    shuffleDeck(players['p2'][1])

    # Each player draw until have 4 cards in hand
    for i in players:
        # print(players[i][1], end="\n\n\n")
        while len(players[i][3]) < 4:
            players[i][3].append(players[i][1][0])
            players[i][1].remove(players[i][1][0])
        # # print both deck status
        # printHandAndDeckCards()

    while victory():
        for i in players:
            # littleSleep()
            # print(f"{i}'s turn")
            # duelStatus(playerTurn)
            turn.turn(players[i])
            if victory() == False:
                break
    
    if players['p1'][14] == False:
        print("Perdiste!")
    elif players['p2'][14] == False:
        print("Ganaste!")
    # else:
    #     return True


# zona de prueba ------
def run():
    gameStart()


if __name__ == '__main__':
    run()


# CÓDIGO VIEJO ---------------------------------------------------------------------------------

# # Variables del juego
# ## Condiciones de victoria
# thereIsNoWinner = True
# # lifePoint0 = not thereIsNoWinner
# # deckEmpty = not thereIsNoWinner
# youWin = "YOU WIN!!!"
# youLose = "Y O U  L O S E"









# def activatingAnEff():
#     # si el oponente activa un efecto, resolverlo, sino, activa y resuelve uno tú
#     pass






# def checkLP():
#     if players['p1'][0] <= 0:
#         print(youLose)
#         return lifePoint0
#     elif players['p2'][0] <=0:
#         print(youWin)
#         return lifePoint0





# mainPhaseOptions = [
# '\nQué quieres hacer?', 
# '1: Invocar un monstruo', 
# '2: Colocar un monstruo', 
# '3: Activar una Magia de tu mano', 
# '4: Activar una Magia del campo', 
# '5: Colocar una Trampa o Magia de tu mano', 
# '6: Activar una trampa del campo', 
# '7: Cambiar la posición de ataque a defensa', 
# '8: Cambiar la posición de defensa boca-abajo a ataque', 
# '9: Cambiar la posición de defensa boca-arriba a ataque', 
# '10: Ir a la Battle Phase', 
# '11: Ir a la End Phase'
# ]

# gameStart():
#     while thereIsNoWinner == True:
#             global TURNSCOUNTER
#             TURNSCOUNTER += 1
#             gameStart()
#             checkLP()
            
#             duelStatus(playerTurn)
#             # Draw Phase
#             drawPhase()
            
#             # Main Phase
#             mainPhase()
            
#             # Battle Phase: Empieza la batalla!
#             # battlePhase()

#             # End Phase
#             endPhase()
        
#         print("Fin del juego :)")