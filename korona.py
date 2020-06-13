import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

url = "https://api.covid19api.com/countries"
url2 = "https://api.covid19api.com/total/country/"
url3 = "https://api.covid19api.com/summary"
url4 = "https://api.covid19api.com/total/dayone/country/"

response = requests.get(url)
json_veri = response.json()

response = requests.get(url2)
json_veri2 = response.json()

response = requests.get(url3)
json_veri3 = response.json()

response1 = requests.get(url4)
json_veri4 = response1.json()

pencere = Tk()
pencere.title("COVID-19")

import datetime;

gun = datetime.datetime.now().strftime("%d");
ay = datetime.datetime.now().strftime("%m");
yil = datetime.datetime.now().strftime("%Y");

dunya = Frame(pencere,background = "darkturquoise")
dunya.grid(row=0 , column=1)

saat = Label(dunya,relief = RIDGE , border = 3, text ="TARİH : "+gun+"/"+ay+"/"+yil,font="Helvetica 14 bold",
             background = "white",width= 30 , height = 10,fg = "darkturquoise")
saat.grid(row = 0 , column = 1)

baslık = Label(dunya,relief = RIDGE , border = 3, text = "🌎 COVİD-19 VERİSİ",
               font="Helvetica 14 bold",background = "white",width= 30 , height = 2)
baslık.grid(row = 1 , column = 1)

newconfirmed = Label(dunya,relief = GROOVE , border = 5,text = "YENİ VAKA",
                     font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
newconfirmed.grid(row = 2 , column = 1)
ncbox = Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
ncbox.insert(END,json_veri3["Global"]["NewConfirmed"])
ncbox.grid(row=2 , column =2)

totalconfirmed = Label(dunya,relief = GROOVE , border = 5,text="TOPLAM VAKA",
                       font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
totalconfirmed.grid(row=3, column=1)
tcbox = Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
tcbox.insert(END,json_veri3["Global"]["TotalConfirmed"])
tcbox.grid(row=3 , column =2)

newdeaths = Label(dunya,relief = GROOVE , border = 5,text="YENİ VEFAT",
                  font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
newdeaths.grid(row=4, column=1)
ndbox =  Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
ndbox.insert(END,json_veri3["Global"]["NewDeaths"])
ndbox.grid(row=4 , column =2)

totaldeaths = Label(dunya,relief = GROOVE , border = 5,text="TOPLAM VEFAT",
                    font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
totaldeaths.grid(row=5, column=1)
tdbox = Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
tdbox.insert(END,json_veri3["Global"]["TotalDeaths"])
tdbox.grid(row=5 , column =2)

newrecovered = Label(dunya,relief = GROOVE , border = 5,text="YENİ İYİLEŞEN",
                     font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
newrecovered.grid(row = 6 , column = 1)
ncbox = Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
ncbox.insert(END,json_veri3["Global"]["NewRecovered"])
ncbox.grid(row = 6 , column = 2)

totalrecovered = Label(dunya,relief = GROOVE , border = 5,text="TOPLAM İYİLEŞEN",
                       font="Helvetica 14 bold",background = "darkturquoise",fg = "white",width= 30 , height = 2)
totalrecovered.grid(row = 7 , column = 1)
tcbox = Listbox(dunya,font="Helvetica 14 bold",width=10,height = 2)
tcbox.insert(END,json_veri3["Global"]["TotalRecovered"])
tcbox.grid(row = 7, column =2)

ulke_slug=[]

def draw():
    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url2+ulke_slug[sira])
    json_veri2 = response.json()
    days=[]
    sayilar=[]

    for i in range(0,len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Confirmed":
            sayilar.append(json_veri2[i]["Confirmed"])
            days.append(i)
        elif grafikBox.get(ACTIVE) == "Recovered":
            sayilar.append(json_veri2[i]["Recovered"])
            days.append(i)
        elif grafikBox.get(ACTIVE) == "Active":
            sayilar.append(json_veri2[i]["Active"])
            days.append(i)
        elif grafikBox.get(ACTIVE) == "Deaths":
            sayilar.append(json_veri2[i]["Deaths"])
            days.append(i)

    figur1 = plt.figure(figsize=(9,6))
    ax = figur1.add_subplot(1,1,1)
    ax.plot(days, sayilar)
    plt.title("COVİD-19 ÜLKE VERİSİ")
    plt.xlabel("GÜN")
    plt.ylabel("İNSAN SAYISI")
    grafik1 = FigureCanvasTkAgg(figur1, pencere)
    grafik1.get_tk_widget().grid(row=0 , column=1)

def draw2():
    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url4 + ulke_slug[sira])
    json_veri4 = response.json()

    vaka = []
    gun = []
    for i in range(0,len(json_veri4)):
        if grafikBox.get(ACTIVE) == "Günlük iyileşen":
            vaka.append(json_veri4[i]["Recovered"])
            gun.append(i)
        elif grafikBox.get(ACTIVE) == "Günlük vaka":
            vaka.append(json_veri4[i]["Confirmed"])
            gun.append(i)
        elif grafikBox.get(ACTIVE) == "Günlük vefat":
            vaka.append(json_veri4[i]["Deaths"])
            gun.append(i)
        elif grafikBox.get(ACTIVE) == "Günlük aktif":
            vaka.append(json_veri4[i]["Active"])
            gun.append(i)

    figur2 = plt.figure(figsize= (9,6))
    ax1 = figur2.add_subplot(1, 1, 1)
    ax1.bar(gun,vaka)
    grafik2 = FigureCanvasTkAgg(figur2, pencere)
    grafik2.get_tk_widget().grid(row=0, column=1)

def drawkontrol():
    if (grafikBox == "Confirmed" ) or (grafikBox =="Recovered" ) or (grafikBox == "Active") or (grafikBox ==  "Deaths"):
        draw()
    elif(grafikBox =="Günlük iyileşen" ) or (grafikBox == "Günlük vaka") or (grafikBox =="Günlük vefat" ) or (grafikBox == "Günlük aktif" ):
        draw2()




#=======================================================================================================================

for i in range(0,len(json_veri)):
    ulke_slug.append(json_veri[i]["Slug"])

Secenek = Frame(pencere,relief = GROOVE , border = 5, background = "darkturquoise")
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
grafikBox.insert(0,"Confirmed")
grafikBox.insert(1,"Recovered" )
grafikBox.insert(2,"Active")
grafikBox.insert(3,"Deaths")
grafikBox.insert(4,"Günlük iyileşen")
grafikBox.insert(5,"Günlük vaka" )
grafikBox.insert(6,"Günlük vefat")
grafikBox.insert(END,"Günlük aktif")

grafikButton = Button(Secenek,relief = RIDGE , border = 5, text="Göster",background = "White",
                      fg= "darkturquoise",font="Helvetica 14 bold",command=drawkontrol)
grafikButton.grid(row=5 , column=0)

pencere.mainloop()
