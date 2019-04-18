import math
x1= float(input("valor del primer punto en X: "))
y1= float(input("valor del primer punto en Y: "))
x2= float(input("valor del segundo punto en X: "))
y2= float(input("valor del segundo punto en Y: "))
radio_tierra = 6371
distancia = radio_tierra * (math.acos(math.cos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 -y2))))
print(distancia, "kilometros")