def mahlapakkide_arv(kogus):
    return round(kogus * 0.4 / 3)
arv = float(input("Sisesta õunte kogus kilogrammides: "))
print(mahlapakkide_arv(arv))