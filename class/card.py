class Card:
    id = int
    name = str
    cardType = str
    text = str

    def __init__(self, id, name, cardType, text):
        self.id = id
        self.name = name
        self.cardType = cardType
        self.text = text