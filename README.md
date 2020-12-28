# Optimizasyon Dersi Proje Odevi Knapsack Algoritmasi

### Hazirlayanlar
    - Mehmet Selcuk Candan 
    - Serhat Burak Altinsoy 

### Knapsack problemi nedir
    Knapsack Problemi
    Sırt çantası problemi (İngilizce: "knapsack problem") bir klasik yöneylem araştırması ve matematiksel olarak "kombinatorik optimizasyon" problemidir.
    Çözüm algoritması bakımından sırt çantası problemi en ünlü NP-hard problemleri arasındadır.
    Sırt çantası problemi"nin tanımlanması için şu notasyon kullanılmaktadır: İsimleri 1 ile n arasında sayı ile ifade edilen n değişik madde bulunur.
    Her bir madde i için değerinin vi ve ağırlığının wi olduğu bilinmektedir. Genel olarak her bir değer ve her bir ağırlık negatif olamazlar.
    Çanta içinde taşınabilecek tüm maddelerin toplam ağırlığının en çok W olup, bunun bir üst sınır olup aşılamayacağı bilinir.
    [Wikipedia](https://tr.wikipedia.org/wiki/S%C4%B1rt_%C3%A7antas%C4%B1_problemi)
    
### Projede kullanilan cozum yontemi
    Internet uzerinde yer alan recursive ve brute-force yontemi kullanmamak icin bir baska yontem gelistirdik.
    Gelistirilen projede kullanicidan alinan agirlik ogelerine bagli tum kombinasyonlar bulunarak max knapsack kapasitesine gore filtrelenir.
    Filtreleme sonucu elimizde kalan kombinasyonlar uzerinden tek tek deger hesabi yapilir ve max deger kullaniciya dondurulur.
    GUI icin Tkinter kullanilmistir.
    Cok buyuk verilerle calistiginiz zaman yavaslama olabilir.
    Programin hata vermemesi icin gereken error handling yapilmistir.