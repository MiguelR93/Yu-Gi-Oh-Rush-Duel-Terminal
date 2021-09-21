import monster, cardEffect


class MonsterEffect(monster.Monster):
    effect = cardEffect.CardEffect("")

    def __init__(self, id, name, attribute, type, level, attack, defense, frontier, text, effect):
        super().__init__(id, name, attribute, type, level, attack, defense, frontier, text)
        self.effect = effect
