import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

url = "https://api.covid19api.com/countries"
url2 = "https://api.covid19api.com/total/country/turkey"

response = requests.get(url)
json_veri = response.json()

response = requests.get(url2)
json_veri2 = response.json()

pencere = Tk()
pencere.title("COVID-19")

days=[]
sayilar=[]

for i in range(0,len(json_veri2)):
    sayilar.append(json_veri2[i]["Confirmed"])
    days.append(i)

figur1 = plt.figure(figsize=(6,6))
ax = figur1.add_subplot(1,1,1)
ax.plot(days, sayilar)
grafik = FigureCanvasTkAgg(figur1, pencere)
grafik.get_tk_widget().grid(row=0 , column=1)

#=======================================================================================================================
Secenek = Frame(pencere,background = "darkturquoise")
Secenek.grid(row=0 , column=0)

ulkeAd = Label(Secenek, text="Ülke Adı",background = "darkturquoise",fg = "white",font="Helvetica 14 bold")
ulkeAd.grid(row=1 , column=0)

ulkebox = Listbox(Secenek, font="Calibri", selectmode="extended",exportselection = 0, height = 15 )
ulkebox.grid(row=2 , column=0)
for i in range(0,len(json_veri)):
    ulkebox.insert(END,json_veri[i]["Country"])

grafik = Label(Secenek, text = "Grafikler",background = "darkturquoise",fg = "white",font="Helvetica 14 bold")
grafik.grid(row=3 , column=0)

grafikBox = Listbox(Secenek, font="Calibri", selectmode="extended",exportselection = 0,height=10)
grafikBox.grid(row=4 , column=0)


grafikButton = Button(Secenek, text="Göster",background = "White", fg= "darkturquoise",font="Helvetica 14 bold")
grafikButton.grid(row=5 , column=0)

pencere.mainloop()
