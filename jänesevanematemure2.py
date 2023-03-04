ring = int(input("Sisestage ringide arv: "))
summa = 0
arv = 1
while arv <= ring:
    summa = int(summa + (arv * (arv+1) /2))
    arv = arv + 1
print("Porgandite koguarv on " + str(summa))
