
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg , NavigationToolbar2Tk)
import datetime

url = "https://api.covid19api.com/countries"
url2 = "https://api.covid19api.com/total/country/"
url3 = "https://api.covid19api.com/summary"
url4 = "https://api.covid19api.com/total/dayone/country/"
url5 = "https://api.covid19api.com/world/total"

response = requests.get(url)
json_veri = response.json()

response = requests.get(url2)
json_veri2 = response.json()

response = requests.get(url3)
json_veri3 = response.json()

response = requests.get(url4)
json_veri4 = response.json()

response  = requests.get(url5)
json_veri5 = response.json()

pencere = Tk()
pencere.title("COVID-19 İstatistiği")

import datetime;

gun = datetime.datetime.now().strftime("%d");
ay = datetime.datetime.now().strftime("%m");
yil = datetime.datetime.now().strftime("%Y");

dunya = Frame(pencere, background="darkturquoise")
dunya.grid(row=0, column=1)

saat = Label(dunya,
             relief=RIDGE,
             border=3,
             text= gun + "/" + ay + "/" + yil,
             font="Helvatica 15 bold",
             background="white",
             width=50,height=4,
             fg="black")
saat.grid(row=0, column=1)

baslık = Label(dunya,
               relief=RIDGE,
               border=3,
               text=" COVİD-19 🌎 VERİSİ ",
               font="Helvetica 14 bold",
               background="white",
               width=50, height=1)
baslık.grid(row=1, column=1)

NewC = str(json_veri3["Global"]["NewConfirmed"])
newconfirmed = Label(dunya,
                     relief=GROOVE,
                     border=5,
                     text="YENİ VAKA : " + NewC ,
                     font="Helvetica 14 bold",
                     background="darkcyan",
                     fg="white",
                     width=50, height=3)
newconfirmed.grid(row=2, column=1)

TotalC = str(json_veri3["Global"]["TotalConfirmed"])
totalconfirmed = Label(dunya,
                       relief=GROOVE,
                       border=5,
                       text="TOPLAM VAKA : " + TotalC ,
                       font="Helvetica 14 bold",
                       background="darkturquoise",
                       fg="white",
                       width=50, height=3)
totalconfirmed.grid(row=3, column=1)

NewD = str(json_veri3["Global"]["NewDeaths"])
newdeaths = Label(dunya,
                  relief=GROOVE,
                  border=5, text="YENİ VEFAT : " + NewD,
                  font="Helvetica 14 bold",
                  background="darkcyan",
                  fg="white",
                  width=50, height=3)
newdeaths.grid(row=4, column=1)

TotalD = str(json_veri3["Global"]["TotalDeaths"])
totaldeaths = Label(dunya,
                    relief=GROOVE,
                    border=5,
                    text="TOPLAM VEFAT : " + TotalD,
                    font="Helvetica 14 bold",
                    background="darkturquoise",
                    fg="white",
                    width=50, height=3)
totaldeaths.grid(row=5, column=1)

NewR = str(json_veri3["Global"]["NewRecovered"])
newrecovered = Label(dunya,
                     relief=GROOVE,
                     border=5,
                     text="YENİ İYİLEŞEN : " + NewR,
                     font="Helvetica 14 bold",
                     background="darkcyan",
                     fg="white",
                     width=50, height=3)
newrecovered.grid(row=6, column=1)

TotalR = str(json_veri3["Global"]["TotalRecovered"])
totalrecovered = Label(dunya,
                       relief=GROOVE,
                       border=5,
                       text="TOPLAM İYİLEŞEN : " + TotalR,
                       font="Helvetica 14 bold",
                       background="darkturquoise",
                       fg="white",
                       width=50, height=3)
totalrecovered.grid(row=7, column=1)


# =======================================================================================================================
ulke_slug = []


