
for i in range(1, 101):
    print(i, end=" ")
print("\n")



for i in range(2, 101, 2):
    print(i, end=" ")
print("\n")



sayi = int(input("Faktöriyelini hesaplamak için bir sayı girin: "))
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")





def asal_mi(n):
    if n < 2:
        return False
    for a in range(2, int(n**0.5) + 1):  
        if n % a == 0:
            return False
    return True

print("1'den 100'e kadar olan asal sayılar:")
for i in range(1, 101):
    if asal_mi(i):
        print(i, end=" ")
