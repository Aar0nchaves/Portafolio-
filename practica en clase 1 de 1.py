# numeros binarios

def entero_a_binario(numero):
    if numero == 0:
        return "0"
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    return binario
def entero_a_octal(numero):
    if numero == 0:
        return "0"
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero = numero // 8
    return octal
def entero_a_hexadecimal(numero):
    if numero == 0:
        return "0"
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            hexadecimal = str(residuo) + hexadecimal
        else:
            hexadecimal = chr(ord("A") + residuo - 10) + hexadecimal
        numero = numero // 16
    return hexadecimal


    
numero_entero = int(input("ingrese un numero entero:"))
resultado_binario = entero_a_binario(numero_entero)
print("El número binario de", numero_entero, "es:", resultado_binario)
resultado_octal = entero_a_octal(numero_entero)
print("El número octal de", numero_entero, "es:", resultado_octal)
resultado_hexadecimal = entero_a_hexadecimal(numero_entero)
print("El número hexadecimal de", numero_entero, "es:", resultado_hexadecimal)

valor=(input("ingrese un valor en base binaria, hexadecimal u octal:"))
