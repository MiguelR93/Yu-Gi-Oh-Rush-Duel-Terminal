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
    
    def counterMonsterInHand(self):
        return len(self.hand)

    def normalSummon(self):
        if self.counterMonsterInHand() < 1:
            print('No hay monstruos para invocar')
        else:
            print('A invocar!')


## Zona de pruebas
if __name__ == '__main__':
    mito = Player([], [], ['Dragón', 'Mago'], [], [], [], [], [], [], [], [], [], 'Mito', 'Kaiba')
    # print(mito.name)
    # print(mito.oponent)
    # print(mito.lp)
    # print(mito.counterMonsterInHand())
    # print(mito.hand)
    mito.normalSummon()