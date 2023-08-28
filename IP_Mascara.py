# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:12:16 2023

@author: ASUS
"""

import socket
import psutil

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
    
    return direccion_ip, mascara_red

ip, mascara = obtener_informacion_red()

print(f"Dirección IP: {ip}")
print(f"Máscara de Red: {mascara}")
