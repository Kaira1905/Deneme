# 1. soru çözüm
# liste = ["345","sadas","324a","14","kemal","11safgas","243-.sad","344f"]

# for eleman in liste:
#     try:
#         eleman = int(eleman)
#         print(eleman)
#     except:
#         pass

# 2. soru çözüm
def cift_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError
    
liste = [111, 452, 66, 71, 55, 52, 12, 8]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError :
        pass