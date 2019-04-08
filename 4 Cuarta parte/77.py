u = "Angela"
c = "42"

for x in range(3):
    u_input = input("Escriba su nombre de usuario: ")
    c_input = input("Escriba su contraseña: ")
    if u == u_input and c == c_input:
        print ("Usuario y contraseña correcta :D")
        break
    else:
        print("Usuario y/o contraseña incorrectas D:")
        print()