# gömülü fonksiyonlar - built-in functions
# user defined - kullanıcı tanımlı fonksiyonlar

# # parametresiz - void functions
# def selamla():
#     # fonksiyon tanımlama - function definition
#     print("Selamlar arkadaşlar...")
#     print("Nasılsınız?")

# print(type(selamla))
# kullanım kısmı - function calling
# selamla()
# selamla()
# selamla()
# selamla()
# selamla()

# def selamla(isim):
#     # fonksiyon tanımlama - function definition
#     print("Selam ", isim)
#     print("Nasılsınız?")

# selamla("ayşe")

# def toplama(a,b,c):
#     print("Sayıların toplamları = ",a+b+c)

# toplama(10,20,30)

# def faktoriyel(sayi):
#     faktoriyel = 1
#     # 6! = 6 * 5 * 4 * 3 * 2 * 1
#     if sayi == 0 or sayi == 1:
#         print("Faktoriyel : ",faktoriyel)
#     else:
#         while sayi > 1:
#             faktoriyel *= sayi
#             sayi -= 1
#         print("Faktoriyel : ",faktoriyel)

# faktoriyel(6)


# def selamla(isim = "İsimsiz"):
#     # fonksiyon tanımlama - function definition
#     print("Selam ", isim)
#     print("Nasılsınız?")

# selamla()

# def bilgileriGoster(ad="Bilgi Yok",soyad="Bilgi Yok",numara="Bilgi Yok"):
#     print("Ad:",ad," Soyad:",soyad," Numara:",numara)

# bilgileriGoster(ad="Selçuk",soyad="Veli",numara=1375)

# print(1,2,3,sep=10)

# esnek sayıda değerler - yıldızlı parametleri

def toplama(*parametreler):
    toplam = 0
    for i in parametreler:
        toplam += i
    print(toplam)

toplama(1,2,3,1,111,11,22)