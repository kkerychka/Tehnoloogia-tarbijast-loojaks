nimi = str(input("Palun sisestage failinimi: "))

with open(nimi) as fail:
    i = 0
    muusika = []
    print("Muusikapalade valik:")
    for rida in fail:
        muusika.append(str(rida))
        i += 1
        print(str(i) + ". " + str(rida))
        
valik = int(input("Vali muusikapala number: "))
valik -= 1
print("Mängitav muusikapala on " + muusika[valik])