print("Binario a octal")
bcd = int(input("Ingrese el número binario de TRES DIGITOS O MENOS: "))
b = int(bcd/100)
cd = int(bcd-(b*100))
c = int(cd/10)
d= int(cd - (c*10))

p=b*(2**2)
q=c*(2**1)
r=d*(2**0)

suma = p+q+r

print (suma)