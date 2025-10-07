#11. Naprogramuj funkciu, ktorá vypíše všetky čísla od 0-N, ktoré sú deliteľné siedmymi a štyrmi.

N = int(input("zadaj parameter N  "))

for i in range(0, N+1):
    if i % 4 == 0 and i % 7 == 0:
        print(i)