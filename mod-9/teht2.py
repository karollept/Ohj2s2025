from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auto kiihdytti nopeuteen {auto1.nopeus} km/h.")
auto1.kiihdyta(-200)
print(f"Auto hätäjarrutti nopeuteen {auto1.nopeus} km/h.")

print(f"""
Lopuksi:
Auton rekisteritunnus on {auto1.rekisteritunnus}.
Auton huippunopeus on  {auto1.huippunopeus} km/h.
Tämänhetkinen auton nopeus on {auto1.nopeus} km/h.
Autolla kuljettu matka on {auto1.kuljettu_matka} km.
""")
