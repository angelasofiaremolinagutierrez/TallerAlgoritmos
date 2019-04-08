#decimal a hexadecimal
n = int(input("Ingrese el número en base decimal: "))
residuos= []
residuos_inv = []
if n==0:
  print("Su número en hexadecimal es:")
  print(n)
else:
  while n != 0 :
    r = n%16
    n = int(n/16)

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