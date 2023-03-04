from time import sleep
pin = int(input("Looge pin-kood: "))
sisestatud_pin = int(input("Sisestage parool: "))
katseid = 3
while sisestatud_pin != pin and katseid > 1:
    print("Parool on vale!")
    sisestatud_pin = int(input("Sisestage parool: "))
    katseid -= 1
if  sisestatud_pin  == pin:
    print("Sisenesid pankasse!")
else:
   print("Katsete arv ületatud! Turvatöötaja kutsutakse 10 sekundi pärast!")
   i = 10
   while i > 0:
      print(i)
      i -= 1
      sleep(1)
   print("Turvatöötaja kutsutud!")

# from time import sleep
# sisestatud_pin = ""
# katseid = 3
# while sisestatud_pin != "1234" and katseid > 0:
#    print("Sisesta PIN-kood:")
#    print("Jäänud on " + str(katseid) + " katset.")
#    katseid -= 1
#    sisestatud_pin = input()
