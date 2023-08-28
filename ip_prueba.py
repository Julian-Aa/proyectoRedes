# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:18:28 2023

@author: ASUS
"""

from tkinter import *
import socket
import psutil

def binario_a_decimal():
    decimal = 0
    binario = cuadroBinario.get()
    longitud = len(binario)
    
    for i in range(longitud):
        digito = int(binario[i])
        posicion = longitud - i - 1
        decimal += digito * (2 ** posicion)
        miResultado.set(decimal)

def decimal_a_binario():
    binario = bin(int(cuadroDecimal.get()))[2:]
    miResultado2.set(binario)

def ip_decimal_to_hex():
    ip_decimal = cuadroIp.get()
    partes = ip_decimal.split('.')
    partes_hex = [format(int(parte), '02X') for parte in partes]
    ip_hexadecimal = ':'.join(partes_hex)
    resultadoHexadecimal.set(ip_hexadecimal)

def obtener_ip_binario():
    direccion_ip, _ = obtener_informacion_red()
    partes = direccion_ip.split('.')
    partes_bin = [format(int(parte), '08b') for parte in partes]
    ip_binario = '.'.join(partes_bin)
    miResultadoBinario.set(ip_binario)

def obtener_informacion_red():
    direccion_ip = socket.gethostbyname(socket.gethostname())
    interfaces = psutil.net_if_addrs()
    mascara_red = None
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address == direccion_ip:
                mascara_red = addr.netmask
                break
    return direccion_ip, mascara_red

raiz = Tk()
raiz.title("Conversor de unidades")
raiz.resizable(0, 0)
raiz.geometry("650x500")

miFrame = Frame(raiz, width=1200, height=600)
miFrame.pack()

miResultado = StringVar()
miResultado2 = StringVar()
resultadoHexadecimal = StringVar()
miResultadoBinario = StringVar()

cuadroBinario = Entry(miFrame)
cuadroDecimal = Entry(miFrame)
cuadroIp = Entry(miFrame)

botonConversor = Button(raiz, text="Convertir de binario a decimal", command=binario_a_decimal)
botonConversor2 = Button(raiz, text="Convertir de decimal a binario", command=decimal_a_binario)
botonConversor3 = Button(raiz, text="Convertir numero IP a hexadecimal", command=ip_decimal_to_hex)
botonIpBinario = Button(raiz, text="Obtener dirección IP en binario", command=obtener_ip_binario)

cuadroResultado = Entry(miFrame, textvariable=miResultado)
cuadroResultado.config(state=DISABLED)
cuadroResultado2 = Entry(miFrame, textvariable=miResultado2)
cuadroResultado2.config(state=DISABLED)
cuadroResultado3 = Entry(miFrame, textvariable=resultadoHexadecimal)
cuadroResultado3.config(state=DISABLED)
cuadroResultadoBinario = Entry(miFrame, textvariable=miResultadoBinario)
cuadroResultadoBinario.config(state=DISABLED)

# ... Código para el empaquetado de elementos ...

cuadroBinario.grid(row=0, column=1)
cuadroResultado.grid(row=2, column=1)

cuadroDecimal.grid(row=3, column=1)
cuadroResultado2.grid(row=5, column=1)

cuadroIp.grid(row=6, column=1)
cuadroResultado3.grid(row=8, column=1)

botonConversor.grid(row=1, column=0, columnspan=2, pady=10)
botonConversor2.grid(row=4, column=0, columnspan=2, pady=10)
botonConversor3.grid(row=7, column=0, columnspan=2, pady=10)
botonIpBinario.grid(row=9, column=0, columnspan=2, pady=10)
cuadroResultadoBinario.grid(row=10, column=1)


# ... Código para el empaquetado de elementos con pack ...

cuadroBinario.pack()
cuadroDecimal.pack()
cuadroIp.pack()

# ... Código para los botones ...

cuadroResultado.pack()
cuadroResultado2.pack()
cuadroResultado3.pack()
cuadroResultadoBinario.pack()


raiz.mainloop()