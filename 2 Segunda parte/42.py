n = int(input("Escriba un número menor a 100.000: "))

if n<100000:
    if n>=10000 or n <-10000:
        print(n,"tiene 5 digitos")
    elif n>=1000 or (n>=-9999 and n<-1000):
        print(n,"tiene 4 digitos")
    elif n>=100 or (n>=-999 and n<-100):
        print(n, "tiene 3 digitos")
    elif n>=10 or (n>=-99 and n<-10):
        print(n, "tiene 2 digitos")
    elif n>=-9:
        print(n,"tiene 1 digito")
else:
    print("el número tiene que ser MENOR que 100.000")