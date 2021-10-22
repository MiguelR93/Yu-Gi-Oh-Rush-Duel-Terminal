import random, copy, time
import script.duel as duel
import script.summon as summon
import script.placeST as placeST
import script.battlePhase as battlePhase
import script.mainPhase as mainPhase


def changingValuesInMonsters(playerTurn):
    for i in playerTurn[7:10]: 
        if (len(i) > 0) and ('MONSTER' in i['cardType']):
            i['summoned this turn?'], i['can change its position?'] = 'no', 'yes'
            while i['attacksCounter'] < 1:
                i['attacksCounter'] += 1


def endPhase(playerTurn):
    changingValuesInMonsters(playerTurn)