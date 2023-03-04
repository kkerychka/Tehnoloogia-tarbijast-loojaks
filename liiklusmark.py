from tkinter import *

raam = Tk()
raam.title("Liiklusmärk nr.364")

tahvel = Canvas(raam, width = 1200, height = 1200)

tahvel.create_rectangle(0, 0, 1200, 1200)
tahvel.create_oval(150, 150, 1000, 1000, fill = "red", outline = "red")
tahvel.create_oval(210, 210, 938, 938, fill = "blue", outline = "blue")
tahvel.create_line(495, 800, 495, 350, width = 90, fill= "white")
tahvel.create_line(650, 800, 650, 350, width = 90, fill= "white")
tahvel.create_line(230, 350, 860, 800, width = 60, fill= "red")



tahvel.pack()
raam.mainloop()