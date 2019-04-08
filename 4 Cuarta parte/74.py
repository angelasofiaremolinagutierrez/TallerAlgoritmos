print("Binario a hexadecimal")
abcd = int(input("Ingrese un número binario DE CUATRO DIGITOS O MENOS: "))
a = int(abcd/1000)
bcd = int(abcd-(a*1000))
b = int(bcd/100)
cd = int(bcd-(b*100))
c = int(cd/10)
d= int(cd - (c*10))

o=a*(2**3)
p=b*(2**2)
q=c*(2**1)
r=d*(2**0)

suma = o+p+q+r

decimal=[10,11,12,13,14,15]
hexa=["A","B","C","D","E","F"]
if suma >= 10:
    print (hexa[suma-10])
else:
    print (suma)