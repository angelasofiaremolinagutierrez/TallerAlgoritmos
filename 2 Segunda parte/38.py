year = int(input("Ingrese el año: "))
year_in_4 = year/4
n_int = int(year_in_4)
n_float = float(year_in_4)
substraction = n_float - n_int
if substraction == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Año bisiesto")
        else:
            print("Año de 365 días")
    else:
        print ("Año bisiesto")
else:
    print ("Año de 365 días")