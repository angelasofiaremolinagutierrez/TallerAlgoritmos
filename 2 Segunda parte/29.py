n = int(input("Ingrese un número: "))

if n%2 == 0 and n > 0 :
    print("El número es par positivo")
if n%2 == 0 and n < 0 :
    print("El número es par negativo")
if n%2 != 0 and n > 0 :
    print("Es un número impar positivo")
if n%2 != 0 and n < 0 :
    print("Es un número impar negativo")
elif n == 0 :
    print("Cero")
#par positivo
#par negativo
#impar positivo
#impar negativo
