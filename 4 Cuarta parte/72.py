#decimal a octal
n = int(input("Ingrese el número en base decimal: "))
residuos= []
residuos_inv = []
if n==0:
  print("Su número en octal es:")
  print(n)
else:
  while n != 0 :
    r = n%8
    residuos.append(r)
    n = int(n/8)

  for x in reversed(residuos):
    strx= str(x) # es necesario pasar la x a string para que luego se pueda hacer el “join”
    residuos_inv.append(strx)

  str_lista = "".join(residuos_inv)
  print("Su número en octal es:")
  print(str_lista)