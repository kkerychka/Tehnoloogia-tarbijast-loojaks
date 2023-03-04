vanus = int(input("Sisestage enda vanus: "))
sugu = str(input("Sisestage enda sugu: ").lower())
tüüp =  int(input("Sisestage treeningu tüüp: "))

max_pulsisagedus_m = 220 - vanus
max_pulsisagedus_n = 206 - 0.88 * vanus

if sugu == "m" and tüüp == 1:
    pulss_max = max_pulsisagedus_m * 0.7
    pulss_min = max_pulsisagedus_m * 0.5
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
elif sugu == "m" and tüüp == 2:
    pulss_max = max_pulsisagedus_m * 0.8
    pulss_min = max_pulsisagedus_m * 0.7
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
elif sugu == "m" and tüüp == 3:
    pulss_max = max_pulsisagedus_m * 0.87
    pulss_min = max_pulsisagedus_m * 0.8
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
elif sugu == "n" and tüüp == 1:
    pulss_max = max_pulsisagedus_n * 0.7
    pulss_min = max_pulsisagedus_n * 0.5
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
elif sugu == "n" and tüüp == 2:
    pulss_max = max_pulsisagedus_n * 0.8
    pulss_min = max_pulsisagedus_n * 0.7
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
elif sugu == "n" and tüüp == 3:
    pulss_max = max_pulsisagedus_n * 0.87
    pulss_min = max_pulsisagedus_n * 0.8
    print("Pulsisagedus peaks olema vahemikus " + str(round(pulss_min)) + " kuni " + str(round(pulss_max)) + ".")
else:
    print("Mingi viga!")