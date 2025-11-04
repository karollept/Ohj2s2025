#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
# yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

from classes.auto import Auto
from classes.auto import Sahkoauto
from classes.auto import Polttomoottoriauto

autot = []
autot.append(Sahkoauto("ABC-15", 180,45, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165,40,32.3))

for a in autot:
    a.kulje(3)
    a.tulosta_tiedot()
