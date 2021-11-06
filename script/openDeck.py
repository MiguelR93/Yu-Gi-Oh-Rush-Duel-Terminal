import csv
import script.card as card

def openDeck():
    try:
        exampleFile = open('deck/lukeDeck.csv')
    except FileNotFoundError:
        exampleFile = open('../deck/lukeDeck.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    deckOrigin = list(exampleData[1:])
    deckResult = []

    for i in deckOrigin:
        if "normal" in i[8]:
            newObject = card.MonsterNormal(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
                i[8],
                i[9]
            )
            deckResult.append(newObject)

        if "effect" in i[8]:
            newObject = card.MonsterEffect(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5],
                i[6],
                i[7],
                i[8],
                i[9],
                i[10]
            )
            deckResult.append(newObject)
        if ("SPELL" in i[2]) or ("TRAP" in i[2]):
            newObject = card.SpellTrap(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5]
            )
            deckResult.append(newObject)

    
    # print(deckResult)
    # for i in deckResult:
    #     print(vars(i), end=',\n')
        # print(i, end=',\n')

    return deckResult


if __name__ == '__main__':
    openDeck()