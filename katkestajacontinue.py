import time
katkestaja = 14
i = 20
while i > 0:
    print(i)
    i -= 1 # i = i - 1
    if i == katkestaja:
        continue
    time.sleep(1)
    print("Tsüklisisu lõpuosa, i = " + str(i))
print("Kõik on läbi")
