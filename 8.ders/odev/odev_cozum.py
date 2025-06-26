# 1. soru çözümü
# sayi = int(input("Lütfen bir sayı giriniz: "))

# i = 1

# toplam = 0
# while i < sayi:
#     if sayi % i == 0:
#         # pozitif tam bölenleri
#         toplam += i
#     i += 1

# if toplam == sayi:
#     print(f"{sayi} mükemmel bir sayıdır.")
# else:
#     print(f"{sayi} mükemmel değildir.")

# 2. soru
# sayi = input("Bir sayı giriniz: ")
# basamak_sayisi = len(sayi)
# sayi = int(sayi)
# toplam = 0
# basamak = 0
# gecici_sayi = sayi

# while gecici_sayi > 0 :
#     # 12 % 10 = 2
#     basamak = gecici_sayi % 10
#     toplam += basamak ** basamak_sayisi
#     # gecici_sayi = 354 // 10  = 35
#     gecici_sayi //= 10

# if toplam == sayi:
#     print(f"{sayi} bir armstrong sayıdır.")
# else:
#     print(f"{sayi} bir armstrong sayısı değildir.")

# 3. soru çözümü
# for i in range(1,11):
#     print("*******************")
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j}")
    
# # 4. soru çözümü
# toplam = 0

# while True:
#     sayi = input("Lütfen bir sayı giriniz (Çıkmak için q'ya basınız): ")
#     if sayi == "q":
#         print("Girdiğiniz sayıların toplamı = ",toplam)
#         break
#     toplam += int(sayi)

# 5. soru çözüm
# for i in range(1,101):
#     if i % 3 != 0:
#         continue
#     print(i)

# 6.soru çözümü
liste = [i for i in range(1,101) if i % 2 == 0]
print(liste)