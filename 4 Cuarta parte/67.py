n= int(input("¿Cuántos números quiere comprobar? "))
mayores = 0
menores = 0
iguales = 0
print("escriba los", n, "números")
for x in range(n):
    a=int(input())
    if a>100:
        mayores=mayores+1
    elif a<100:
        menores= menores+1
    else:
        iguales = iguales+1

print("Hay", mayores, "números mayores que 100")
print("Hay", menores, "números menores que 100")
print("Hay", iguales, "números iguales a 100")