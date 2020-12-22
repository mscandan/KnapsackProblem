# Mehmet Selçuk Candan B171210104 selcuk.candan@ogr.sakarya.edu.tr
# Serhat Burak Altinsoy B161210010 serhat.altinsoy@ogr.sakarya.edu.tr

"""
    Knapsack Problemi
    Sırt çantası problemi (İngilizce: "knapsack problem") bir klasik yöneylem araştırması ve matematiksel olarak "kombinatorik optimizasyon" problemidir.
    Çözüm algoritması bakımından sırt çantası problemi en ünlü NP-hard problemleri arasındadır.
    Sırt çantası problemi"nin tanımlanması için şu notasyon kullanılmaktadır: İsimleri 1 ile n arasında sayı ile ifade edilen n değişik madde bulunur.
    Her bir madde i için değerinin vi ve ağırlığının wi olduğu bilinmektedir. Genel olarak her bir değer ve her bir ağırlık negatif olamazlar.
    Çanta içinde taşınabilecek tüm maddelerin toplam ağırlığının en çok W olup, bunun bir üst sınır olup aşılamayacağı bilinir.
    https://tr.wikipedia.org/wiki/S%C4%B1rt_%C3%A7antas%C4%B1_problemi
"""
from itertools import combinations
import sys
import os
import tkinter as tk
from tkinter.constants import CENTER

import tkinter.messagebox as messagebox


def degerleriDondur():
    """
    Hesapla butonu calistiginda kullanicinin girdigi derlerin alinmasi ve ekranda hesaplatilmasi
    """
    # kullanicinin deger girip girmedigini kontrol eder eger girmediyse ekrana uyari mesaji verir
    if e1.get() == "" or e2.get() == "" or e3.get == "" or e2.get() == "Örnek = 1,2,3" or e3.get() == "Örnek = 1,2,3":
        messagebox.showwarning("UYARI", "Kutular Boş Bırakılamaz !!!")
    #degilse islemler devam eder
    else:
        # Kullanici bir hata ile karsilastiginda hatayi yakalamak icin try except yapisi kullanildi 
        try:
            kapasitePure = int(
                e1.get())  # kullaninin girdigi kapasite degerinin alinmasi
            # kullanicinin girdigi agirlik degerlerinin alinmasi ve ',' karakterine gore bolunerek bir diziye atanmasi
            agirliklarPure = e2.get().split(",")
            # kullanicinin girdigi value degerlerinin alinmasi ve ',' karakterine gore bolunerek bir diziye atanmasi
            valueDegerleriPure = e3.get().split(",")
            # Kullanicidan alinan string degerlerin kullanilabilmesi icin int'e cevrilmesi 
            agirliklarInt = []
            valueInt = []
            for i in agirliklarPure:
                agirliklarInt.append(int(i))
            for i in valueDegerleriPure:
                valueInt.append(int(i))

            tumKombinasyonlar = everyPossibleCombination(agirliklarInt, kapasitePure)
            optimumKombinasyonIndex = combIndexBul(tumKombinasyonlar, agirliklarInt)
            optimumSonuc = maxValue(optimumKombinasyonIndex, valueInt)
            # value degerleri ile agirlik degerleri sayisi esit degilse ekrana uyari mesaji verir eger esitse sonucu ekrana yazdirir
            if len(agirliklarInt) == len(valueInt):
                outputLabel.config(text="Sonuç = " + str(optimumSonuc),
                            bg = "green",
                            fg  = "yellow")
            else:
                messagebox.showwarning("UYARI", "Ağırlık ve value değerleri eşit sayıda olmalıdır !!!")
        # Kullanici Entry'lere istenilen disinda bir deger girdiginde hata mesaji verir
        except ValueError:
            messagebox.showerror("HATA", "Hatalı Kullanıcı Girişi !!!\nKutuların yanında belirtilen şekilde kutuları doldurunuz !!!")
        # Kullanici deger sayilarini ayni sayida vermediginde ekrana hata mesaji verir
        except IndexError:
            messagebox.showerror("HATA", "Hatalı Kullanıcı Girişi !!\nAğırlık ve value değerleri eşit sayıda olmalıdır !!!")



def kullanicidanDegerAta(_kapasite, _agirliklar, _valueInt):
    """
    Kullanicidan programin calismasi icin gerekli olan degerleri alan ve aldigi degerleri donduren fonksiyon
    """
    sirtCantasiKapasite = _kapasite
    esyaAgirlik = _agirliklar
    esyaValue = _valueInt
    return sirtCantasiKapasite, esyaAgirlik, esyaValue


def everyPossibleCombination(agirlik, kapasite):
    """
    Kullanicidan alinan agirliklara ait tum kombinasyonlari alir ve kapasiteye uygun olmayanlari filtreleyerek
    tum olasi kombinasyonlari return eder
    """
    combs = sum([list(map(list, combinations(agirlik, i)))
                 for i in range(len(agirlik) + 1)], [])
    # tum kombinasyonlarda ilk eleman [] olarak gelmektedir o eleman diziden atilir
    combs.pop(0)
    # tum olasiklarin icerisinde gezerek agirlik toplamlari max kapasiteden kucuk veya esit olanlari mumkun olanlar dizine ekler
    possCombs = []
    for i in range(0, len(combs)):
        if toplamAgirlikBul(combs[i]) <= kapasite:
            possCombs.append(combs[i])
    return possCombs


