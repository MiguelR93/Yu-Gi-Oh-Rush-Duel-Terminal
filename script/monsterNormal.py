import script.monster as monster

# import monster


class MonsterNormal(monster.Monster):

    def __init__(self, id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text):
        super().__init__(id, name, cardType, attribute, typeMonster, level, attack, defense, frontier, text)