class Card:
    id = int
    name = str
    text = str

    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.text = text