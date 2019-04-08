print("Binario a decimal")
abcd = int(input("Ingrese un número binario DE CUATRO DIGITOS O MENOS: "))
a = int(abcd/1000) #3
bcd = int(abcd-(a*1000)) #245
b = int(bcd/100) #2
cd = int(bcd-(b*100)) #45
c = int(cd/10) #4
d= int(cd - (c*10)) #5

o=a*(2**3)
p=b*(2**2)
q=c*(2**1)
r=d*(2**0)

suma = o+p+q+r

print (suma)