abcd = int(input("Ingrese un número de cuatro dígitos: ")) #3245
a = int(abcd/1000) #3
bcd = int(abcd-(a*1000)) #245
b = int(bcd/100) #2
cd = int(bcd-(b*100)) #45
c = int(cd/10) #4
d= int(cd - (c*10)) #5

print (abcd)
print (str(d)+str(c)+str(b)+str(a))