n= int(input("¿Cuántos números quiere comprobar? "))
positivos = 0
negativos = 0
pares = 0
impares = 0
multiplos8 = 0
print("escriba los", n, "números")
for x in range(n):
    a=int(input())
    if a>0:
        positivos = positivos+1
    if a<0:
        negativos=negativos+1
    if a%2 == 0:
        pares = pares +1
    if a%2 != 0:
        impares = impares + 1
    if a%8 == 0:
        multiplos8 = multiplos8+1
print("Hay", positivos, "números positivos")
print("Hay", negativos, "números negativos")
print("Hay", pares, "números pares")
print("Hay", impares, "números impares")
print("Hay", multiplos8, "números que son múltiplos de 8")