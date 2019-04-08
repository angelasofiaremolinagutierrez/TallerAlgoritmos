#mua d=vo*t + (at^2)/2
print("Nota: escriba la velocidad en m/s, el tiempo en s, y la aceleración en m/s^2")
vo= int(input("Ingrese la velocidad inicial del objeto: "))
t= int(input("Ingrese el tiempo que tardó el movimiento: "))
a = int(input("Ingrese la aceleración que llevaba el objeto: "))
d = (vo*t) + ((a*t*t)/2)

print ("La distancia recorrida fueron: ", d, "metros")