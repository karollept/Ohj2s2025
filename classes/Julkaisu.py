class publication:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu {self.nimi}")

class kirja(publication):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(kirjailija {self.kirjoittaja}, {self.sivumaara} sivua)")

class lehti(publication):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(päätoimittaja {self.paatoimittaja})")