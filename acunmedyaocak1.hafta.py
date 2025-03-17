isim = input(" Adınızı girin: ")
yas = int(input(" Yaşınızı girin: "))
dogumYili = int(input(" Doğum yılınızı girin: "))

print(f"Merhaba {isim}! {yas} yaşındasın ve {dogumYili} yılında doğmuşsun.")



sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))


toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
if sayi2 != 0:
    bolum = sayi1 / sayi2
else:
    bolum = "Sayı sıfıra bölünemez."


print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
