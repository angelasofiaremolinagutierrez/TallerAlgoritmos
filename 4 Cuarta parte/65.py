n=int(input("¿Cuantos números quiere promediar? "))
print("Escriba un conjunto de numeros")
sumap=0
sumaip=0
cont_par=0
cont_impar=0
for x in range (n):
    a=int(input())
    if a%2 ==0:
        sumap = sumap+a
        cont_par=cont_par+1
    else:
        sumaip = sumaip + a
        cont_impar=cont_impar+1

prom1= sumap/cont_par
prom2=sumaip/cont_impar

print("Promedio de pares: ",prom1)
print("Promedio de impares: ",prom2)