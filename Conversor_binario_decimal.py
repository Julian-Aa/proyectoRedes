def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        digito = int(binario[i])
        posicion = longitud - i - 1
        decimal += digito * (2 ** posicion)
    
    return decimal

binario = input("Ingresa un número binario: ")
decimal = binario_a_decimal(binario)
print(f"El número binario {binario} es igual a {decimal} en decimal.")

def decimal_a_binario(decimal_number):
    binary_representation = bin(decimal_number)
    print(f"El número {decimal_number} en binario es: {binary_representation}")
    
decimal_number = int(input("Ingresa un número decimal: "))
decimal_a_binario(decimal_number)

