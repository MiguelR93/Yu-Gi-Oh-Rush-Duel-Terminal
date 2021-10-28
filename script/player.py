import script.duel as duel


class Player():
    def __init__(self, deck, extraDeck, hand, gy, excavated, fieldSpellCardZone, leftMonsterCardZone, centerMonsterCardZone, rightMonsterCardZone, leftSTCardZone, centerSTCardZone, rightSTCardZone, name, oponent):
        self.lp = 8000 # 00
        self.deck = deck # 01
        self.extraDeck = extraDeck # 02
        self.hand = hand # 03
        self.gy = gy # 04
        self.excavated = excavated # 05
        self.fieldSpellCardZone = fieldSpellCardZone # 06
        self.leftMonsterCardZone = leftMonsterCardZone # 07
        self.centerMonsterCardZone = centerMonsterCardZone # 08
        self.rightMonsterCardZone = rightMonsterCardZone # 09
        self.playerMonsterZones = [self.leftMonsterCardZone, self.centerMonsterCardZone, self.rightMonsterCardZone]
        self.leftSTCardZone = leftSTCardZone # 10
        self.centerSTCardZone = centerSTCardZone # 11
        self.rightSTCardZone = rightSTCardZone # 12
        self.playerSTZones = [self.leftSTCardZone, self.centerSTCardZone, self.rightSTCardZone]
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
          

    def normalSummon(self, position):
        if self.counterMonsterInHand() < 1:
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
                self.summonLoop(position, summonAMonster)




            elif int(self.hand[summonAMonster].level) <=6:
                if len(self.playerMonsterZones) < 1:
                    print("No cuentas con monstruos suficientes")
                    duel.littleSleep()
                    # input()
                else:
                    # mostrar los monstruos a sacrificar
                    # print("entramos a sacrificar")
                    # input()

                    pass
                    # sacrifice1(self, summonAMonster, position)
            elif int(self.hand[summonAMonster].level) >= 7:
                if len(self.playerMonsterZones) < 2:
                    print("No cuentas con monstruos suficientes")
                    duel.littleSleep()
                else:
            #         # mostrar los monstruos a sacrificar
            #         # print("entramos a sacrificar")
            #         # input()
                    
                    pass
                    # sacrifice1(self, summonAMonster, position)
        except IndexError:
            print('Valor equivocado')
        except ValueError:
            print('Debes ingresar un número')
        duel.littleSleep()
        # input()


    def counterMonsterInHand(self):
        COUNTER = 0
        for i in self.hand:
            if 'MONSTER' in i.cardType:
                COUNTER += 1

        # if COUNTER > 0:
        #     print(f"Hay {COUNTER} monstruos en mano")
        # else:
        #     print(f"No hay monstruos en mano")
        
        return COUNTER



    def summonLoop(self, position, summonAMonster):
        MONSTER_ZONE_COUNTER = 0
        for i in self.playerMonsterZones:
            if len(i) > 0:
                MONSTER_ZONE_COUNTER += 1
                
        if MONSTER_ZONE_COUNTER > 2:
            print("No hay zonas disponibles")
            duel.littleSleep()
        else:
            while True:
                duel.littleSleep()
                try:
                    monstersZones = ["1: zona Izquierda", "2: zona central", "3: zona derecha"]
                    print('\nEn dónde quieres ponerlo?')
                    for i,a in enumerate(self.playerMonsterZones):
                        if len(a) == 0:
                            print(monstersZones[i])
                    monsterZonePosition = int(input("\nEscribe el número a la izquierda: "))
                    if len(self.playerMonsterZones[monsterZonePosition]) != 0:
                        if summonKind == 'tribute Summon':
                            print("Zona ocupada, elige otra")
                            duel.littleSleep()
                            continue
                        else:
                            ocupado = int(input("Esa zona está ocupada!\nQuieres elegir otra?\n1: sí\n2: no\n"))
                            if ocupado == 1:
                                continue
                            elif ocupado == 2:
                                break
                    elif len(self.playerMonsterZones[monsterZonePosition]) == 0:                        
                        # playerTurn.hand[summonAMonster]['position'], playerTurn.hand[summonAMonster]['summonKind'], playerTurn.hand[summonAMonster]['summoned this turn?'], playerTurn.hand[summonAMonster]['can change its position?'], playerTurn.hand[summonAMonster]['attacksCounter'] = position, summonKind, 'yes', 'no', 1 # incluir esto en la clase monster.py
                        # print(self.hand[summonAMonster]) # imprime el estado del monstruo
                        self.playerMonsterZones[monsterZonePosition] = self.hand[summonAMonster] # pone el monstruo de la mano en el campo
                        self.hand.remove(self.hand[summonAMonster]) # quita de la mano al monstruo invocado
                        break
                    else:
                        print("No es una zona de monstruo")
                        duel.littleSleep()
                        continue
                except IndexError:
                    print('Valor equivocado')
                    # input()
                    duel.littleSleep()
                    continue
                except ValueError:
                    print('Debes ingresar un número')
                    duel.littleSleep()
                    continue



## Zona de pruebas
if __name__ == '__main__':
    mito = Player([], [], [], [], [], [], [], [], [], [], [], [], 'Jugador', None)
    # print(mito.name)
    # print(mito.oponent)
    # print(mito.lp)
    # print(mito.counterMonsterInHand())
    # print(mito.hand)
    # mito.normalSummon()
    mito.counterMonsterInHand()
