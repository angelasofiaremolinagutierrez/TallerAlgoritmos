n=int(input("¿Cuantos números quiere promediar?"))
suma = 0
for x in range (n):
  a=int(input(x+1))
  suma = a+suma
print("La suma de los números es:",suma)
promedio = suma/n
print("El promedio es: ", promedio)