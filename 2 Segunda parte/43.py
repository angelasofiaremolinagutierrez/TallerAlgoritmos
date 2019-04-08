a=float(input("Escriba el primer número: "))
b=float(input("Escriba el segundo número: "))
c=float(input("Escriba el tercer número: "))
numeros = [a,b,c]
print(numeros)
if a>b and b>c:
    print ("Disminuyendo")
elif a<b and b<c:
    print("Aumentando")
else:
    print ("Los números no tienen un orden especifico")