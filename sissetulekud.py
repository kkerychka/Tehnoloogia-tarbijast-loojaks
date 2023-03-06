with open("konto.txt") as fail:
    konto = []
    i = 0
    for rida in fail:
        if float(rida) > 0:
            konto.append(float(rida))
            print(konto[i])
            i += 1
            
            