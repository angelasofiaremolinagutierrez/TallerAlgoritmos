#d = sqrt((x1-x2)^2 + (y1-y2)^2)
import math
x1= int(input("Escriba el valor en x del primer punto: "))
y1= int(input("Escriba el valor en y del primer punto: "))
x2= int(input("Escriba el valor en x del segundo punto: "))
y2= int(input("Escriba el valor en y del segundo punto: "))

d= math.sqrt( (pow((x1-x2),2)) + (pow((y1-y2),2)))

print("La distancia entre el primer punto y el segundo punto es: ", d, "unidades")