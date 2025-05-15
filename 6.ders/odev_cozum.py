# Çözüm 1
# boy = float(input("Boyunuzu giriniz: "))
# kilo = int(input("Kilonuzu giriniz: "))

# bki = kilo / (boy * boy)
# print(bki)

# if bki < 18.5:
#     print("Zayıf kilolu kategorisinde yer alıyorsunuz")
# elif bki < 25:
#     print("Normal kilolu kategorisinde yer alıyorsunuz")
# elif bki < 30:
#     print("Fazla kilolu kategorisinde yer alıyorsunuz")
# else:
#     print("Obez kategorisinde yer alıyorsunuz")

# Çözüm 2
# sayi1 = int(input("Birinci sayıyı giriniz: "))
# sayi2 = int(input("İkinci sayıyı giriniz: "))
# sayi3 = int(input("üçüncü sayıyı giriniz: "))

# if sayi1 >= sayi2 and sayi1 >= sayi3:
#     print("En büyük sayı: ",sayi1)
# elif sayi2 > sayi1 and sayi2 >= sayi3:
#     print("En büyük sayi: ",sayi2)
# else:
#     print("En büyük sayı: ",sayi3)

# Çözüm 3
# vize1 = int(input("Birinci vize notunuzu giriniz: "))
# vize2 = int(input("İkinci vize notunuzu giriniz: "))
# final1 = int(input("Final notunuzu giriniz: "))

# genel_ort = vize1 * 30 / 100 + vize2 * 30 / 100 + final1 * 40 / 100

# print("Genel Ortalama: ",genel_ort)

# if genel_ort >= 90:
#     print("AA")
# elif genel_ort >= 85:
#     print("BA")
# elif genel_ort >= 80:
#     print("BB")
# elif genel_ort >= 75:
#     print("CB") 
# elif genel_ort >= 70:
#     print("CC")
# elif genel_ort >= 65:
#     print("DC")
# elif genel_ort >= 60:
#     print("DD")
# elif genel_ort >= 55:
#     print("FD")  
# elif genel_ort < 55:
#     print("FF")  

# Çözüm 4
sekil = input("Hangi şeklin tipini öğrenmek istiyorsunuz(üçgem, dörtgen): ")
print(sekil)

if sekil == "dörtgen":
    print("Lütfen kenarları sırasıyla giriniz!")
    a = int(input("Kenar-1: "))
    b = int(input("Kenar-2: "))
    c = int(input("Kenar-3: "))
    d = int(input("Kenar-4: "))
    if a == b and a == c and a == d:
        print("Bu şekil Kare'dir")
    elif a == c and b == d:
        print("Bu şekil Dikdörtgen'dir")
    else:
        print("Bu şekil normal bir dörtgendir.")
elif sekil == "üçgen":
    a = int(input("Kenar-1: "))
    b = int(input("Kenar-2: "))
    c = int(input("Kenar-3: "))
    if abs(b-c) < a and b+c > a and abs(a-c) < b and a+c > b and abs(a-b) < c and a+b > c:
        if a == b and a == c:
            print("Bu üçgen bir eşkenar üçgendir.")
        elif a == b or a == c or b == c:
            print("Bu üçgen bir ikizkenar üçgendir.")
        else:
            print("Bu üçgen bir çeşitkenar üçgendir.")
    else:
        print("Bu kenarlar ile üçgen çizilemez")
else:
    print("Geçersiz şekil girdiniz.")