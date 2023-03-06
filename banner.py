def banner(sone):
    return sone.upper()
    
arv = int(input("Mitu korda soovite reklaamlauset kuvada?: "))
sone = str(input("Sisestage reklaamlauset: "))

# while arv > 0:
#     print(banner(sone))
#     arv -= 1

for i in range(arv):
    print(banner(sone))