def draw():

    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url2 + ulke_slug[sira])
    json_veri2 = response.json()

    days = []
    sayilar = []

    for i in range(0, len(json_veri2)):

        if grafikBox.get(ACTIVE) == "Onaylanmış vaka":
            sayilar.append(json_veri2[i]["Confirmed"])
            days.append(i)

        elif grafikBox.get(ACTIVE) == "İyileşen":
            sayilar.append(json_veri2[i]["Recovered"])
            days.append(i)

        elif grafikBox.get(ACTIVE) == "Aktif vaka":
            sayilar.append(json_veri2[i]["Active"])
            days.append(i)

        elif grafikBox.get(ACTIVE) == "Vefat":
            sayilar.append(json_veri2[i]["Deaths"])
            days.append(i)

    figur1 = plt.figure(figsize=(10, 6))

    ax = figur1.add_subplot(1, 1, 1)
    ax.plot(days, sayilar, color="blue")
    plt.title("COVİD-19 ÜLKE VERİSİ")
    plt.xlabel("GÜN")
    plt.ylabel("İNSAN SAYISI")

    grafik = FigureCanvasTkAgg(figur1, pencere)
    grafik.get_tk_widget().grid(row=0, column=1)

    frame = Frame(pencere)
    frame.grid(row=1, column=1)
    toolbar = NavigationToolbar2Tk(grafik, frame)


def draw2():

    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url4 + ulke_slug[sira])
    json_veri4 = response.json()

    vaka = []
    gun = []

    for i in range(0, len(json_veri4)):

        if grafikBox.get(ACTIVE) == "Günlük İyileşen":
            vaka.append(json_veri4[i]["Recovered"])

        elif grafikBox.get(ACTIVE) == "Günlük Onaylanmış vaka":
            vaka.append(json_veri4[i]["Confirmed"])

        elif grafikBox.get(ACTIVE) == "Günlük Vefat":
            vaka.append(json_veri4[i]["Deaths"])

        elif grafikBox.get(ACTIVE) == "Günlük Aktif vaka":
            vaka.append(json_veri4[i]["Active"])

    vaka2 = []
    for i in range(0, len(vaka) - 1):
        vaka2.append(vaka[i + 1] - vaka[i])
        gun.append(i)

    figur2 = plt.figure(figsize=(10, 6))

    ax1 = figur2.add_subplot(1, 1, 1)
    ax1.bar(gun, vaka2, color="#f9af2b", edgecolor="#f05131")
    plt.title("COVİD-19 ÜLKE VERİSİ")
    plt.xlabel("GÜN")
    plt.ylabel("İNSAN SAYISI")

    grafik2 = FigureCanvasTkAgg(figur2, pencere)
    grafik2.get_tk_widget().grid(row=0, column=1)

    frame = Frame(pencere)
    frame.grid(row=1, column=1)
    toolbar = NavigationToolbar2Tk(grafik2, frame)


