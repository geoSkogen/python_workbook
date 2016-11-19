from tkinter import *
from tkinter import messagebox

top = Tk()

C = Canvas(top, bg="blue", height=412, width=580)

filename = PhotoImage(file = "calamity_jane.gif")
image = C.create_image(100, 100, anchor = NE, image = filename)
C.place()
top.mainloop()
