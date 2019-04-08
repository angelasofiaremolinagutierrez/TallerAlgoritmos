n=int(input("Escriba el inicio del rango: "))
m=int(input("Escriba el fin del rango: "))
if m>n:
      for x in range (n,m+1):
        print(x)
else:
    m<n
    print("verifique que el inicio del rango sea menor a su fin")