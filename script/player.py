import script.duel as duel
import script.monster as monster
import script.spellTrap as spellTrap


class Player():
    def __init__(self, deck, extraDeck, hand, gy, excavated, fieldSpellCardZone, leftMonsterCardZone, centerMonsterCardZone, rightMonsterCardZone, leftSTCardZone, centerSTCardZone, rightSTCardZone, name, oponent):
        self.lp = 8000 # 00
        self.deck = deck # 01
        self.extraDeck = extraDeck # 02
        self.hand = hand # 03
        self.gy = gy # 04
        self.excavated = excavated # 05
        self.fieldSpellCardZone = fieldSpellCardZone # 06
        # self.leftMonsterCardZone = leftMonsterCardZone # 07
        # self.centerMonsterCardZone = centerMonsterCardZone # 08
        # self.rightMonsterCardZone = rightMonsterCardZone # 09
        self.playerMonsterZones = [
            leftMonsterCardZone, # 07
            centerMonsterCardZone, # 08
            rightMonsterCardZone, # 09
            ]
        # self.leftSTCardZone = leftSTCardZone # 10
        # self.centerSTCardZone = centerSTCardZone # 11
        # self.rightSTCardZone = rightSTCardZone # 12
        self.playerSTZones = [
            leftSTCardZone,  # 10
            centerSTCardZone,  # 11
            rightSTCardZone # 12
            ]
        self.name = name # 13
        self.victoryStatus = True # 14
        self.oponent = oponent # 15

    ### DRAW PHASE ---------------------------
    def drawPhase(self):
        if self.cardsInHand() >= 5:
            self.drawACard()
        else:
            while (len(self.hand) < 5) and (duel.victory() == True):
                self.drawACard()


    def cardsInHand(self):
        return len(self.hand)


    def drawACard(self):
        if len(self.deck) == 0:
            print("No hay cartas en el deck")
            self.victoryStatus = False
        else:
            self.hand.append(self.deck[0]) # añade la carta del deck a la mano
            self.deck.remove(self.deck[0]) # quita del deck la carta añadida a la mano
          
    ### MAIN PHASE ---------------------------
    ### Monsters
    def normalSummon(self, position):
        if self.counterCardTypeInHand('MONSTER') < 1:
            print('No hay monstruos para invocar')
            duel.littleSleep()
        else:
            # print('A invocar!')
            for a,i in enumerate(self.hand):
                if 'MONSTER' in i.cardType:
                    print(f"{a}: {i.name}")                    
            try:
                summonAMonster = int(input("ingresa el índice del monstruo (el número a su izquierda): "))
                if 'MONSTER' not in self.hand[summonAMonster].cardType: # Cuando lo que se elige no es un monstruo
                    print('Eso no es un monstruo')
                elif int(self.hand[summonAMonster].level) <= 4: # Cuando lo que se elige es un monstruo nvl<=4
                    # print(f"\nNivel del monstruo: {self.hand[summonAMonster].level}\n")
                    self.summonLoop('normalSummon',  position, summonAMonster)
                elif (self.hand[summonAMonster].level == 5) or (self.hand[summonAMonster].level == 6):
                    if self.counterMonsterInMyField() < 1:
                        print("No cuentas con monstruos suficientes")
                        duel.littleSleep()
                    else:
                        self.sacrifice1('tributeSummon', position, summonAMonster)                
                elif self.hand[summonAMonster].level >= 7:
                    if self.counterMonsterInMyField() < 2:
                        print("No cuentas con monstruos suficientes")
                        duel.littleSleep()
                    else:
                        self.sacrifice2('tributeSummon', position, summonAMonster)
            except IndexError:
                print('Valor equivocado')
            except ValueError:
                print('Debes ingresar un número')
            duel.littleSleep()


    def counterCardTypeInHand(self, chosenCardType):
        COUNTER = 0
        for i in self.hand:
            if chosenCardType in i.cardType:
                COUNTER += 1
        return COUNTER
    

    def counterSTInMyField(self):
        COUNTER = 0
        for i in self.playerSTZones:
            if type(i) != list:
                COUNTER += 1
        return COUNTER
    

    def counterMonsterInMyField(self):
        COUNTER = 0
        for i in self.playerMonsterZones:
            if type(i) != list:
                COUNTER += 1
        return COUNTER


    def sacrifice1(self, summonKind, position, summonAMonster):
        print("Monstruos en campo\n")
        for a,i in enumerate(self.playerMonsterZones):
            if type(i) != list:
                print(f"{a}: {i.name}")
        try:
            chosen = int(input("Elige el monstruos a sacrificar:"))
            self.gy.append(self.playerMonsterZones[chosen]) # envía al gy
            self.playerMonsterZones[chosen] = [] # quita del campo al monstruo sacrificado
            self.summonLoop('tribute Summon', position, summonAMonster)
        except IndexError:
            print('Valor equivocado')
            # input()
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            duel.littleSleep()


    def sacrifice2(self, summonKind, position, summonAMonster):    
        while True:
            duel.littleSleep()
            print("\nMonstruos en campo:")
            tributeAble = []
            for i,a in enumerate(self.playerMonsterZones):
                if type(a) != list:
                    print(f"{i}: {a.name}")
                    tributeAble.append(i)
            choosed = []
            tributed = int(input("Elige el primer monstruo a sacrificar: "))
            if tributed not in tributeAble:
                print("No es un valor válido")
                duel.littleSleep()
                continue
            choosed.append(tributed)
            try:
                print("Elige el segundo monstruo a sacrificar o vuelve a elegir al primero para cambiarlo: ")
                tributed2 = int(input())
                if tributed2 == choosed[0]:
                    continue
                elif tributed2 not in tributeAble:
                    print("No es un valor válido")
                    duel.littleSleep()
                elif tributed2 != choosed[0]:
                    tributeAble.append(tributed2)
                    break
                    duel.littleSleep()
            except IndexError:
                print('Valor equivocado')
                continue
                duel.littleSleep()
            except ValueError:
                print('Debes ingresar un número')
                continue
                duel.littleSleep()
        self.gy.append(self.playerMonsterZones[tributed])
        self.playerMonsterZones[tributed] = []
        self.gy.append(self.playerMonsterZones[tributed2])
        self.playerMonsterZones[tributed2] = []
        self.summonLoop('tribute Summon', position, summonAMonster)    


    def summonLoop(self, summonKind, position, summonAMonster):
        if self.counterMonsterInMyField() > 2:
            print("No hay zonas disponibles")
            duel.littleSleep()
        else:
            while True:
                try:
                    monstersZones = ["0: zona Izquierda", "1: zona central", "2: zona derecha"]
                    print('\nEn dónde quieres ponerlo?')
                    for a,i in enumerate(self.playerMonsterZones):
                        # enumera la zonas del campo del jugador, si la zona NO está ocupada será de tipo lista y se mostrará
                        if type(i) == list:
                            print(monstersZones[a])                    
                    monsterZonePosition = int(input("\nEscribe el número a la izquierda: "))
                    
                    if type(self.playerMonsterZones[monsterZonePosition]) != list:
                        ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                        if ocupado == 1:
                            continue
                        elif ocupado == 2:
                            break
                    elif type(self.playerMonsterZones[monsterZonePosition]) == list:
                        self.playerMonsterZones[monsterZonePosition] = self.hand[summonAMonster] # pone el monstruo de la mano en el campo
                        self.hand.remove(self.hand[summonAMonster]) # quita de la mano al monstruo invocado
                        self.playerMonsterZones[monsterZonePosition].position = position
                        self.playerMonsterZones[monsterZonePosition].summonKind = summonKind
                        break
                    else:
                        print("No es una zona de monstruo")
                        duel.littleSleep()
                        continue
                except IndexError:
                    print('Valor equivocado')
                    duel.littleSleep()
                    continue
                except ValueError:
                    print('Debes ingresar un número')
                    duel.littleSleep()
                    continue


    ### ST
    def placeSpellTrap(self, position):
        try:
            placeST = int(input("ingresa el índice de la magia/trampa (el número a su izquierda): "))
            if 'MONSTER' in self.hand[placeST].cardType: # Cuando lo que se elige es un monstruo y no debería serlo
                print('Eso no es una magia/trampa')
                duel.littleSleep()
            elif ('TRAP' in self.hand[placeST].cardType) and (position == 'active'):
                print("No puedes activar una trampa desde tu mano")
                duel.littleSleep()
            else:
                self.placeSTLoop(position, placeST)
        except IndexError:
            print('Valor equivocado')
            # input()
            duel.littleSleep()
        except ValueError:
            print('Debes ingresar un número')
            duel.littleSleep()


    def placeSTLoop(self, position, placeST):
        # sTZoneCounter = 0
        # for i in self.playerSTZones:
        #     if isinstance(i, spellTrap.SpellTrap):
        #         sTZoneCounter += 1
        # if sTZoneCounter > 2:
        #     print("No hay zonas disponibles")
        #     duel.littleSleep()
        if self.counterSTInMyField() > 2:
            print("No hay zonas disponibles")
            duel.littleSleep()


        else:
            while True:
                # duel.duelStatus(playerTurn)
                try:
                    sTZones = ["0: zona Izquierda", "1: zona central", "2: zona derecha"]
                    print('\nEn dónde quieres ponerlo?')
                    for a,i in enumerate(self.playerSTZones):
                        if type(i) == list:
                            print(sTZones[a])
                    sTZonePosition = int(input("\nEscribe el número a la izquierda: "))
                    if type(self.playerSTZones[sTZonePosition]) != list:
                        # print("Zona ocupada, elige otra")
                        # duel.littleSleep()
                        # continue
                        # else:
                        ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                        if ocupado == 1:
                            continue
                        elif ocupado == 2:
                            break
                    elif (sTZonePosition > 3) or (sTZonePosition < 0):
                        print("No es una zona de magia/trampa")
                        duel.littleSleep()
                        continue
                    else:
                        self.hand[placeST].position = position # incluir en la clase
                        # print(self.hand[placeST]) # imprime el estado de la s/t
                        self.playerSTZones[sTZonePosition] = self.hand[placeST] # pone la s/t
                        self.hand.remove(self.hand[placeST]) # quita de la mano a la s/t
                        if position == 'set':
                            self.hand[placeST].placedThisTurn = True # incluir en la clase
                            pass
                        elif position == 'active':
                            print("Activo una Magia!")
                            duel.littleSleep()
                            # activeEff.activeEff(playerTurn, sTZonePosition)
                        break
                except IndexError:
                    print('Valor equivocado')
                    # input()
                    duel.littleSleep()
                    continue
                except ValueError:
                    print('Debes ingresar un número')
                    duel.littleSleep()
                    continue

    ### BATTLE PHASE ---------------------------
    ### END PHASE ---------------------------
    def endPhase(self):
        pass


## Zona de pruebas
if __name__ == '__main__':
    mito = Player([], [], [], [], [], [], [], [], [], [], [], [], 'Jugador', None)
    # print(mito.name)
    # print(mito.oponent)
    # print(mito.lp)
    # print(mito.counterCardTypeInHand())
    # print(mito.hand)
    # mito.normalSummon()
    mito.counterCardTypeInHand()
