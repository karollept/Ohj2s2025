from classes.Julkaisu import publication
from classes.Julkaisu import kirja
from classes.Julkaisu import lehti

julkaisut = []
julkaisut.append(kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(lehti("Aku Ankka", "Aki Hyyppä"))

for j in julkaisut:
    j.tulosta_tiedot()
