aasta = int(input("Palun sisestage, millise aasta andmeid vajate: "))
aasta -= 2011

fail = open("rebased.txt", encoding="utf-8")
jrnd = []
for rida in fail:
    jrnd.append(int(rida))
fail.close()
print(str(aasta + 2011) + ". aastal oli vastuvõetud " + str(jrnd[aasta]))