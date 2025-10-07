#2.    Naprogramuj funkciu, ktorá vypíše čísla od 1-N, N je vstupný parameter za sebou, budú oddelené čiarkou

N = int(input("zadaj n: "))

print(",".join(str(i) for i in range(1, N + 1)))