parool = int(input("Sisestage parool: "))
parool_on = 1234

if parool == parool_on:
    print("Õige parool!")
else:
    print("Parool on vale!")
    if len(str(parool)) > len(str(parool_on)):
        print("Sisestatud parool on liiga suur.")
    if len(str(parool)) < len(str(parool_on)):
        print("Sisestatud parool on liiga väike.")
        
        
"""---------------------------------------------------------------------------------------------------------------"""
kontoseis = 100
 
sisestatud_pin = input("Sisesta PIN-kood: ")
if sisestatud_pin == "1234":
    print("Sisenesid pangaautomaati! Pangakontol on " + str(kontoseis) + " eurot.")
    print("Sisesta, mitu eurot soovid välja võtta:")
    soovitud_raha = int(input())
    if soovitud_raha <= kontoseis:
        kontoseis = kontoseis - soovitud_raha #kontoseisu väärtus väheneb
        print("Raha välja võetud: " + str(soovitud_raha) + " eurot.")
    else:
        print("Kontol ei ole nii palju raha!")
    print("Pangakontol on järgi: " + str(kontoseis) + " eurot.")
else:
    print("Vale parool! Ligipääs keelatud!")