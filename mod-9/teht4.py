from classes.auto import Auto
import random

def highscore(Auto):
    print("Highscore – Kilpailun tulokset")
    print(f"{'Auto':<10} {'Matka (km)':<12} {'Nopeus (km/h)':<15} {'Huippunopeus':<13}")
    print("-" * 50)

    autot.sort(key=lambda auto: auto.kuljettu_matka, reverse=True)

    for auto in autot:
        print(f"{auto.rekisteritunnus:<10} {auto.kuljettu_matka:<12} {auto.nopeus:<15} {auto.huippunopeus:<13}")

def kisa_kierros(Auto):
    while True:
        for auto in Auto:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
            #print(f"{auto.rekisteritunnus}: nopeus {auto.nopeus} km/h, matka {auto.kuljettu_matka} km")
            if auto.kuljettu_matka >= 10000:
                highscore(Auto)
                return

auto1 = Auto("ABC-1", random.randint(100,200))
auto2 = Auto("ABC-2", random.randint(100,200))
auto3 = Auto("ABC-3", random.randint(100,200))
auto4 = Auto("ABC-4", random.randint(100,200))
auto5 = Auto("ABC-5", random.randint(100,200))
auto6 = Auto("ABC-6", random.randint(100,200))
auto7 = Auto("ABC-7", random.randint(100,200))
auto8 = Auto("ABC-8", random.randint(100,200))
auto9 = Auto("ABC-9", random.randint(100,200))
auto10 = Auto("ABC-10", random.randint(100,200))

autot = [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10]
kisa_kierros([auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10])
