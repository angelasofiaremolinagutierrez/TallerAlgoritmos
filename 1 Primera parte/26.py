print("Esriba T si la afirmacion es verdadera y F si es falsa")
print()
print("True OR False")
r= input("?")
if r.lower() == "t":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")

print()
print("False OR False")
r= input("?")
if r.lower() == "f":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")

print()
print("True AND True")
r= input("?")
if r.lower() == "t":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")

print()
print("False AND True")
r= input("?")
if r.lower() == "f":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")

print()
print("(False AND False) OR (True AND True)") #false or true = TRUE
r= input("?")
if r.lower() == "t":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")

print()
print("(False OR False) AND (True AND True)") #false and true = FALSE
r= input("?")
if r.lower() == "f":
    print ("Correcto :)")
else:
    print ("Incorrecto :(")