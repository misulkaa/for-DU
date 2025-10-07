#3.    Naprogramuj funkciu, ktorá vypíše každé druhé číslo, počínajúc čislom 5 až po N

N = int(input(" zadaj N  "))

for i in range(5, N+1, 2):
    print(i)