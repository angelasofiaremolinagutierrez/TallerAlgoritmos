n = int(input("Escriba un número entre 1 y 10: "))
numeros=[" ",1,2,3,4,5,6,7,8,9,10]
nombres=[" ","Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez"]

if n>=1 and n<=10:
    print((numeros[n]),"--->",(nombres[n]))
else:
    print("Tiene que ser un número entre 1 y 10")