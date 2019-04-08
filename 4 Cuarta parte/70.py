#decimal a binario
n = int(input("Ingrese el número en base decimal: "))
residuos= []
residuos_inv = []
if n==0:
  print("Su número en binario es:")
  print("0"*4)
else:
  while n != 0 :
    r = n%2
    residuos.append(r)
    n = int(n/2)

  lenght = len(residuos)
  if lenght%4 != 0:
    ceros_faltantes = 4 - (lenght%4)
    ceros = "0 "*ceros_faltantes
    residuos_inv.append(ceros)

  for x in reversed(residuos):
    strx= str(x) # es necesario pasar la x a string para que luego se pueda hacer el “join”
    residuos_inv.append(strx)

  str_lista = " ".join(residuos_inv)
  print("Su número en binario es:")
  print(str_lista)