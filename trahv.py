nimi = str(input("Sisestage oma nimi: "))
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
arvutus = (tegelik_kiirus - lubatud_kiirus) * 3
trahv = min(190, arvutus)
print(nimi + " kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")

"""
if arvutus < 190:
    print(nimi + ", kiiruse ületamise eest on teie trahv " + str(arvutus) + " eurot")
else:
    print(nimi + ", kiiruse ületamise eest on teie trahv on 190 eurot")
"""