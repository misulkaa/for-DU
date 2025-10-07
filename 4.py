#  Naprogramuj funkciu, ktorá vypíše čísla od 1 po N a ich druhé mocniny. Pričom N je argumentom funkcie.
#  Napr. Pre N=9

N = int(input(" zadaj N  "))

for i in range(1, N+1):
    print(i, i **2)