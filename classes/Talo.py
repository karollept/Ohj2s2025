from classes.Hissi import elevator

class house:
    def __init__(self, hissien_maara, alin_kerros = 1, ylin_kerros = 9):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara

        self.hissit = []
        for i in range(hissien_maara):
            nimi = f"elevator{i + 1}"
            hissi = elevator(nimi, alin_kerros, ylin_kerros)
            self.hissit.append(hissi)
        print(self.hissit)

    def aja_hissia(self, nimi, haluttu_kerros):
        if 1 <= nimi <= len(self.hissit):
            hissi = self.hissit[nimi-1]
            hissi.siirry_kerrokseen(haluttu_kerros)
        else:
            print(f"Hissi numero {nimi} ei ole olemassa.")

    def palohalytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
