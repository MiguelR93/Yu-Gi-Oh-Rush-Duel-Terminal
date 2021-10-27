import script.card as card

# import card


class Monster(card.Card):
    
    def __init__(self, id, name, cardType, attribute, type, level, attack, defense, frontier, text):
        super().__init__(id, name, cardType, text)
        self.attribute = attribute
        self.type = type
        self.level = level
        self.attack = attack
        self.defense = defense
        self.frontier = frontier

    def normalSummon():
        pass