import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def __repr__(self):
        return f"{self.rekisteritunnus} (huippunopeus: {self.huippunopeus})"

    def kiihdyta(self, muutos):
        self.muutos = muutos
        self.nopeus = self.nopeus + self.muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = self.nopeus

    def kulje(self, aika):
        self.aika = aika
        self.kuljettu_matka = self.kuljettu_matka + self.aika * self.nopeus


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, akkukapasiteetti, kuljettu_matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettu_matka)

    def tulosta_tiedot(self):
        print(f"Auton {self.rekisteritunnus} matkamittarilukemat ovat:"
              f"nopeus {self.nopeus}, kuljettu matka {self.kuljettu_matka}, akkukapasiteetti {self.akkukapasiteetti} ja auton huippunopeus on {self.huippunopeus}.")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, bensatankin_koko, kuljettu_matka=0):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus, nopeus, kuljettu_matka)

    def tulosta_tiedot(self):
        print(f"Auton {self.rekisteritunnus} matkamittarilukemat ovat:"
              f"nopeus {self.nopeus}, kuljettu matka {self.kuljettu_matka}, bensatankin koko {self.bensatankin_koko} ja auton huippunopeus on {self.huippunopeus}.")