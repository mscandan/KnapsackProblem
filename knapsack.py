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


def valueVeAgirlikYazdir(value, agirlik):
    """
    Kullanicidan alinan esyalara ait value ve agirlik degerlerini ekrana yazdiran fonksiyon
    """
    # print(chr(27) + "[2J")  # Terminal ekranini temizler
    for i in range(0, len(value)):
        print(i+1, ". esyanin agirlik degeri = ", agirlik[i])
        print(i+1, ". esyanin value degeri = ", value[i], "\n")


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
    total = 0
    for i in comb:
        total = total + value[i]
    return total


def toplamAgirlikBul(comb):
    toplam = 0
    if len(comb) is 1:
        toplam = comb[0]
        return toplam
    else:
        for i in range(0, len(comb)):
            toplam = toplam + int(comb[i])
        return toplam


def showResults(optCombIndex, optValue):
    print("Optimum value =", optValue)
    print("Optimum comb index =", optCombIndex)


    # Program baslar
if __name__ == "__main__":
    # Kullanicidan alinan degerlerin alinmasi ve daha sonra kullanmak uzere degiskenlere atanmasi
    kapasite, agirlik, degerler, esyaSayisi = kullanicidanDegerAl()
    tumKombinasyonlar = everyPossibleCombination(agirlik, kapasite)
    optimumKombinasyonIndex = combIndexBul(tumKombinasyonlar, agirlik)
    optimumSonuc = maxValue(optimumKombinasyonIndex, degerler)
    print("Optimum sonuc =", optimumSonuc)
