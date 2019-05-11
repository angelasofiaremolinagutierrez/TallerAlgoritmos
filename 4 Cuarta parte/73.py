print("Binario a decimal")
num = input("Ingrese un número binario: ")
digitos=len(num)
exp = 0 #contador exponentes
suma = 0
for x in range(1,digitos+1):

    m1 = int(num[-x])
    m2= 2**exp
    s = m1*m2
    suma = suma + s
    exp = exp+1

print("Número en base decimal:",suma)