valor_original = int(input("Cuanto pago en su compra: "))
valor_IVA = valor_original * 0.19
valor_final = valor_original + valor_IVA

print("El valor de su compra con el IVA incluido es: " + str(valor_final))