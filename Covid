import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *


url = "https://api.covid19api.com/summary"
response = requests.get(url)
json_veri = response.json()

pencere = Tk()
pencere.title("COVID-19")

Secenek = Frame(pencere,background = "darkturquoise")
Secenek.grid(row=0 , column=0)

ulkeAd = Label(Secenek, text="Ülke Adı",background = "darkturquoise",fg = "white",font="Helvetica 14 bold")
ulkeAd.grid(row=1 , column=0)

ulkebox = Listbox(Secenek, font="Calibri", selectmode="extended",exportselection = 0, height = 20 )
ulkebox.grid(row=2 , column=0)
for i in json_veri["Countries"]:
    ulkebox.insert(END, i["Country"])

grafik = Label(Secenek, text = "Grafikler",background = "darkturquoise",fg = "white",font="Helvetica 14 bold")
grafik.grid(row=3 , column=0)

grafikBox = Listbox(Secenek, font="Calibri", selectmode="extended",exportselection = 0,height=10)
grafikBox.grid(row=4 , column=0)
for i in json_veri["Global"]:
    grafikBox.insert(END,i)

grafikButton = Button(Secenek, text="Göster",background = "White", fg= "darkturquoise",font="Helvetica 14 bold")
grafikButton.grid(row=5 , column=0)


pencere.mainloop()
