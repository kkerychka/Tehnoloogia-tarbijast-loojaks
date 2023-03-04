ring = int(input("Sisestage ringide arv: "))
summa = 0
arv = 2
while arv <= ring:
    summa = summa +arv
    arv = arv + 2
print("Porgandite koguarv on " + str(summa))