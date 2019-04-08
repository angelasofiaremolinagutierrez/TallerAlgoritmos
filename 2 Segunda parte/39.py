import math
ax2 = int(input("Escriba la variable a, que es la que acompaña a la X^2: "))
bx = int(input("Escriba la variable b, que es la que acompaña a la X: "))
c = int(input("Escriba la variable c, que es el número unitario: "))

#d = discriminante de la cuadratica
d = math.sqrt((bx*bx)-(4*ax2*c))

#cuando d>0
cuadratica_pos = (-bx + d)/(2 * ax2)
cuadratica_neg = (-bx - d)/(2 * ax2)
#cuando d=0
cuadratica_d0 = -bx/(2*ax2)
#cuando d<0
#no tiene solucion en los números reales

if d > 0 :
    print ("Solución 1: " + str(cuadratica_pos))
    print ("Solución 2: " + str(cuadratica_neg))

elif d == 0 :
    print ("Única solución: " + str(cuadratica_d0))

else:
    d < 0
    print("No existe solución en los números reales")