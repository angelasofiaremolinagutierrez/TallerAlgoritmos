n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input ("Tercera nota: "))
n4 = float(input ("Cuarta nota: "))
n5 = float(input ("Quinta nota: "))

n1_15 = n1*0.15
n2_20 = n2*0.20
n3_15 = n3*0.15
n4_30 = n4*0.30
n5_20 = n5*0.20

nota_final = (n1_15) + (n2_20) + (n3_15)+ (n4_30)+ (n5_20)

if ((n1 or n2 or n3 or n4 or n5)>5) or ((n1 or n2 or n3 or n4 or n5)<0) :
    print("Las notas ingresadas deben estar entre 0 y 5.")
else:
    nota_final<=5
    if nota_final >=3 :
        if nota_final >= 4.5 :
            print("Felitaciones, aprobó con una nota alta de: "+ str(nota_final))
        else:
            nota_final < 4.5
            print("Aprobó con:"+ str(nota_final))

    else:
        nota_final < 3
        if nota_final < 3 and nota_final >= 2:
            print ("Su nota final fue: "+ str(nota_final) + " Reprobó, debe habilitar.")
        else:
            nota_final < 2 and nota_final >= 0
            print ("Su nota final fue: "+ str(nota_final) + ". Reprobó y no puede habilitar")