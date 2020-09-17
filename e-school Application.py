from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3 as sql
baglanti = sql.connect("data.db")
baglanti.execute("CREATE TABLE IF NOT EXISTS Ogrenciler (OgrNo,Ad,Soyad)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Dersler (DersKodu,DersAdı)")
baglanti.execute("CREATE TABLE IF NOT EXISTS Notlar (OgrNo,DersKodu,Vize,Final)")


pen = Tk()
pen.title("1191602061 Alperen KAPUSUZ")


def Ekleme():
    listbox1.insert(END, inputOgrNo.get() + ' ' +  inputAd.get() + ' ' + inputSoyad.get())
    baglanti.execute("INSERT INTO Ogrenciler VALUES(?,?,?)",
                     [inputOgrNo.get(), inputAd.get(), inputSoyad.get()])
    baglanti.commit()

def Silme():
    if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for i in range(listbox1.size(), -1, -1):
            if listbox1.select_includes(i):
                baglanti.execute("DELETE FROM Ogrenciler WHERE OgrNo=? AND Ad=? AND Soyad=?",
                                 listbox1.get(i).split(' '))
                baglanti.commit()
                listbox1.delete(i)


kutu1 = Frame(pen, relief=SUNKEN,border=9,width=50, height=50)
kutu1.grid(row=0 , column=0)


lblBAS=Label(kutu1, text="ÖĞRENCİ BİLGİSİ", font="Helvetica 14 bold")
lblBAS.grid(row=0 , column=1)

lblOgrNo = Label(kutu1 , text="OgrNo :", font="Calibri", width=7)
inputOgrNo = Entry(kutu1, font="Calibri", width=30)
lblOgrNo.grid(row=1 , column=0)
inputOgrNo.grid(row=1 , column=1)

lblAd = Label(kutu1 , text="Ad : ", font="Calibri", width=7)
inputAd = Entry(kutu1, font="Calibri",width=30)
lblAd.grid(row=2 , column=0)
inputAd.grid(row=2 , column=1)

lblSoyad = Label(kutu1 , text="Soyad :", font="Calibri", width=7)
inputSoyad = Entry(kutu1 , font="Calibri", width=30)
lblSoyad.grid(row=3 , column=0)
inputSoyad.grid(row=3 , column=1)

listbox1 = Listbox(kutu1, font="Calibri", selectmode="extended", width=30,exportselection=0)
listbox1.grid(row=5, column=1)


cmdEkle = Button(kutu1 , text="Ekle", font="Calibri", command=Ekleme)
cmdEkle.grid(row=4, column=1)

cmdSil = Button(kutu1 , text="Seçili olanları sil", font="Calibri", command=Silme)
cmdSil.grid(row=6 , column=1)


def Ekleme1():
        listbox2.insert(END, inputDersKodu.get( ) + ' ' + inputDersAdı.get( ))
        baglanti.execute("INSERT INTO Dersler VALUES(?,?)",
                         [inputDersKodu.get( ), inputDersAdı.get( )])
        baglanti.commit( )

def Silme1():
    if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
        for j in range(listbox2.size(), -1, -1):
            if listbox2.select_includes(j):
                baglanti.execute("DELETE FROM Dersler WHERE DersKodu=? AND DersAdı=?" ,
                                 listbox2.get(j).split(' ',1))
                baglanti.commit()
                listbox2.delete(j)

                
kutu2 = Frame(pen, relief=SUNKEN,border=9,width=50, height=50)
kutu2.grid(row=0 , column=2)

lblbas=Label(kutu2, text="DERSLER", font="Helvetica 14 bold")
lblbas.grid(row=0 , column=3)

lblDersKodu=Label(kutu2, text="DersKod:", font="Calibri", width=7, anchor="e")
inputDersKodu= Entry(kutu2, font="Calibri", width=30)
lblDersKodu.grid(row=1, column=2)
inputDersKodu.grid(row=1, column=3)

lblDersAdı=Label(kutu2, text="DersAd:", font="Calibri", width=7, anchor="e")
inputDersAdı= Entry(kutu2, font="Calibri", width=30)
lblDersAdı.grid(row=2, column=2)
inputDersAdı.grid(row=2, column=3)

listbox2 = Listbox(kutu2, font="Calibri", selectmode="extended", width=30,exportselection=0)
listbox2.grid(row=5, column=3)

cmdEkle1 = Button(kutu2, text="Ekle", font="Calibri", command=Ekleme1)
cmdEkle1.grid(row=4, column=3)

cmdSil1 = Button(kutu2, text="Seçili olanları sil", font="Calibri", command=Silme1)
cmdSil1.grid(row=6 , column=3)

def Ekleme2():
        listbox3.insert(END,listbox1.get(ACTIVE).split(' ')[0]+' '+listbox2.get(ACTIVE).split(' ')[0]+' '+inputVize.get()+ ' ' +inputFinal.get())
        baglanti.execute("INSERT INTO Notlar VALUES(?,?,?,?)",
                         [listbox1.get(ACTIVE).split(' ')[0], listbox2.get(ACTIVE).split(' ')[0],inputVize.get( ),inputFinal.get( )])
        baglanti.commit( )


def Silme2():
        if tkMessageBox.askyesno("UYARI", "Seçili Kayıtları silmek istediğinize emin misiniz?"):
            for k in range(listbox3.size( ), -1, -1):
                if listbox3.select_includes(k):
                    baglanti.execute("DELETE FROM Notlar WHERE OgrNo=? AND DersKodu=? AND Vize=? AND Final=?",
                                     listbox3.get(k).split(' '))
                    baglanti.commit( )
                    listbox3.delete(k)

                    
kutu3 = Frame(pen, relief=SUNKEN,border=9,width=50, height=50)
kutu3.grid(row=0 , column=4)

lblBas=Label(kutu3, text="NOTLAR", font="Helvetica 14 bold")
lblBas.grid(row=0 , column=5)

lblVize=Label(kutu3, text="VizeNot:", font="Calibri", width=7, anchor="e")
inputVize= Entry(kutu3, font="Calibri", width=30)
lblVize.grid(row=1, column=4)
inputVize.grid(row=1, column=5)

lblFinal=Label(kutu3, text="FinalNot:", font="Calibri", width=7, anchor="e")
inputFinal= Entry(kutu3, font="Calibri", width=30)
lblFinal.grid(row=2, column=4)
inputFinal.grid(row=2, column=5)

listbox3 = Listbox(kutu3, font="Calibri", selectmode="extended", width = 30)
listbox3.grid(row=5, column=5)

cmdEkle2 = Button(kutu3, text="Ekle", font="Calibri", command=Ekleme2)
cmdEkle2.grid(row=4, column=5)

cmdSil2 = Button(kutu3, text="Seçili olanları sil", font="Calibri", command=Silme2)
cmdSil2.grid(row=6 , column=5)



for kayıt in baglanti.execute("SELECT * FROM Ogrenciler"):
    listbox1.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2])
for kayıt in baglanti.execute("SELECT * FROM Dersler"):
    listbox2.insert(END, kayıt[0] + ' ' + kayıt[1] )
for kayıt in baglanti.execute("SELECT * FROM Notlar"):
    listbox3.insert(END, kayıt[0] + ' ' + kayıt[1] + ' ' + kayıt[2]+ ' ' + kayıt[3])

pen.mainloop()
