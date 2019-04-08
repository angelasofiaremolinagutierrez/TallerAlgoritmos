#$5.000 por km
#minimo cobro de $100.000
d=int(input("Escriba la distancia en kilometros que va a recorrer: "))
e=int(input("Escriba el numero de días de estancia: "))

costo_regular = d*5000 #d menor a 1000 km
descuento = costo_regular*0.15
costo_descuento = costo_regular - descuento #con descuento

if costo_regular > 100000 :
    if d > 1000 and e>7 :
        print("Su pasaje vale $"+ str(costo_descuento)) #descuento del 15%
    else:
        print(costo_regular)

else:
    print("Su pasaje vale $100.000")