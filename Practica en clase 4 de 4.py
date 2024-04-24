cant_dias=["lunes", "martes", "miercoles","jueves","viernes","sabado","domingo"]
monto=[int(input("monto lunes:")),int(input("monto martes:")),int(input("monto miercoles:")), int(input("monto jueves:")),int(input("monto viernes:")),int(input("monto sabado:")),int(input("monto domingo:"))]
vpt1=monto[0]
vpt2=monto[1]
vpt3=monto[2]
vpt4=monto[3]
vpt5=monto[4]
vpt6=monto[5]
vpt7=monto[6]


def dias_habiles(dias_ganancia):
   
    for index in range (7):
        print("el día",cant_dias[index],"consiguió un monto de:",monto[index])
    
    

   
total_monto_sem=vpt1+vpt2+vpt3+vpt4+vpt5+vpt6+vpt7
dias_habiles(monto)
print ("El monto total obtenido esta semana es de:",total_monto_sem,"y el dia que obtuvo menos fue:")
