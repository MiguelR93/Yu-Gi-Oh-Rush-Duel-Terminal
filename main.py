import random, os


player1 = [ 
    8000, # 0 = "lp"
    [
        {'id': '1', 'name': 'Rush Dragon Dragears', 'text': '[Requirement]: You can send the top card of your Deck to the GY.\n[Effect]: This turn, this card can make a second attack during the Battle Phase it destroyed a monster by battle.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '7', 'attack': '2500', 'defense': '1500', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '2', 'name': 'Gravity Press Dragon', 'text': '[Requirement] You can send 1 card from your hand to the GY.\n[Effect] Choose 1 face-up monster your opponent controls. It loses 700 ATK/DEF until the end of this turn.', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '6', 'attack': '1500', 'defense': '1000', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '3', 'name': 'Fire Guardian', 'text': 'The gatekeeper guarding the path to the Fire Dragon Kingdom. Those who cannot withstand its blazing breath are not qualified to go any further.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '6', 'attack': '2100', 'defense': '400', 'frontier': '[normal]'}, 
        {'id': '4', 'name': 'Dragon Knight of Darkness', 'text': 'A dragon knight who leads the dark army. His merciless strikes are without equal. The evil sword he wields consumes the souls of his enemies, continuing to grow.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '5', 'attack': '1600', 'defense': '1100', 'frontier': '[normal]'}, 
        {'id': '5', 'name': 'Dragolite', 'text': 'It came from an underground mineral vein. It keeps fighting using the energy of an unknown ore as a power source. Its super hard hitting blows are simply outstanding!', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '4', 'attack': '1500', 'defense': '0', 'frontier': '[normal]'}, 
        {'id': '6', 'name': 'Twin-Edge Dragon', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: This card can make a second attack this turn.', 'attribute': 'LIGHT', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '0', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '7', 'name': "Dragon's Priestess", 'text': "A young priestess from the bloodline of an ancient dragon. She offers her prayers daily for the peace of her tribe. It's said that her clear eyes can change the future of those they lay upon.", 'attribute': 'WATER', 'type': 'Dragon', 'level': '3', 'attack': '1100', 'defense': '100', 'frontier': '[normal]'}, 
        {'id': '8', 'name': 'Dragon Bat', 'text': "A mysterious organism, researchers are still split over whether it's a bird or a beast. A flock of these flying together appears sort of draconian, so maybe it's a dragon.", 'attribute': 'DARK', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '400', 'frontier': '[normal]'}, 
        {'id': '9', 'name': 'Phoenix Dragon', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: Add 1 monster (Level 5 or higher Dragon) from your GY to your hand.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '2', 'attack': '500', 'defense': '500', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '10', 'name': 'Palm-Sized Drago', 'text': "A tiny dragon that loves peace. It's very used to people and will come close if you toss it some nuts. Apparently the ring hanging on its neck has some amazing secret.", 'attribute': 'WIND', 'type': 'Dragon', 'level': '1', 'attack': '0', 'defense': '1400', 'frontier': '[normal]'}, 
        {'id': '11', 'name': 'Dragonic Pressure', 'text': 'none', 'cardType': 'SPELL', 'icon': 'normal', 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'}, 
        {'id': '12', 'name': "Fire Dragon's Heatflash", 'text': 'none', 'cardType': 'SPELL', 'icon': 'normal', 'effect': '[Requirement]: If you control a face-up monster (Dragon).\n[Effect]: Destroy 1 Spell/Trap your opponent controls.'}
    ], # 1 = "deck"
    [], # 2 = "extraDeck"
    [], # 3 = "hand"
    [], # 4 = "gy"
    [], # 5 = "excavated"
    {}, # 6 = "fieldSpellCardZone"
    {}, # 7 = "leftMonsterCardZone"
    {}, # 8 = "centerMonsterCardZone"
    {}, # 9 = "rightMonsterCardZone"
    {}, # 10 = "leftSTCardZone"
    {}, # 11 = "centerSTCardZone"
    {} # 12 = "rightSTCardZone"
]    
player2 = [ 
    8000, # "lp"
    [{'id': '1', 'name': 'Rush Dragon Dragears', 'text': '[Requirement]: You can send the top card of your Deck to the GY.\n[Effect]: This turn, this card can make a second attack during the Battle Phase it destroyed a monster by battle.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '7', 'attack': '2500', 'defense': '1500', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '2', 'name': 'Gravity Press Dragon', 'text': '[Requirement] You can send 1 card from your hand to the GY.\n[Effect] Choose 1 face-up monster your opponent controls. It loses 700 ATK/DEF until the end of this turn.', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '6', 'attack': '1500', 'defense': '1000', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '3', 'name': 'Fire Guardian', 'text': 'The gatekeeper guarding the path to the Fire Dragon Kingdom. Those who cannot withstand its blazing breath are not qualified to go any further.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '6', 'attack': '2100', 'defense': '400', 'frontier': '[normal]'}, 
        {'id': '4', 'name': 'Dragon Knight of Darkness', 'text': 'A dragon knight who leads the dark army. His merciless strikes are without equal. The evil sword he wields consumes the souls of his enemies, continuing to grow.', 'attribute': 'DARK', 'type': 'Dragon', 'level': '5', 'attack': '1600', 'defense': '1100', 'frontier': '[normal]'}, 
        {'id': '5', 'name': 'Dragolite', 'text': 'It came from an underground mineral vein. It keeps fighting using the energy of an unknown ore as a power source. Its super hard hitting blows are simply outstanding!', 'attribute': 'EARTH', 'type': 'Dragon', 'level': '4', 'attack': '1500', 'defense': '0', 'frontier': '[normal]'}, 
        {'id': '6', 'name': 'Twin-Edge Dragon', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: This card can make a second attack this turn.', 'attribute': 'LIGHT', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '0', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '7', 'name': "Dragon's Priestess", 'text': "A young priestess from the bloodline of an ancient dragon. She offers her prayers daily for the peace of her tribe. It's said that her clear eyes can change the future of those they lay upon.", 'attribute': 'WATER', 'type': 'Dragon', 'level': '3', 'attack': '1100', 'defense': '100', 'frontier': '[normal]'}, 
        {'id': '8', 'name': 'Dragon Bat', 'text': "A mysterious organism, researchers are still split over whether it's a bird or a beast. A flock of these flying together appears sort of draconian, so maybe it's a dragon.", 'attribute': 'DARK', 'type': 'Dragon', 'level': '3', 'attack': '1000', 'defense': '400', 'frontier': '[normal]'}, 
        {'id': '9', 'name': 'Phoenix Dragon', 'text': '[Requirement]: You can send 1 card from your hand to the GY.\n[Effect]: Add 1 monster (Level 5 or higher Dragon) from your GY to your hand.', 'attribute': 'FIRE', 'type': 'Dragon', 'level': '2', 'attack': '500', 'defense': '500', 'frontier': '[effect]', 'effect': 'none'}, 
        {'id': '10', 'name': 'Palm-Sized Drago', 'text': "A tiny dragon that loves peace. It's very used to people and will come close if you toss it some nuts. Apparently the ring hanging on its neck has some amazing secret.", 'attribute': 'WIND', 'type': 'Dragon', 'level': '1', 'attack': '0', 'defense': '1400', 'frontier': '[normal]'}, 
        {'id': '11', 'name': 'Dragonic Pressure', 'text': 'none', 'cardType': 'SPELL', 'icon': 'normal', 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'}, 
        {'id': '12', 'name': "Fire Dragon's Heatflash", 'text': 'none', 'cardType': 'SPELL', 'icon': 'normal', 'effect': '[Requirement]: If you control a face-up monster (Dragon).\n[Effect]: Destroy 1 Spell/Trap your opponent controls.'}], # "deck"
    [], # "extraDeck"
    [], # "hand"
    [], # "gy"
    [], # "excavated"
    {}, # "fieldSpellCardZone"
    {}, # "leftMonsterCardZone"
    {}, # "centerMonsterCardZone"
    {}, # "rightMonsterCardZone"
    {}, # "leftSTCardZone"
    {}, # "centerleftSTCardZone"
    {} # "rightleftSTCardZone"
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
    # s/t
    for i in player2[-1:-4:-1]:
        print(i,end="   ")
    print("\n")
    # monstruos
    for i in player2[-4:-7:-1]:
        print(i,end="   ")
    print("\n\nTu campo:")
    # monstruos
    for i in player1[7:10]:
        # if type(i) == dict:
        #     print(i['name'], end="   ")
        if len(i) > 0:
            print(i['name'], end="   ")
        else:
            print(i, end="   ")
    print("\n")
    # s/t
    for i in player1[10:13]:
        print(i,end="   ")
    # Tu campo:
    print("\n")
    print(f"Tus Lp: {player1[0]}")
    print(f"Tu deck: {len(player1[1])}")
    # imprimiendo la mano:
    print(f"Tu mano: {len(player1[3])}")
    for i,a in enumerate(player1[3]):
        if 'level' in player1[3][i]:
            print(f"{i}: {player1[3][i]['name'], player1[3][i]['level']}")
        else:
            print(f"{i}: {player1[3][i]['name'], player1[3][i]['cardType'], player1[3][i]['icon']}")


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