#Naprogramuj funkciu, ktorá vypíše pre čísla od <odkiaľ> <pokial> aj ich druhé odmocniny
# (zaokrúhlené na 2 des.miesta). Pričom hodnoty <odkiaľ> <pokial> sú parametre funkcie.

M = int(input(" zadaj M  "))
N = int(input(" zadaj N  "))

for i in range(M, N+1):
    print((i, round(i**0.5, 2)))