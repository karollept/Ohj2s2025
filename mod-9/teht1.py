#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
# ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

from classes.auto import Auto


auto1 = Auto("ABC-123", 142)

print(f"""
Auton rekisteritunnus on {auto1.rekisteritunnus}.
Auton huippunopeus on  {auto1.huippunopeus} km/h.
Tämänhetkinen auton nopeus on {auto1.nopeus} km/h.
Autolla kuljettu matka on {auto1.kuljettu_matka} km.
""")