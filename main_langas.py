from tkinter import *
from main_langas_funkc import Funkcijos
import webbrowser

class Main_langas:
    def __init__(self, langas):
        self.langas = langas
        self.f_pasisveikinimas = Frame(self.langas)
        self.f_mygtukai = Frame(self.langas)
        self.l_langas = Label(self.f_pasisveikinimas, text="Sveiki atvyke i Beno Valaicio kontaktini langa", border=5, relief=SUNKEN)
        self.b_cv = Button(self.f_pasisveikinimas, text="CV", border=10, command=self.run_cv_langas)
        self.b_fb = Button(self.f_mygtukai, text="Facebook", border=5, command=self.fb_linkas)
        self.b_ig = Button(self.f_mygtukai, text="Instagram", border=5, command=self.ig_linkas)
        self.b_lin = Button(self.f_mygtukai, text="LinkedIn", border=5, command=self.lin_linkas)

        self.f_pasisveikinimas.pack()
        self.l_langas.pack(side=TOP)
        self.b_cv.pack()
        self.f_mygtukai.pack(side=BOTTOM)
        self.b_fb.grid(sticky=S, column=1, row=1)
        self.b_ig.grid(sticky=S, column=2, row=1)
        self.b_lin.grid(sticky=S, column=3, row=1)

    def run_cv_langas(self):
        self.cv_langas = Toplevel(self.langas)
        self.app = Funkcijos(self.cv_langas)
    
    def fb_linkas(self):
        webbrowser.open_new_tab("https://www.facebook.com/benas.valaitis/")
    def ig_linkas(self):
        webbrowser.open_new_tab("https://www.instagram.com/benas_val/")
    def lin_linkas(self):
        webbrowser.open_new_tab("https://www.linkedin.com/in/benas-valaitis-92b7991a3/")