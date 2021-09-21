import card, cardEffect


class SpellTrap(card.Card):
    cardType = str
    icon = str
    effect = cardEffect.CardEffect("")

    def __init__(self, id, name, cardType, icon, effect, text):
        super().__init__(id, name, text)
        self.cardType = cardType
        self.icon = icon
        self.effect = effect