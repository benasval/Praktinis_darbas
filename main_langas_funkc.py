from tkinter import *
from PIL import ImageTk, Image


class Funkcijos:

    def __init__(self, main):
        self.main = main
        self.main.title("Beno CV")
        self.f_main = Frame(self.main)
        photo = ImageTk.PhotoImage(Image.open("D:/cv_png.png")) 
        self.l_photo = Label(self.main, image=photo)
        self.b_close = Button(self.f_main, text="close", border=5, command=self.main.destroy)       

        self.l_photo.pack(side=TOP, fill=BOTH, expand=YES)
        self.f_main.pack(side=BOTTOM, fill=X)
        self.b_close.pack()
        
        
        self.main.mainloop()

    