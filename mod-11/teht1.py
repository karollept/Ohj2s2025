#Toteuta seuraava luokkahierarkia Python-kielellä:
# Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

from classes.Julkaisu import publication
from classes.Julkaisu import kirja
from classes.Julkaisu import lehti

julkaisut = []
julkaisut.append(kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(lehti("Aku Ankka", "Aki Hyyppä"))

for j in julkaisut:
    j.tulosta_tiedot()
