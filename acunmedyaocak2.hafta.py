
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")





harfNotu = int(input("Notunuzu girin: "))
if 90 <= harfNotu <= 100:
    print("Harf notunuz: A")
elif 80 <= harfNotu <= 89:
    print("Harf notunuz: B")
elif 70 <= harfNotu <= 79:
    print("Harf notunuz: C")
elif 60 <= harfNotu <= 69:
    print("Harf notunuz: D")
else:
    print("Harf notunuz: F")





yas = int(input("Yaşınızı girin: "))
if 0 <= yas <= 12:
    print("Yaş grubunuz: Çocuk")
elif 13 <= yas <= 19:
    print("Yaş grubunuz: Genç")
elif 20 <= yas <= 59:
    print("Yaş grubunuz: Yetişkin")
else:
    print("Yaş grubunuz: Yaşlı")
