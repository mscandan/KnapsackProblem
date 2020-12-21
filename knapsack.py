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

__DEBUG__ = False  # test-case yapiliyor mu


def degerleriDondur():
    print("annen nerede")


"""
GUI tasarimi
"""
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
master = tk.Tk()
tk.Label(master, text="Sirt cantasi kapasitesi").grid(row=0)
tk.Label(master, text="Agirliklar").grid(row=1)
tk.Label(master, text="Value Degerleri").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
tk.Button(master,
          text='Hesapla', command=degerleriDondur).grid(row=3,
                                                        column=1,
                                                        sticky=tk.W,
                                                        pady=4)
tk.mainloop()


def kullanicidanDegerAl():
    """
    Kullanicidan programin calismasi icin gerekli olan degerleri alan ve aldigi degerleri donduren fonksiyon
    """
    # Esya sayisinin alinmasi ve kontrol edilmesi
    esyaSayisi = int(input("Kac esya olacagini giriniz: "))
    while esyaSayisi <= 0:
        print("Hatali sayi girdiniz esya sayisi negatif veya sifir olamaz")
        esyaSayisi = int(input("Kac esya olacagini giriniz: "))
    # Esya sayisinin alinmasi ve kontrol edilmesi tamamlandi
    # Sirt cantasi kapasitesinin alinmasi ve kontrol edilmesi
    sirtCantasiKapasite = int(input("Sirt cantasi kapasitesini giriniz: "))
    while sirtCantasiKapasite <= 0:
        print("Hatali deger girdiniz sirt cantasi kapasitesi negatif veya sifir olamaz")
        sirtCantasiKapasite = int(input("Sirt cantasi kapasitesini giriniz: "))
    # Sirt cantasi kapasitesinin alinmasi ve kontrol edilmesi tamamlandi
    # Girdilerin alinmasi
    girdiSayac = 0
    esyaAgirlik = []
    esyaValue = []
    while girdiSayac < esyaSayisi:
        print(girdiSayac + 1, ". esya icin agirlik ve value degerlerini giriniz")
        # Esyanin agirlik degerinin alinmasi ve kontrolu
        esyaAgirlik.append(int(
            input("Agirlik degerini giriniz: ")))
        while esyaAgirlik[girdiSayac] <= 0:
            print("Hatali deger girdiniz agirlik degeri negatif veya sifir olamaz")
            esyaAgirlik[girdiSayac] = int(
                input("Agirlik degerini giriniz: "))
        # Esyanin agirlik degerinin alinmasi ve kontrolu tamamlandi
        # Esyanin value degerinin alinmasi ve kontrolu
        esyaValue.append(int(
            input("Value degerini giriniz: ")))
        while esyaValue[girdiSayac] <= 0:
            print("Hatali deger girdiniz value degeri negatif veya sifir olamaz")
            esyaValue[girdiSayac] = int(
                input("Value degerini giriniz: "))
        # Esyanin value degerinin alinmasi ve kontrolu tamamlandi
        girdiSayac = girdiSayac + 1
    # Girdilerin alinmasi tamamlandi
    return sirtCantasiKapasite, esyaAgirlik, esyaValue, esyaSayisi


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


    # Program baslar
if __name__ == "__main__":
    if(__DEBUG__):
        # Kullanicidan alinan degerlerin alinmasi ve daha sonra kullanmak uzere degiskenlere atanmasi
        kapasite, agirlik, degerler, esyaSayisi = kullanicidanDegerAl()
        tumKombinasyonlar = everyPossibleCombination(agirlik, kapasite)
        optimumKombinasyonIndex = combIndexBul(tumKombinasyonlar, agirlik)
        optimumSonuc = maxValue(optimumKombinasyonIndex, degerler)
        print("Optimum sonuc =", optimumSonuc)
