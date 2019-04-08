n= int(input("Ingrese un número: "))
divisores=[]
cont_div = 0
for x in range(1,n+1):
	if n%x == 0:
		cont_div += 1
		divisores.append(x)
print (n,"tiene",cont_div,"divisores:")
print(divisores)