tkm=["tas","kagit","makas"]
tur=1
benim_puanim=0
salihin_puani=0

import random

tas=tkm[0]
kagit=tkm[1]
makas=tkm[2]

print("""TAS KAGIT MAKAS OYUNUNA
HOSGELDINIZ!""")
isim=input("isminiz:")


while tur<=10:
    tur+=1
    sec=input("secim yap:")
    bisey=random.choice(tkm)
    print("salih:", bisey)
    if sec==tas:
        if tas==bisey:
            print("ikiniz de 1 puan aldiniz")
            benim_puanim+=1
            salihin_puani+=1
        elif makas==bisey:
            print(isim,"1 puan aldi.")
            benim_puanim+=1
        else:
            print("salih 1 puan aldi.")
            salihin_puani += 1
    elif sec==kagit:
        if tas==bisey:
            print(isim,"1 puan aldi.")
            benim_puanim += 1
        elif makas==bisey:
            print("salih 1 puan aldi.")
            salihin_puani += 1
        else:
            print("ikiniz de 1 puan aldiniz")
            benim_puanim += 1
            salihin_puani += 1
    else:
        if tas==bisey:
            print("salih 1 puan aldi.")
            salihin_puani += 1
        elif kagit==bisey:
            print(isim,"1 puan aldi.")
            benim_puanim += 1
        else:
            print("ikiniz de 1 puan aldiniz")
            benim_puanim += 1
            salihin_puani += 1
print(isim,benim_puanim,"\nsalih",salihin_puani)
if benim_puanim>salihin_puani:
    print("Tebrikler kazandiniz!")
elif benim_puanim<salihin_puani:
    print("salih kazandi!")
else:
    print("Berabere kaldiniz!")
input()