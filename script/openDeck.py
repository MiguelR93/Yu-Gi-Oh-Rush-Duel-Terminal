import monsterNormal, monsterEffect, spellTrap, csv

exampleFile = open('lukeDeck.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
deckOrigin = list(exampleData[1:])
deckResult = []

if __name__ == '__main__':
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

        if "effect" in i[8]:
            newObject = monsterEffect.MonsterEffect(
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
            newObject = spellTrap.SpellTrap(
                i[0],
                i[1],
                i[2],
                i[3],
                i[4],
                i[5]
            )
            deckResult.append(newObject)

    
    print(deckResult)
    for i in deckResult:
        print(vars(i), end=',\n')