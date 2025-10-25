from classes.auto import Auto
import random

class competition:
    def __init__(self, nimi, pituus_kilometreina, autojen_maara):
        self.nimi = nimi
        self.pituus_kilometreina = pituus_kilometreina
        self.autojen_maara = autojen_maara

        self.autot = []
        for i in range(autojen_maara):
            rekisteritunnus = f"ABC-{i + 1}"
            auto = Auto(rekisteritunnus, random.randint(100,200))
            self.autot.append(auto)
        print(self.autot)

    def highscore(self):
        print("Kierroksen tulokset")
        print(f"{'Auto':<10} {'Matka (km)':<12} {'Nopeus (km/h)':<15} {'Huippunopeus':<13}")
        print("-" * 50)

        self.autot.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)

        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} {auto.kuljettu_matka:<12} {auto.nopeus:<15} {auto.huippunopeus:<13}")

    def tunti_kuluu(self):
        while True:
            for auto in self.autot:
                auto.kiihdyta(random.randint(-10, 15))
                auto.kulje(1)

                if auto.kuljettu_matka >= self.pituus_kilometreina:
                    return

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_kilometreina:
                self.highscore()
                return