def draw3():

    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url2 + ulke_slug[sira])
    json_veri2 = response.json()

    gun = []
    veri = []

    gun1 = []
    veri1 = []

    gun2 = []
    veri2 = []

    gun3 = []
    veri3 = []

    for i in range(0, len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Tüm Veriler":
            veri.append(json_veri2[i]["Confirmed"])
            gun.append(i)

    for i in range(0, len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Tüm Veriler":
            veri1.append(json_veri2[i]["Recovered"])
            gun1.append(i)

    for i in range(0, len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Tüm Veriler":
            veri2.append(json_veri2[i]["Active"])
            gun2.append(i)

    for i in range(0, len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Tüm Veriler":
            veri3.append(json_veri2[i]["Deaths"])
            gun3.append(i)

    figur3 = plt.figure(figsize=(10, 6))

    data = figur3.add_subplot(2, 2, 1)
    data.plot(gun, veri, color="#76EE00")
    plt.title("Onaylanmış vaka")

    data1 = figur3.add_subplot(2, 2, 2)
    data1.plot(gun1, veri1, color="#BF3EFF")
    plt.title("İyileşen")

    data2 = figur3.add_subplot(2, 2, 3)
    data2.plot(gun2, veri2, color="blue")
    plt.title("Aktif vaka")

    data3 = figur3.add_subplot(2, 2, 4)
    data3.plot(gun3, veri3, color="red")
    plt.title("Vefat")

    grafik3 = FigureCanvasTkAgg(figur3, pencere)
    grafik3.get_tk_widget().grid(row=0, column=1)

    frame = Frame(pencere)
    frame.grid(row=1, column=1)
    toolbar = NavigationToolbar2Tk(grafik3, frame)


def draw4():

    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url4 + ulke_slug[sira])
    json_veri4 = response.json()

    gun = []
    veri = []

    gun1 = []
    veri1 = []

    gun2 = []
    veri2 = []

    gun3 = []
    veri3 = []

    for i in range(0, len(json_veri4)):
        if grafikBox.get(ACTIVE) == "Günlük Tüm Veriler":
            veri.append(json_veri4[i]["Confirmed"])

    veria = []
    for i in range(0, len(veri) - 1):
        veria.append(veri[i + 1] - veri[i])
        gun.append(i)

    for i in range(0, len(json_veri4)):
        if grafikBox.get(ACTIVE) == "Günlük Tüm Veriler":
            veri1.append(json_veri4[i]["Recovered"])

    verib = []
    for i in range(0, len(veri1) - 1):
        verib.append(veri1[i + 1] - veri1[i])
        gun1.append(i)

    for i in range(0, len(json_veri4)):
        if grafikBox.get(ACTIVE) == "Günlük Tüm Veriler":
            veri2.append(json_veri4[i]["Active"])

    veric = []
    for i in range(0, len(veri2) - 1):
        veric.append(veri2[i + 1] - veri2[i])
        gun2.append(i)

    for i in range(0, len(json_veri4)):
        if grafikBox.get(ACTIVE) == "Günlük Tüm Veriler":
            veri3.append(json_veri4[i]["Deaths"])

    verid = []
    for i in range(0, len(veri3) - 1):
        verid.append(veri3[i + 1] - veri3[i])
        gun3.append(i)

    figur4 = plt.figure(figsize=(10, 6))

    data = figur4.add_subplot(2, 2, 1)
    data.bar(gun, veria, color="#76EE00")
    plt.title("Onaylanmış vaka")

    data1 = figur4.add_subplot(2, 2, 2)
    data1.bar(gun1, verib, color="#BF3EFF")
    plt.title("İyileşen")

    data2 = figur4.add_subplot(2, 2, 3)
    data2.bar(gun2, veric, color="blue")
    plt.title("Aktif vaka")

    data3 = figur4.add_subplot(2, 2, 4)
    data3.bar(gun3, verid, color="red")
    plt.title("Vefat")

    grafik4 = FigureCanvasTkAgg(figur4, pencere)
    grafik4.get_tk_widget().grid(row=0, column=1)

    frame = Frame(pencere)
    frame.grid(row=1, column=1)
    toolbar = NavigationToolbar2Tk(grafik4, frame)


def draw5():

    ad = ulkebox.curselection()
    sira = int(ad[0])

    print(ulke_slug[sira])
    response = requests.get(url2 + ulke_slug[sira])
    json_veri2 = response.json()

    numbers = []
    day = []

    numbers1 = []
    day1 = []

    numbers2 = []
    day2 = []

    numbers3 = []
    day3 = []

    for i in range(0, len(json_veri2)):
        if grafikBox.get(ACTIVE) == "Karşılaştırma Grafiği":
            numbers.append(json_veri2[i]["Confirmed"])
            day.append(i)

        if grafikBox.get(ACTIVE) == "Karşılaştırma Grafiği":
            numbers1.append(json_veri2[i]["Recovered"])
            day1.append(i)

        if grafikBox.get(ACTIVE) == "Karşılaştırma Grafiği":
            numbers2.append(json_veri2[i]["Active"])
            day2.append(i)

        if grafikBox.get(ACTIVE) == "Karşılaştırma Grafiği":
            numbers3.append(json_veri2[i]["Deaths"])
            day3.append(i)

    figur5 = plt.figure(figsize=(10, 6))

    cc = figur5.add_subplot(1, 1, 1)
    cc.plot(day, numbers, color="#76EE00")
    cc.plot(day1, numbers1, color="#BF3EFF")
    cc.plot(day2, numbers2, color="blue")
    cc.plot(day3, numbers3, color="red")
    cc.legend(("Confirmed", "Recovered", "Active", "Deaths"), title="VERİ")

    plt.title("COVİD-19 ÜLKE VERİSİ")
    plt.xlabel("GÜN")
    plt.ylabel("İNSAN SAYISI")

    grafik5 = FigureCanvasTkAgg(figur5, pencere)
    grafik5.get_tk_widget().grid(row=0, column=1)

    frame = Frame(pencere)
    frame.grid(row=1, column=1)
    toolbar = NavigationToolbar2Tk(grafik5, frame)


def draw6():

    if grafikBox.get(ACTIVE) == "Dünya Pasta Grafiği":

        pasta = Frame(pencere, background="darkturquoise")
        pasta.grid(row = 0 , column = 1 )

        toplambaslık = Label(pasta,relief=GROOVE, border=1, text="TOPLAM VERİ" ,
                       font="Helvetica 14 bold", background="white", fg="black",width=41, height=2)
        toplambaslık.grid(row = 0 , column = 1)

        ToplamC = str(json_veri3["Global"]["TotalConfirmed"])
        toplamvaka = Label(pasta, relief=GROOVE, border=3, text="VAKA : " + ToplamC ,
                       font="Helvetica 14 bold", background="darkturquoise", fg="white",width=41, height=2)
        toplamvaka.grid(row = 1 , column = 1)

        ToplamD = str(json_veri3["Global"]["TotalDeaths"])
        toplamvefat = Label(pasta, relief=GROOVE, border=3, text="VEFAT : " + ToplamD,
                            font="Helvetica 14 bold", background="darkturquoise", fg="white",width=41, height=2)
        toplamvefat.grid(row = 2 , column = 1)

        ToplamR = str(json_veri3["Global"]["TotalRecovered"])
        toplamiyilesen = Label(pasta, relief=GROOVE, border=3, text="İYİLEŞEN : " + ToplamR,
                               font="Helvetica 14 bold", background="darkturquoise", fg="white",width=41, height=2)
        toplamiyilesen.grid(row= 3 , column = 1)

        dunya_veri = ["Onaylanan", "Vefat", "İyileşen"]
        dunya_sayı = [str(json_veri3["Global"]["TotalConfirmed"]),str(json_veri3["Global"]["TotalDeaths"]),
                      str(json_veri3["Global"]["TotalRecovered"])]

        figur1 = plt.figure(figsize=(5, 4))
        ax = figur1.add_subplot(1, 1, 1)
        ax.pie(dunya_sayı,labels = dunya_veri,autopct="%1.1f%%", startangle=90,wedgeprops=dict(width=0.5))

        grafik = FigureCanvasTkAgg(figur1, pasta)
        grafik.get_tk_widget().grid(row=4, column=1)

        yenibaslık = Label(pasta, relief=GROOVE, border=1, text="YENİ VERİ",
                             font="Helvetica 14 bold", background="white", fg="black",  width=41, height=2)
        yenibaslık.grid(row=0, column=2)

        yeniC = str(json_veri3["Global"]["NewConfirmed"])
        yenivaka = Label(pasta, relief=GROOVE, border=3, text="YENİ VAKA : " + yeniC,
                             font="Helvetica 14 bold", background="darkcyan", fg="white",width=41, height=2)
        yenivaka.grid(row=1, column=2)

        yeniD = str(json_veri3["Global"]["NewDeaths"])
        yenivefat = Label(pasta, relief=GROOVE, border=3, text="YENİ VEFAT : " + yeniD,
                          font="Helvetica 14 bold", background="darkcyan", fg="white",width=41, height=2)
        yenivefat.grid(row=2, column=2)

        yeniR = str(json_veri3["Global"]["NewRecovered"])
        yeniyilesen = Label(pasta, relief=GROOVE, border=3, text="YENİ İYİLEŞEN : " + yeniR,
                             font="Helvetica 14 bold", background="darkcyan", fg="white",width=41, height=2)
        yeniyilesen.grid(row=3, column=2)

        dunya_veri1 = ["Onaylanan", "Vefat", "İyileşen"]
        dunya_sayı1 = [str(json_veri3["Global"]["NewConfirmed"]),str(json_veri3["Global"]["NewDeaths"]),
                       str(json_veri3["Global"]["NewRecovered"])]

        figur1 = plt.figure(figsize=(5, 4))
        ax = figur1.add_subplot(1, 1, 1)
        ax.pie(dunya_sayı1 ,labels = dunya_veri1,autopct="%1.1f%%", startangle=90,wedgeprops=dict(width=0.5))
        grafik = FigureCanvasTkAgg(figur1, pasta)
        grafik.get_tk_widget().grid(row=4, column=2)


def draw7():

    if grafikBox.get(ACTIVE) == "Toplam Tablo":

        ülke = Frame(pencere,background="darkturquoise", relief=RIDGE, border=3)
        ülke.grid(row=0, column=1)

        toplam = Label(ülke, relief=RIDGE, border=3, text="ONAYLANAN VAKA",
                       font="Helvetica 14 bold", background="darkcyan",fg="white", width=27, height=1)
        toplam.grid(row=0, column=1)
        toplambox = Listbox(ülke, width=34, height=28, font="Helvetica 13 bold", background="darkcyan", fg="white",
                            highlightcolor="darkcyan")
        toplambox.grid(row=1, column=1)

        toplam1 = Label(ülke, relief=RIDGE, border=3, text="VEFAT",
                        font="Helvetica 14 bold",background="darkcyan",fg="white", width=27, height=1)
        toplam1.grid(row=0, column=2)

        toplambox1 = Listbox(ülke, width=34, height=28, font="Helvetica 13 bold", background="darkcyan", fg="white",
                             highlightcolor="darkcyan")
        toplambox1.grid(row=1, column=2)

        toplam2 = Label(ülke, relief=RIDGE, border=3, text="İYİLEŞEN",
                        font="Helvetica 14 bold", background="darkcyan",fg="white", width=27, height=1)
        toplam2.grid(row=0, column=3)

        toplambox2 = Listbox(ülke, width=34, height=28, font="Helvetica 13 bold", background="darkcyan", fg="white",
                             highlightcolor="darkcyan")
        toplambox2.grid(row=1, column=3)

        for i in range(0, len(json_veri3["Countries"])):

            TC = str(json_veri3["Countries"][i]["TotalConfirmed"])
            toplambox.insert(END, json_veri3["Countries"][i]["Country"] + ":" + TC)


            TD = str(json_veri3["Countries"][i]["TotalDeaths"])
            toplambox1.insert(END, json_veri3["Countries"][i]["Country"] + ":" + TD)


            TR = str(json_veri3["Countries"][i]["TotalRecovered"])
            toplambox2.insert(END, json_veri3["Countries"][i]["Country"] + ":" + TR)


def draw8():

    if grafikBox.get(ACTIVE) == "Günlük Tablo":

        ülkegun = Frame(pencere,
                        background="darkturquoise",
                        relief=RIDGE,
                        border=3)
        ülkegun.grid(row=0, column=1)

        toplamgun = Label(ülkegun,
                          relief=RIDGE,
                          border=3,
                          text="YENİ ONAYLANAN",
                          font="Helvetica 14 bold",
                          background="darkcyan",
                          fg="white",
                          width=27, height=1)
        toplamgun.grid(row=0, column=1)

        toplamgunbox = Listbox(ülkegun,width=34, height=28,font="Helvetica 13 bold",
                               background="darkcyan",fg="white",highlightcolor="darkcyan")
        toplamgunbox.grid(row=1, column=1)

        toplam1gun = Label(ülkegun, relief=RIDGE, border=3, text="YENİ VEFAT",
                    font="Helvetica 14 bold", background="darkcyan", fg="white", width=27, height=1)
        toplam1gun.grid(row=0, column=2)

        toplambox1gun = Listbox(ülkegun, width=34, height=28, font="Helvetica 13 bold", background="darkcyan",
                                fg="white",highlightcolor="darkcyan")
        toplambox1gun.grid(row=1, column=2)

        toplam2gun = Label(ülkegun, relief=RIDGE, border=3, text="YENİ İYİLEŞEN",
                    font="Helvetica 14 bold", background="darkcyan", fg="white", width=27, height=1)
        toplam2gun.grid(row=0, column=3)

        toplambox2gun = Listbox(ülkegun, width=34, height=28, font="Helvetica 13 bold", background="darkcyan",
                                fg="white",highlightcolor="darkcyan")
        toplambox2gun.grid(row=1, column=3)

        for i in range(0, len(json_veri3["Countries"])):

            NC = str(json_veri3["Countries"][i]["NewConfirmed"])
            toplamgunbox.insert(END, json_veri3["Countries"][i]["Country"] + ":" + NC)

            ND = str(json_veri3["Countries"][i]["NewDeaths"])
            toplambox1gun.insert(END, json_veri3["Countries"][i]["Country"] + ":" + ND)

            NR = str(json_veri3["Countries"][i]["NewRecovered"])
            toplambox2gun.insert(END, json_veri3["Countries"][i]["Country"] + ":" + NR)


def draw9():

    if grafikBox.get(ACTIVE) == "Ülke karşılaştırma":

        slug = []

        def ülke1():
            ad = ulke1box.curselection()
            sira = int(ad[0])

            print(slug[sira])
            response = requests.get(url2 + slug[sira])
            json_veri2 = response.json()

            gun = []
            veri = []

            for i in range(0, len(json_veri2)):
                if  krsgrafbox.get(ACTIVE) == "Onaylanmış vaka":
                    veri.append(json_veri2[i]["Confirmed"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if  krsgrafbox.get(ACTIVE) == "İyileşen":
                    veri.append(json_veri2[i]["Recovered"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if krsgrafbox.get(ACTIVE) == "Aktif vaka":
                    veri.append(json_veri2[i]["Active"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if krsgrafbox.get(ACTIVE) == "Vefat":
                    veri.append(json_veri2[i]["Deaths"])
                    gun.append(i)

            figurkrs = plt.figure(figsize=(4, 3))

            data = figurkrs.add_subplot(1,1,1)
            data.plot(gun, veri)
            plt.title("1.ÜLKE")

            grafik = FigureCanvasTkAgg(figurkrs, karsılastırma1)
            grafik.get_tk_widget().grid(row = 3, column=1)

        def ülke2():
            ad = ulke2box.curselection()
            sira = int(ad[0])

            print(slug[sira])
            response = requests.get(url2 + slug[sira])
            json_veri2 = response.json()

            gun = []
            veri = []

            for i in range(0, len(json_veri2)):
                if  krsgrafbox.get(ACTIVE) == "Onaylanmış vaka":
                    veri.append(json_veri2[i]["Confirmed"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if  krsgrafbox.get(ACTIVE) == "İyileşen":
                    veri.append(json_veri2[i]["Recovered"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if krsgrafbox.get(ACTIVE) == "Aktif vaka":
                    veri.append(json_veri2[i]["Active"])
                    gun.append(i)

            for i in range(0, len(json_veri2)):
                if krsgrafbox.get(ACTIVE) == "Vefat":
                    veri.append(json_veri2[i]["Deaths"])
                    gun.append(i)

            figurkrs = plt.figure(figsize=(4, 3))

            data = figurkrs.add_subplot(1,1,1)
            data.plot(gun, veri)
            plt.title("2.ÜLKE")

            grafik = FigureCanvasTkAgg(figurkrs, karsılastırma1)
            grafik.get_tk_widget().grid(row = 3, column=2)



        for i in range(0, len(json_veri)):
                slug.append(json_veri[i]["Slug"])

        karsılastırma1 = Frame(pencere, background="darkturquoise")
        karsılastırma1.grid(row=0, column=1)

        figur1 = plt.figure(figsize=(4,3))
        ax = figur1.add_subplot(1, 1, 1)
        plt.title("1.ÜLKE")
        grafik = FigureCanvasTkAgg(figur1, karsılastırma1)
        grafik.get_tk_widget().grid(row=3, column=1)

        figur2 = plt.figure(figsize=(4, 3))
        ax = figur2.add_subplot(1, 1, 1)
        plt.title("2.ÜLKE")
        grafik = FigureCanvasTkAgg(figur2, karsılastırma1)
        grafik.get_tk_widget().grid(row=3, column=2)

        ulke1 = Label(karsılastırma1, text= "1.ÜLKE SEÇİN",relief=RIDGE, border=3,
                       font="Calibri 12 bold", background="darkcyan",fg="white",width = 51)
        ulke1.grid(row =0 , column = 1)

        ulke1box = Listbox(karsılastırma1,font="Calibri", background="darkcyan", fg="white", exportselection=0,width = 40,
                           height = 12 )
        ulke1box.grid(row =1 , column = 1)

        for i in range(0, len(json_veri)):
                ulke1box.insert(END, json_veri[i]["Country"])

        ulke2 = Label(karsılastırma1, text="2.ÜLKE SEÇİN", relief=RIDGE, border=3,
                      font="Calibri 12 bold", background="darkcyan", fg="white",width = 51)
        ulke2.grid(row=0, column=2)

        ulke2box = Listbox(karsılastırma1, font="Calibri", background="darkcyan", fg="white", exportselection=0,width = 40,
                           height=12  )
        ulke2box.grid(row=1, column=2)
        for i in range(0, len(json_veri)):
                ulke2box.insert(END, json_veri[i]["Country"])

        krsgraf = Label(karsılastırma1,text= "GRAFİK SEÇİN",relief=RIDGE, border=3,
                       font="Calibri 12 bold", background="darkcyan", fg="white", width = 20)
        krsgraf.grid(row = 0 , column = 3)

        krsgrafbox = Listbox(karsılastırma1,font="Calibri", selectmode="single", background="darkcyan", fg="white",
                             exportselection=0, height = 12)
        krsgrafbox.grid(row = 1 , column = 3)

        krsgrafbox.insert(0, "Onaylanmış vaka")
        krsgrafbox.insert(1, "İyileşen")
        krsgrafbox.insert(2, "Aktif vaka")
        krsgrafbox.insert(END, "Vefat")

        krsbuton = Button(karsılastırma1, text="Göster",command = ülke1,width= 20, relief=RIDGE, border=5,background="White",
                      fg="darkcyan",font="Calibri 10 bold")
        krsbuton.grid(row= 2, column = 1 )

        krsbuton1 = Button(karsılastırma1, text="Göster",command = ülke2,width= 20, relief=RIDGE, border=5,background="White",
                    fg="darkcyan",font="Calibri 10 bold")
        krsbuton1.grid(row= 2, column = 2 )


def drawkontrol():

    if (grafikBox.get(ACTIVE) == "Onaylanmış vaka") or (grafikBox.get(ACTIVE) == "İyileşen") or (
            grafikBox.get(ACTIVE) == "Aktif vaka") or (grafikBox.get(ACTIVE) == "Vefat"):
        draw()

    elif (grafikBox.get(ACTIVE) == "Tüm Veriler"):
        draw3()

    elif (grafikBox.get(ACTIVE) == "Günlük Tüm Veriler"):
        draw4()

    elif (grafikBox.get(ACTIVE) == "Karşılaştırma Grafiği"):
        draw5()

    elif (grafikBox.get(ACTIVE) == "Dünya Pasta Grafiği"):
        draw6()

    elif  (grafikBox.get(ACTIVE) == "Toplam Tablo"):
        draw7()

    elif (grafikBox.get(ACTIVE) == "Günlük Tablo"):
        draw8()

    elif (grafikBox.get(ACTIVE) == "Ülke karşılaştırma"):
        draw9()

    else:
        draw2()


for i in range(0, len(json_veri)):
    ulke_slug.append(json_veri[i]["Slug"])

Secenek = Frame(pencere,
                relief=GROOVE,
                border=5,
                background="darkturquoise")
Secenek.grid(row=0, column=0)

ulkeAd = Label(Secenek,
               text="Ülke Seçimi",
               background="darkturquoise",
               fg="white",
               font="Helvetica 14 bold",
               width = 15)
ulkeAd.grid(row=1, column=0)

ulkebox = Listbox(Secenek,
                  font="Calibri",
                  selectmode="single",
                  exportselection=0,
                  height=13,
                  width = 25)
ulkebox.grid(row=2, column=0)

for i in range(0, len(json_veri)):
    ulkebox.insert(END, json_veri[i]["Country"])

grafik = Label(Secenek,
               text="Grafik Seçimi",
               background="darkturquoise",
               fg="white",
               font="Helvetica 14 bold",
               width = 15)
grafik.grid(row=3, column=0)

grafikBox = Listbox(Secenek,
                    font="Calibri",
                    selectmode="single",
                    exportselection=0,
                    height=11,
                    width = 25)
grafikBox.grid(row=4, column=0)

grafikBox.insert(0, "Onaylanmış vaka")
grafikBox.insert(1, "İyileşen")
grafikBox.insert(2, "Aktif vaka")
grafikBox.insert(3, "Vefat")
grafikBox.insert(4, "Günlük Onaylanmış vaka")
grafikBox.insert(5, "Günlük İyileşen")
grafikBox.insert(6, "Günlük Aktif vaka")
grafikBox.insert(7, "Günlük Vefat")
grafikBox.insert(8, "Karşılaştırma Grafiği")
grafikBox.insert(9, "Tüm Veriler")
grafikBox.insert(10, "Günlük Tüm Veriler")
grafikBox.insert(11,"Toplam Tablo")
grafikBox.insert(12,"Günlük Tablo")
grafikBox.insert(13,"Ülke karşılaştırma")
grafikBox.insert(END, "Dünya Pasta Grafiği")

grafikButton = Button(Secenek,
                      relief=RIDGE,
                      border=5,
                      text="Göster",
                      background="White",
                      fg="darkcyan",
                      font="Helvetica 14 bold",
                      command=drawkontrol)
grafikButton.grid(row=5, column=0)

pencere.mainloop()
