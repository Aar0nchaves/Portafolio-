
kilometros=[int(input("km lunes:")),int(input("km martes:")),int(input("km miercoles:")),int(input("km jueves:")),int(input("km viernes:")),int(input("km sabado:")),int(input("km domingo:"))]
vpt1=kilometros[0]
vpt2=kilometros[1]
vpt3=kilometros[2]
vpt4=kilometros[3]
vpt5=kilometros[4]
vpt6=kilometros[5]
vpt7=kilometros[6]

dias=["lunes", "martes", "miercoles","jueves","viernes","sabado","domingo"]
def ver_datos(km_x_dia):
    for index in range(7):
        print("el dia",dias[index],"recorrió:",kilometros[index])
        
tot_recorri=vpt1+vpt2+vpt3+vpt4+vpt5+vpt6+vpt7             
ver_datos(dias)
print ("El total de kilometros recorridos esta semana es:", tot_recorri)
