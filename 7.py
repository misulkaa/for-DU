#Naprogramuj funkciu, ktorá vypíše všetky čísla od 1-N, ktoré sú deliteľné troma.

N = int(input(" zadaj N  "))

for i in range(1, N+1):
    if i % 3 == 0:
        print(i)
        