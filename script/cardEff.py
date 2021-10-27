



class DragonicPressure():
    # TEXT: 'effect': '[Requirement]: Send 3 monsters (Dragon) from your hand to the GY.\n[Effect]: Destroy all monsters on the field. If a monster is destroyed by this effect, you can Special Summon 1 monster (Level 4 or lower Dragon) from your GY to your field in face-up Defense Position.'

    # 1. CONDICIÓN: A) Debe evaluar si hay monstruos en el campo; B) Debe evaluar si el jugador tiene al menos 3 dragones en mano; RESULTADO: Debe destruir los monstruos del campo (si es que hay alguno) y contar si destruyó alguno
    # 2 CONDICIÓN: A) haber destruido al menos un monstruo con este efecto; B) ver si hay algún monstruo de nvl <= 4 en GY del jugador; RESULTADO: el jugador elige un monstruo nvl <= 4 de su GY y lo invoca en posición de defensa boca arriba

    def __init__(self):
        self.mIF = int(input("Monstruos en Campo: "))
        self.dIH = int(input("Monstruos en Mano: "))
        self.mD = int(input("Monstruos destruidos: "))
        self.mIGY = int(input("Monstruos nvl <=4 en GY: "))



    def effect(self, mIF, dIH, mD, mIGY):
        self._counterMonsterInField(mIF)
        self._counterDragonInHand(dIH)
        if (self._counterMonsterInField(mIF) > 0) and (self._counterDragonInHand(dIH) >= 3):
            self._sendDragonInHandToGY()
            self._destroyAllMonsterInField()
            self._counterMonsterDestroyed(mD)
        if (self._counterMonsterDestroyed(mD) > 0) and (self._counterMonsterDragonNvlFourOrLessInGY(mIGY) >= 1):
            self._specialSummonDragonNvlFourOrLessFromGYInDFU()


    def _counterDragonInHand(self, dIH):
        print('Contando a los dragones en mano')
        print(dIH)
        return dIH

    def _counterMonsterInField(self, mIF):
        print('Contando a los monstruos en campo')
        print(mIF)
        return mIF

    def _sendDragonInHandToGY(self):
        print('Enviando monstruos de mano a GY')

    def _destroyAllMonsterInField(self):
        print('Destruyendo a los monstruos en campo')

    def _counterMonsterDestroyed(self, mD):
        print('Contando a los monstruos destruidos por este efecto')
        print(mD)
        return mD

    def _counterMonsterDragonNvlFourOrLessInGY(self, mIGY):
        print('Contando monstruos de nvl <= 4 en GY')
        print(mIGY)
        return mIGY

    def _specialSummonDragonNvlFourOrLessFromGYInDFU(self):
        print('Invocando desde el GY')


if __name__ == '__main__':
    eff = DragonicPressure()
    eff.effect()