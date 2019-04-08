n=int(input("Escriba el inicio del rango: "))
m=int(input("Escriba el fin del rango: "))
if m>n:
    suma = 0
    for x in range (n,m+1):
        suma = x+suma

    print("La suma de los números naturales entre",n, "y",m, "es",suma)
else:
    m<n
    print("verifique que el inicio del rango sea menor a su fin")