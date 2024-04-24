
a = int(input("ingrese un numero:"))
b = int(input("ingrese un numero:"))
c = int(input("ingrese un numero:"))

if a>b & b>c:
    print(a,b,c)

elif b>a & c>a:
    print (b,c,a)
    
elif c>a & a>b:
    print (c,a,b)

elif b>a & a>c:
    print (b,a,c)

elif c>b & b>a:
    print (c,b,a)

elif a>b & c>b:
    print(a,c,b)
else: print ("numeros ordenados")
