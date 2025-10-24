import random

class elevator:
    def __init__(self, sijainti = 1, alin_kerros = 1, ylin_kerros = 7):
        self.sijainti = sijainti
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylös(self):
        if self.sijainti < self.ylin_kerros:
            self.sijainti += 1
        else:
            return



