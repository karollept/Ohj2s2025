import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

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




