import script.monsterNormal as monsterNormal
# import script.monsterEffect as monsterEffect
# import script.spellTrap as spellTrap
import csv

# import monsterNormal
# import monsterEffect
# import spellTrap


def openDeck():
    exampleFile = open('../deck/lukeDeck.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    deckOrigin = list(exampleData[1:])
    deckResult = []

    for i in deckOrigin:
        if "normal" in i[8]:
            newObject = monsterNormal.MonsterNormal(
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

        # if "effect" in i[8]:
        #     newObject = monsterEffect.MonsterEffect(
        #         i[0],
        #         i[1],
        #         i[2],
        #         i[3],
        #         i[4],
        #         i[5],
        #         i[6],
        #         i[7],
        #         i[8],
        #         i[9],
        #         i[10]
        #     )
        #     deckResult.append(newObject)
        # if ("SPELL" in i[2]) or ("TRAP" in i[2]):
        #     newObject = spellTrap.SpellTrap(
        #         i[0],
        #         i[1],
        #         i[2],
        #         i[3],
        #         i[4],
        #         i[5]
        #     )
        #     deckResult.append(newObject)

    
    # print(deckResult)
    for i in deckResult:
        print(vars(i), end=',\n')
        # print(i, end=',\n')

    return deckResult


if __name__ == '__main__':
    openDeck()