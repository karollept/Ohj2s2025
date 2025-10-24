import random

class elevator:
    def __init__(self, nimi, alin_kerros, ylin_kerros):
        self.nimi = nimi
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.sijainti = self.alin_kerros

    def __repr__(self):
        return f"{self.nimi} (kerros: {self.sijainti})"

    def kerros_ylos(self):
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
        if haluttu_kerros < self.alin_kerros or haluttu_kerros > self.ylin_kerros:
            print(f"{self.nimi}: Kerros {haluttu_kerros} ei ole sallittu ({self.alin_kerros}-{self.ylin_kerros})")
            return

        print(f"{self.nimi} lähtee kerroksesta {self.sijainti} kohti kerrosta {haluttu_kerros}")
        while self.sijainti != haluttu_kerros:
            if haluttu_kerros > self.sijainti:
                self.kerros_ylos()
            else:
                self.kerros_alas()
        print(f"{self.nimi} saapui kerrokseen {self.sijainti}")