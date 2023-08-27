#importamos todos los elementos de tkinter que sera nuestra interfaz
from tkinter import *

raiz = Tk()
raiz.title("Conversor de unidades")
raiz.resizable(0,0)
raiz.geometry("650x350")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

#-----------------CONVERSOR DE BINARIO A DECIMAL------------------

miResultado=StringVar()
nombreLabel= Label(miFrame, text="Numero binario a convertir: ")
nombreLabel.grid(row=0,column=0, pady=10)
cuadroBinario = Entry(miFrame)
cuadroBinario.grid(row=0, column=1)

#metodo conversor de binario a decimal
def binario_a_decimal():
    decimal = 0
    binario = cuadroBinario.get()
    #leera la cantidad de numeros
    longitud = len(binario)
    
    for i in range(longitud):
        #toma digito a digito
        digito = int(binario[i])
        #calcula la posicion en la que se encuentra del total de numeros
        posicion = longitud - i - 1
        #suma de la formula realizada para la conversion de numero binario a decimal
        decimal += digito * (2 ** posicion)
        miResultado.set(decimal)
    return decimal


botonConversor = Button(raiz, text="Convertir de binario a decimal", command=binario_a_decimal)
botonConversor.pack()

nombreLabel= Label(miFrame, text="Resultado numero decimal: ")
nombreLabel.grid(row=2,column=0, pady=10)
cuadroResultado = Entry(miFrame, textvariable=miResultado)
cuadroResultado.config(state=DISABLED)
cuadroResultado.grid(row=2, column=1)

#-----------------CONVERSOR DE DECIMAL A BINARIO------------------
miResultado2=StringVar()
nombreLabel2= Label(miFrame, text="Numero decimal a convertir: ")
nombreLabel2.grid(row=3,column=0, pady=10)
cuadroDecimal = Entry(miFrame)
cuadroDecimal.grid(row=3, column=1)

#metodo conversor de decimal a binario
def decimal_a_binario():
    miResultado2.set(bin(int(cuadroDecimal.get())))

botonConversor2 = Button(raiz, text="Convertir de decimal a binario"    , 
                         command=decimal_a_binario)
botonConversor2.pack()

nombreLabel2= Label(miFrame, text="Resultado numero binario: ")
nombreLabel2.grid(row=4,column=0, pady=10)
cuadroResultado2 = Entry(miFrame, textvariable=miResultado2)
cuadroResultado2.config(state=DISABLED)
cuadroResultado2.grid(row=4, column=1)
    
#-----------------CONVERSOR DE IP A HEXADECIMAL------------------
resultadoHexadecimal=StringVar()
nombreLabel3= Label(miFrame, text="Numero decimal a convertir: ")
nombreLabel3.grid(row=5,column=0, pady=10)
cuadroIp = Entry(miFrame)
cuadroIp.grid(row=5, column=1)

def ip_decimal_to_hex():
    ip_decimal = cuadroIp.get()
    # Dividir la dirección IP en sus cuatro partes
    partes = ip_decimal.split('.')
    
    # Convertir cada parte decimal en hexadecimal
    partes_hex = [format(int(parte), '02X') for parte in partes]
    
    # Unir las partes hexadecimales con dos puntos (:)
    ip_hexadecimal = ':'.join(partes_hex)
    resultadoHexadecimal.set(ip_hexadecimal)
    return ip_hexadecimal
botonConversor2 = Button(raiz, text="Convertir numero IP a hexadecimal"    , 
                         command=ip_decimal_to_hex)
botonConversor2.pack()

nombreLabel2= Label(miFrame, text="Resultado numero hexadecimal: ")
nombreLabel2.grid(row=6,column=0, pady=10)
cuadroResultado3 = Entry(miFrame, textvariable=resultadoHexadecimal)
cuadroResultado3.config(state=DISABLED)
cuadroResultado3.grid(row=6, column=1)

#encargado de correr la interfaz (bucle infinito)
raiz.mainloop()


