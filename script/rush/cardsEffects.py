import script.card as card
import script.listCardEff as listCardEff

class DragonicPressure(card.SpellTrap):

    def __init__(self, id, name, cardType, icon, effect, text):
        super().__init__(id, name, cardType, icon, effect, text)

    def cardEffect(self, playerTurn):
    # TEXT: 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'

    # 1. CONDICIÓN: A) Debe evaluar si hay monstruos en el campo; B) Debe evaluar si el jugador tiene al menos 3 dragones en mano; RESULTADO: Debe destruir los monstruos del campo (si es que hay alguno) y contar si destruyó alguno
    # 2 CONDICIÓN: A) haber destruido al menos un monstruo con este efecto; B) ver si hay algún monstruo de nvl <= 4 en GY del jugador; RESULTADO: el jugador elige un monstruo nvl <= 4 de su GY y lo invoca en posición de defensa boca arriba

        listCardEff.counterMonsterInField(playerTurn)
        listCardEff.counterDragonInHand(playerTurn)
        if (listCardEff.counterMonsterInField(playerTurn) > 0) and (listCardEff.counterDragonInHand(playerTurn) >= 3):
            listCardEff.sendDragonInHandToGY(playerTurn)
            # destroyAllMonsterInField()
            listCardEff.sendDragonInHandToGY(playerTurn)
        if (listCardEff.sendDragonInHandToGY(playerTurn) > 0) and (listCardEff.counterMonsterDragonNvlFourOrLessInGY(playerTurn) >= 1):
            listCardEff.specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn)