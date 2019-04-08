a= int(input("Ingrese un número: "))
b= int(input("Otro:"))

if a<b:
    print (b, "es mayor que",a)
if b<a:
    print (a, "es mayor que",b)
elif b==a :
    print(a, "es igual a", b)