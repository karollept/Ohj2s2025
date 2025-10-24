import random

class elevator:
    def __init__(self, sijainti = 1, alin_kerros = 1, ylin_kerros = 9):
        self.sijainti = sijainti
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylös(self):
        if self.sijainti < self.ylin_kerros:
            self.sijainti += 1
        else:
            return

    def kerros_alas(self):
        if self.sijainti > self.alin_kerros:
            self.sijainti -= 1
        else:
            return

    def siirry_kerrokseen(self, haluttu_kerros):
        self.haluttu_kerros = haluttu_kerros
        if self.haluttu_kerros > self.ylin_kerros:
            print(
                  f"Hissillä ei pääse kerrokseen {haluttu_kerros}, tällä hissillä pääsee vain kerrokseen {self.ylin_kerros}.")
        elif self.haluttu_kerros < self.alin_kerros:
            print(
                f"Hissillä ei pääse kerrokseen {haluttu_kerros}, tällä hissillä pääsee vain kerrokseen {self.alin_kerros}.")
        else:
            while self.sijainti != self.haluttu_kerros:
                if self.sijainti > self.haluttu_kerros:
                    self.sijainti -= 1
                else:
                    self.sijainti += 1


