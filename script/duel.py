import random, os, time
# contiene los elementos del juego: jugadores, turnos, contador de LP y condiciones de victoria

# Variables del juego
## Condiciones de victoria
thereIsNoWinner = True
# lifePoint0 = not thereIsNoWinner
# deckEmpty = not thereIsNoWinner
youWin = "YOU WIN!!!"
youLose = "Y O U  L O S E"
TURNSCOUNTER = 0
def littleSleep(): time.sleep(1)


def shuffleDeck(playersDeck):
    random.shuffle(playersDeck)


def activatingAnEff():
    # si el oponente activa un efecto, resolverlo, sino, activa y resuelve uno tú
    pass


def ocupiedMonsterZones(): # convertir en anónima
    COUNTER = 0
    for i in player1[7:10]:
        if len(i) > 0:
            COUNTER += 1
    return COUNTER


def duelStatus(): # imprime el estado del duelo: LP, deck, mano, campo, cementerio de ambos jugadores
    os.system("clear")
    print(f"Zonas de Monstruo ocupadas: {ocupiedMonsterZones()}")
    print(f"Turn: {TURNSCOUNTER}")
    print(f"Rival LP: {player2[0]}")
    print(f"Deck rival: {len(player2[1])}") # deck
    print(f"Cartas en mano rival: {len(player2[3])}") # mano
    print(f"Cartas en GY rival: {len(player2[4])}")
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
            print(f"{i['name']} | Posición: {i['position']}| Nivel: {i['level']} ATK/{i['attack']} DEF/{i['defense']}",sep="//", end="   ")
        else:
            print(i, end="   ")
    print("\n")
    # s/t
    for i in player1[10:13]:
        if len(i) > 0:
            print(f"{i['name']} | {i['cardType']} | Posición: {i['position']}",sep="//", end="   ")
        else:
            print(i,end="   ")
    # Tu campo:
    print("\n")
    print(f"Tus Lp: {player1[0]}")
    print(f"Tu deck: {len(player1[1])}")
    print(f"Tu GY: {len(player1[4])}")
    # imprimiendo la mano:
    print(f"Tu mano: {len(player1[3])}")
    for i,a in enumerate(player1[3]):
        if 'level' in player1[3][i]:
            print(f"{i}: {player1[3][i]['name']}| Nvl: {player1[3][i]['level']} ATK/{player1[3][i]['attack']} DEF/{player1[3][i]['defense']}")
        else:
            print(f"{i}: {player1[3][i]['name']} | {player1[3][i]['cardType']} | {player1[3][i]['icon']}")


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





mainPhaseOptions = [
'\nQué quieres hacer?', 
'1: Invocar un monstruo', 
'2: Colocar un monstruo', 
'3: Activar una Magia de tu mano', 
'4: Activar una Magia del campo', 
'5: Colocar una Trampa o Magia de tu mano', 
'6: Activar una trampa del campo', 
'7: Cambiar la posición de ataque a defensa', 
'8: Cambiar la posición de defensa boca-abajo a ataque', 
'9: Cambiar la posición de defensa boca-arriba a ataque', 
'10: Ir a la Battle Phase', 
'11: Ir a la End Phase'
]


# NUEVO INICIO!