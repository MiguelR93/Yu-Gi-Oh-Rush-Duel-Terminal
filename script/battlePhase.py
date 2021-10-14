def battlePhase():
    activatingAnEff()
    for i,a in enumerate(player1[7:10]):
        print(f"{i}: {a}", sep="\\")
    chosed = int(input("\nElige un monstruo para atacar:\n"))