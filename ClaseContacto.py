#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Lenovo
#
# Created:     30-05-2018
# Copyright:   (c) Lenovo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.key = nombre+apellido
        self.next = None

    def getInformacion(self):
        print("Nombre: ",self.nombre)
        print("Apellido: ",self.apellido)
        print("Número de Telefono: ",self.telefono)
        print("Email: ",self.email)
