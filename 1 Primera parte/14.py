#mua x=vo*t + (at^2)/2
#caida libre h = (g*t^2)/2
#c.l. t = sqrt(2h/g)
import math
h = int(input("Altura desde la cual se suelta el objeto (altura en metros): "))
t= math.sqrt((2*h)/9.8)
print ("El objeto tardará", t, "segundos en caer al piso")