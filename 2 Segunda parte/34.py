print("Ingrese 3 numeros")
n1 = int( input("Numero 1: "))
n2 = int( input("Numero 2: "))
n3 = int( input("Numero 3: "))

if n1>n2 and n1>n3 :
    print (str(n1) + " es el mayor")
if n2>n1 and n2>n3 :
    print (str(n2) + " es el mayor")
if n3>n1 and n3>n2 :
    print (str(n3) + " es el mayor")
if n1==n2 and n1==n3 :
    print (str(n1)+ ", " + str(n2) + " y " +str(n3) + " son iguales")