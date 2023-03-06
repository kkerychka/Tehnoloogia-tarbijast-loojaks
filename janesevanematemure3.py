ring = int(input("Sisestage ringide arv: "))
ring += 1
porgand = 0
for i in range(0, ring, 2):
    porgand = porgand + i
print("Saadavate porgandite arv on " + str(porgand))