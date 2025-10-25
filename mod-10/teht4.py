from classes.Kilpailu import competition

kilpailu1 = competition("Suuri romuralli", 8000, 10)

tunnit = 0
while not kilpailu1.kilpailu_ohi():
    kilpailu1.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu1.tilanne()

print("")
print(f"{kilpailu1.nimi} päättyi tilanteeseen")
kilpailu1.tilanne()
print(f"{kilpailu1.nimi} päättyi {tunnit} tunnin jälkeen!")
