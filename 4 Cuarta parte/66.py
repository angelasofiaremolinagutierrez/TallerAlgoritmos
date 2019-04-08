n=float(input("Ingrese un número entero positivo: "))
n_int = int(n)
n_resta = n - n_int
while n<0 or n_resta !=0 :
    n=float(input("Ingrese un número entero positivo: "))
    n_int = int(n)
    n_resta = n - n_int
print(n,"fin")