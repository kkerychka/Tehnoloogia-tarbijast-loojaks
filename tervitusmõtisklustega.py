def tervitus(arv):
    print('Võõrustaja: "Tere!"')
    print('Täna ' + str(arv) + '. kord tervitada, mõtiskleb võõrustaja')
    print('Külaline: "Tere, suur tänu kutse eest!"')

külalised = int(input("Sisestage külaliste arv: "))
for i in range(1, külalised + 1):
    tervitus(i)