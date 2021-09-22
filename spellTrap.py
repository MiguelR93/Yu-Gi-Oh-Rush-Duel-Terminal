import card, cardEffect


class SpellTrap(card.Card):
    icon = str
    effect = cardEffect.CardEffect("")

    def __init__(self, id, name, cardType, icon, effect, text):
        super().__init__(id, name, cardType, text)
        self.icon = icon
        self.effect = effect