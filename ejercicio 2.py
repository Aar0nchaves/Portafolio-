#Estadistica de N niños

alt_ni0=int(0)
alt_ni1=int(0)
alt_ni2=int(0)
alt_ni3=int(0)
alt_ni4=int(0)
suma=int(0)
n_ni=int(input("ingrese la cantidad de estudiantes:"))

for i in range(n_ni):
    alt_ni=int(input("digite la altura en centimetros:"))
    if alt_ni < 100:
        alt_ni0 += 1
    elif alt_ni >= 100 and alt_ni <= 120:
        alt_ni1 += 1
    elif alt_ni >= 121 and alt_ni <= 130:
        alt_ni2 += 1
    elif alt_ni >= 131 and alt_ni <= 140:
        alt_ni3 += 1
    elif alt_ni > 140:
        alt_ni4 += 1
    suma=suma+alt_ni

print ("la cantidad de niños que miden menos de 100 cm son", alt_ni0)
print ("la cantidad de niños que miden entre 100 y 120cm son", alt_ni1)
print ("la cantidad de niños que miden entre 121 y 130cm son", alt_ni2)
print ("la cantidad de niños que miden entre 131 y 140cm son", alt_ni3)
print ("la cantidad de niños que miden más de 140 cm son", alt_ni4)
print ("el promedio de estaturas es:", suma/n_ni)
