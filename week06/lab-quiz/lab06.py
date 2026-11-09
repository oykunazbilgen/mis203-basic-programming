kulup_branslari = ("Yazılım","Tasarım","Pazarlama")
tum_ogrenciler = []

print("Kulüp Brranşları:", kulup_branslari)
print("Tüm Öğrenciler Listesi:", tum_ogrenciler)


ogrenci1 = "Ali" .strip()
ogrenci2 = "Ece".strip()
ogrenci3 = "Esma".strip()

ogrenci1 = [ogrenci1 ,["Yazılım" , "Tasarım"]]
ogrenci2 = [ogrenci2 ,["Pazarlama"]]
ogrenci3 = [ogrenci3 ,["Yazılım","Pazarlama"]]

tum_ogrenciler.append(ogrenci1)
tum_ogrenciler.append(ogrenci2)
tum_ogrenciler.append(ogrenci3)

baskan_ad = "Zeynep".strip()
baskan = [baskan_ad,["Yazılım","Tasarım","Pazarlama"]]
tum_ogrenciler.insert(0, baskan)

toplam_sayi = len(tum_ogrenciler)
print(f"Toplam Öğrenci Sayısı: {toplam_sayi}")

tum_ogrenciler.remove(ogrenci3)
print("Güncel Öğrenci Sayısı:", tum_ogrenciler)

son_cikan_ogrenci = tum_ogrenciler.pop()
son_cikan_isim = son_cikan_ogrenci[0]
print(f"Sistemden en son çıkan öğrenci: {son_cikan_isim}")

yeni_ogrenci_ad = "Burak Tan".strip()
yeni_ogrenci = [yeni_ogrenci_ad, ["Tasarım"]]
tum_ogrenciler.append(yeni_ogrenci)


sirali_kopya = sorted(tum_ogrenciler)
print("Alfabetik Sıralanmış Geçici Kopya:", sirali_kopya)
print("Orijinal Liste Değişmedi:", tum_ogrenciler)


tum_ogrenciler.sort()
print("Orijinal Liste Kalıcı Olarak Sıralanmış Hali:", tum_ogrenciler)