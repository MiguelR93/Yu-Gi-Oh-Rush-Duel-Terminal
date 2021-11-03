# import random, copy, time
# import script.duel as duel
# import script.summon as summon
# import script.placeST as placeST
# import script.battlePhase as battlePhase
# import script.mainPhase as mainPhase


# def statusReset(playerTurn):
#     # must reset status of cards like attack o change their position
#     for i in playerTurn.playerMonsterZones:
#         if (type(i) != []) and (i.cardType == 'MONSTER'):
#             i.summonedThisTurn = False
#             i.canAttackThisTurn = 1
#             i.canChangeItsPosition = True
    
#     for i in playerTurn.playerSTZones:
#         if (type(i) != []) and ((i.cardType == 'SPELL') or ((i.cardType == 'TRAP'))):
#             i.placedThisTurn = False
#             i.canBeActivatedThisTurn = True



# def endPhase(playerTurn):
#     # this is the last must happen:
#     statusReset(playerTurn)