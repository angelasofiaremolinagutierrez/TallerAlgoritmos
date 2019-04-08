#Solo se pueden retirar multiplos de 5000
cantidad = input("¿Qué cantidad quiere retirar? ")
cant_float = float(cantidad)
cant_int = int(cant_float)

divisible_5k = cant_int % 5000

y=cant_int%50000
z=y%20000
w=z%10000
t=w%5000

ny=(cant_int - y)/50000
nz=(y-z)/20000
nw=(z-w)/10000
nt=(w-t)/5000

if cant_float - cant_int == 0:
    if divisible_5k == 0 :

        if cant_int < 5000:
          print("No se puede retirar esa cantidad")
        if ny >= 1 :
          print("50000 * " + str(ny))
        if nz >= 1 :
          print ("20000 * " + str(nz))
        if nw >= 1 :
          print ("10000 * " + str(nw))
        if nt >= 1:
          print ("5000 * " + str(nt) )
    else:
        print ("Cantidad no válida")
else:
  print("Cantidad no válida")