def combIndexBul(combs, weight):
    """
    Gecerli tum kombinasyonlari bulunan agirlik degerlerinin kullanicidan alinan agirlik degerleri dizisinde sahip oldugu indexleri bulur
    """
    indexler = combs
    for i in range(0, len(combs)):
        for j in range(0, len(combs[i])):
            for k in range(0, len(weight)):
                # Eger kombinasyonlar icerisinde bulunan agirlik orijinal agirlik dizisinde bulunan bir elemanin agirligina esitse o elemanin agirliklar dizisindeki indexini dondurur
                if combs[i][j] == weight[k]:
                    indexler[i][j] = k
    return indexler


def maxValue(combIndex, value):
    """
    Mumkun olan tum kombinasyonlar arasinda en fazla value sahip olan kombinasyonu ve value degerini dondurur
    """
    values = []
    for i in combIndex:
        total = combValue(i, value)
        values.append(total)
    # Tum value degerleri arasindan en buyuk degeri getirir
    optValue = 0
    for i in range(0, len(values)):
        if values[i] > optValue:
            optValue = values[i]
    return optValue


def combValue(comb, value):
    """
    Bir kombinasyonun sahip oldugu value degerini dondurur
    """
    total = 0
    for i in comb:
        total = total + value[i]
    return total


def toplamAgirlikBul(comb):
    """
    Bir kombinasyonun sahip oldugu toplam agirlik degerini dondurur
    """
    toplam = 0
    if len(comb) == 1:
        toplam = comb[0]
        return toplam
    else:
        for i in range(0, len(comb)):
            toplam = toplam + int(comb[i])
        return toplam

"""
GUI tasarimi
"""
if os.environ.get('DISPLAY', '') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')
master = tk.Tk()
#pencere basligimizi burada belirtiyoruz
master.title("Knapsack Algoritması")
#pencere ilk acildigindaki boyutunu belirtiyoruz ve
# + ile ekledigimiz ise pencere ilk acildiginda konumunu belirtiyoruz
master.geometry("570x250+250+250")
#pencerimizin boyutunu sabitlemek icin kullanildi
master.resizable(0, 0)
#labeller olusturuluyor tasarimi ve konumu belirlendi
tk.Label(master,text = "Pozitif sadece bir sayısal değer giriniz !!! ",
                fg = "red",
                font = ("Open Sans", "10", "bold")).grid(row = 1,column = 0)

tk.Label(master,text = "Aralarını virgül ile ayırarak pozitif değerleri yazınız !!! ",
                fg = "red",
                font = ("Open Sans", "10", "bold")).grid(row = 3,column = 0)

tk.Label(master,text = "Aralarini virgul ile ayirarak pozitif değerleri yazınız !!!",
                fg = "red",
                font = ("Open Sans", "10", "bold")).grid(row = 5,column = 0)
tk.Label(master, 
        text="Sırt çantasi kapasitesi",
        fg= "green",
        bg = "yellow",
        justify = "center",
        width = 18,
        height = 1,
        font = ("Open Sans", "12", "italic")
        ).grid(row=0,column = 1)
tk.Label(master, text="Ağırlıklar",
        fg= "green",
        bg = "yellow",
        justify = "center",
        width = 18,
        height = 1,
        font = ("Open Sans", "12", "italic")
        ).grid(row=2,column = 1)
tk.Label(master, text="Value Değerleri",
        fg= "green",
        bg = "yellow",
        justify = "center",
        width = 18,
        height = 1,
        font = ("Open Sans", "12", "italic")).grid(row=4,column = 1)
outputLabel = tk.Label(master, text="Sonuç",    
                       bg = "yellow",
                       fg  = "green",
                       width = 30,
                       height = 2,
                       font = ("Open Sans", "15", "bold"))
outputLabel.grid(row=9, column=0)
outputLabel.config(anchor=CENTER)
# Kullanicinin girdi verecegi entryler yani kutucuklar olusturuldu
e1 = tk.Entry(master, width = 20,font = ("Open Sans", "11", "italic"))
e2 = tk.Entry(master,width =20,font = ("Open Sans", "11", "italic"))
e3 = tk.Entry(master,width = 20,font = ("Open Sans", "11", "italic"))
# Kutularin ici program acildiginda asagida verilen string ifade ile acilacaktir
e2.insert(0, "Örnek = 1,2,3")
e3.insert(1, "Örnek = 1,2,3")
# Kutularin pencere uzerindeki konumlari ayarlandi
e1.grid(row=1, column=1)
e2.grid(row=3, column=1)
e3.grid(row=5, column=1)
# Buton olusturuldu tasarimi duzenlendi ve tiklandiginda degerleriDondur fonksiyonunu calistirir
tk.Button(master,
          text='Hesapla', command=degerleriDondur, 
          bg = "pink",
          fg = "black",
          width = 15,
          height = 1,
          font = ("Open Sans", "11", "normal")).grid(row=6,
                                                        column=1,
                                                        sticky=tk.W,
                                                        pady=4,
                                                        padx=30)
tk.mainloop()
