#13. naprogramuj funkciu, ktorá sčíta všetky párne čísla od 1-N

N = int(input(" zadaj N  "))

y = 0

for i in range(1, N+1):
    if i % 2 == 0:
        y = y + i

print(y)