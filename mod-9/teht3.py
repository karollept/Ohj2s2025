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
