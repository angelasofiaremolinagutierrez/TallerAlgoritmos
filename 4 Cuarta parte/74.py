print("Binario a hexadecimal")
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

#luego de decimal a hexadecimal
residuos= []
residuos_inv = []
if suma==0:
  print("Su número en hexadecimal es:")
  print(suma)
else:
  while suma != 0 :
    r = suma%16
    suma = int(suma/16)

    if r>=10:
      numeros = ["10","11","12","13","14","15"]
      letras = ["A","B","C","D","E","F"]
      r_letra = letras[r-10]
      residuos.append(r_letra)
    elif r<10:
      residuos.append(r)

  for x in reversed(residuos):
    strx= str(x)
    residuos_inv.append(strx)

  str_lista = "".join(residuos_inv)
  print("Su número en hexadecimal es:")
  print(str_lista)
