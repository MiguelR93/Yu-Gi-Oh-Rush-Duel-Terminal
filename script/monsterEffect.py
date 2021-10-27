import script.monster as monster
import script.cardEffect as cardEffect

# import monster
# import cardEffect

class MonsterEffect(monster.Monster):
    effect = cardEffect.CardEffect("")

    def __init__(self, id, name, cardType, attribute, type, level, attack, defense, frontier, text, effect):
        super().__init__(id, name, cardType, attribute, type, level, attack, defense, frontier, text)
        self.effect = effect
