print("Binario a octal")
num = input("Ingrese un número binario: ")
#lo volvemos decimal
digitos=len(num)
exp = 0 #contador exponentes
suma = 0
for x in range(1,digitos+1):

    m1 = int(num[-x])
    m2= 2**exp
    s = m1*m2
    suma = suma + s
    exp = exp+1

print (suma)
#luego de decimal a octal
residuos= []
residuos_inv = []
if suma==0:
  print("Su número en octal es:")
  print(suma)
else:
  while suma != 0 :
    r = suma%8
    residuos.append(r)
    suma = int(suma/8)

  for x in reversed(residuos):
    strx= str(x) # es necesario pasar la x a string para que luego se pueda hacer el “join”
    residuos_inv.append(strx)

  str_lista = "".join(residuos_inv)
  print("Su número en octal es:")
  print(str_lista)