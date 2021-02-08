boy=float(input('boyunuz(m):'))
kilo=float(input('kilonuz(kg):'))
indeks=kilo/(boy*boy)
if indeks<10:
    print(round(indeks),"zayifsiniz")
elif 10<=indeks<25:
    print(round(indeks),"kilonuz normal")
elif 25<=indeks<30:
    print(round(indeks),'fazla kilolusunuz')
elif 30<=indeks<40:
    print(round(indeks),"obezsiniz")
else:
    print(round(indeks),"asiri sismansiniz")
input()



