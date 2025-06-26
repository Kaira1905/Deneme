# Object Oriented Programming - Nesne Yönelimli (Tabanlı) Programla

# liste = [1,2,3,4,5]

# liste.append(6)
# print(liste)
# print(type(liste))

# sozluk = dict()
# print(type(sozluk))

# print(type((1,2,3,4)))

# def toplama(a,b):
#     return a+b

# print(type(toplama))

# sınıf - class

# class Araba:
#     model = "Renault Megane"
#     renk = "Kırmızı"
#     beygir_gucu = 110
#     silindir = 4

# araba1 = Araba()
# # print(type(araba1))
# print("Araba1 özellikleri")
# print(araba1.model)
# print(araba1.renk)
# print(araba1.beygir_gucu)
# print(araba1.silindir)

# araba2 = Araba()
# print("Araba2 özellikleri")
# print(araba2.model)
# print(araba2.renk)
# print(araba2.beygir_gucu)
# print(araba2.silindir)

# print(Araba.renk)

# print(dir(Araba))

# class Araba:
#     def __init__(self, model = 'Bilgi Yok', renk = 'Bilgi Yok', beygir_gucu = 'Bilgi Yok', silindir = 'Bilgi Yok'):
#         # constructor - yapıcı - yapılandırıc metod
#         print("init fonksiyonu çalıştı.")
#         # özellikler - attribute
#         self.model = model
#         self.renk = renk
#         self.beygir_gucu = beygir_gucu
#         self.silindir = silindir

# araba1 = Araba("Subaru İmpreza", 'Yeşil', 110, 4)

# araba2 = Araba("Honda Civic", 'Mavi', 120, 4)

# araba3 = Araba(beygir_gucu = 85, renk = 'siyah')

# print(araba3.model)
# print(araba3.renk)
# print(araba3.beygir_gucu)
# print(araba3.silindir)

class Yazilimci:
    def __init__(self, isim, soyisim, numara, maas, diller):
        # attributes - özellik
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    
    # methods
    def bilgileriGoster(self):
        print(f""" 
            Çalışan Bilgileri:
              
            İsim: {self.isim}
            
            Soyisim: {self.soyisim}

            Şirket Numarası: {self.numara}

            Maaş: {self.maas}

            Bildiği programlama dilleri: {self.diller}
        """)

yazilimci1 = Yazilimci("Ali", "Veli", 1375, 100000, ["Python","Javascript","C"])

yazilimci2 = Yazilimci("Ayşe","Fatma", 111, 110000, ["Python","Go","Ruby","SQL"])

yazilimci1.bilgileriGoster()

yazilimci2.bilgileriGoster()

# print("Yazılımcı 1 bilgileri:")
# print(yazilimci1.isim)
# print(yazilimci1.soyisim)
# print(yazilimci1.numara)
# print(yazilimci1.maas)
# print(yazilimci1.diller)

# print("Yazılımcı 2 bilgileri:")
# print(yazilimci2.isim)
# print(yazilimci2.soyisim)
# print(yazilimci2.numara)
# print(yazilimci2.maas)
# print(yazilimci2.diller)