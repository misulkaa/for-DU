#Naprogramuj funkciu, ktorá pre dané x z intervalu <1,20> bude počítať funkčné hodnoty podľa predpisu
# y= (x**2-1)/(x-3) .

y = 0
x = 0
for i in range(1, 21):
        if i == 3:
            print("x =  3  funkcia neni definovana")
        else:
           x += 1
           y = (i ** 2 - 1) / (i - 3)
           print("x = ", x, "y =", y)
