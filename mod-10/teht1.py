from classes.Hissi import elevator

elevator1 = elevator()
elevator1.siirry_kerrokseen(7)
print(elevator1.sijainti)
elevator1.siirry_kerrokseen(elevator1.alin_kerros)
print(elevator1.sijainti)
