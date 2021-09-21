import monster


class MonsterNormal(monster.Monster):

    def __init__(self, id, name, attribute, type, level, attack, defense, frontier, text):
        super().__init__(id, name, attribute, type, level, attack, defense, frontier, text)