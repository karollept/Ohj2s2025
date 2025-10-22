#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.

#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

from classes.auto import Auto
import random


auto1 = Auto("ABC-1")
auto2 = Auto("ABC-2")
auto3 = Auto("ABC-3")
auto4 = Auto("ABC-4")
auto5 = Auto("ABC-5")
auto6 = Auto("ABC-6")
auto7 = Auto("ABC-7")
auto8 = Auto("ABC-8")
auto9 = Auto("ABC-9")
auto10 = Auto("ABC-10")

while Auto max(kuljettu_matka)<1000:
    Auto.kiihdyta()

print(f"""
Lopuksi auton kuljettua 1,5 tuntia:
Auton rekisteritunnus on {auto1.rekisteritunnus}.
Auton huippunopeus on  {auto1.huippunopeus} km/h.
Tämänhetkinen auton nopeus on {auto1.nopeus} km/h.
Autolla kuljettu matka on {auto1.kuljettu_matka} km.
""")