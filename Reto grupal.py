#Aarón Chaves Cascante

import os

def agregar_datos():

    archivo_almacen=open("almacenamineto de montos.txt","w")
    
    vendedor=str(input("vendedor:"))
    venta_realiz=str(input("monto de la venta:"))
    vendedor2=str(input("vendedor:"))
    venta_realiz2=str(input("monto de la venta:"))
    vendedor3=str(input("vendedor:"))
    venta_realiz3=str(input("monto de la venta:"))

    archivo_almacen.write("\n")
    archivo_almacen.write("vendedor:")
    archivo_almacen.write(vendedor)
    archivo_almacen.write("\n")
    archivo_almacen.write("monto: $")
    archivo_almacen.write(venta_realiz)
    archivo_almacen.write("\n")
    archivo_almacen.write("\n")
    archivo_almacen.write("vendedor:")
    archivo_almacen.write(vendedor2)
    archivo_almacen.write("\n")
    archivo_almacen.write("monto: $")
    archivo_almacen.write(venta_realiz2)
    archivo_almacen.write("\n")
    archivo_almacen.write("\n")
    archivo_almacen.write("vendedor:")
    archivo_almacen.write(vendedor3)
    archivo_almacen.write("\n")
    archivo_almacen.write("monto: $")
    archivo_almacen.write(venta_realiz3)
    archivo_almacen.write("\n")
    archivo_almacen.write("\n")
    archivo_almacen.close()

def mostrar_datos():
    archivo_almacen=open("almacenamineto de montos.txt","r")
    datos=archivo_almacen.read()
    print(datos)

    
agregar_datos()
mostrar_datos()


