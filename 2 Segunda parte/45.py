n = int(input("Escriba un número entre 1 y 7: "))
numeros=[" ",1,2,3,4,5,6,7]
nombres=[" ","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]

if n>=1 and n<=7:
    print((numeros[n]),"--->",(nombres[n]))
else:
    print("Tiene que ser un número entre 1 y 7")