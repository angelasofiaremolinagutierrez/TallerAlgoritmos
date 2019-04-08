valor = int(input("Cuanto pago en su compra: "))

valor_IVA = valor * 0.19
valor_final = valor + valor_IVA
descuento = valor_final* 0.05
valor_con_descuento = valor_final - descuento
if valor > 150000 :
    print ("Debe pagar:",valor_con_descuento,"Con un descuento de: ", descuento)
if valor < 150000 and valor > 0 :
    print("El valor de su compra es: " + str(valor_final))