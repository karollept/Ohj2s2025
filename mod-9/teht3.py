#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
#Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.


from classes.auto import Auto

auto1 = Auto("ABC-123", 142, 60, 2000)

print(f"""
Aluksi:
Auton rekisteritunnus on {auto1.rekisteritunnus}.
Auton huippunopeus on  {auto1.huippunopeus} km/h.
Tämänhetkinen auton nopeus on {auto1.nopeus} km/h.
Autolla kuljettu matka on {auto1.kuljettu_matka} km.
""")

auto1.kulje(1.5)

print(f"""
Lopuksi auton kuljettua 1,5 tuntia:
Auton rekisteritunnus on {auto1.rekisteritunnus}.
Auton huippunopeus on  {auto1.huippunopeus} km/h.
Tämänhetkinen auton nopeus on {auto1.nopeus} km/h.
Autolla kuljettu matka on {auto1.kuljettu_matka} km.
""")
