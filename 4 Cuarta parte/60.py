n=int(input("escriba un número"))

for x in range(1,n+1):
    if x%2 ==0:
        x= x*-1
    print(x)