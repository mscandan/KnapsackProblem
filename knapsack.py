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


def knapsack(kapasite, agirlik, value, esyaSayisi):
    """
    Sirt cantasinda tasinabilecek maksimum degeri dondurur
    """
    # Eger koyulacak esya veya kapasite kalmamissa program 0 dondurur
    if esyaSayisi == 0 or kapasite == 0:
        return 0
    # Eger eklenecek olan esyanin agirligi kapasiteden buyukse sonraki esyaya gecilir
    if(agirlik[esyaSayisi - 1] > kapasite):
        return knapsack(kapasite, agirlik, value, esyaSayisi - 1)
    # Esya eklenecek durumda ise esyayi ekler ve sonraki esyaya gecer ya da eklemeden sonraki esyaya gecer karar verme hangi ikisi maksimumsa o sekilde olur
    else:
        return max(value[esyaSayisi - 1] + knapsack(kapasite - agirlik[esyaSayisi - 1], agirlik, value, esyaSayisi - 1), knapsack(kapasite, agirlik, value, esyaSayisi-1))


def everyPossibleCombination():
    """
    Kullanicidan alinan agirliklara ait tum kombinasyonlari alir ve kapasiteye uygun olmayanlari filtreleyerek 
    tum olasi kombinasyonlari return eder
    """
    agirlik = [10, 20, 30, 40, 50]
    kapasite = 60
    combs = sum([list(map(list, combinations(agirlik, i)))
                 for i in range(len(agirlik) + 1)], [])
    # tum kombinasyonlarda ilk eleman [] olarak gelmektedir o eleman diziden atilir
    combs.pop(0)
    # tum olasiklarin icerisinde gezerek agirlik toplamlari max kapasiteden kucuk veya esit olanlari mumkun olanlar dizine ekler
    possCombs = []
    for i in range(0, len(combs)):
        if toplamAgirlikBul(combs[i]) <= kapasite:
            possCombs.append(combs[i])
    for i in possCombs:
        print(i)
    return possCombs


def toplamAgirlikBul(comb):
    toplam = 0
    if len(comb) is 1:
        toplam = comb[0]
        return toplam
    else:
        for i in range(0, len(comb)):
            toplam = toplam + int(comb[i])
        return toplam


def testCase():
    value = [60, 100, 120]
    agirlik = [10, 20, 30]
    kapasite = 50
    esyaSayisi = len(value)
    print(knapsack(kapasite, agirlik, value, esyaSayisi))

    # Program baslar
if __name__ == "__main__":
    # Test Case
    print("Test Case -> 1")
    print("Every possible combination -> 2")
    isTestCase = int(input("Secim = "))
    if isTestCase is 1:
        testCase()
    elif isTestCase is 2:
        everyPossibleCombination()
    else:
        # Kullanicidan alinan degerlerin alinmasi ve daha sonra kullanmak uzere degiskenlere atanmasi
        kapasite, agirlik, value, esyaSayisi = kullanicidanDegerAl()
        print(knapsack(kapasite, agirlik, value, esyaSayisi))
        valueVeAgirlikYazdir(value, agirlik)
