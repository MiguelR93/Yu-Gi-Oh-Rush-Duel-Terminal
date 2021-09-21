import card


class Monster(card.Card):
    attribute = str
    type = str
    level = str
    attack = int
    defense = int
    frontier = list
    
    def __init__(self, id, name, attribute, type, level, attack, defense, frontier, text):
        super().__init__(id, name, text)
        self.attribute = attribute
        self.type = type
        self.level = level
        self.attack = attack
        self.defense = defense
        self.frontier = frontier