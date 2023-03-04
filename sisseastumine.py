punktisumma = float(input("Palun sisesta punktisumma: "))

if punktisumma < 0 or punktisumma > 100:
    print("Vigane punktisumma")
elif punktisumma >= 66 and punktisumma < 85:
    print("Kandideerimine vastuvõtule")
elif punktisumma >= 85:
    print("Vastuvõtt tagatud")
else:
    print("Vähem kui kandideerimiseks vajalik")