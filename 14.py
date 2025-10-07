#Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné ôsmimi

z = int(input("zadaj zaciatok intervalu  "))
k = int(input("koniec intervalu  "))

x = 0

for i in range(z, k+1):
    if i % 8 == 0:
        x = x + 1

print(x)