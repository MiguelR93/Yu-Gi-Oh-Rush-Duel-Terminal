import random, copy, time, os
import script.turn as turn
import script.openDeck as openDeck
import script.monster as monster
import script.spellTrap as spellTrap
import script.player as player


# contiene los elementos del juego: jugadores, turnos, contador de LP y condiciones de victoria
TURNSCOUNTER = 0
players = {}


# Duel tools ----------------
def littleSleep(): time.sleep(1)


def victory():
    if players['p1'].victoryStatus == False:
        return False
    elif players['p2'].victoryStatus == False:
        return False
    else:
        return True


def turnStarts():
    global TURNSCOUNTER
    TURNSCOUNTER += 1


def currentlyTurn():
    return TURNSCOUNTER


def ocupiedMonsterZones(playerTurn): # convertir en anónima
    COUNTER = 0
    for i in playerTurn.playerMonsterZones:
        # if len(i) > 0:
        if type(i) == 'script.monsterNormal.MonsterNormal':
            COUNTER += 1
    return COUNTER


def duelStatus(playerTurn): # imprime el estado del duelo: LP, deck, mano, campo, cementerio de ambos jugadores
    os.system("clear")
    print(f"Turn: {TURNSCOUNTER}")
    print(f"Turno de: {playerTurn.name}\n\n")
    # print(f"Zonas de Monstruo ocupadas: {ocupiedMonsterZones(playerTurn)}") # esta cambia en función del jugador en turno
    print(f"Rival LP: {max(players['p2'].lp,0)}")
    print(f"Deck rival: {len(players['p2'].deck)}") # deck
    print(f"Cartas en mano rival: {len(players['p2'].hand)}") # mano
    
    # ----v OPONENT'S HAND
    for i,a in enumerate(players['p2'].hand):
        if players['p2'].hand[i].cardType == 'MONSTER':
            print(f"{i}: {players['p2'].hand[i].name}| Nvl: {players['p2'].hand[i].level} ATK/{players['p2'].hand[i].attack} DEF/{players['p2'].hand[i].defense}")
        else:
            print(f"{i}: {players['p2'].hand[i].name} | {players['p2'].hand[i].cardType} | {players['p2'].hand[i].icon}")
    # ----^ OPONENT'S HAND

    print(f"Cartas en GY rival: {len(players['p2'].gy)}")
    print("\nCampo oponente:")
    # s/t
    for i in players['p2'].playerSTZones:
        if isinstance(i, spellTrap.SpellTrap):
            print(f"{i.name} | {i.cardType} | Posición: {i.position} | Colocada este turno: {i.placedThisTurn}",sep="//", end="   ")
        else:
            print(i,end="   ")
    print("\n")
    # monstruos
    for i in players['p2'].playerMonsterZones:
        if isinstance(i, monster.Monster):
            print(f"{i.name} | Posición: {i.position}| Nivel: {i.level} ATK/{i.attack} DEF/{i.defense} | Invocado Este turno: {i.summonedThisTurn} | Ataques: {i.canAttackThisTurn} | Posición: {i.position}| Tipo de Invocación: {i.summonKind}",sep="//", end="   ")
        else:
            print(i, end="   ")
    print("\n\nTu campo:")
    # monstruos
    for i in players['p1'].playerMonsterZones:
        # if type(i) == dict:
        #     print(i.name, end="   ")
        # print(type(i))
        # if len(i) > 0:
        if isinstance(i, monster.Monster):
        # if (type(i) == 'script.monsterNormal.MonsterNormal') or (type(i) == 'script.monsterEffect as monsterEffect'):
        # if isinstance(i, monster): # mejorar para sustituir al de arriba
            # print(f"{i.name} | Posición: {i.position}| Nivel: {i.level} ATK/{i.attack} DEF/{i.defense} | puede cambiar de posición: {i['can change its position?']} | Veces que puede atacar: {i['attacksCounter']}",sep="//", end="   ")
            print(f"{i.name} | Posición: {i.position}| Nivel: {i.level} ATK/{i.attack} DEF/{i.defense} | Invocado Este turno: {i.summonedThisTurn} | Ataques: {i.canAttackThisTurn} | Posición: {i.position}| Tipo de Invocación: {i.summonKind}",sep="//", end="   ")
            # print('bien :)')
        else:
            print(i, end="   ")
            # print('mal :C')
    print("\n")
    # s/t
    for i in players['p1'].playerSTZones:
        if isinstance(i, spellTrap.SpellTrap):
            print(f"{i.name} | {i.cardType} | Posición: {i.position} | Colocada este turno: {i.placedThisTurn}",sep="//", end="   ")
        else:
            print(i,end="   ")
    # Tu campo:
    print("\n")
    print(f"Tus Lp: {players['p1'].lp}")
    print(f"Tu deck: {len(players['p1'].deck)}")
    print(f"Tu GY: {len(players['p1'].gy)}")
    # imprimiendo la mano:
    print(f"Tu mano: {len(players['p1'].hand)}")
    for i,a in enumerate(players['p1'].hand):
        # if 'level' in players['p1'].hand[i]:
        if players['p1'].hand[i].cardType == 'MONSTER':
            print(f"{i}: {players['p1'].hand[i].name}| Nvl: {players['p1'].hand[i].level} ATK/{players['p1'].hand[i].attack} DEF/{players['p1'].hand[i].defense}")
        else:
            print(f"{i}: {players['p1'].hand[i].name} | {players['p1'].hand[i].cardType} | {players['p1'].hand[i].icon}")
    # print(f"Esto es aparte: \n LMZ: {players['p1'].leftMonsterCardZone}\n CMZ: {players['p1'].centerMonsterCardZone}\n RMZ: {players['p1'].rightMonsterCardZone}\n AMZ: {players['p1'].playerMonsterZones}")




