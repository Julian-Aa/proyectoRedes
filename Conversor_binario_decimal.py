#importamos todos los elementos de tkinter que sera nuestra interfaz
from tkinter import *
import socket
import psutil

raiz = Tk()
raiz.title("Conversor de unidades")
raiz.resizable(0,0)
raiz.geometry("650x500")

miFrame = Frame(raiz, width=1200, height=1200)
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
    binario = bin(int(cuadroDecimal.get()))  # Obtiene la representación binaria con "0b"
    binario_sin_prefix = str(binario)[2:]    # Quita los primeros dos caracteres (0b)
    miResultado2.set(binario_sin_prefix)

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

#-----------------OBTENER IP Y MASCARA DE RED------------------
resultadoIp=StringVar()
resultadoMascara=StringVar()
def obtener_informacion_red():
    # Obtener la dirección IP del host local
    direccion_ip = socket.gethostbyname(socket.gethostname())

    # Obtener la información de las interfaces de red
    interfaces = psutil.net_if_addrs()

    # Filtrar y obtener la máscara de red de la interfaz activa
    mascara_red = None
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == direccion_ip:
                mascara_red = addr.netmask
                break
    resultadoIp.set(direccion_ip)
    resultadoMascara.set(mascara_red)
    return direccion_ip, mascara_red


nombreLabel3= Label(miFrame, text="Resultado de IP: ")
nombreLabel3.grid(row=7,column=0, pady=10)
cuadroResultado4 = Entry(miFrame, textvariable=resultadoIp)
cuadroResultado4.config(state=DISABLED)
cuadroResultado4.grid(row=7, column=1)

nombreLabel4= Label(miFrame, text="Mascara de RED: ")
nombreLabel4.grid(row=8,column=0, pady=10)
cuadroResultado5 = Entry(miFrame, textvariable=resultadoMascara)
cuadroResultado5.config(state=DISABLED)
cuadroResultado5.grid(row=8, column=1)

botonConversor2 = Button(raiz, text="Obtener IP y mascara de RED"    , 
                         command=obtener_informacion_red)
botonConversor2.pack()

#encargado de correr la interfaz (bucle infinito)
raiz.mainloop()


