import script.card as card

# import card


class Monster(card.Card):
    
    def __init__(self, id, name, cardType, attribute, type, level, attack, defense, frontier, text):
        super().__init__(id, name, cardType, text)
        self.attribute = attribute
        self.type = type
        self.level = int(level)
        self.attack = attack
        self.defense = defense
        self.frontier = frontier
        
        # # nuevos atributos: -------
        # self._normalSummonAble = True
        # self._setAble = True
        # self._specialSummonAble = True
        self.position = None # [attack, defense face-down, defense face-up]
        self.summonKind = None # [normalSummon, set, tributeSummon, specialSummon]
        self.summonedThisTurn = True
        self.canAttackThisTurn = 1


    # def normalSummon(self):
    #     pass
    #     if self.level <= 4:
    #         print("Felicidades, invocaste un monstruo de nvl 4 o menor!")
    #     elif self.level > 4 and self.level < 7:
    #         print("Felicidades, invocaste un monstruo de nvl 5 o 6!")
    #     else:
    #         print("Felicidades, invocaste un monstruo de nvl 7 o mayor!")

    
    # def declareAttack(self):
    #     pass
    
    # def changePosition(self):
    #     pass