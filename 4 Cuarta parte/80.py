n = int(input("¿Cuántas filas quiere en su triangulo? "))
acum = 0
a = [0]
for x in range (1,n+1):
  a.append(str(x))
  acum = acum + x
  print(a[1:x+1])
