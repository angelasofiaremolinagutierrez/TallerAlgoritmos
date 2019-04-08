n_bultos = int(input("¿Cuántos bultos ingresa al vuelo? "))
peso_total = 0
precio_bultos = 0
peso_bultos =[]
print("Ingrese el peso de cada uno de sus",n_bultos, "bultos")
for x in range(n_bultos):
    c_bulto=int(input())
    peso_bultos.append(c_bulto)
    peso_total=peso_total + c_bulto
    if c_bulto < 500 and c_bulto>0:
        if c_bulto<25:
            precio_bultos = precio_bultos + 0
        elif c_bulto>25 and c_bulto<300:
            precio_bultos = precio_bultos + 1500
        elif c_bulto>301 and c_bulto<500:
            precio_bultos = precio_bultos + 2500
    else:
        print("el bulto excede el peso máximo")

peso_bultos.sort()
promedio = peso_total/n_bultos
precio_dolares = precio_bultos/3168 #div en el precio dolar hoy
print("Se ingresaron",n_bultos,"bultos")
print("El bulto más pesado pesa",peso_bultos[-1], "kilogramos")
print("El bulto más liviano pesa",peso_bultos[0], "kilogramos")
print("El promedio del peso de los bultos es de:",promedio)
print("El precio de la carga en pesos es de: $",precio_bultos)
print("El precio de la carga en dolares es de: $",precio_dolares)