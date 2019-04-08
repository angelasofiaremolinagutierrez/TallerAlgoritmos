import math
print("Area de un hexagono")
lado = int(input("¿Cuanto mide uno de los lados? "))
apotema = math.sqrt((lado*lado)-((lado/2)*(lado/2)))
perimetro = lado*6
area = (perimetro*apotema)/2
print (str(area))