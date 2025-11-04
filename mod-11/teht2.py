from classes.auto import Auto
from classes.auto import Sahkoauto
from classes.auto import Polttomoottoriauto

autot = []
autot.append(Sahkoauto("ABC-15", 180,45, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165,40,32.3))

for a in autot:
    a.kulje(3)
    a.tulosta_tiedot()
