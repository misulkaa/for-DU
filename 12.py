#Naprogramuj funkciu , ktorá sčíta dokopy čísla od 1 do N. (N -parameter funkcie)

N = int(input("zadaj N  "))

x = 0
for i in range(1, N+1):
    x = x+i

print(x)