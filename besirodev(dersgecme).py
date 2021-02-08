dersler=["matematik","dil ve anlatim","cografya","edebiyat"]


print("VIZE-FINAL NOTLARI DEGERLENDIRMESI")

ad=input("adiniz:")
soyad=input("soyadiniz:")
no=int(input("numaraniz:"))

print("vize notlariniz:")

mtv=float(input("matematik:"))
dav=float(input("dil ve anlatim:"))
cv=float(input("cografya:"))
ev=float(input("edebiyat:"))

vize=int(mtv+dav+cv+ev)

print("vize notunuz:",round(vize*0.4))

print("final notlariniz:")

mtf=float(input("matematik:"))
daf=float(input("dil ve anlatim:"))
cf=float(input("cografya:"))
ef=float(input("edebiyat:"))

final=int(mtf+daf+cf+ef)

print("final notunuz:",round(final*0.6))

ortalama=(vize*0.4)+(final*0.6)

print("ad:{}\nsoyad:{}\nnumara:{}\nvize:{}\nfinal:{}\nortalama:{}".format(ad,soyad,no,vize,final,ortalama))

if ortalama<40:
    print("KALDI!")
else:
    print("GECTI!")
input()
