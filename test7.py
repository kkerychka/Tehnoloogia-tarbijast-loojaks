from tkinter import *
from math import *
import time
raam = Tk()
raam.title("Kell")
# tahvli laius
w = 500
# tahvli pikkus
h = 500
 
tahvel = Canvas(raam, width=w, height=h, bg="white")
 
# kella raam
tahvel.create_oval(10,10,w-10,h-10)
# kella keskpunkt
tahvel.create_oval(w/2-5,h/2-5,w/2+5,h/2+5,fill="black")
sek_id = tahvel.create_line(w/2,h/2,w/2,20,fill="red")
 
def uuenda(): 
    # loeme jooksva sekundi
    sekundid = time.localtime().tm_sec
 
    # osuti liikuva tipu koordinaadid
    # arvutame sekundiosuti pikkuse
    r = min(w/2,h/2)-20
 
    # arvutame x koordinaadi
    x = r*cos(pi/2-sekundid/60.0*2*pi)
 
    # arvutame y koordinaadi
    y = -r*sin(pi/2-sekundid/60.0*2*pi)
 
    # uuendame osuti positsiooni
    tahvel.coords(sek_id, 0, 0, x, y)
 
    # nihutame keskele
    tahvel.move(sek_id, w/2, h/2)
 
    #ootame 1 sekundi ja siis uuendame kellaaega uuesti
    raam.after(1000, uuenda)
 
uuenda()
tahvel.pack()
raam.mainloop()