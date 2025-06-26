# # kalıtım - inheritance

# class Calisan:
#     def __init__(self, isim, soyisim, maas, departman):
#         print("Çalışan sınıfının init fonksiyonu çalıştı.")
#         self.isim = isim
#         self.soyisim = soyisim
#         self.maas = maas
#         self.departman = departman
    
#     def bilgileriGoster(self):
#         print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı.")
#         print(f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nMaas: {self.maas}\nDepartman: {self.departman}")

#     def departman_degistir(self, yeni_departman):
#         print("Çalışan sınıfının departman değiştir fonksyionu çalıştı.")
#         self.departman = yeni_departman

# class Yonetici(Calisan):
#     def zam_yap(self, zam_miktari):
#         print("Maaşa zam yapılıyor...")
#         self.maas += zam_miktari

# # object - instance - instantiate etmek - obje - nesne
# yonetici1 = Yonetici("Mehmet","Demir",500000,"IK")

# yonetici1.bilgileriGoster()
# yonetici1.zam_yap(88000)
# yonetici1.bilgileriGoster()

# # yonetici1.departman_degistir("Yazılım")

# # yonetici1.bilgileriGoster()

# # print(dir(yonetici1))

# # # overriding (iptal etme) - override etmek

class Calisan:
    def __init__(self, isim, soyisim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu çalıştı.")
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman
    
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı.")
        print(f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nMaas: {self.maas}\nDepartman: {self.departman}")

    def departman_degistir(self, yeni_departman):
        print("Çalışan sınıfının departman değiştir fonksyionu çalıştı.")
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, departman, sorumlu_kisi_sayisi):
        # overriding
        print("Yönetici sınıfının init fonksiyonu")
        super().__init__(isim,soyisim,maas,departman)
        self.sorumlu_kisi_sayisi = sorumlu_kisi_sayisi

    def zam_yap(self, zam_miktari):
        print("Maaşa zam yapılıyor...")
        self.maas += zam_miktari

    def bilgileriGoster(self):
        # overriding
        print("Yönetici Class'ının bilgileri göster fonksiyonu çalışıyor.")
        print(f"Yönetici İsim: {self.isim}\nYönetici Soyisim: {self.soyisim}\nMaas: {self.maas}\nDepartman: {self.departman}")

# object - instance - instantiate etmek - obje - nesne
yonetici1 = Yonetici("Mehmet","Demir",500000,"IK", 10)

yonetici1.bilgileriGoster()