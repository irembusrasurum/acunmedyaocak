
sayilar = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)




toplam = sum(sayilar)
ortalama = toplam / len(sayilar)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

print(f"Toplam: {toplam}, Ortalama: {ortalama}, En büyük: {en_buyuk}, En küçük: {en_kucuk}")




kelimeler = []
for i in range(5):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelimeler.append(kelime)

kelimeler.reverse()
print("Ters sıralanmış liste:", kelimeler)




tekrarli_liste = [1, 2, 3, 2, 4, 5, 1, 6, 4]
benzersiz_liste = list(set(tekrarli_liste))

print("Tekrar eden elemanlar kaldırıldı:", benzersiz_liste)
