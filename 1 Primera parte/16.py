#mua vf = sqrt(vo^2 + 2ad)
#mua vf = vo + at
import math
print("Nota: escriba la velocidad en m/s, el tiempo en s, y la aceleración en m/s^2")
vo = int(input("Ingrese la velocidad inicial: "))
a= int(input("Ingrese la aceleración: "))
t= int(input("Ingrese el tiempo del movimiento: "))
vf= vo + (a*t)
print("La velocidad final del objeto es: ", vf)