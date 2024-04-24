nombres=[str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:")),str(input("ingrese su nombre:"))]
posi=[1,2,3,4,5,6,7,8,9,10]
def ver_nombres (cant_nom):
    for index in range (10):
        print ("la persona", nombres[index], "ocupa la posicion:", posi[index])
ver_nombres(nombres)
