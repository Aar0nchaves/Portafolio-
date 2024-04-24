#15 salarios
suma=0
dif=0
for i in range(1,5):
    sal=float(input("digite salario:"))
    if sal<500.0:
         dif=500.0-sal
         suma=suma+dif
    else:
        sal=sal
   
print ("se necesita",suma,"para que al menos todos ganen $500.0")
      
