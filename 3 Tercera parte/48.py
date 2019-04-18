a = input("Escriba algo: ")
print()
print("Original:", a)

inv = []
length = len(a)
for x in range(length):
    prim = length - x
    sec = prim - 1
    elem_inv = a[sec]
    inv.append(elem_inv)

final = ''.join(inv)
print("Invertido:", final)

