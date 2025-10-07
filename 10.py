# vypíš čísla od 1-N odzadu, za sebou. Ak N=5 , výsledok by mal byť: 5,4,3,2,1

N = int(input("zadaj n "))
for i in range(N, 0, -1):
    print(i)