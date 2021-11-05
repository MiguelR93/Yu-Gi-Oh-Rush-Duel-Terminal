



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
            # self._destroyAllMonsterInField()
            self._counterMonsterDestroyed(mD)
        if (self._counterMonsterDestroyed(mD) > 0) and (self._counterMonsterDragonNvlFourOrLessInGY(mIGY) >= 1):
            self._specialSummonDragonNvlFourOrLessFromGYInDFU()


    def _counterDragonInHand(self, playerTurn):
        print('Contando a los dragones en mano')
        # print(dIH)
        # return dIH

        # 1. Contar los monstruos en la mano del jugador que son tipo dragón
        COUNTER = 0
        for i in playerTurn[3]:
            if (i['cardType'] == 'MONSTER') and (i['type'] == 'Dragon'):
                COUNTER += 1
        return COUNTER

    def _counterMonsterInField(self, playerTurn):
        print('Contando a los monstruos en campo')
        # print(mIF)
        # return mIF
        COUNTER = 0
        for i in playerTurn[15][9:6:-1]:
            if (len(i) > 0) and (i['cardType'] == 'MONSTER'):
                COUNTER += 1
        for i in playerTurn[7:10]:
            if (len(i) > 0) and (i['cardType'] == 'MONSTER'):
                COUNTER += 1
        return COUNTER

    def _sendDragonInHandToGY(self, playerTurn):
        print('Enviando monstruos de mano a GY')
        # Debe permitir elegir monstruos tipo dragón en mano para descartarlos como costo
        for a,i in enumerate(playerTurn[3]):
            if (i['cardType'] == 'MONSTER') and (i['type'] == 'Dragon'):
                print(f"{a}: {i['name']}")
        
        choosed = []
        while len(choosed) < 3:
            try:
                monster = int(input("Escribe el número a la izquierda: "))
                if monster not in choosed:
                    choosed.append(monster)
                elif monster in choosed:
                    choosed.remove(monster)
                else:
                    raise IndexError
            except IndexError:
                print('Valor equivocado')
                continue
                duel.littleSleep()
            except ValueError:
                print('Debes ingresar un número')
                continue
        
        for i in choosed:
            playerTurn[4].append[i]
            playerTurn[3].remove(i)


    # def _destroyAllMonsterInField(self):
    #     print('Destruyendo a los monstruos en campo')



    def _counterMonsterDestroyed(self, mD):
        print('Contando a los monstruos destruidos por este efecto')
        print(mD)
        return mD
        # cada ciclo debe ver si hay un monstruo en la zona de monstruo respectiva, luego debe añadirlo al GY, removerlo del campo, y añadir 1 al contador de monstruos destruidos
        COUNTER = 0
        for i in playerTurn[15][9:6:-1]:
            if (len(i) > 0) and (i['cardType'] == 'MONSTER'):
                playerTurn[15][4].append(i)
                i = []
                COUNTER += 1
        for i in playerTurn[7:10]:
            if (len(i) > 0) and (i['cardType'] == 'MONSTER'):
                playerTurn[4].append(i)
                i = []
                COUNTER += 1
        return COUNTER


    def _counterMonsterDragonNvlFourOrLessInGY(self, mIGY):
        print('Contando monstruos de nvl <= 4 en GY')
        # print(mIGY)
        # return mIGY
        COUNTER = 0
        for i in playerTurn[4]:
            if (i['cardType'] == 'MONSTER') and ((i['type'] == 'Dragon') and (int(i['level']) <= 4):
                COUNTER += 1
        if COUNTER > 0:
            for a,i in enumerate(playerTurn[4])
                if (i['cardType'] == 'MONSTER') and ((i['type'] == 'Dragon') and (int(i['level']) <= 4):
                    print(f"{a}: {i['name']}")
        else:
            print("No hay monstruos para invocar")
        choosedMonster = int(input("Elige: "))

        self._specialSummonDragonNvlFourOrLessFromGYInDFU(playerTurn[4][choosedMonster])        

    def _specialSummonDragonNvlFourOrLessFromGYInDFU(choosedMonster):
        print('Invocando desde el GY')
        # hace una invocación especial en posición de defensa


if __name__ == '__main__':
    eff = DragonicPressure()
    eff.effect()