pares = 1
cincos = 1
total_ingresos = 1
n=int(input("Escriba un número positivo: "))
if n>0:
    while pares < 100 and cincos < 80:
        n=int(input("Escriba un número positivo: "))
        if n%2==0:
            pares = pares + 1
        elif n==5:
            cincos = cincos + 1
        total_ingresos = total_ingresos + 1
else:
    print("Verifique que se un número positivo")
print("Se ingresaron:", total_ingresos, "números")