def printHandAndDeckCards():
    for i in players:
        print(f"\n\n\n{i}'s mano: {players[i].hand}\n\n\n")
        print(f"\n\n\n{i}'s Deck: {players[i].deck}", end="\n\n\n")
    


    

    


# Game start! ----------------
def gameStart():
    # inicializando jugadores:
    mito = player.Player(openDeck.openDeck(), 'Jugador')
    com = player.Player(openDeck.openDeck(), 'COM')
    mito.oponent = com
    players['p1'] = mito
    players['p2'] = com


    # Game start ------
    # shuffle both players' deck
    players['p1'].shuffleDeck()
    players['p2'].shuffleDeck()

    # Each player draw until have 4 cards in hand
    for i in players:
        # print(players[i].deck, end="\n\n\n")
        while len(players[i].hand) < 4:
            players[i].hand.append(players[i].deck[0])
            players[i].deck.remove(players[i].deck[0])
        # # print both deck status
        # printHandAndDeckCards()

    # game loop
    while victory():
        for i in players:
            # littleSleep()
            # print(f"{i}'s turn")
            # duelStatus(playerTurn)
            turn.turn(players[i])
            if victory() == False:
                break
    
    if players['p1'].victoryStatus == False:
        print("Perdiste!")
    elif players['p2'].victoryStatus == False:
        print("Ganaste!")
    # else:
    #     return True


# zona de prueba ------
def run():
    gameStart()


if __name__ == '__main__':
    run()


# # CÓDIGO VIEJO ---------------------------------------------------------------------------------

# # # Variables del juego
# # ## Condiciones de victoria
# # thereIsNoWinner = True
# # # lifePoint0 = not thereIsNoWinner
# # # deckEmpty = not thereIsNoWinner
# # youWin = "YOU WIN!!!"
# # youLose = "Y O U  L O S E"









# # def activatingAnEff():
# #     # si el oponente activa un efecto, resolverlo, sino, activa y resuelve uno tú
# #     pass






# # def checkLP():
# #     if players['p1'].lp <= 0:
# #         print(youLose)
# #         return lifePoint0
# #     elif players['p2'].lp <=0:
# #         print(youWin)
# #         return lifePoint0





# # mainPhaseOptions = [
# # '\nQué quieres hacer?', 
# # '1: Invocar un monstruo', 
# # '2: Colocar un monstruo', 
# # '3: Activar una Magia de tu mano', 
# # '4: Activar una Magia del campo', 
# # '5: Colocar una Trampa o Magia de tu mano', 
# # '6: Activar una trampa del campo', 
# # '7: Cambiar la posición de ataque a defensa', 
# # '8: Cambiar la posición de defensa boca-abajo a ataque', 
# # '9: Cambiar la posición de defensa boca-arriba a ataque', 
# # '10: Ir a la Battle Phase', 
# # '11: Ir a la End Phase'
# # ]

# # gameStart():
# #     while thereIsNoWinner == True:
# #             global TURNSCOUNTER
# #             TURNSCOUNTER += 1
# #             gameStart()
# #             checkLP()
            
# #             duelStatus(playerTurn)
# #             # Draw Phase
# #             drawPhase()
            
# #             # Main Phase
# #             mainPhase()
            
# #             # Battle Phase: Empieza la batalla!
# #             # battlePhase()

# #             # End Phase
# #             endPhase()
        
# #         print("Fin del juego :)")