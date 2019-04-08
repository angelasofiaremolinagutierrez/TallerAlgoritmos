#Ingrese los segundos exactos, no decimales 
s = int(input("Ingrese la cantidad de segundos: "))
parte_horas_int = int(s/3600) #23
#parte_horas_float = float(s/3600) #23.99972

segundos_en_minutos = s - (parte_horas_int * 3600) #86399-(23*3600)=3599
parte_minutos_int = int(segundos_en_minutos/60) #3599/60 = 59
#parte_minutos_float = float(segundos_en_minutos/60) #3599/60 = 59.9833

segundos_restantes = segundos_en_minutos - (parte_minutos_int * 60) #3599-(59*60)=59

horas = parte_horas_int
minutos = parte_minutos_int
segundos = segundos_restantes
print(horas,":",minutos,":",segundos)